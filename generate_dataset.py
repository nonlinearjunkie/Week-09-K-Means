import csv
import random 

technical_know_hows=["Sharp","Well-trained","Strategic planners","Bully","Resourceful"
                            "Goal oriented","Well-networked","Well-organized","Well trained","Creative","Smart",
                            "Skillful","Oppurtinists"]

personal_traits=["Impatient","Determined","Insensitive","Secretive","Aggressive","Strong-willed","Passionate"
                 "Insensitive","Chaotic state of mind","Inhuman Psyche","Vengeful","Coercive","Coward","Selfish",
                 "Unethical","Risk-taker","Loner","Incited","Gullible","Conviction in Violence","Emotional","Control freak"
                 "Psychologically Deviant","Psychiatric conditions","Identity crisis"]


social_characterstics=["Anti-establishment","Lack Social skills","Inferiority complex","Low self-worth","Marginalised","Mass-destruction" 
                      "Misguided","Brain-washed","Anti-social","Anti-state","Unlawful","Rebellious","Reinforcement available",
                       "Intolerance to diversity of opinion","Need to outsmart others","Rationalization","Social dissatisfaction"]  

motivating_factors=["Monetary Gain","Greed ","Political beliefs","Emotions",
                    "Disregard for law","Intolerance","Thrill-seeking","Risk tolerance","Manipulate others",
                    "Need to Control others","Concealed existence","Political support","Religious fundamentalism",
                    "Experimentation","No fear of punishment","Curiosity",
                    "Revenge","Anger","Lust","Plain boredom","Enhancing selfworth"]     


with open('cybercrime_profiles.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ "Technical Know How", "Personal Traits","Social Characterstics","Motivating Factors"])

    for i in range(1000):
        row=[]
        technical_know_how=random.choice(technical_know_hows) 
        personal_trait=random.choice(personal_traits)
        social_characterstic=random.choice(social_characterstics)
        motivating_factor=random.choice(motivating_factors)
        row=[technical_know_how,personal_trait,social_characterstic,motivating_factor]
        writer.writerow(row)

