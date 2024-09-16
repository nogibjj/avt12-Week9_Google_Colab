'''
library file
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data1="NBA_Data.csv"

def load_dataset(data):
    df=pd.read_csv(data)
    return df

def grab_mean(data,col):
    return data[col].mean()

def create_histogram(data,col):
    data[col].hist()
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Basic Histogram')


def nba_summary(data):
    return data.describe()

def heat_map(data,col1,col2):
    return 

def grab_median(data,col):
    return data[col].median()

def grab_stdev(data,col):
    return data[col].stdev()

def grab_max(data,col):
    return data[col].max()

def histogram_3ptfg(data):
    plt.figure(figsize=(10,6))
    plt.hist(data["3P%"], bins=20)
    plt.title("3 Point Percentage in 2023-24 Season")
    plt.xlabel("NBA Players")
    plt.ylabel("%")
    plt.savefig("3_pt_data.png")
    plt.show()

def bar_chart_points(data):
    df=pd.read_csv(data)
    plt.figure(figsize=(10,6))
    plt.bar(df["Pos"],df["PTS"],color ='maroon', 
        width = 0.4)
    plt.savefig("points_by_position.png")
    plt.show()
    

