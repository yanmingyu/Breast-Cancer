import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as snsfrom sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("./data.csv")