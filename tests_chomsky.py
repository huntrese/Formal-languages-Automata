import automata
import grammarHelper
tests = [
    {
        "grammar": """Variant 21:
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

        """,
        "expected_tier": 3  # Expected tier level for this grammar
    },
    {
        "grammar": """Variant 21:
        VN={S, A, B},
            VT={a, b},
            P={
                S → aS
                S → A
                A → bB
                B → a
                B → b
            }
        """,
        "expected_tier": 3  # Expected tier level for this grammar
    },
    {
        "grammar": """Variant 21:
        VN={S, A, B, C},
            VT={a, b},
            P={
                S → aA
                A → bB
                A → B
                B → aC
                C → b
            }
        """,
        "expected_tier": 3  # Expected tier level for this grammar
    },
    {
        "grammar": """Variant 21:
        VN={X, Y},
            VT={e, a, b},
            P={
                X → e 
                X → a 
                X → aY
                Y → b 
            }
        """,
        "expected_tier": 3  # Expected tier level for this grammar
    },
    {
        "grammar": """Variant 21:
        VN={S, X},
            VT={e, a, b, c},
            P={
                S → Xa 
                X → a 
                X → aX 
                X → abc 
                X → e
            }
        """,
        "expected_tier": 2  # Expected tier level for this grammar
    },{
        "grammar": """Variant 21:
        VN={A, B},
            VT={a, b, c},
            P={
                AB → AbBc 
                A → bcA 
                B → b 
            }
        """,
        "expected_tier": 1  # Expected tier level for this grammar
    },{
        "grammar": """Variant 21:
        VN={A, B},
            VT={a, b, c},
            P={
                S → ACaB 
                Bc → acB 
                CB → DB 
                aD → Db 
            }
        """,
        "expected_tier": 1  # Expected tier level for this grammar
    },
    
    ]

for test in tests:
    grammar = test["grammar"].strip()
    expected_tier = test["expected_tier"]
    rules, VN, VT = grammarHelper.grammar_to_language(grammar)
    fa = automata.FiniteAutomaton(rules)
    actual_tier = fa.clasify()
    result= actual_tier == expected_tier
    if not result:
        print(f"XXXX - Test failed: Expected tier {expected_tier}, got {actual_tier}")
    else :
        print(f"       Test completed: Expected tier {expected_tier}, got {actual_tier}")

