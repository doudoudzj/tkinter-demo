#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 演示如何增加图例
# 图的背景显示有网格并设置网格颜色
from matplotlib import pyplot as plt

# 主要x 和y的个数要相同，不然会报错
x = [5, 6, 7, 8]
y = [7, 3, 8, 3]

x1 = [2, 5, 3, 9]
y1 = [5, 3, 2, 7]

# 可以设置颜色，g代表green, r代表red，y代表yellow，b代表blue，g代表black
# linewidth = 5，设置线条粗细
# label 设置线条名称
plt.plot(x, y, 'b', linewidth=5, label='Line One')
plt.plot(x1, y1, 'r', linewidth=8, label='Line Two')

# 给这个图，添加标题和XY轴名称，注意这地方不能输入中文，matplotlib应该
# 对中文支持不好，写中文，会显示乱码，方块字
plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True, color='k')

plt.show()
