import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
Raw_Data = pd.read_csv("rawdata.csv")
counter = 0

for Experiment in Raw_Data["Experiment"].unique():
    counter += 1
    counter2 = 0
    if counter == 1:
        Expr_name = "Survival of Mosquitoes Exposed to DABS"
    if counter == 2:
        Expr_name = "Shelf Life of DABS 38 Days storage"
    if counter == 3:
        Expr_name = "Shelf Life of DABS 80 Days storage"
    if counter == 4:
        Expr_name = "Shelf Life of DABS 118 Days storage"
    if counter == 5:
        Expr_name = "DABS Performance on Unstarved Blood Fed Mosquitoes"
    if counter == 6:
        Expr_name = "DABS Performance on Starved Blood Fed Mosquitoes"
    if counter == 7:
        Expr_name = "DABS Performance on Parous Mosquitoes"
    if counter == 8:
        Expr_name = "Mechanism of Toxicity"
    Ex = Raw_Data[Raw_Data.Experiment == Experiment]
    Toxin_list = []
    Toxin_name_list = []
    input_data = []

    for Toxin_type in Ex["Toxin"].unique():
        Toxin_list.append(Ex[Ex.Toxin == Toxin_type])
        Toxin_name_list.append(str(Toxin_type))

    for data_toxin in Toxin_list:
        if Toxin_name_list[counter2] == "Control":
            color = 'rgba(93, 164, 214, 0.57)'
        if Toxin_name_list[counter2] == "Boric Acid":
            color = 'rgba(255, 65, 54, 0.57)'
        if Toxin_name_list[counter2] == "Control+Ablation":
            color = 'rgba(255, 144, 14, 0.57)'
        if Toxin_name_list[counter2] == "Boric Acid+Ablation":
            color = 'rgba(44, 160, 101, 0.57)'
        input_data.append(go.Box(
        x = data_toxin["Time_of_Exposure"],
        y = data_toxin["Mosquitoes"],
        name = Toxin_name_list[counter2],
        boxpoints = "all",
        hoverinfo = "text",
        jitter = 0.5,
        fillcolor = color,
        pointpos = -1.5,
        text = data_toxin["Replicate"],
        marker = dict(size = 5),
        line = dict(color = color)
        )
        )
        counter2 += 1
    layout = go.Layout(
        title = Expr_name,
        boxmode = "group",
        yaxis = dict(title = "Number of live mosquitoes"),
        xaxis = dict(title = "Time of exposure (hours)")
    )
    Figure  = go.Figure(data = input_data, layout = layout)
    plotly.offline.plot(Figure, filename = "%s.html" % Expr_name)
