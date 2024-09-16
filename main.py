import pandas as pd
import matplotlib.pyplot as plt

data1="NBA_Data.csv"

def load_dataset(data):
    df=pd.read_csv(data)
    return df

def nba_summary(data):
    return data.describe()

def histogram_3ptfg(data):
    plt.figure(figsize=(10,6))
    plt.hist(data["3P%"], bins=20)
    plt.title("3 Point Percentage in 2023-24 Season-1")
    plt.xlabel("NBA Players")
    plt.ylabel("%")
    plt.savefig("3_pt_data.png")
    return plt.show()

def bar_chart_points(data):
    df=pd.read_csv(data)
    plt.figure(figsize=(10,6))
    plt.bar(df["Pos"],df["PTS"],color ='maroon', 
        width = 0.4)
    plt.savefig("points_by_position.png")
    plt.show()

def g_describe(data):
    g=load_dataset(data)
    return nba_summary(g)

histogram_3ptfg(data1)
bar_chart_points(data1)

def save_to_md():
    test=g_describe(data1)
    with open("nbastats.md","a", encoding='utf-8') as file:
        file.write("Describe:\n")
        file.write(test)
        file.write("n\n")
        file.write("![NBA_1](points_by_position.png)\n")
        file.write("n\n")
        file.write("![NBA_2](3_pt_data.png)\n")

if __name__ == "__main__":
    save_to_md()
