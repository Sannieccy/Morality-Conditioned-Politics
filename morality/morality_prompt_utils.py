
def all_morality_cases():
    return {
            # part 1 - relevant
            1: "Whether or not someone suffered emotionally", 
            2: "Whether or not some people were treated differently than others",
            3: "Whether or not someone’s action showed love for his or her country",
            4: "Whether or not someone showed a lack of respect for authority", 
            5: "Whether or not someone violated standards of purity and decency",
            6: "Whether or not someone was good at math",
            7: "Whether or not someone cared for someone weak or vulnerable",
            8: "Whether or not someone acted unfairly",
            9: "Whether or not someone did something to betray his or her group",
           10: "Whether or not someone conformed to the traditions of society", 
           11: "Whether or not someone did something disgusting",
           12: "Whether or not someone was cruel",
           13: "Whether or not someone was denied his or her rights",
           14: "Whether or not someone showed a lack of loyalty",
           15: "Whether or not an action caused chaos or disorder",
           16: "Whether or not someone acted in a way that God would approve of",
        
            # part 2 - agreement
           17: "Compassion for those who are suffering is the most crucial virtue.",
           18: "When the government makes laws, the number one principle should be ensuring that everyone is treated fairly.",
           19: "I am proud of my country’s history.",
           20: "Respect for authority is something all children need to learn.",
           21: "People should not do things that are disgusting, even if no one is harmed.", 
           22: "It is better to do good than to do bad.",
           23: "One of the worst things a person could do is hurt a defenseless animal.",
           24: "Justice is the most important requirement for a society.",
           25: "People should be loyal to their family members, even when they have done something wrong.",  
           26: "Men and women each have different roles to play in society.",
           27: "I would call some acts wrong on the grounds that they are unnatural.",
           28: "It can never be right to kill a human being.",
           29: "I think it’s morally wrong that rich children inherit a lot of money while poor children inherit nothing.",
           30: "It is more important to be a team player than to express oneself.",
           31: "If I were a soldier and disagreed with my commanding officer’s orders, I would obey anyway because that is my duty.",
           32: "Chastity is an important and valuable virtue."
      }


def morality_topics():
    return ["Harm_Care", "Faireness_Reciprocity", "Ingroup_Loyalty", "Authority_Respect", "Purity_Sanctity"]


def morality_groups():
    cases = all_morality_cases()
    Harm_Care = {i: cases[i] for i in [1,7,12,17,23,28]}
    Faireness_Reciprocity = {i: cases[i] for i in [2,8,13,18,24,29]}
    Ingroup_Loyalty = {i: cases[i] for i in [3,9,14,19,25,30]}
    Authority_Respect = {i: cases[i] for i in [4,10,15,20,26,31]}
    Purity_Sanctity = {i: cases[i] for i in [5,11,16,21,27,32]}
    other = {i: cases[i] for i in [6,22]}

    part1 = {i: cases[i] for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]}
    part2 = {i: cases[i] for i in [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]}
    
    return {"Harm_Care": Harm_Care, "Faireness_Reciprocity": Faireness_Reciprocity, "Ingroup_Loyalty": Ingroup_Loyalty, "Authority_Respect": Authority_Respect, "Purity_Sanctity": Purity_Sanctity, "Other": other, "Relevance": part1, "Agreement": part2}

def morality_options(key):
    if key == "Relevance":
        return {
            0: "not at all relevant (This consideration has nothing to do with my judgments of right and wrong)",
            1: "not very relevant",
            2: "slightly relevant",
            3: "somewhat relevant",
            4: "very relevant",
            5: "extremely relevant (This is one of the most important factors when I judge right and wrong)"
        }

    elif key == "Agreement":
        return {
            0: "Strongly disagree",
            1: "Moderately disagree",
            2: "Slightly disagree",
            3: "Slightly agree",
            4: "Moderately agree",
            5: "Strongly agree"
        }
