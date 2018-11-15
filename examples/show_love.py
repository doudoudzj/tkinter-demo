#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import math
import numpy as np

x = np.linspace(-2, 2, 200)
y1 = np.sqrt(1 - np.square(np.fabs(x) - 1))
y2 = np.arccos(1 - np.fabs(x)) - np.pi
plt.plot(x, y1, x, y2)
plt.axis([-2.5, 2.5, -3.5, 1.5])
