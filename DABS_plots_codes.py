import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
Raw_Data = pd.read_csv("rawdata.csv")

#Plot Experiment 1
Experiment1 = Raw_Data[Raw_Data.Experiment == 1]
Toxin_list = []
input_data = []

for Toxin_type in Experiment1["Toxin"].unique():
    Toxin_list.append(Experiment1[Experiment1.Toxin == Toxin_type])

for data_toxin in Toxin_list:
    input_data.append(go.Box(
    x = data_toxin["Time_of_Exposure"],
    y = data_toxin["Mosquitoes"],
    boxpoints = "all",
    hoverinfo = "text",
    jitter = 0.5,
    pointpos = -1.5,
    text = data_toxin["Replicate"],
    marker = dict(size = 5)
    )
    )
layout = go.Layout(
    title = "Experiment 1",
    boxmode = "group",
    yaxis = dict(title = "Number of live mosquitoes"),
    xaxis = dict(title = "Time of exposure (hours)")
)
Figure  = go.Figure(data = input_data, layout = layout)
plotly.offline.plot(Figure, filename = "Experiment1.html")

#Plot Experiment 2

Experiment2 = Raw_Data[Raw_Data.Experiment == 2]
Toxin_list = []
input_data = []

for Toxin_type in Experiment2["Toxin"].unique():
    Toxin_list.append(Experiment2[Experiment2.Toxin == Toxin_type])

for data_toxin in Toxin_list:
    input_data.append(go.Box(
    x = data_toxin["Time_of_Exposure"],
    y = data_toxin["Mosquitoes"],
    boxpoints = "all",
    hoverinfo = "text",
    jitter = 0.5,
    pointpos = -1.5,
    text = data_toxin["Replicate"],
    marker = dict(size = 5)
    )
    )
layout = go.Layout(
    title = "Experiment 2",
    boxmode = "group",
    yaxis = dict(title = "Number of live mosquitoes"),
    xaxis = dict(title = "Time of exposure (hours)")
)
Figure  = go.Figure(data = input_data, layout = layout)
plotly.offline.plot(Figure, filename = "Experiment2.html")

#Plot Experiment 3

Experiment3 = Raw_Data[Raw_Data.Experiment == 2]
Toxin_list = []
input_data = []

for Toxin_type in Experiment3["Toxin"].unique():
    Toxin_list.append(Experiment3[Experiment3.Toxin == Toxin_type])

for data_toxin in Toxin_list:
    input_data.append(go.Box(
    x = data_toxin["Time_of_Exposure"],
    y = data_toxin["Mosquitoes"],
    boxpoints = "all",
    hoverinfo = "text",
    jitter = 0.5,
    pointpos = -1.5,
    text = data_toxin["Replicate"],
    marker = dict(size = 5)
    )
    )
layout = go.Layout(
    title = "Experiment 3",
    boxmode = "group",
    yaxis = dict(title = "Number of live mosquitoes"),
    xaxis = dict(title = "Time of exposure (hours)")
)
Figure  = go.Figure(data = input_data, layout = layout)
plotly.offline.plot(Figure, filename = "Experiment3.html")

#Plot Experiment 4

Experiment4 = Raw_Data[Raw_Data.Experiment == 2]
Toxin_list = []
input_data = []

for Toxin_type in Experiment4["Toxin"].unique():
    Toxin_list.append(Experiment4[Experiment4.Toxin == Toxin_type])

for data_toxin in Toxin_list:
    input_data.append(go.Box(
    x = data_toxin["Time_of_Exposure"],
    y = data_toxin["Mosquitoes"],
    boxpoints = "all",
    hoverinfo = "text",
    jitter = 0.5,
    pointpos = -1.5,
    text = data_toxin["Replicate"],
    marker = dict(size = 5)
    )
    )
layout = go.Layout(
    title = "Experiment 4",
    boxmode = "group",
    yaxis = dict(title = "Number of live mosquitoes"),
    xaxis = dict(title = "Time of exposure (hours)")
)
Figure  = go.Figure(data = input_data, layout = layout)
plotly.offline.plot(Figure, filename = "Experiment4.html")
