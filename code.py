import pandas as pd 
import plotly.figure_factory as ff 
import statistics as st 
import random

df = pd.read_csv("medium_data.csv/medium_data.csv")
data = df["reading_time"].tolist()

reading_mean = st.mean(data)

print(f"mean of reading time is : {reading_mean}")

data_set = []
for i in range(0,30):
    random_data = random.randint(0,len(data))
    value = data[random_data]
    data_set.append(value)
    
mean = st.mean(data_set)
std = st.stdev(data_set)

def random_mean(number):
    data_set = []
    for i in range(0,number):
        random_data = random.randint(0,len(data) - 1 )
        value = data[random_data]
        data_set.append(value)
    
    mean = st.mean(data_set)
    return mean
    
def setup():
    mean_list = []
    for i in range(0,100):
        set = random_mean(30)
        mean_list.append(set)
    mean = st.mean(mean_list)
    print(f"mean of sample is : {mean}")
    show_fig(mean_list)
    
def show_fig(m_list):
    fig = ff.create_distplot([m_list],["mean of list"], show_hist =False)
    fig.show()

setup()
#Standard deviation of the sampling mean = 1/10 of reading time Standard deviation