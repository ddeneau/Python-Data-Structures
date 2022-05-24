# Accepts key-value pairs.
import email
from queue import Queue

from numpy import empty


class Node:

    def __init__(self, data):
        self.data = data


class PriorityQueue:

    def __init__(self):
        self.list = list()
        self.size = 0
        self.last_in = None

    def put_in(self, node):
        place_at = 0
        index = 0

        for node_in in list:
            if node_in < node:
                place_at = index
            else:
                index = index + 1


        self.list.insert(node, place_at)
        self.size = self.size + 1
        self.last_in = node


class Graph:

    def __init__(self):
        self.nodes = dict()  # Mapping of keys to nodes.
        self.mappings = dict()

    def add_node(self, key, data):
        self.nodes[key] = data
        self.mappings[data] = list()

    def add_adjacency(self, start, stop):
        neighbors = self.mappings.get(start)
        neighbors.apppend(stop)
        self.mappings[start] = neighbors

    def print(self):
        for n in self.nodes.keys():
            print(str(n))
    
    def breath_first_search(self, target):
        nodes_visited = PriorityQueue()
        lowest_cost = None

        while nodes_visited is empty:
            for edge in nodes_visited


