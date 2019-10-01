import os
import argparse
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter,AutoMinorLocator

ap = argparse.ArgumentParser()

ap.add_argument("-o","--outfigure", required=True,
                help="Output Figure Name")
ap.add_argument("-wf", "--widthfig", required=False,
                help="Figure width in inches")
ap.add_argument("-hf", "--heightfig", required=False,
                help="Figure height in inches")
args = vars(ap.parse_args())


alexnet_data = [41.56,57.42,1.02]
inception_data = [37.94,60.93,1.13]
resnet_data = [35.86,62.95,1.19]

output = args['outfigure']

alexnet_no_fp = alexnet_data[0]
alexnet_fma = alexnet_data[1]
alexnet_other_fp = alexnet_data[2]

inception_no_fp = resnet_data[0]
inception_fma = resnet_data[1]
inception_other_fp = resnet_data[2]

resnet_no_fp = inception_data[0]
resnet_fma = inception_data[1]
resnet_other_fp = inception_data[2]


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


plt.rc('text', usetex=True)
plt.rcParams["font.family"] = "Times New Roman"
plt.rc('ytick', labelsize=12)
plt.rc('axes', labelsize=16)
plt.rc('xtick', labelsize=16)
plt.close('all')


ind = 0
width = 0.8
alpha = 1.0

fig, ax = plt.subplots()
p1 = ax.bar(x=ind, height=alexnet_other_fp, width=width, bottom=alexnet_no_fp+alexnet_fma, color=colour_wheel[7], alpha = alpha)
p2 = ax.bar(x=ind, height=alexnet_fma, width=width, bottom=alexnet_no_fp, color='grey', alpha = alpha*0.9)
p3 = ax.bar(x=ind, height=alexnet_no_fp, width=width, color=colour_wheel[22], alpha = alpha*0.8)

p4 = ax.bar(x=ind+1, height=inception_other_fp, width=width, bottom=inception_no_fp+inception_fma, color=colour_wheel[7], alpha = alpha)
p5 = ax.bar(x=ind+1, height=inception_fma, width=width, bottom=inception_no_fp, color='grey', alpha = alpha*0.9)
p6 = ax.bar(x=ind+1, height=inception_no_fp, width=width, color=colour_wheel[22], alpha = alpha*0.8)

p7 = ax.bar(x=ind+2, height=resnet_other_fp, width=width, bottom=resnet_no_fp+resnet_fma, color=colour_wheel[7], alpha = alpha)
p8 = ax.bar(x=ind+2, height=resnet_fma, width=width, bottom=resnet_no_fp, color='grey', alpha = alpha*0.9)
p9 = ax.bar(x=ind+2, height=resnet_no_fp, width=width, color=colour_wheel[22], alpha = alpha*0.8)

x = np.arange(3)
plt.xticks(x, ('AlexNet', 'Inception', 'ResNet'))
plt.ylabel('Percentage of Instructions')
ax.yaxis.major.formatter._useMathText = True
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.legend((p1[0],p2[0],p3[0]),('Other FP32','FMA','No FP'), frameon = False, loc='lower center',
          ncol = 3, handlelength=1, prop={'size':16}, bbox_to_anchor=(0.5,-0.17) )
plt.grid(b=True)
ax.set_axisbelow(True)
fig.set_size_inches(4, 6)
plt.savefig(output, dpi=300, bbox_inches='tight')
plt.show()

