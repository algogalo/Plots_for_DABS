import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)

Raw_Data = pd.read_csv("rawdata.csv")

Ex_8 = Raw_Data[Raw_Data.Experiment == 8]
Ex_8 = Raw_Data[Raw_Data.Experiment == 8]
Toxin_list = []
array_list = []
for Toxin_type in Ex_8["Toxin"].unique():
    Toxin_list.append(Ex_8[Ex_8.Toxin == Toxin_type])

for data_toxin in Toxin_list:
    data_time = data_toxin[data_toxin.Time_of_Exposure == 48]
    array_list.append(data_time["Mosquitoes"])
print "Descriptive Statistics 1"
print array_list[0].describe()
print "Descriptive Statistics 2"
print array_list[1].describe()
print "Descriptive Statistics 3"
print array_list[2].describe()
print "Descriptive Statistics 4"
print array_list[3].describe()


print stats.f_oneway(array_list[0], array_list[1], array_list[2],array_list[3])

Ex_8_48h = Ex_8[Ex_8.Time_of_Exposure == 48]
Ex_8_48h_Toxincounts = Ex_8_48h.loc[:,['Toxin', 'Mosquitoes']]

MultiComp = MultiComparison(Ex_8_48h_Toxincounts['Mosquitoes'],
                            Ex_8_48h_Toxincounts['Toxin'])

print(MultiComp.tukeyhsd().summary())
