

import unittest

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        #set the queue to an array of the entire node
        queue = [self]

        #use a current variable to store the current node at the beginning of the queue



        while len(queue) > 0:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for child in currentNode:
                queue.append(child)
        return array





def test_case_1():
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    array = []
    graph.breadthFirstSearch(array)
        #self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])


test_case_1()


