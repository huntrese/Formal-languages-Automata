import collections
"""Variant 11
Q = {q0,q1,q2,q3},
∑ = {a,b,c},
F = {q3},
δ(q0,a) = q1,
δ(q1,b) = q2,
δ(q2,c) = q0,
δ(q1,a) = q3,
δ(q0,b) = q2,
δ(q2,c) = q3.
"""

def grammar_to_language(grammar):
    terminals="abcdefghijklmnoprstqwxyz"
    nonterminals=terminals.upper()
    lines=grammar.split("\n")
    VN = lines[1].split("=")[1].translate({ord(c): None for c in "{} "}).split(",")[:-1]
    VT = lines[2].split("=")[1].translate({ord(c): None for c in "{} "}).split(",")[:-1]
    F = VT
    is_fa_grammar=0
    if "F =" in lines[3]:
        is_fa_grammar=1
        for i in range(3, len(lines)):
            line = lines[i]
            if not line:
                continue
            
            line = line.replace(".","").replace(" ","")
            line = line[:-1] if line[-1]=="," else line
            
            
            for char in VT:
                ind=VT.index(char)
                line = line.replace(VT[ind],terminals[ind])
            for char in VN:
                ind=VN.index(char)
                line = line.replace(VN[ind],nonterminals[ind])
            

            lines[i] = line
        for char in VT:
            ind=VT.index(char)
            VT[ind]=terminals[ind]
        for char in VN:
            ind=VN.index(char)
            VN[ind]=nonterminals[ind]
        
        if "F=" in lines[3]:
            F_part = lines[3].split("=")[1].strip().replace("{","").replace("}","").split(",")  # Extract the part after "F ="

            F = [char.strip() for char in F_part]        

    grammar_rules = lines[3+is_fa_grammar:]
    rules = collections.defaultdict(list)

    for rule in grammar_rules:
        rule = rule.replace("→","=")
        if rule and "{" not in rule and "}" not in rule:
            lhs, rhs = rule.split("=")
            if is_fa_grammar:
                rhs=lhs.split(",")[1].replace(")","")+rhs
                lhs=lhs.split(",")[0].replace("δ(","")
            rules[lhs.strip()].append(rhs.strip())

    return rules,VN,VT,F