import json,re
RULES={
    'COMMENT':["COMMENT"],
    'PATIENT_INFO':['LITERAL','OPERATOR','NUMERICAL'],
}


def parse(tokens):
    index=len(tokens)
    body = []
    found_rules=[]
    for rule in RULES:
        tokens_structure=" ".join([token['type'] for token in tokens])

        ans=[(m.start(0), m.end(0),rule) for m in re.finditer(" ".join(RULES[rule]),tokens_structure)]
        found_rules.extend(ans)

    found_rules.sort()
    
    index=0
    for found in found_rules:
        rule_Set=RULES[found[2]]
        size=len(rule_Set)

        body.append({found[2]:tokens[index:index+size]})
        index+=size
    assert index==len(tokens), "Not all tokens were parsed, check if all tokens belong to ruleset"
            
    return {"Type":"Program","body":body}