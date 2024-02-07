import collections

def grammar_to_language(grammar):
    lines=grammar.split("\n")
    VN = lines[1].split("=")[1].translate({ord(c): None for c in "{} "}).split(",")[:-1]
    VT = lines[2].split("=")[1].translate({ord(c): None for c in "{} "}).split(",")[:-1]
    grammar_rules = lines[3:]
    rules = collections.defaultdict(list)

    for rule in grammar_rules:
        if rule and "{" not in rule and "}" not in rule:
            lhs, rhs = rule.split("→")
            rules[lhs.strip()].append(rhs.strip())
    print(rules)
    return rules,VN,VT