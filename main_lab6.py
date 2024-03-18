from src.lab3.tokenizer_v2 import Tokenizer
from src.lab6.parser import parse
import json
t=Tokenizer("""
Patient: 1
Pregnancies: 5 
Glucose: 130 
BloodPressure: 80 
SkinThickness: 25 
Insulin: 100 
BMI: 28.5 
DiabetesPedigreeFunction: 0.55 
Age: 40 
Outcome: 1
#i dont like this

""")
t.lines_plit()
response=t.tokenize()
parse_Tree=parse(response)
    

parse_Tree=json.dumps(parse_Tree,indent=4)
print(parse_Tree)
    
