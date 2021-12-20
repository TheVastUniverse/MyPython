"""
作者：小宇
日期：2021年12月20日
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = [u'SimHei']  # 设置字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示坐标轴负号

x = np.arange(-10, 12, 1)  # x从-10取到12，间距为1（不设置则默认为1），取左不取右

plt.title("示例")  # 设置标题

plt.text(12, -4, "练习$ \\alpha \\beta \pi \lambda \omega $", size=15)
# 在坐标(12,-4)处添加文本，大小为15，用$\‘数学符号’$的形式可在文本中显示数学符号（两个'\'连在一起表示显示一个'\'）

plt.plot(x, x, color='g', marker='^')  # color设置颜色（不设置则自动选择颜色），marker设置点的形状（不设置则不显示）
plt.plot(x, x * 2, color='0.5', marker='p')
plt.plot(x, x * 3, color='#FF00FF', marker='.')
plt.plot(x, x * 4, color=(0.1, 0.2, 0.3), marker='*')
plt.legend(['一', '二', '三', '四'])  # 对应各曲线设置图例

plt.xlim(xmin=-5, xmax=20)  # 调整坐标轴范围
plt.ylim(ymin=-10, ymax=20)

plt.locator_params('x', nbins=20)  # 设置坐标轴刻度数目
plt.locator_params('y', nbins=15)
# plt.locator_params(nbins=20) #同时对x,y轴进行设置

plt.xlabel("x-axis")  # 设置x轴文字显示
plt.ylabel("y-axis")  # 设置y轴文字显示

plt.show()
