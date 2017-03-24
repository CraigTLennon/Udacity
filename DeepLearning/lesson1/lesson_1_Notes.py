'''
Created on Mar 24, 2017

@author: clennon
'''
#test import
#import tensorflow as tf
import numpy as np
import math as m 

def softmax(x):
  
    return np.exp(x)/np.sum(np.exp(x), axis=0)

#test
# print(softmax([1,1,1,1,1,1]))
# print(softmax([0,0,0,0,]))
# print(softmax([0,0,0,0,1,0]))
# print(softmax([1,0,2,3,.9,1]))

# scores=[3,1,0.2]
# print(softmax(scores))
# import matplotlib.pyplot as plt
# import matplotlib as mp 
# 
# print(mp.matplotlib_fname())
# x=np.arange(-2.0,6.0,0.1)
# scores=np.vstack([x,np.ones_like(x),0.2*np.ones_like(x)])
# plt.plot(x, softmax(scores).T, linewidth=2)
# plt.show()

# x=1000000000
# y=1000000000
# for i in range(0,1000000):
#     x=x-.000001
# print(y-x)

#Guideline, have zero mean and equal variance when DivisionImpossible
