class Student:
    def __init__(self,height,name,age,smart):
        self.height = height
        self.name = name
        self.age= age
        self.smart = smart
    def results(self):
        print(f"stats of {self.name} are")
        print(f"{self.name} is {self.height}")
        print(f"{self.name} is {self.age} years of age ")
        print(f"{self.name} is {self.smart} smart")

import numpy as np
import matplotlib.pyplot as plt
class SimpleLinRegression:
    def __init__(self,data_set,target_data):
        self.data_set= data_set
        self.target_data=target_data
    def predict_y(self):
        x = np.array(self.data_set)
        y = np.array(self.target_data)
        n = len(x)
        ax = (n*np.sum(x*y)) - (np.sum(x))*(np.sum(y))
        bx = (n*np.sum(x*x))  - (np.sum(x)**2)
        m = ax/bx
        b = np.mean(y) - np.mean(x)*m
        y_pred = m*x +b
        return(y_pred)
    def plotup(self,x,y,y_pred):
        plt.scatter(x,y)
        plt.plot(x,y_pred)
        plt.show ()




        