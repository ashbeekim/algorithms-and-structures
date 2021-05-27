##################################### Basic #####################################
import sys
import numpy as np
import pandas as pd
###################################################################################

##################################### Math #####################################
import math
from math import sin, cos, sqrt, atan2, radians
###################################################################################

##################################### Time #####################################
import time
from datetime import date
from datetime import timedelta
from datetime import datetime
import datetime as dt
import calendar
import holidays
###################################################################################

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
###################################################################################

##################################### Geometry #####################################
from folium import FeatureGroup, LayerControl, Map, Marker
from folium.plugins import HeatMap
import folium

import geoplotlib
###################################################################################

##################################### Seperate & Preprocessing & Engineering #####################################
from sklearn.model_selection import train_test_split, cross_val_score, KFold, StratifiedKFold, GroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
###################################################################################

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
###################################################################################

##################################### NY_TAXI #####################################


###################################################################################

##################################### NY_TAXI #####################################


###################################################################################

##################################### NY_TAXI #####################################


###################################################################################
