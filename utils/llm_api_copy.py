import os
os.environ["HF_HOME"] = "./"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

import re
import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from openai import OpenAI

HF_TOKEN = 
OPENAI_API_KEY = 

_gpt_client = None
def _get_openai_client():
    global _gpt_client
    if _gpt_client is None:
        if not OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY not set.")
        _gpt_client = OpenAI(api_key=OPENAI_API_KEY)
    return _gpt_client

_PIPELINE_CACHE = {}

GEN_CFG = dict(
    temperature=0,
    max_tokens=256,      # OpenAI
    max_new_tokens=256,  # HF
    torch_dtype=torch.bfloat16,
    do_sample=False,
    top_k=0,
    top_p=1,
)

def apply_prompt_template(message, model_name):
    return [
        {"role": "system", "content": message.get("system", "")},
        {"role": "user",   "content": message.get("user", "")},
    ]

def extract_json_from_response(response_text):
    match = re.search(r"\{[\s\S]*\}", response_text)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None

def _ask_openai(model_name, messages):
    client = _get_openai_client()
    resp = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=GEN_CFG["max_tokens"],
        n=1,
        stop=None,
        temperature=GEN_CFG["temperature"],
        top_p=GEN_CFG["top_p"],
    )
    return resp.choices[0].message.content

def _ask_openai5(model_name, messages):
    client = _get_openai_client()
    resp = client.responses.create(
        model=model_name,
        input=messages,
        max_output_tokens=GEN_CFG["max_new_tokens"],
        temperature=GEN_CFG["temperature"],
        top_p=GEN_CFG["top_p"],
        reasoning={"effort": "none"} 
    )
    return resp.output_text


def _get_hf_pipeline(model_key: str):
    if model_key in _PIPELINE_CACHE:
        return _PIPELINE_CACHE[model_key]

    if model_key in ["llama2_7b", "llama-2-7b"]:
        model_id = "meta-llama/Llama-2-7b-chat-hf"

    elif model_key in ["llama2_13b", "llama-2-13b"]:
        model_id = "meta-llama/Llama-2-13b-chat-hf"

    elif model_key in ["llama32_3b", "llama3_2_3b"]:
        model_id = "meta-llama/Llama-3.2-3B-Instruct"

    elif model_key in ["llama31_8b", "llama3_1_8b"]:
        model_id = "meta-llama/Llama-3.1-8B-Instruct"

    elif model_key in ["qwen25_7b", "qwen-2.5-7b", "qwen2.5_7b"]:
        model_id = "Qwen/Qwen2.5-7B-Instruct"

    elif model_key in ["qwen25_14b", "qwen-2.5-14b", "qwen2.5_14b"]:
        model_id = "Qwen/Qwen2.5-14B-Instruct"

    elif model_key in ["mistral_7b", "mistral-7b"]:
        model_id = "mistralai/Mistral-7B-Instruct-v0.1"

    elif model_key in ["mistral_7b_v2", "mistral-7b-v2"]:
        model_id = "mistralai/Mistral-7B-Instruct-v0.2"

    elif model_key in ["mistral_7b_v3", "mistral-7b-v3"]:
        model_id = "mistralai/Mistral-7B-Instruct-v0.3"

    elif model_key in ["yi15_6b", "yi-1.5-6b", "yi1.5_6b"]:
        model_id = "01-ai/Yi-1.5-6B-Chat"

    elif model_key in ["falcon_7b", "falcon-7b"]:
        model_id = "tiiuae/falcon-7b-instruct"

    elif model_key in ["phi-3-mini"]:
        model_id = "microsoft/Phi-3-mini-4k-instruct"

    elif model_key in ["phi-3-small"]:
        model_id = "microsoft/Phi-3-small-8k-instruct"

    elif model_key in ["phi-3-medium"]:
        model_id = "microsoft/Phi-3-medium-4k-instruct"
        
    else:
        raise ValueError(f"Unsupported HF model key: {model_key}")

    
    if "falcon" in model_key:
        pl = pipeline("text-generation", model=model_id, torch_dtype=GEN_CFG["torch_dtype"], device_map="auto", trust_remote_code=True)
    elif "phi" in model_key:
        tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
        tok.padding_side = "left"
        if tok.pad_token_id is None and tok.eos_token:
            tok.pad_token = tok.eos_token
        
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=GEN_CFG["torch_dtype"],   
            attn_implementation="flash_attention_2",   
            trust_remote_code=True,
        )

        pl = pipeline(
            "text-generation",
            model=model,
            tokenizer=tok,
        )

    else:
        pl = pipeline("text-generation", model=model_id, torch_dtype=GEN_CFG["torch_dtype"], device_map="auto")

    
    tok = pl.tokenizer
    tok.padding_side = "left"
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    
    _PIPELINE_CACHE[model_key] = pl
    return pl

def _ask_hf(model_key, prompt_text):
    pl = _get_hf_pipeline(model_key)
    if "llama3" in model_key:
        terminators = [pl.tokenizer.eos_token_id,
                       pl.tokenizer.convert_tokens_to_ids("<|eot_id|>")]
        sequences = pl(
            prompt_text,
            do_sample=GEN_CFG["do_sample"],
            top_k=GEN_CFG["top_k"],
            num_return_sequences=1,
            return_full_text=False,
            max_new_tokens=GEN_CFG["max_new_tokens"],
            eos_token_id=terminators,
            pad_token_id=pl.tokenizer.eos_token_id,
        )

    elif ("mistral" in model_key) or ("falcon" in model_key):
        sequences = pl(
            prompt_text,
            do_sample=GEN_CFG["do_sample"],
            top_k=GEN_CFG["top_k"],
            num_return_sequences=1,
            return_full_text=False,
            max_new_tokens=GEN_CFG["max_new_tokens"],
            pad_token_id=pl.tokenizer.eos_token_id,
        )
        
    else:
        sequences = pl(
            prompt_text,
            do_sample=GEN_CFG["do_sample"],
            top_k=GEN_CFG["top_k"],
            num_return_sequences=1,
            return_full_text=False,
            max_new_tokens=GEN_CFG["max_new_tokens"],
        )
    return sequences[0]["generated_text"]

def llm_api(message, model_name):
    model_key = model_name.lower().strip()
    # OpenAI
    if model_key in ["gpt-4o", "gpt4o"]:
        return _ask_openai("gpt-4o", apply_prompt_template(message, model_key))
    if model_key in ["gpt-4o-mini", "gpt4omini"]:
        return _ask_openai("gpt-4o-mini", apply_prompt_template(message, model_key))
    if model_key in ["gpt-52"]:
        return _ask_openai5("gpt-5.2", apply_prompt_template(message, model_key))
        
    # HuggingFace
    return _ask_hf(model_key, apply_prompt_template(message, model_key))  # HF

def unload_model(model_key: str | None = None):
    if model_key is None:
        _PIPELINE_CACHE.clear()
    else:
        _PIPELINE_CACHE.pop(model_key, None)
    torch.cuda.empty_cache()
