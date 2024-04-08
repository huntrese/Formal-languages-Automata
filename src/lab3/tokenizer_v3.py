import json,re

TOKENS=[
    [r"\# .*", "COMMENT"],
    [r"\S*if|else|elif","CONDITIONAL"],
    [r"\(","ARGUMENT_START"],
    [r"[A-Za-z]+","LITERAL"],
    [r":|==|>=|<=|<|>|!=","OPERATOR"],
    [r"\)","ARGUMENT_END"],
    [r"{","BODY_START"],

    [r"}","BODY_END"],

    [r"[+-]?((\d+(\.\d+)?)|(\.\d+))","NUMERICAL"],
]

class Tokenizer:
    def __init__(self,string):
        self._string=string

    def lines_plit(self):
        self._string=self._string.split("\n")

    def tokenize(self):
        response = []
        index = 0
        for line in self._string:
            print("DDD ", line, index)

            working_line = line
            for regex, token in TOKENS:
                matches = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(regex, working_line)]
                print(matches)

                for match_start, match_end, match_string in matches:
                    s, e = index + match_start, index + match_end
                    response.append({"type": token, "value": match_string, "start": s, "end": e})
                    if token in ["COMMENT", "IF"]:
                        working_line = working_line[:match_start] + working_line[match_end:]

            index += len(line)
        response = sorted(response, key=lambda x: x['start'])

        return response



if __name__== "__main__":
    t=Tokenizer("""
    if (a==b){
#   test this thingy
        Patient : 
        Pregnancies : 5 
        Glucose : 130 
    } else {
        Insulin : 100 
                
    }
    BloodPressure : 80 
    SkinThickness : 25 
    BMI : 28.5 
    DiabetesPedigreeFunction : 0.55 
    Age : 40 
    Outcome : 1

    """)
    t.lines_plit()
    response=t.tokenize()
    for i in response:
        print(i)