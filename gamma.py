# from math import *
# Q = 8000*1.602176634*10**(-19)#8000颗粒带电量1.602176634*10**(-19)
# #1.602189*10**(-19)
# e0 = 8.854187817*10**(-12)#真空介电常数
# b = 2.72*10**(-4)#颗粒平均间距
# kb = 1.380649*10**(-23)#玻尔兹曼常数
# T = 29053.68762#温度
# G = Q**2/(4*pi*e0*b*kb*T)#gamma
# print(G)


# def calculategamma(x):
#     gamma = pow(8000*1.6e-19,2)/(4*3.14*8.85e-12*2.7e-3*1.38e-23*x)
#     return gamma
#
# print(calculategamma(34278.00917))#debye400,kappa1.18

import numpy as np
def calcu_gamma(Q=8000*1.60e-19, Td=1000):
    b = pow(np.pi * 6400 / pow(0.0335, 2), -0.5)
    Qs = pow(Q, 2)
    fpibktd = 4 * np.pi*b*1.380649e-23 * Td * 8.854e-12
    return Qs / fpibktd
# print(calcu_gamma(Td=19299.58296))
# print(calcu_gamma(Td=26458.96))
# print(calcu_gamma(Td=34278.01))
# print(calcu_gamma(Td=35378.05))
# print(calcu_gamma(Td=33426.12))

print(calcu_gamma(Td=33553.63))

# b = 0.000236
# debey = 800e-6
# kappa = b/debey
# print(kappa)