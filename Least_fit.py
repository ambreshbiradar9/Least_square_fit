import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt

df=pd.read_excel(r'C:\Users\Srinivas\Desktop\Coding\points_1.xlsx')
x=df['X'].to_numpy()
k=df['Z'].to_numpy()

x = np.linspace(0, 1, 101)
y=1+x+x*np.random.random(len(x))

plt.figure(figsize=(10,8))

def func(x,a,b):
    k=a*x+b
    return k

alpha=optimize.curve_fit(func,xdata=x,ydata=y)[0]
plt.figure(figsize=(10,8))
plt.plot(x,y,'b.')
plt.plot(x,alpha[0]*x+alpha[1],'r')