from bokeh.plotting import output_file, show, figure
import pandas

dataset=pandas.DataFrame(columns=['X','Y'])
dataset['X']=[1,2,3,4,5]
dataset['Y']=[1,4,9,16,25]

p=figure(plot_width=500, plot_height=400)
p.circle(dataset['X'],dataset['Y'],size=5)
output_file("Scatter_charts.html")
show(p)