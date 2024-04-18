import src.lab1.grammarHelper as grammarHelper

import src.lab1.language as language
from collections import defaultdict
variant="""Varuiant 20
VN={S, A, B, C, D},
VT={a, b, c}, 
P={ 
    S → ABACa
    A → aA
    A →
    B → bB
    B → Da
    B → 
    C → c
    D → AB

}
"""

rules, VN, VT, F = grammarHelper.grammar_to_language(variant)



lang=language.Language(rules,VN,VT,F)
for source in lang.rules:
    destination = lang.rules[source]
    print(source, destination)
        
epsilon_tries=5
while epsilon_tries>0:
    epsilon_transitions=[]
    epsilon_tries-=1
    for source in lang.rules:
        destination = lang.rules[source]
        for option in destination:
            if not option:
                epsilon_transitions.append(source)
                lang.rules[source].remove(option)
    # print(epsilon_transitions,"Are epsilon")
    if not epsilon_transitions:
        continue
    mapping={}
    for source in lang.rules:
        destination = lang.rules[source]
        for option in destination:
            epsilon_indexes=[]

            for epsilon in epsilon_transitions:
                if epsilon in option:
                    for index, char in enumerate(option):
                        if char == epsilon:
                            epsilon_indexes.append((index, char))
            # print(source,destination)
            # print(epsilon_transitions,epsilon_indexes)
            if  not epsilon_indexes:
                continue
            li=set()
            final_option=option
            for to_remove in epsilon_indexes:
                new_option=option[:to_remove[0]]+" "+option[to_remove[0]+1:]
                li.add(new_option.replace(" ",""))
                final_option=final_option[:to_remove[0]]+" "+final_option[to_remove[0]+1:]
            li.add(final_option.replace(" ",""))
            # lang.rules[source].remove(option)
            for i in li:
                if i not in lang.rules[source]:
                    lang.rules[source].append(i)

print()

for source in lang.rules:
    destination = lang.rules[source]
    print(source, destination)

unit_tries=2
while unit_tries>0:
    unit_transitions=[]
    unit_tries-=1
    for source in lang.rules:
        destination = lang.rules[source]
        for option in destination:
            if option in VN:
                unit_transitions.append((source,option))
                lang.rules[source].remove(option)
    if not unit_transitions:
        continue
    for source in lang.rules:

        destination = lang.rules[source]
        for option in destination:
            for unit_transition in unit_transitions:
                if unit_transition[0] in option:
                    new_trans=option.replace(unit_transition[0],unit_transition[1],1)
                    if new_trans not in lang.rules[source]:
                        lang.rules[source].append(new_trans)
                    


print()
lang.rules[source]=list(set(lang.rules[source]))
for source in lang.rules:
    destination = lang.rules[source]
    print(source, destination)

accessible={x:False for x in lang.rules.keys()}
accessible['S']=True
print(accessible)
for source in lang.rules:
        destination = lang.rules[source]
        for option in destination: 
            for non_terminal in accessible.keys():
                if non_terminal in option:
                    accessible[non_terminal] = True
print(accessible)
for source in accessible.keys():
    if accessible[source] == False:
        lang.rules.pop(source)

print()
lang.rules[source]=list(set(lang.rules[source]))
for source in lang.rules:
    destination = lang.rules[source]
    print(source, destination)