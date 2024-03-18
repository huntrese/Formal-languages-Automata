import json
class Tokenizer:
    def __init__(self,string):
        self._string=string

    def lines_plit(self):
        self._string=self._string.split("\n")
    def tokenize(self):

        response=[]

        for line in self._string:
            
            line=line.replace("\n","").replace(" ","")
            lexemes=line.split(":")
            if lexemes == ['']:
                continue
            lexemes.insert(1,":")
            for token in lexemes:
                each = {}
                if token.isnumeric():
                    each["type"]= "NUM"
                    if "."in token:
                        each["type"]="FLOAT"
                elif ":" == token:
                    each['type'] = "OPERATOR"
                else:
                    each['type'] = "IDENTIFIER"
                each["value"] = token
                
                response.append(each)
        return response

