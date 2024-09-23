from astropy.modeling import models, fitting
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([
    210,
    220,
    230,
    240,
    250,
    260,
    270,
    280,
    290
])
y = np.array([
0.952394009,
0.951573193,
0.955129981,
0.961422682,
0.96497947,
0.976744175,
0.986867309,
0.984404922,
0.970451415
])

g_init = models.Gaussian1D(amplitude=1., mean=250, stddev=10000.)
fit_g = fitting.LevMarLSQFitter()
g = fit_g(g_init, x, y)

print(g.mean.value, g.stddev.value)

a = np.array([
    210,
    220,
    230,
    240,
    250,
    260,
    270,
    280,
    290
])
b = g(a)

plt.title('高斯拟合', fontsize=20)
plt.xlabel('切割位置', fontsize=20)
plt.ylabel('准确率', fontsize=20)
plt.plot(a, b, '-', label='拟合曲线')
plt.plot(x, y, '.', label='原始数据')
plt.legend(fontsize=20) # 显示图例，即每条线对应 label 中的内容
plt.xlabel('切割位置', fontsize=20)
plt.show()