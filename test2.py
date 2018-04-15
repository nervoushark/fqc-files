#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget


# if __name__ == '__main__':

#     app = QApplication(sys.argv)

#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('Simple')
#     w.show()

#     sys.exit(app.exec_())

import sys
import random

class Neuron:
    """docstring for ClassName"""
    def __init__(self, name):
        self.name = ""
        self.__weight = random.random()  

    def __str__(self):
        return("Neuron name: " + self.name + " (" + str(self.__weight) + ")")

class Layer:
    """docstring for """
    def __init__(self):
        self.neurons = []
        self.prevLayer = None
        self.nextLayer = None
    # def 
      
class InputLayer(Layer):
    """docstring for """
    def __init__(self):
        super(InputLayer, self).__init__()
                 
class TestInputLayer(Layer):
    """docstring for """
    def __init__(self):
        # self.neurons = []
        super(TestInputLayer, self).__init__("1", 3)
        names = ["Credit sum", "Gender", "Education"]
        for i in names:
            self.neurons.append(Neuron(i))

# class ClassName(object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         super(ClassName, self).__init__()
#         self.arg = arg
        
        
if __name__ == '__main__':
    n = Neuron("Neuron First")
    print(n)
    # n.setName("asd")
    # try:
    #     print("Neuron name:", n.name)
    # except Exception:
    #     print("Can't get access to attr")
    # s = n.getName
    # print(Neuron.getName(n))
    # g = Neuron("Neuron Second")
    # print(g)
    