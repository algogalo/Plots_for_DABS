import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

Raw_Data = pd.read_csv("rawdata.csv")

df = Raw_Data.loc[:,["Experiment", "Replicate", "Toxin", "Time_of_Exposure", "Mosquitoes"]]
