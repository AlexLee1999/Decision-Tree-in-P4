import numpy as np
import pandas as pd
import argparse
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz

parser = argparse.ArgumentParser()
parser.add_argument('-i', required=True)
parser.add_argument('-o', required=True)
args = parser.parse_args()
MAX_DEPTH = 3
i_file = args.i
o_file = args.o

def parse_tree(tree, features, file):
    left = tree.tree_.children_left
    right = tree.tree_.children_right
    threshold = tree.tree_.threshold
    fea = [features[i] for i in tree.tree_.feature]
    value = tree.tree_.value
    idx = np.argwhere(left == -1)[:, 0]

    def recurse(left, right, child, parse=None):
        if parse is None:
            parse = [child]
        if child in left:
            parent = np.where(left==child)[0].item()
            split = 'l'
        else:
            parent = np.where(right==child)[0].item()
            split = 'r'

        parse.append((parent, split, threshold[parent], fea[parent]))
        if parent == 0:
            parse.reverse()
            return parse
        else:
            return recurse(left, right, parent, parse)

    for i, child in enumerate(idx):
        to_write = ' when '
        for node in recurse(left, right, child):
            if len(str(node)) < MAX_DEPTH:
                continue

            if node[1] == 'l':
                to_write = to_write + node[3] + "<=" + str(node[2]) + ' and '
            else:
                to_write = to_write + node[3] + ">" + str(node[2]) + ' and '

        tmp = list(value[child][0])
        ind = tmp.index(max(tmp))
        to_write = to_write[:-4] + ' then ' + str(ind + 1)
        file.write(to_write)
        file.write(";\n")


set1 = pd.read_csv(i_file, on_bad_lines='skip')
set_data = set1.values.tolist()
X = [[i[2], i[7]] for i in set_data]
#X = [[i[2], int(i[3].replace(":", ""), 16), i[7]] for i in set_data]
y = [i[10] for i in set_data]
features = ['pkt_size', 'ip_protocol']
#features = ['pkt_size','eth_src','ip_protocol']
target = ["Smart Home Devices", "Sensors", "Audio Devices", "Video Devices", "Misc."]

X = np.array(X)
y = np.array(y)
dt_clf = DecisionTreeClassifier(max_depth=MAX_DEPTH)
dt_clf.fit(X,y)
dot_data = export_graphviz(dt_clf,
                           out_file=None,
                           feature_names=features,
                           class_names=target,
                           filled=True,
                           rounded=True)
graph = graphviz.Source(dot_data)
graph.format = 'png'
graph.render("decision_tree")
tree = open(o_file,"w+")
#tree.write("ip_proto = ")
#tree.write(str(ip_proto))
#tree.write(";\n")
parse_tree(dt_clf,features,tree)

tree.close()
