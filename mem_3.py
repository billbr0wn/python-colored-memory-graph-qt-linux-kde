#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
##from PyQt5.QtQuick import *
from PyQt5.uic import *
##from PyQt5.QtQml import *
from PyQt5.QtChart import *
import psutil
import random



#-------------------------------------------------
    
__author__ = '__Bill__'



class _Window_(QMainWindow):
    """
    -------------------(_Example_)------------------
    """
    def __init__(self):
        super().__init__()
        print(_Window_.__doc__)




#-----------------------drop shadow ---------------o

        self.effect = QGraphicsDropShadowEffect()

        self.effect = QGraphicsDropShadowEffect()
        self.effect.setBlurRadius(10)
        self.effect.setXOffset(5)
        self.effect.setYOffset(-5)
        self.effect.setColor(Qt.black)

        
#-------------timer-----------------

        self.cpu_percentage = psutil.cpu_percent(interval=0.05)
        self.memory = psutil.virtual_memory()[5]
        self.memory_percent = self.memory / 80000000
        print('self.memory_percent  = ', self.memory_percent)
        self.switch_functions = (False)
        
       
        self.timer  = QTimer()
        self.timer.timeout.connect(self.update_bar__)
        self.timer.start(750)
        
        
        self.blank_tick = (0)


#------------memory values-----------------o
        
        self.tick_mem_0 = (100)
        self.tick_mem_1 = (100)
        self.tick_mem_2 = (100)
        self.tick_mem_3 = (100)
        self.tick_mem_4 = (100)
        self.tick_mem_5 = (100)
        self.tick_mem_6 = (100)
        self.tick_mem_7 = (100)

        self.series_bottom = QLineSeries()
        self.series_mem = QLineSeries()
        self.series_cpu2 = QLineSeries()

        self.series_bottom << QPointF(0, 0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(0,0) << QPointF(7,0);



#--------------add values to chart-----------------------o
        
        self.series_mem.append(0, self.tick_mem_0);
        self.series_mem.append(0, self.tick_mem_1);
        self.series_mem.append(0, self.tick_mem_2);
        self.series_mem.append(0, self.tick_mem_3);
        self.series_mem.append(0, self.tick_mem_4);
        self.series_mem.append(0, self.tick_mem_5);
        self.series_mem.append(0, self.tick_mem_6);
        self.series_mem.append(0, self.tick_mem_7);

        
        self.series = QAreaSeries(self.series_bottom, self.series_mem)
        
        self.series.setName("Batman")
        self.series.setBorderColor(QColor.fromRgb(25,25,25, 5)) #color for center line

  

#-----------background-chart---------------------

        self.chart = QChart()
        self.chart_blank = QChart()
        
        self.chart.addSeries(self.series);
        
        self.chart.setTitle("memory");


        self.chart.axisX = QValueAxis()
        self.chart.setAxisX(self.chart.axisX)
        self.chart.addAxis(self.chart.axisX, Qt.AlignBottom);

        
        self.chart.axisY = QValueAxis()
        self.chart.setAxisY(self.chart.axisY)
        self.chart.addAxis(self.chart.axisY, Qt.AlignRight);

        self.chart.setBackgroundBrush(QColor.fromRgb(25,25,25, 0))# transparent background

        self.chart.legend().setVisible(False);#turn off graph legend    
        self.chart.setDropShadowEnabled(True) #shadow under window
        self.chart.setPlotAreaBackgroundVisible(False)
        

        
#------------chart view---------------------
  
        self.chartView = QChartView(self.chart);
        self.chartView.setRenderHint(QPainter.Antialiasing);
    
        self.chartView.setChart(self.chart)
        self.chart.setMargins(QMargins(-65,0,0,0))#how much of chart is visible

        self.initGUI()

        
        
    def update_bar__(self):
        #print('update_bar__')

        self.memory = psutil.virtual_memory()[5]
        self.memory_percent = self.memory / 80000000

        self.chart.removeAllSeries() #clear graph readout before next data entry

        self.cpu_percentage = psutil.cpu_percent(interval=0.05)
        self.tick_mem_7 = self.memory_percent
                        
        self.tick_mem_0 = self.tick_mem_1#sequence values
        self.tick_mem_1 = self.tick_mem_2
        self.tick_mem_2 = self.tick_mem_3
        self.tick_mem_3 = self.tick_mem_4
        self.tick_mem_4 = self.tick_mem_5
        self.tick_mem_5 = self.tick_mem_6
        self.tick_mem_6 = self.tick_mem_7


        self.series_bottom = QLineSeries()
        self.series_mem = QLineSeries()

        self.series_bottom.append(0, self.blank_tick);#bottom of graph
        self.series_bottom.append(1, self.blank_tick);
        self.series_bottom.append(2, self.blank_tick);
        self.series_bottom.append(3, self.blank_tick);
        self.series_bottom.append(4, self.blank_tick);
        self.series_bottom.append(5, self.blank_tick);
        self.series_bottom.append(6, self.blank_tick);
        self.series_bottom.append(7, self.blank_tick);

#-----------
        
        self.series_mem.append(0, 100);#load values
        self.series_mem.append(1, self.tick_mem_1);#top edge
        self.series_mem.append(2, self.tick_mem_2);
        self.series_mem.append(3, self.tick_mem_3);
        self.series_mem.append(4, self.tick_mem_4);
        self.series_mem.append(5, self.tick_mem_5);
        self.series_mem.append(6, self.tick_mem_6);
        self.series_mem.append(7, self.tick_mem_7);


#------------------load into new graph
        
        self.series = QAreaSeries(self.series_bottom, self.series_mem)
        self.series.setColor(QColor.fromRgb(0, 204, 0, 90))#set color for graph readout
        self.chart.addSeries(self.series)

        print('self.memory_percent  = ', self.memory_percent)

        

    def initGUI(self):

        self.setWindowFlags(Qt.FramelessWindowHint # hides the window controls
                             #| Qt.SplashScreen |#
                              | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGraphicsEffect(self.effect)

        self.setCentralWidget(self.chartView);
        #self.setGeometry(500,200, 100,20)
        self.resize(250, 150);
        self.move(1700,750)
        self.setWindowTitle('My Window')
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    _Win_ = _Window_()
    app.exec_()
