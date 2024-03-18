
import numpy as np


class Language():
    rules = {}
    words = []
    VN=[]
    VT=[]
    F=[]
    nfa=False
    def __init__(self,rules,VN,VT,F):
        self.rules=rules
        self.VN=VN
        self.VT=VT
        self.F=F

    def generate_word(self, number,initial = "S"):
        
        choices = self.rules[initial]
        start = np.random.choice(choices)
        steps = [f"\n{initial} -> {start}"]
        unique=0
        
        aut=self.F != self.VT
        condition = not any(char in self.F for char in start) if aut else any(c.isupper() for c in start)
        while condition :
            non_terminals = [i for i, c in enumerate(start) if c in self.VN]
            if (not non_terminals) and (not aut):
                break
            if aut and any(char in self.F for char in start):
                for char in self.F:
                    start=start.replace(char,"")
                break
            
            for i in non_terminals[::-1]:
                options = self.rules[start[i]]
                replacement = np.random.choice(options)
                start = start[:i] + replacement + start[i + 1 :]
                steps.append(f" -> {start}")
        if start not in self.words:
            self.words.append(start)
            unique=1
            print("\n".join(steps))

        if number > 0:
            self.generate_word(number - unique,initial)

        return start