import numpy as np
import grammarHelper
from automata import FiniteAutomaton
import networkx as nx
import matplotlib.pyplot as plt

class Language():
    rules = {}
    words = []
    VN=[]
    VT=[]
    def __init__(self,rules,VN,VT):
        self.rules=rules
        self.VN=VN
        self.VT=VT

    def generate_word(self, number):
        start = self.rules["S"][0]
        steps = [f"\nS -> {start}"]
        unique=0
        while any(c.isupper() for c in start):
            non_terminals = [i for i, c in enumerate(start) if c.isupper()]
            for i in non_terminals[::-1]:
                options = self.rules[start[i]]
                replacement = np.random.choice(options)
                start = start[:i] + replacement + start[i + 1 :]
                steps.append(f" -> {start}")

        if start not in self.words:
            self.words.append(start)
            unique=1
            print("\n".join(steps))

        if number > 0:
            self.generate_word(number - unique)

        return start



grammar="""Variant 21:
VN={S, B, C, D},
VT={a, b, c}, 
P={ 
    S → aB     
    B → bS    
    B → aC   
    B → b    
    C → bD   
    D → a    
    D → bC
    D → cS
}

"""
rules, VN, VT = grammarHelper.grammar_to_language(grammar)



lang=Language(rules,VN,VT)
lang.generate_word(5)
print(lang.words)
print(lang.VN)
print(lang.VT)

fa = FiniteAutomaton(rules)



input_string = "ab"
if fa.can_generate(input_string):
    print(f"The string '{input_string}' can be obtained from the grammar.")
else:
    print(f"The string '{input_string}' cannot be obtained from the grammar.")

fa.getAutomata()