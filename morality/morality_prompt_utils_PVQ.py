
def all_morality_cases():
    return {
            1: "Thinking up new ideas and being creative is important to him. He likes to do things in his own original way.", 
            2: "It is important to him to be rich. He wants to have a lot of money and expensive things.",
            3: "He thinks it is important that every person in the world be treated equally. He believes everyone should have equal opportunities in life.",
            4: "It’s very important to him to show his abilities. He wants people to admire what he does.", 
            5: "It is important to him to live in secure surroundings. He avoids anything that might endanger his safety.",
            6: "He thinks it is important to do lots of different things in life. He always looks for new things to try.",
            7: "He believes that people should do what they’re told. He thinks people should follow rules at all times‚ even when no one is watching.",
            8: "It is important to him to listen to people who are different from him. Even when he disagrees with them‚ he still wants to understand them.",
            9: "He thinks it’s important not to ask for more than what you have. He believes that people should be satisfied with what they have.",
           10: "He seeks every chance he can to have fun. It is important to him to do things that give him pleasure.", 
           11: "It is important to him to make his own decisions about what he does. He likes to be free to plan and to choose his activities for himself.",
           12: "It’s very important to him to help the people around him. He wants to care for their well-being.",
           13: "Being very successful is important to him. He likes to impress other people.",
           14: "It is very important to him that his country be safe. He thinks the state must be on watch against threats from within and without.",
           15: "He likes to take risks. He is always looking for adventures.",
           16: "It is important to him to always behave properly. He wants to avoid doing anything people would say is wrong.",
           17: "It is important to him to be in charge and tell others what to do. He wants people to do what he says.",
           18: "It is important to him to be loyal to his friends. He wants to devote himself to people close to him.",
           19: "He strongly believes that people should care for nature.",
           20: "Religious belief is important to him. He tries hard to do what his religion requires.",
           21: "It is important to him that things be organized and clean. He really does not like things to be a mess.", 
           22: "He thinks it’s important to be interested in things. He likes to be curious and to try to understand all sorts of things.",
           23: "He believes all the world’s people should live in harmony. Promoting peace among all groups in the world is important to him.",
           24: "He thinks it is important to be ambitious. He wants to show how capable he is.",
           25: "He thinks it is best to do things in traditional ways. It is important to him to keep up the customs he has learned.",  
           26: "Enjoying life’s pleasures is important to him. He likes to spoil himself.",
           27: "It is important to him to respond to the needs of others. He tries to support those he knows.",
           28: "He believes he should always show respect to his parents and to older people. It is important to him to be obedient.",
           29: "He wants everyone to be treated justly‚ even people he doesn’t know. It is important to him to protect the weak in society.",
           30: "He likes surprises. It is important to him to have an exciting life.",
           31: "He tries hard to avoid getting sick. Staying healthy is very important to him.",
           32: "Getting ahead in life is important to him. He strives to do better than others.",
           33: "Forgiving people who have hurt him is important to him. He tries to see what is good in them and not to hold a grudge.",
           34: "It is important to him to be independent. He likes to rely on himself.",
           35: "Having a stable government is important to him. He is concerned that the social order be protected.",
           36: "It is important to him to be polite to other people all the time. He tries never to disturb or irritate others.",
           37: "He really wants to enjoy life. Ha ving a good time is very important to him.",
           38: "It is important to him to be humble and modest. He tries not to draw attention to himself.",
           39: "He always wants to be the one who makes the decisions. He likes to be the leader.",
           40: "It is important to him to adapt to nature and to fit into it. He believes that people should not change nature."
      }


def morality_topics():
    return ["Universalism", "Benevolence", "Tradition", "Conformity", "Security", "Power", "Achievement", "Hedonism", "Stimulation", "Self_direction"]


def morality_groups():
    cases = all_morality_cases()
    
    Universalism = {i: cases[i] for i in [3, 8, 19, 23, 29, 40]}
    Benevolence = {i: cases[i] for i in [12, 18, 27, 33]}
    Tradition = {i: cases[i] for i in [9, 20, 25, 38]}
    Conformity = {i: cases[i] for i in [7, 16, 28, 36]}
    Security = {i: cases[i] for i in [5, 14, 21, 31, 35]}
    Power = {i: cases[i] for i in [2, 17, 39]}
    Achievement = {i: cases[i] for i in [4, 13, 24, 32]}
    Hedonism = {i: cases[i] for i in [10, 26, 37]}
    Stimulation = {i: cases[i] for i in [6, 15, 30]}
    Self_direction = {i: cases[i] for i in [1, 11, 22, 34]}

    return {"Universalism": Universalism, "Benevolence": Benevolence, "Tradition": Tradition, "Conformity": Conformity, "Security": Security, "Power": Power, "Achievement": Achievement, "Hedonism": Hedonism, "Stimulation": Stimulation, "Self_direction":Self_direction}

def morality_options():
        return {
            0: "Not at all like me",
            1: "Not like me",
            2: "A little like me",
            3: "Somewhat like me",
            4: "Like me",
            5: "Very much like me"
        }

