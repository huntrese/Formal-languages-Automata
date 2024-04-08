import src.lab1.grammarHelper as grammarHelper

import src.lab1.language as language
from collections import defaultdict
variant="""
(a|b)(c|d)E+G?
P(Q|R|S)T(UV|W|X)*Z+
1(0|1)*2(3|4)^(5)36
"""
grammars=[]
REGEX = [x for x in variant.split("\n") if x]
terminals="Sabcdefghijklmnoprtqwxyz"
nonterminals=terminals.upper()
print(REGEX)
mapping={}
for index,expr in enumerate(REGEX):
    print(expr)
    mapping[index]=defaultdict(dict)
    mapping[index]={x:x.lower() for x in expr if x.isalpha()}
    print(mapping)
    expr=expr.lower()
    final="\n"

    starting=0

    expr=expr.replace("("," ").replace(")"," ").replace("*"," * ").replace("^"," ^ ").replace("+"," + ").replace("?"," ? ")
    expr=[x for x in expr.split(" ") if x]
    VT=[]
    for i,node in enumerate(expr):
        node=str(node)
        if "|" in node:
            choices=node.split("|")
            for choice in choices:
                final+=f'{nonterminals[starting]} → {choice}{nonterminals[starting+1]}\n'
                if choice not in VT:
                    VT.append(choice)
        elif node == "+":
            final+=f'{nonterminals[starting]} → {nonterminals[starting-1]}\n'
            starting-=1

        elif node == "*":
            final+=f'{nonterminals[starting-1]} → {nonterminals[starting]}\n'
            final+=f'{nonterminals[starting]} → {nonterminals[starting-1]}\n'
            starting-=1

        elif node == "?":
            final+=f'{nonterminals[starting-1]} → {nonterminals[starting]}\n'
            starting-=1
        elif node == "^":
            times = int(expr[i+1])
            
            for j in range(times-1):

                previous=[x for x in final.split("\n") if x]
                previous = [x for x in previous if (x[0]==nonterminals[starting-1+j])]
                s=""
                
                for x in previous:

                    s+=nonterminals[starting+j]
                    s+=x[1:-1]
                    s+=nonterminals[starting+j+1]
                    s+="\n"

                final+=s
            starting+= times-2


        elif node.isalnum():
            if expr[i-1] == "^":
                continue
            final+=f'{nonterminals[starting]} → {node}{nonterminals[starting+1]}\n'
            VT.append(node)
        starting+=1

    
    final+=f'{nonterminals[starting]} →  \n'


    lb="{"
    rb="}"
    grammar=f"Varianta 20:\n VN= {lb}{', '.join(list(nonterminals[:starting+1]))}{rb},\n VT= {lb}{', '.join(VT)}{rb},\n P={lb}{final}{rb}"
    print(grammar)
    grammars.append(grammar)



for index,grammar in enumerate(grammars):
    rules, VN, VT, F = grammarHelper.grammar_to_language(grammar)



    lang=language.Language(rules,VN,VT,F)

    lang.generate_word(5,'S')
    for word in lang.words:
        for key,value in mapping[index].items():
            if value!=key:
                word = word.replace(value,key)
        print("Generated words: ",word)