import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import yfinance as yf
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
from matplotlib import markers
from streamlit_option_menu import option_menu
from ta.volatility import BollingerBands
from ta.trend import MACD, EMAIndicator, SMAIndicator
from ta.momentum import RSIIndicator
import datetime
import pytz
from datetime import date
import socket
from csv import writer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import os
pd.set_option('future.no_silent_downcasting', True)

######Halaman Utama
st.set_page_config(page_title="DOLMAS", layout="wide")
st.header('TRADING EMAS TERHADAP DOLLAR')
######End of Halaman Utama

###### FUNGSI MENU #############
def main():
    selected2 = option_menu(None, ["Home", "Cari Data", "Screener", 'Prediksi'], 
                            icons=['house', 'file-earmark-text', 
                            'sliders2-vertical', 'graph-up-arrow'], menu_icon="cast", default_index=0, orientation="horizontal")
    if selected2 == 'Cari Data':
         dataframe()
    else:
         tech_indicators(
### Taruh kalo ada menu
###### END OF FUNGSI MENU #############
@st.cache_resource

####### FUNGSI AMBIL DATA SAHAM ############
def download_data(op, start_date, end_date):
    df = yf.download(op, start=start_date, end=end_date, progress=False)
    return df
####### END OF FUNGSI AMBIL DATA SAHAM ############
