# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:40:26 2020

@author: SP
"""
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:.2f}'.format

'''
1.Plot Total Sales Per Month for Year 2011.  How the total sales have
increased over months in Year 2011. Which month has lowest Sales?
'''
table1 = pd.read_csv("775_m6_datasets_v1.0/BigMartSalesData.csv")
table = table1.loc[table1['Year'] == 2011,['Month','Amount']]
table = table.groupby('Month')['Amount'].sum()
#print(table)
## second method
#table.plot.line()

## first method
#plt.plot(table)
#plt.ticklabel_format(style='plain')

'''
2.Plot Total Sales Per Month for Year 2011 as Bar Chart. Is Bar Chart 
Better to visualize than Simple Plot?

Enhancement
1.Change the bar chart to show the value of bar
'''

plt.ticklabel_format(style='plain')
table.sort_values().plot.bar()
l_data_pr = list(table)
def create_value_labels(l_data,decimals,x_adjust,y_adjust):
    for x,y in enumerate(l_data):
        plt.text(x+x_adjust,y+y_adjust,round(l_data[x],decimals),color='b',fontweight='bold')

create_value_labels(l_data_pr,1,0,-50)

'''
3.Plot Pie Chart for Year 2011 Country Wise.
Which Country contributes highest towards sales?

Enhancement
2.In Pie Chart Play With Parameters shadow=True, startangle=90 and
see how different the chart looks
'''
# table2 = table1.loc[table1['Year'] == 2011,['Country','Amount']]
# table2 = table2.groupby('Country')['Amount'].sum()
# table2.sort_values().plot.pie(shadow=True, startangle=90)

'''
4.Plot Scatter Plot for the invoice amounts and see the concentration 
of amount. In which range most of the invoice amounts are
concentrated

Enhancement
3.In scatter plot change the color of Scatter Points
'''
# table3 = table1.loc[table1['Year'] == 2011,['InvoiceNo','Amount']]
# table3 = table3.groupby('InvoiceNo')['Amount'].sum()
# plt.scatter(table3.values,table3.values,color='magenta')
# plt.grid()