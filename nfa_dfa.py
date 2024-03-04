import collections

def convert_dfa(dfa):
    converted_dfa = {}
    for state, transitions in dfa.items():
        converted_transitions = []
        for symbol, next_state in transitions.items():
            converted_transitions.append(symbol + next_state)
        converted_dfa[state] = converted_transitions
    return converted_dfa

def convert_nfa_to_dfa(lang):
    dic = {}
   
    for lhs, rhs in lang.rules.items():
        for choice in rhs:
            upper = ""
            for c in choice:
                upper += c if c.isupper() else ""
            lower = ""
            for c in upper:
                lower += choice.replace(c, "")
            
            if lhs not in dic:
                dic[lhs] = {}
            if lower in dic[lhs]:
                dic[lhs][lower] += upper
                continue
            dic[lhs][lower] = upper
    dfa={}
    queue = [{'A'}]  # Start with the initial state
    visited = set()

    while queue:
        current_states = queue.pop(0)
        current_states_str = ''.join(sorted(current_states))
        if current_states_str in visited:
            continue
        visited.add(current_states_str)
        dfa[current_states_str] = {}
        dfa_state = {}
        
        for state in current_states:
            if state in dic:
                for symbol, next_state in dic[state].items():
                    if symbol not in dfa_state:
                        dfa_state[symbol] = next_state
                    else:
                        dfa_state[symbol] += next_state

        for symbol, next_states in dfa_state.items():
            next_state_set = ''.join(sorted(set(next_states)))
            dfa[current_states_str][symbol] = next_state_set
            if next_state_set not in visited:
                queue.append(next_state_set)
    

    formatted_dfa = convert_dfa(dfa)
    return dfa

def which_type(lang):
    for lhs in lang.rules.keys():
        lhs_lower=[]
        for rhs in lang.rules[lhs]:
            lower=[c for c in rhs if c.islower()]
            lhs_lower.append(''.join(lower))
        if len(lhs_lower)!=len(set(lhs_lower)):
            lang.nfa=True

    if lang.nfa:
        print("This automata is a NFA!")
    else:
        print("This automata is a DFA!")