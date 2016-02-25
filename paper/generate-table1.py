#!/usr/bin/env python

import matplotlib.pyplot as plt

# ./align -n 10 | ./score-alignments

data = {
    'align': {
        10: {
            "Precision": 0.237037,
            "Recall": 0.280374,
            "AER": 0.750663,
            "Time": 0.18
        },
        100: {
            'Precision': 0.449653,
            'Recall': 0.405325,
            'AER': 0.566740,
            "Time": 2.49
        },
        500: {
            'Precision': 0.555809,
            'Recall': 0.470414,
            'AER': 0.481338,
            'Time': 30.6
        },
        1000: {
            'Precision': 0.582734,
            'Recall': 0.488166,
            'AER': 0.459603,
            'Time': 91.3
        },
        2000: {
            'Precision': 0.596698,
            'Recall': 0.517751,
            'AER': 0.438320,
            'Time': 284.58
        }
    }
}

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.scatter(data['align'].keys(),
            [data['align'][n]['Precision'] for n in data['align'].keys()],
            s=20, c='b', marker='o', label="Precision")
ax1.scatter(data['align'].keys(),
            [data['align'][n]['Recall'] for n in data['align'].keys()],
            s=20, c='r', marker='o', label="Recall")
ax1.scatter(data['align'].keys(),
            [data['align'][n]['AER'] for n in data['align'].keys()],
            s=20, c='g', marker='o', label="AER")

ax2.scatter(data['align'].keys(),
            [data['align'][n]['Time'] for n in data['align'].keys()],
            s=10, c='k', marker='o', label="Time")

plt.legend(loc="upper left")
plt.show()
