import json,re

TOKENS=[
    [r"\A\#.*$", "COMMENT"],
    [r"\b[A-Za-z]+\b","LITERAL"],
    [r":","OPERATOR"],
    [r"[+-]?((\d+(\.\d+)?)|(\.\d+))","NUMERICAL"],
    

    








]

# if token.isnumeric():
#     each["type"]= "NUM"
#     if "."in token:
#         each["type"]="FLOAT"
# elif ":" == token:
#     each['type'] = "OPERATOR"
# else:
#     each['type'] = "IDENTIFIER"


class Tokenizer:
    def __init__(self,string):
        self._string=string

    def lines_plit(self):
        self._string=self._string.split("\n")
    def tokenize(self):

        response=[]

        for line in self._string:
            for regex, token in TOKENS:
                match=re.findall(regex,line)
                if not match:
                    continue
                match=match[0] if type(match[0])==tuple else match

                longest_match = max(match, key=lambda match: len(match))                
                response.append({"type":token,"value":longest_match})

                line=line.replace(longest_match,"")
        return response
t=Tokenizer("""
Patient: 
Pregnancies: 5 
Glucose: 130 
BloodPressure: 80.5 
SkinThickness: 25 
Insulin: 100 
BMI: 28.5 
DiabetesPedigreeFunction: 0.55 
Age: 40 
Outcome: 1
# damn this is good
""")
t.lines_plit()
response=t.tokenize()
for i in response:
    print(i)
    
