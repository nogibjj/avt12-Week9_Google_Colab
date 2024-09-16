from main import g_describe, save_to_md

test_file="NBA_Data.csv"

def test_describe():
    # testing out nba_summary
    test_summary=g_describe(test_file)
    assert test_summary.shape == (8,27)
    

def test_markdown():
    #converts to markdown
    save_to_md(test_file)





if __name__ == "__main__":
    test_describe()
    test_markdown()
