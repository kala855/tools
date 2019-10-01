import os
import argparse
import pandas as pd
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter,AutoMinorLocator

# To parse the input arguments by command line
ap = argparse.ArgumentParser()
ap.add_argument("-f","--file", required=True,
                help = "csv file to be plotted")
ap.add_argument("-xl","--xlabel", required=False,
                help="X axis label name")
ap.add_argument("-yl","--ylabel", required=False,
                help="Y axis label name")
ap.add_argument("-o","--outfigure", required=False,
                help="Output Figure Name")
ap.add_argument("-wf", "--widthfig", required=False,
                help="Figure width in inches")
ap.add_argument("-hf", "--heightfig", required=False,
                help="Figure height in inches")
ap.add_argument("-ll","--legendloc", required=False,
                help="Legend location in the plot")

args = vars(ap.parse_args())
file = args['file']
xlabel = args['xlabel']
ylabel = args['ylabel']
output_name = args['outfigure']
width = args['widthfig']
height = args['heightfig']
legend_loc = args['legendloc']
data = pd.read_csv(file)


if xlabel is None:
    xlabel = 'Epochs'
if ylabel is None:
    ylabel = 'Accuracy'
if output_name is None:
    output_name = 'output.pdf'
if width is None:
    width = 9.0
else:
    width = float(width)
if height is None:
    height = 7.0
else:
    height = float(height)

if legend_loc is None:
    legend_loc = 'upper left'

# Plotting process starts here
# Make some style choices for plotting
colour_wheel =['#eeeeee',
               '#cccccc',
               '#999999',
               '#666666',
               '#333333',
               '#000000',
               '#329932',
               '#ff6961',
               'b',
               '#6a3d9a',
               '#fb9a99',
               '#e31a1c',
               '#fdbf6f',
               '#ff7f00',
               '#cab2d6',
               '#6a3d9a',
               '#ffff99',
               '#b15928',
               '#67001f',
               '#b2182b',
               '#d6604d',
               '#f4a582',
               '#fddbc7',
               '#f7f7f7',
               '#d1e5f0',
               '#92c5de',
               '#4393c3',
               '#2166ac',
               '#053061',
               '#5da687',
               '#66ad77',
               '#79b161',
               '#94b448',
               '#b4b32d',
               '#d8af0e',
               '#ffa600',
               '#979ca6',
               '#a39cbe',
               '#c696c5',
               '#f08bb6',
               '#ff848f',
               '#ff8d59',
               '#ffa600']



alpha = 1.0

plt.rcParams["font.family"] = "Times New Roman"
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('axes', labelsize=16)

labels = list(data.columns)[1:]

plt.close('all')
fig, ax = plt.subplots()

barWidth = 0.13
d1 = list(data['FP32'])
d2 = list(data['MP'])
d3 = list(data['DYN100'])
d4 = list(data['DYN300'])
d5 = list(data['DYN500'])
d6 = list(data['DYN1000'])
d7 = list(data['DYN2000'])

# Set position of bar on X axis

r1 = np.arange(len(d1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]

p1 = ax.bar(r1, d1, width = barWidth, label='FP32', color=colour_wheel[0], alpha=alpha)
p2 = ax.bar(r2, d2, width = barWidth, label='MP', color=colour_wheel[1], hatch='/', alpha=alpha)
p3 = ax.bar(r3, d3, width = barWidth, label='DYN100', color=colour_wheel[2], hatch='-', alpha=alpha)
p4 = ax.bar(r4, d4, width = barWidth, label='DYN300', color=colour_wheel[3], hatch='.', alpha=alpha)
p5 = ax.bar(r5, d5, width = barWidth, label='DYN500', color=colour_wheel[4], hatch='+', alpha=alpha)
p6 = ax.bar(r6, d6, width = barWidth, label='DYN1000', color=colour_wheel[5], hatch='O', alpha=alpha)
p7 = ax.bar(r7, d7, width = barWidth, label='DYN2000', color=colour_wheel[23], hatch='|', alpha=alpha)

ax.set_xlabel('Percentage Memory Instructions in the Critical Path')
ax.set_ylabel('Normalized Execution Time')
ax.set_ylim(0.3,1.0)
cur_axes = plt.gca()
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.major.formatter._useMathText = True
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.legend(bbox_to_anchor=(0.5,-0.17), frameon = False, loc='lower center', ncol = 7, handlelength=1, prop={'size':16})
plt.grid(b=True)
ax.set_axisbelow(True)
fig.set_size_inches(width, height)
plt.savefig(output_name, dpi=300)
plt.show()

