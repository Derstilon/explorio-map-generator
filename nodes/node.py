from typing import List
import networkx as nx

class Node():
    @staticmethod
    def print_arguments(G: nx.DiGraph, node: str, keys: List[str]):
        return '\n'.join([f'{G.nodes[node][key]}' for key in keys if key in G.nodes[node]])
    
    @staticmethod
    def increment_label_counter(G: nx.DiGraph, counter: str):
        value = G.graph[counter]
        G.graph[counter] += 1
        return value