import grammarHelper
from automata import FiniteAutomaton
import nfa_dfa
import language



grammar="""Variant 20:
VN={S, A, B, C},
VT={a, b, c, d}, 
P={ 
    S → dA     
    A → d    
    A → aB   
    B → bC    
    C → cA
    C → aS
}

"""
rules, VN, VT, F = grammarHelper.grammar_to_language(grammar)



lang=language.Language(rules,VN,VT,F)

print(lang.VN)
print(lang.VT)
print(lang.F)


print(lang.rules)

fa= FiniteAutomaton(rules,F=lang.F,initial='S')
fa.getAutomata("FA for language(NFA/DFA)")

lang.generate_word(5,'A')
print("Generated words: ",lang.words)
input_string = "aaaab"
fa.canGenerate(input_string)