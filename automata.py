import networkx as nx
import matplotlib.pyplot as plt

from collections import defaultdict

class FiniteAutomaton:
    def __init__(self, grammar):
        self.grammar = grammar
        self.transitions = defaultdict(list)
        self.start_symbol = 'S'
        self._build_transitions()

    def _build_transitions(self):
        for non_terminal, productions in self.grammar.items():
            for production in productions:
                if len(production) > 1:
                    self.transitions[non_terminal].append((production[0], production[1:]))
                else:
                    self.transitions[non_terminal].append((production,))

    def _can_reach(self, state, input_string):
        if not input_string:
            return True
        for transition in self.transitions[state]:
            if transition[0] == input_string[0]:
                if self._can_reach(transition[-1], input_string[1:]):
                    return True
        return False

    def can_generate(self, input_string):
        return self._can_reach(self.start_symbol, input_string)

    def getAutomata(self):
        
        rules=self.grammar
        G = nx.DiGraph()
        n=0
        used_keys={}
        node_colors=[]

            

        for node, edges in rules.items():
            if node not in used_keys:
                used_keys[node] = n
                n +=  1
                node_colors.append("lightblue")

            for edge in edges:
                uppercase = [x for x in edge if x.isupper()]

                if uppercase:
                    for char in uppercase:
                        if char not in used_keys:
                            used_keys[char] = n
                            n +=  1
                            node_colors.append("lightblue")

                        
                        if G.has_edge(f'q_{used_keys[char]}',f'q_{used_keys[node]}'):
                            existing = G.get_edge_data(f'q_{used_keys[char]}',f'q_{used_keys[node]}')
                            G.add_weighted_edges_from([(f'q_{used_keys[node]}', f'q_{used_keys[char]}',f"{existing['weight']} \n{edge}")])
                        else:
                            G.add_edge(f'q_{used_keys[node]}', f'q_{used_keys[char]}',weight=edge)


                else:
                    if edge not in used_keys:
                        used_keys[edge] = n
                        n +=  1
                    G.add_edge(f'q_{used_keys[node]}', f'q_{used_keys[edge]}',weight=edge)
                    node_colors.append("red")


        G.add_edge(" ","q_0")

        node_colors.append("white")

        pos = {" ": (-10, 4), "q_0": (-1, 0)}

        spring_pos = nx.spring_layout(G, pos=pos, k=10,fixed=[" ","q_0"],weight="weights")

        pos.update(spring_pos)

        for node in pos:
            pos[node] = [pos[node][0] * 2, pos[node][1] * 2]

        weights = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1500)
        nx.draw_networkx_edges(G, pos, node_size=1500)
        nx.draw_networkx_labels(G, pos, font_weight='bold', font_size=12)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
        plt.show()
