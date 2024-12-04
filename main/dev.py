from statsmodels.regression.rolling import RollingOLS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr
import yfinance as yf
import datetime as dt
import pandas_datareader
import warnings
warnings.filterwarnings('ignore')

pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

