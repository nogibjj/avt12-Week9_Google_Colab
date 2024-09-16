'''
library file
'''
import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(data):
    df = pd.read_csv(data)
    return df

#data1="NBA_Data.csv"
#df=pd.read_csv(data1)

#def grab_mean(data,col):
    #return data[col].mean()

#def create_histogram(data,col):
    #data[col].hist()
    #plt.xlabel('Values')
    #plt.ylabel('Frequency')
    #plt.title('Basic Histogram')




#def heat_map(data,col1,col2):
    #return 

#def grab_median(data,col):
    #return data[col].median()

#def grab_stdev(data,col):
    #return data[col].stdev()

#def grab_max(data,col):
    #return data[col].max()

def grab_mean(data,col):
    return data[col].mean()

def grab_median(data,col):
    return data[col].median()

def grab_stdev(data,col):
    return data[col].std()

def histogram_ast(data):
    df = load_dataset(data)
    plt.figure(figsize=(10, 6))
    plt.hist(df["AST"], bins=20)
    plt.title("Assists in 2023-24 Season-1")
    plt.xlabel("NBA Players")
    plt.ylabel("%")
    plt.savefig("assists.png")
    plt.show()


def bar_chart_points(data):
    df = pd.read_csv(data)
    plt.figure(figsize=(10, 6))
    plt.bar(df["Pos"], df["AST"], color="maroon", width=0.4)
    plt.xlabel("Players Position")
    plt.ylabel("Player Assists")
    plt.savefig("points_by_position1.png")
    plt.show()


    

