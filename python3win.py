from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


def func(x, a1, a2, a3, a4):
    return a1*np.sin(a2*(x+a3))+a4  # 自定义要拟合的函数


data = np.array(pd.read_csv("D:\WORK\GitHub\SCUPT\data.csv"))  # 从csv文件获取数据
x0 = np.array(data[:, 0])
y0 = np.array(data[:, 1])
x = np.linspace(0, 3, 300)

popt, pcov = curve_fit(func, x0, y0)
a1 = popt[0]
a2 = popt[1]
a3 = popt[2]
a4 = popt[3]
print(a1, a2, a3, a4)
y = func(x, a1, a2, a3, a4)
# 进行拟合，获得四个系数，并构建函数

plt.figure(figsize=(8, 4))
plt.scatter(x0, y0, 16, marker='o',
            color='r',
            label="实验结果")  # 绘制散点图
plt.plot(x, y, 'b',
         linewidth=1,
         label="拟合曲线")

plt.xlabel("T(S)")
plt.ylabel("X(mm)")
plt.legend()
plt.title("摩擦振子实验结果及正弦拟合", fontsize=16)
plt.show()