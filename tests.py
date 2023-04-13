import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lib.sd_util
import os
from pandasgui import show
import sys
from PyQt5.QtCore import QSize, Qt
import PyQt5.QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSlider, QVBoxLayout, QGridLayout, QGroupBox, QLabel

# constants
FNAME = 'tests/tests.csv'

# main entry
def main():
    test1()
    # test2()
    test3()

def test1():
    df = lib.sd_util.read(FNAME)
    lib.sd_util.graph(df)

def test2():
    df = pd.DataFrame({"time":None, "temperature":None},index=[0])
    print(df)

    plt.ion
    fig, ax = plt.subplots()

    gui = show(df, settings = {'block': False})

    i = 0
    while i < 100:
        ax.clear()
        j = np.random.choice(list(range(60,80)))
        df2 = pd.DataFrame({"time":i,"temperature":j}, index=[0])
        df = pd.concat([df,df2])
        pgdf = gui.store.data['df']
        pgdf.refresh_ui()
        print(df)
        # now live animate
        df.plot(x="time",y="temperature",ax=ax)
        plt.draw()
        plt.pause(1)
        i+=1

    plt.show()

def test3():
    
    class MainWindow(QWidget):
        def __init__(self):
            
            super().__init__()

            grid = QGridLayout()
            grid.addWidget(self.createSlider(),0, 0)
            self.setLayout(grid)
            self.setWindowTitle("Sustainable Data")
            self.resize(500, 500)

        def createSlider(self):
            groupBox = QGroupBox("Max Temp.")

            slider = QSlider(Qt.Horizontal)

            slider.label = QLabel(alignment=Qt.AlignCenter)
            label_minimum = QLabel(alignment=Qt.AlignLeft)
            slider.minimumChanged.connect(label_minimum.setNum)
            sjlider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue(77)
            slider.setTickPostition(QSlider.TicksBothSides)
            slider.setTickInterval(1)

            vbox = QVBoxLayout()
            vbox.addWidget(slider)
            groupBox.setLayout(vbox)

            return groupBox

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()


# running main 
if __name__ == '__main__':
    main()
