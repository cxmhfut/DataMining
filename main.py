# encoding=utf-8

import trees
import treePlotter

fr = open('golf.txt', 'r')
golf = [inst.strip().split(' ') for inst in fr.readlines()]
print(golf)
golfLabels = ['Outlook', 'Temperature', 'Humidity', 'Windy']
golfTree = trees.createTree(golf, golfLabels)
print(golfTree)
treePlotter.createPlot(golfTree)
