import grammarHelper
from automata import FiniteAutomaton
import nfa_dfa
import language



grammar="""Variant 28
Q = {q0,q1,q2,q3},
∑ = {a,b,c},
F = {q3},
δ(q0,a) = q0,
δ(q0,a) = q1,
δ(q1,a) = q1,
δ(q1,c) = q2,
δ(q1,b) = q3,
δ(q0,b) = q2,
δ(q2,b) = q3.
"""
rules, VN, VT, F = grammarHelper.grammar_to_language(grammar)



lang=language.Language(rules,VN,VT,F)

print(lang.VN)
print(lang.VT)
print(lang.F)


print(lang.rules)

fa= FiniteAutomaton(rules,F=lang.F,initial='A')
fa.getAutomata("FA for language(NFA/DFA)")
dfa_rules=nfa_dfa.convert_nfa_to_dfa(lang)
dfa = FiniteAutomaton(dfa_rules,F=lang.F,initial='A')
    

lang.generate_word(5,'A')
print("Generated words: ",lang.words)
input_string = "aaaab"
dfa.canGenerate(input_string)
nfa_dfa.which_type(lang)

dfa.getAutomata("FA for language, DFA")