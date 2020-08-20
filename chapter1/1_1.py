import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# データをロードする
oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands =',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding="latinl", na_values="n/a")

# データを準備する

