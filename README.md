# Morality-Conditioned-Politics

This repository contains code and data for reproducing experiments in our [arXiv preprint](http://arxiv.org/abs/2601.08634).

## Repository Structure

```
.
├── data                    
│   └── prompts # Prompts used to elicit political opinions conditioned on moral values
│
├── morality                       # Morality-related data construction and processing
│   ├── generate_prompt            # Prepare moral conditions for the prompt template
│   ├── morality_prompt_utils      # Data construction util for Moral Foundations Questionnaire (MFQ)
│   ├── morality_prompt_utils_PVQ  # Data construction util for Portrait Values Questionnaire (PVQ)
│   └── morality_prompt_utils_deut # Data construction util for FactualDilemmas and Oxford Utilitarianism Scale (OUS)
│
├── politics             # Politic-related data construction and processing
│   ├── utils            # Utils used to obtain the PCT scores
│   └── generate_prompts # Prepare political component for the prompt template
│   
├── utils       # Utils for moral conditioned PCT
│   └── llm_api # Util for LLM API calls
│
├── analysis                                   # Metrics and figure plotting
├── moral2politics_MFQ                         # Morality_conditioned_pct generation (on Benchmark MFQ + PCT)
├── morality_prompt_utils_PVQ                  # Morality_conditioned_pct generation (on Benchmark PVQ + PCT)
└── moral2politics_greatestgood_factualdilemma # Morality_conditioned_pct generation (on Benchmark FactualDilemmas/OUS + PCT)
```

## 📋 Moral Instruments and Political Compass Test

| Instrument | Abbreviation | Reference |
|------------|--------------|-----------|
| Moral Foundations Questionnaire | MFQ | [Website](https://moralfoundations.org/questionnaires/) |
| Oxford Utilitarianism Scale | OUS | [PDF](https://luciuscaviola.com/OUS_English_Original.pdf) |
| Factual Dilemmas | - | [Repository](https://osf.io/cg5tq/files/ephu6) |
| Portrait Values Questionnaire (40-item) | PVQ-40 | [Source](https://scholarworks.gvsu.edu/orpc/vol2/iss2/9) |
| Political Compass Test | PCT | [Website](https://www.politicalcompass.org/test) |
