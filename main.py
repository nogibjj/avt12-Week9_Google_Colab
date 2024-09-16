from mylib.nbacheck import *


def g_describe(data):
    g=load_dataset(data)
    return nba_summary(g)

def save_to_md():
    test=g_describe(data1)
    with open("nbastats.md","a") as file:
        file.write("Describe:\n")
        file.write(test)
        file.write("n\n")
        file.write("![NBA_1](points_by_position.png)\n")
        file.write("n\n")
        file.write("![NBA_2](3_pt_data.png)\n")

if __name__ == "__main__":
    save_to_md()
