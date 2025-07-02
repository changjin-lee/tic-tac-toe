# test-matplotlib.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import sys, os

# current_dir = os.path.abspath(os.path.dirname(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.append(parent_dir)

# Import rcParams to use Korean fonts.
from matplotlib import rcParams
rcParams["font.family"] = "Malgun Gothic"
rcParams["axes.unicode_minus"] = False

data = np.random.normal(0, 1, 1000) # 평균 0, 표준편차 1인 데이터 생성
plt.hist(data, bins=30) # 30개의 구간으로 나눔
plt.xlabel("값")
plt.ylabel("빈도")
plt.title("히스토그램")
plt.show()