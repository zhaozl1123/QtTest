# self.mysql_connection_test.clicked.connect(MainWindow._mysql_connection_test)

import datetime
import numpy as np
import matplotlib.pyplot as plt


def histGraph4Pg(data: list, bins: int=200):
    res = plt.hist(data, bins=bins)
    ys = res[0].tolist()
    xs = res[1].tolist()
    _diffs = np.diff(xs)
    _gap = np.average(_diffs)
    xs = xs[0:-1] + _diffs
    return xs, ys, _gap

def getNowDateAndTime(format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(format)

def placeholdOrText(obj):
    if len(obj.text()) == 0:
        return obj.placeholderText()
    else:
        return obj.text()

def drawWithPyqtGraph(pltObj, data: list, item: str, color="r"):
    pltObj.plot(data, pen=color)


def transferTimestamp2FormatStr(timestamp: int, format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.fromtimestamp(int(timestamp)/1000000000).strftime(format)

if __name__ == '__main__':
    _time = "1614556800"
    print(transferTimestamp2FormatStr(_time))