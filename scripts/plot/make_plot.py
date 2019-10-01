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
ap.add_argument("-c", "--columns", required=False,
                help = "comma separated columns numbers to plot, \
                if it is not defined then all columns are used")
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
ap.add_argument("-elimit","--epochslimit", required=False,
                help="Number of epochs to be plotted")

args = vars(ap.parse_args())
file = args['file']
xlabel = args['xlabel']
ylabel = args['ylabel']
output_name = args['outfigure']
width = args['widthfig']
height = args['heightfig']
legend_loc = args['legendloc']
xlimit = args['epochslimit']

data = pd.read_csv(file)
if args['columns'] is not None:
    columns = list(map(int,args['columns'].split(',')))
else:
    columns = range(0, len(data.columns))
data = data.iloc[:, columns]

if xlabel is None:
    xlabel = 'Epochs'
if ylabel is None:
    ylabel = 'Accuracy'
if output_name is None:
    output_name = 'output.pdf'
if width is None:
    width = 8.0
else:
    width = float(width)
if height is None:
    height = 6.0
else:
    height = float(height)
if legend_loc is None:
    legend_loc = 'upper left'

# Plotting process starts here
# Make some style choices for plotting
colour_wheel =['#329932',
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
            '#053061']

dashes_styles = [[3,1],
            [1000,1],
            [2,1,10,1],
            [4, 1, 1, 1, 1, 1]]

marker_styles = ['.',
                 ',',
                 'o',
                 'v',
                 '^',
                 '<',
                 '>',
                 '1',
                 '2',
                 '3',
                 '4',
                 '8',
                 's',
                 'p',
                 'P',
                 '*',
                 'h',
                 'H',
                 '+',
                 'x',
                 'X',
                 'D',
                 'd',
                 '|',
                 '_',
                 '0',
                 '1',
                 '2']

# plt.rc('font', family='New Roman', serif='Times')
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('axes', labelsize=14)


plt.close('all')
fig, ax = plt.subplots()
x = data.iloc[:,0]

for j,series in enumerate(data.columns[1:]):
    alpha_val = 0.9
    line_thick = 1.5
    ax.plot(x,
            data[series],
            color = colour_wheel[j%len(colour_wheel)],
            linestyle = '-',
            dashes = dashes_styles[j%len(dashes_styles)],
            lw = line_thick,
            label = series,
            alpha = alpha_val,
            marker = marker_styles[j%len(marker_styles)])


if xlimit is not None:
    ax.set_xlim(0,float(xlimit))

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.major.formatter._useMathText = True
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.legend(frameon = False, loc=legend_loc, ncol = 1, handlelength=3, prop={'size': 14})
plt.grid(b=True)
fig.set_size_inches(width, height)
plt.savefig(output_name, dpi=300, bbox_inches='tight')
plt.show()

