# To plot Top1 and Top5 graphs
python3 make_plot_top1_top5.py -f ../data/alexnet_data.csv -ll "lower right" -o alexnet_bs_256.pdf -wf 6 -hf 3
python3 make_plot_top1_top5.py -f ../data/inception_data.csv -ll "lower right" -o inception_bs_64.pdf -wf 6 -hf 3
python3 make_plot_top1_top5.py -f ../data/resnet_data.csv -ll "lower right" -o resnet_bs_64.pdf -wf 6 -hf 3
