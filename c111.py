import random 
import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff 
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
std = statistics.stdev(data)
mean = statistics.mean(data)

s_1_start, s_1_end = mean-std, mean+std
s_2_start, s_2_end = mean-(2*std), mean+(2*std)
s_3_start, s_3_end = mean-(3*std), mean+(3*std)


def setup():
    mean_list=[]
    for i in range(0,100):
        mean_sets = random_means(30)
        mean_list.append(mean_sets)
    show_graph(mean_list)

def random_means(counter):
    dataset=[]
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
    print("The mean of samples is "+str(mean))

def show_graph(mean_list):
    data_1 = mean_list
    sampling_mean =statistics.mean(mean_list)
    sampling_std = statistics.stdev(mean_list)
    print(sampling_mean)
    print(sampling_std)
    z_score = (sampling_mean/mean)/std
    print("The z score is "+ str(z_score))
    fig = ff.create_distplot([data_1],["claps"],show_hist= False)
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.20], mode="lines",  name="mean")) 
    fig.add_trace(go.Scatter(x=[sampling_mean,sampling_mean], y=[0,0.20], mode="lines",  name="Sample mean")) 
    fig.add_trace(go.Scatter(x=[s_1_start,s_1_start], y=[0,0.17], mode="lines",  name="Std 1 start"))
    fig.add_trace(go.Scatter(x=[s_1_end,s_1_end], y=[0,0.17], mode="lines",  name="Std 1 end"))
    fig.add_trace(go.Scatter(x=[s_2_start,s_2_start], y=[0,0.17], mode="lines",  name="Std 2 start"))
    fig.add_trace(go.Scatter(x=[s_2_end,s_2_end], y=[0,0.20], mode="lines",  name="Std 2 end"))
    fig.add_trace(go.Scatter(x=[s_3_start,s_3_start], y=[0,0.17], mode="lines",  name="Std 3 start"))
    fig.add_trace(go.Scatter(x=[s_3_end,s_3_end], y=[0,0.20], mode="lines",  name="Std 3 end"))

    fig.show()


setup()