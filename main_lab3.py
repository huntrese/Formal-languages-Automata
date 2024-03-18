from src.lab3.tokenizer_v2 import Tokenizer
t=Tokenizer("""
Patient: 
Pregnancies: 5 
Glucose: 130 
BloodPressure: 80 
SkinThickness: 25 
Insulin: 100 
BMI: 28.5 
DiabetesPedigreeFunction: 0.55 
Age: 40 
Outcome: 1

""")
t.lines_plit()
response=t.tokenize()
for i in response:
    print(i)
    