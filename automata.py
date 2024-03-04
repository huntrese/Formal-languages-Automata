import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
class FiniteAutomaton:
    def __init__(self, grammar, F, initial="S"):
        self.grammar = grammar
        self.transitions = defaultdict(list)
        self.rules=defaultdict(dict)
        self.start_symbol = initial
        self.F=F
        self.convert()
        self._build_transitions()

    def _build_transitions(self):
        for non_terminal, productions in self.rules.items():
            # print(non_terminal,productions)
            for production in productions:
                symbol = productions[production]
                self.transitions[non_terminal].append((production,symbol))


    def convert(self):
        for state,transition in self.grammar.items():
            dic={}
            if type(transition)==list:
                for choice in transition:
                    print(choice)
                    upper = "".join([c for c in choice if c.isupper()])
                    if not upper:
                        dic[choice]=[choice]
                        continue
                    if choice.replace(upper,"") not in dic: 
                        dic[choice.replace(upper,"")]=[upper]
                        continue

                    dic[choice.replace(upper,"")].append(upper)
                self.rules[state]=dic
            else:
                self.rules=self.grammar

    def _can_reach(self, state, input_string):
        if not input_string:
            return True
        for transition in self.transitions[state]:
            if transition[0] == input_string[0]:
                if self._can_reach(transition[-1], input_string[1:]):
                    return True
        return False

    def _can_generate(self, input_string):
        return self._can_reach(self.start_symbol, input_string)
    
    def canGenerate(self,input_string):
        if self._can_generate(input_string):
            print(f"The string '{input_string}' can be obtained from the grammar.")
        else:
            print(f"The string '{input_string}' cannot be obtained from the grammar.")
    def getAutomata(self,title):
        initial=self.start_symbol
        G = nx.DiGraph()
        edge_list = []
        node_colors = {}

        for node, edges in self.transitions.items():
            print(node,edges)
            if any(final in node for final in self.F):
                node_colors[node]="red"
            else:
                node_colors[node]="skyblue"
            
            for edge in edges:
                if type(edge[1]) == str:
                    G.add_edge(node, edge[1], label=edge[0])
                    edge_list.append(edge[0])
                    if any(final in edge[1] for final in self.F):
                        node_colors[edge[1]]="red"
                    else:
                        node_colors[edge[1]]="skyblue"
                    continue

                for choice in edge[1]:
                    G.add_edge(node, choice, label=edge[0])
                    edge_list.append(edge[0])

                    if any(final in choice for final in self.F):
                        node_colors[choice]="red"
                    else:
                        node_colors[choice]="skyblue"
                

        node_colors = node_colors.values()
        pos = nx.spring_layout(G)

        nx.draw(G, pos, with_labels=True, node_color=node_colors, font_size=12, font_weight="bold")
        for i,edge in enumerate(G.edges()):
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            x, y = (x0 + x1) / 2, (y0 + y1) / 2
                        
            x -= 0.02
            y += 0.08

            
            plt.text(x, y, edge_list[i], bbox=dict(facecolor='white', alpha=0.5), horizontalalignment='center')
        for i,node in enumerate(G.nodes()):
            if initial in node:
                x, y = pos[node]
                plt.annotate("", xy=(x, y), xytext=(x-20, y-20),
                 textcoords="offset points", ha="center", va="center",
                 arrowprops=dict(arrowstyle="->", linewidth=2))

        
        man = plt.get_current_fig_manager()
        man.set_window_title(title)
        plt.show()