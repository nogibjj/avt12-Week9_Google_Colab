# avt12-Google Colab-Miniproject 9

In this project, while I forked over my first individual project, I have included a Google Colab link to run the Python script to prepare charts and tables separately. I include the link below. The data visualizations shown below reflect those rendered using Google Colab.

Format.yml
[![CI](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/format.yml/badge.svg)](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/format.yml)

Build.yml
[![CI](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/install.yml/badge.svg)](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/install.yml)

Test.yml
[![CI](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/test.yml/badge.svg)](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/test.yml)

Lint.yml
[![CI](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/lint.yml/badge.svg)](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/lint.yml)

## **Youtube Link to Walkthrough**
https://youtu.be/8j9T2OB416U

## **Diagram of Repository**

avt12-Week2Pandas/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── mylib/
│      └── library.py
│      └── __pycache__
├── .gitignore
├── assists.png
├── main.ipynb
├── main.py
├── Makefile
├── NBA_Data.csv
├── nbastats.md
├── points_by_position1.png
├── README.md
├── requirements.txt
├── test_lib.py
└── test_main.py

## **Data Source**

For this assignment, I used the records from the recently concluded 2023-2024 NBA season. This data was made available at basketball-reference.com, and I attach the link to the data below. In total, there are records from 572 players tracked within this dataset, and the variables featured include shooting percentages, assists, steals, turnovers, position, minutes played, age, and team. There were many ways this data could have been analyzed, but I was especially curious to learn more about assists, as I believe passing is a vital component of the game. The two graphs I include focus on assists, both with respect to position and with respect to the distribution of assists among players. https://www.basketball-reference.com/leagues/NBA_2024_totals.html

## **Functions**

As part of the data summary, the library contains several functions intended to highlight the data.

```grab_stdev(data,col)``` - returns the standard deviation of the provided column within the dataset

```grab_max(data,col)``` - returns the maximum value within the provided column within the dataset

```grab_median(data,col)``` - returns the median of the provided column within the dataset

```grab_mean(data,col)``` - returns the mean of all values within the provided column within the dataset

```histogram_ast(data)```  - prepares the graph for assists within the dataset. In this case, it is meant to represent the distribution of player assists.

```bar_chart_points(data)``` - this prepares a bar chart to show the assists based on position played by the player.

```create_histogram(data,col)``` - this function prepares a histogram to represent all the values within a provided column within the dataset.

```load_dataset(data)``` - loads the dataset into a pandas dataframe


## **Example Summary Output**

I include here a snapshot of the descriptive statistics, as applied to all variables present within the dataset.

<img width="605" alt="image" src="https://github.com/user-attachments/assets/91f6a5f3-4586-4575-993b-027aa91dbcae">


## **Data Visualizations**

Below showcases the two visualizations produced using the functions called in the main file. These both pertain to the assists distribution within the NBA from last season.

### Data Visualization 1 - Histogram of Assist Totals

![Figure_1](https://github.com/user-attachments/assets/3604d4c0-5e1b-4100-ae11-ce4ac4bf5cdc)

### Data Visualization 2 - Assists by Position

![Figure_2](https://github.com/user-attachments/assets/26724b1a-1fbf-432f-af89-7d68698a0e3d)





