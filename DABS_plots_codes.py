import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

Raw_Data = pd.read_csv("rawdata.csv")

df = Raw_Data.loc[:,["Experiment", "Replicate", "Toxin", "Time_of_Exposure", "Mosquitoes"]]

Experiment1 = df[df.Experiment == 1]

data_control = Experiment1[Experiment1.Toxin == "Ctrl"]

data_boric_acid = Experiment1[Experiment1.Toxin == "Boric_Acid"]

trace0 = go.Box(
    x = data_control["Time_of_Exposure"],
    y = data_control["Mosquitoes"],
    name = "Control",
    boxpoints = "all",
    hoverinfo = "text",
    jitter = 0.3,
    pointpos = -1.5,
    text = data_control["Replicate"],
    marker = dict(size = 5)
    )

trace1 = go.Box(
    x = data_boric_acid["Time_of_Exposure"],
    y = data_boric_acid["Mosquitoes"],
    name = "Boric_Acid",
    boxpoints = "all",
    hoverinfo = "text",
    jitter = 0.3,
    pointpos = -1.5,
    text = data_boric_acid["Replicate"],
    marker = dict(size = 5)
    )

input_data = [trace0, trace1]

layout = go.Layout(
    title = "Experiment 1",
    boxmode = "group",
    yaxis = dict(title = "Number of live mosquitoes"),
    xaxis = dict(title = "Time (hours)")
)
Figure  = go.Figure(data = input_data, layout = layout)
plotly.offline.plot(Figure)
