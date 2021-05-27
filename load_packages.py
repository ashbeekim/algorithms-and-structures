##################################### Connect between colab and kaggle #####################################
#구글드라이브 마운트
import os
from google.colab import drive  
drive.mount('/content/drive')

# 파일 업로드
from google.colab import files
files.upload()

#코랩-캐글
# Ensure kaggle.json is in the location ~/.kaggle/kaggle.json to use the API.
!mkdir -p ~/.kaggle #sample_data에 저장됨
!cp kaggle.json ~/.kaggle
# Permission Warning 이 일어나지 않도록 
!chmod 600 ~/.kaggle/kaggle.json
!cd ~/.kaggle  
############################################################################################################

##################################### Mount colab to google drive #####################################
#구글 드라이브에 캐글 데이터 다운로드
import os  
os.environ['KAGGLE_CONFIG_DIR'] = "~/.kaggle/"
from google.colab import drive  
drive.mount('/content/drive')
!cd ~/.kaggle  

# # # 본인이 참가한 모든 대회 보기 
!kaggle competitions list
# 캐글 데이터셋 리스트 확인
!kaggle datasets list
#캐글 데이터셋 리스트 검색
!kaggle datasets list -s Movies
# !kaggle competitions download -c house-prices-advanced-regression-techniques
# !kaggle datasets download -d percevalw/englishfrench-translations  
# !unzip englishfrench-translations.zip  
# !ls
#######################################################################################################

##################################### Basic #####################################
import os
import sys
import numpy as np
import pandas as pd
from tqdm.notebook import trange, tqdm
import json

# 최대 줄 수 설정
pd.set_option('display.max_rows', 1500)
# 최대 열 수 설정
pd.set_option('display.max_columns', 1500)
# 표시할 가로의 길이
pd.set_option('display.width', 1500)
###################################################################################

##################################### Math #####################################
import math
from math import sin, cos, sqrt, atan2, radians
################################################################################

##################################### Time #####################################
import time
from datetime import date
from datetime import timedelta
from datetime import datetime
import datetime as dt
import calendar
import holidays
################################################################################

##################################### Visualization #####################################
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from pandas.plotting import scatter_matrix
import matplotlib.dates as mdates
import matplotlib as mpl

import plotly.express as px
import altair as alt

import ggplot
import pygal
import gleam
import bokeh
import missingo
########################################################################################

##################################### Geometry #####################################
import haversine as hs
from haversine import haversine, Unit

from folium import FeatureGroup, LayerControl, Map, Marker
from folium.plugins import HeatMap
import folium

import geoplotlib

import mapboxgl
mapboxgl.__version__
MAPBOX_API_KEY = "자신의 mapbox api token (pk... 로 시작함)"
from mapboxgl.viz import *
import pydeck as pdk
####################################################################################

##################################### Seperate & Preprocessing & Engineering #####################################
from sklearn.model_selection import train_test_split, cross_val_score, KFold, StratifiedKFold, GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
##################################################################################################################

##################################### Machine Learning #####################################
#from sklearn.ensemble import (RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier)

import lightgbm as lgb
import xgboost as xgb
from xgboost import XGBRegressor, XGBRFRegressor

#from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor 
#캐글버전땜에 안 되는듯...
from sklearn.decomposition import PCA

from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
########################################################################################

##################################### Evaluation #####################################
from sklearn.metrics import roc_curve
from sklearn.metrics import recall_score, f1_score, roc_auc_score 
from sklearn.metrics import accuracy_score, precision_score, precision_recall_curve
from sklearn.metrics import explained_variance_score
######################################################################################

##################################### Analysis #####################################
import statsmodels.api as sm
from sklearn.inspection import permutation_importance
from sklearn.metrics import classification_report, confusion_matrix
from xgboost import plot_importance
####################################################################################

##################################### Setting #####################################
import warnings
warnings.simplefilter('ignore')
warnings.filterwarnings('ignore')
import gc
gc.collect()
import subprocess

# # # tips(from 현호님)  #속도 빨라짐
# from numba import cuda, jit, prange, vectorize, guvectorize
# #numba
# @jit(nopython=True)
# #prange 병렬화
# @jit(nopython=True, parallel=True)
####################################################################################

#[package list] https://pandas.pydata.org/pandas-docs/stable/ecosystem.html?highlight=geo
