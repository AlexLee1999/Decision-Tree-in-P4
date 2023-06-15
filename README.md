# Decision Tree in P4
## Table of contents
- [Decision Tree in P4](#decision-tree-in-p4)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Dataset](#dataset)
  - [Usage](#usage)
  - [Requirements](#requirements)
  - [References](#references)

## Introduction
- Implement the Decision Tree method in the [paper](https://www.cl.cam.ac.uk/~nz247/publications/xiong2019dream.pdf)
- Based on the framework from P4 Tutorial exercises, we implement the Packet Classifier in P4. 

## Dataset
- [IOT TRAFFIC TRACES](https://iotanalytics.unsw.edu.au/iottraces.html) (September 22nd, 2016)


## Usage
Run Decision Tree:
```
python3 decisionTree.py -i <input_file> <output_file>
```

Build mininet & run 
```
make run 
xterm h1 h2
```

Send data
```
python3 send_with_length.py <ip_address> <message length> <TCP/UDP>
```

Receiving data

```
python3 receive.py
```


## Requirements

- python >=3.6
- numpy
- pandas
- scikit-learn
- graphviz
- scapy

## References

- [P4 Tutorial](https://github.com/p4lang/tutorials)
- [Do Switches Dream of Machine Learning? Toward In-Network Classification](https://www.cl.cam.ac.uk/~nz247/publications/xiong2019dream.pdf)

