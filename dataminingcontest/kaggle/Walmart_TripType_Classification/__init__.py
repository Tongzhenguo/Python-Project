import pandas as pd
import numpy as np

from sklearn import preprocessing
from scipy.spatial.distance import cosine

trainfile_orig = pd.read_csv('data_processing/train.csv')
trainfile = trainfile_orig.copy()

test_orig = pd.read_csv('data_processing/test.csv')
test = test_orig.copy()

