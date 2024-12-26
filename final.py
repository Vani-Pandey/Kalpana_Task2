from PyQt5.QtWidgets import (QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,QWidget, QTabWidget, QGridLayout, QPushButton,QFrame,QMainWindow)
from PyQt5.QtGui import QPixmap,QPalette, QBrush, QLinearGradient, QColor
from PyQt5.QtCore import Qt,QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import sys
plt.rcParams.update({
    'font.size': 8,             
    'xtick.labelsize': 7,     
    'ytick.labelsize': 7,         
})

def button_clicked():
    sender = app.sender()
    if sender:
        print(f"Button clicked: {sender.text()}")

def create_graph(tab):
    global time_data
    global altitude_data
    global pressure_data
    global voltage_data
    global gyro_data_r
    global accel_data_r
    global gnss_altitude_data
    global canvas1, canvas2, canvas3, canvas4, canvas5, canvas6
    global altitude_line, pressure_line, voltage_line, gyro_line, accel_line, gnss_altitude_line
    graph_layout = QGridLayout()
    graph_layout.setSpacing(20)
    
    graph_widget = QWidget() 
    graph_widget.setLayout(graph_layout)
    graph_widget.setStyleSheet("background-color:#B191DA;") 
    
    csv_file = "trial_data.csv" 
    data = pd.read_csv(csv_file)
    data = data.sort_values(by="TIME_STAMPING")
    time_data=data["TIME_STAMPING"]
    time_data = pd.to_datetime(time_data, format='%H:%M:%S')  
    time_data = (time_data - time_data.iloc[0]).dt.total_seconds() 
    
    # Altitude 
    altitude_data = data["ALTITUDE"]
    #Pressure
    pressure_data = data["PRESSURE"] 
    #Voltage
    voltage_data = data["VOLTAGE"]
    #Gyro r
    gyro_data_r = data["GYRO_R"]
    #ACCEL r 
    accel_data_r = data["ACC_R"]
    #Gnss_altitude
    gnss_altitude_data = data["GNSS_ALTITUDE"]
    n=len(time_data)
    
    fig1 = Figure(figsize=(1,1))
    fig1.patch.set_facecolor("#B191DA")
    ax1= fig1.add_subplot(111)
    altitude_line ,= ax1.plot(time_data[:n], altitude_data[:n], color="#5285bdff", label="Altitude" ,linewidth=1)
    ax1.set_title("Altitude vs Time",fontdict={'fontname': 'Arial', 'fontsize': 11, 'fontweight': 'bold'})
    ax1.legend(fontsize=7)
    ax1.grid()
    canvas1 = FigureCanvas(fig1)
    graph_layout.addWidget(canvas1, 0, 0)
    
    fig2 = Figure(figsize=(1,1))
    fig2.patch.set_facecolor("#B191DA")
    ax2 = fig2.add_subplot(111)
    pressure_line ,=ax2.plot(time_data[:n],  pressure_data[:n], color="#5285bdff", label="Pressure",linewidth=1)
    ax2.set_title("Pressure vs Time",fontdict={'fontname': 'Arial', 'fontsize': 11, 'fontweight': 'bold'})
    ax2.legend(fontsize=7)
    ax2.grid()
    canvas2 = FigureCanvas(fig2)
    graph_layout.addWidget(canvas2, 0, 1)
    
    
    fig3 = Figure(figsize=(3,3))
    fig3.patch.set_facecolor("#B191DA")
    ax3 = fig3.add_subplot(111)
    voltage_line, = ax3.plot(time_data[:n], voltage_data[:n], color="#5285bdff", label="Voltage",linewidth=1)
    ax3.set_title("Voltage vs Time",fontdict={'fontname': 'Arial', 'fontsize': 11, 'fontweight': 'bold'})
    ax3.legend(fontsize=7)
    ax3.grid()
    canvas3 = FigureCanvas(fig3)
    graph_layout.addWidget(canvas3, 0, 2)
    
    
    fig4 = Figure(figsize=(3,3))
    fig4.patch.set_facecolor("#B191DA")
    ax4 = fig4.add_subplot(111)
    gyro_line, = ax4.plot(time_data[:n], gyro_data_r[:n], color="#5285bdff", label="Gyro",linewidth=1)
    ax4.set_title("Gyro_R vs Time",fontdict={'fontname': 'Arial', 'fontsize': 11, 'fontweight': 'bold'})
    ax4.legend(fontsize=7)
    ax4.grid()
    canvas4 = FigureCanvas(fig4)
    graph_layout.addWidget(canvas4, 1, 0)
    
    
    fig5 = Figure(figsize=(3,3))
    fig5.patch.set_facecolor("#B191DA")
    ax5 = fig5.add_subplot(111)
    accel_line, = ax5.plot(time_data[:n], accel_data_r[:n], color="#5285bdff", label="Accel",linewidth=1)
    ax5.set_title("Accel_R vs Time",fontdict={'fontname': 'Arial', 'fontsize': 11, 'fontweight': 'bold'})
    ax5.legend(fontsize=7)
    ax5.grid()
    canvas5 = FigureCanvas(fig5)
    graph_layout.addWidget(canvas5, 1, 1)
    
    
    fig6 = Figure(figsize=(3,3))
    fig6.patch.set_facecolor("#B191DA")
    ax6 = fig6.add_subplot(111)
    gnss_altitude_line,=ax6.plot(time_data[:n], gnss_altitude_data[:n], color="#5285bdff", label="Gnss",linewidth=1)
    ax6.set_title("GNSS_Altitude vs Time",fontdict={'fontname': 'Arial', 'fontsize': 11, 'fontweight': 'bold'})
    ax6.legend(fontsize=7)
    ax6.grid()
    canvas6 = FigureCanvas(fig6)
    graph_layout.addWidget(canvas6, 1, 2)
    
    tab_layout = QVBoxLayout(tab)
    tab_layout.addWidget(graph_widget)
    update_plot()
index=0
def update_plot():
    global index
    if index < len(time_data): 
        altitude_line.set_data(time_data[:index+1], altitude_data[:index+1])
        pressure_line.set_data(time_data[:index+1], pressure_data[:index+1])
        voltage_line.set_data(time_data[:index+1], voltage_data[:index+1])
        gyro_line.set_data(time_data[:index+1], gyro_data_r[:index+1])
        accel_line.set_data(time_data[:index+1], accel_data_r[:index+1])
        gnss_altitude_line.set_data(time_data[:index+1], gnss_altitude_data[:index+1])
        canvas1.draw()
        canvas2.draw()
        canvas3.draw()
        canvas4.draw()
        canvas5.draw()
        canvas6.draw()
        index += 1

 
app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle("Team Kalpana Software Task")
main_window.setGeometry(100, 100, 1100, 775)


#main frame 
main_frame = QFrame(main_window)
main_frame.setGeometry(0, 0, 1100, 750)
gradient = QLinearGradient(0, 0, main_frame.width(), main_frame.height())  
gradient.setColorAt(0, QColor(0, 0, 0))
gradient.setColorAt(1, QColor(121, 102, 180))
palette = QPalette()
palette.setBrush(QPalette.Background, QBrush(gradient))
main_frame.setAutoFillBackground(True)
main_frame.setPalette(palette)
main_window.setCentralWidget(main_frame)


#top_frame
top_frame=QFrame(main_frame)
top_frame.setGeometry(0, 0, main_frame.width(), 130)
top_frame.setStyleSheet("background-color: #0F0D33;")
layout = QGridLayout()
layout.setAlignment(Qt.AlignTop)
top_frame.setLayout(layout)

#top labels

label1 = QLabel("SOFTWARE STATE")
label1.setStyleSheet("color: #bde2bc; font: bold 13pt arial;padding-left: 50px; padding-right: 100px; padding-top: 10px; padding-bottom: 0px;")
label1.setAlignment(Qt.AlignCenter)
layout.addWidget(label1, 0, 0)

label2 = QLabel("TEAM KALPANA : 2024-CANSAT-ASI-023")
label2.setStyleSheet("color: #bde2bc; font: bold 15pt arial;padding-left: 90px; padding-right: 60px; padding-top: 10px; padding-bottom: 0px;")
label2.setAlignment(Qt.AlignCenter)
layout.addWidget(label2, 0, 1)

label3 = QLabel("TIME")
label3.setStyleSheet("color: #bde2bc; font: bold 13pt arial;padding-left: 12px; padding-right: 12px; padding-top: 10px; padding-bottom: 0px; ")
label3.setAlignment(Qt.AlignCenter)
layout.addWidget(label3, 0, 2)

label4 = QLabel("PACKET COUNT")
label4.setStyleSheet("color: #bde2bc; font: bold 13pt arial;padding-left: 12px; padding-right: 12px; padding-top: 10px; padding-bottom: 0px;")
label4.setAlignment(Qt.AlignCenter)
layout.addWidget(label4, 0, 3)

input_box1 = QLineEdit()
input_box1.setFixedWidth(180)
input_box1.setStyleSheet("background-color: white; color: black; padding: 5px; font: 11pt arial;border: 2px solid red;border-radius: 11px; width: 20px; margin-left:42px; ")
input_box1.setText("LAUNCH_PAD")
input_box1.setAlignment(Qt.AlignCenter)
layout.addWidget(input_box1, 1, 0) 


input_box2 = QLineEdit()
input_box2.setFixedWidth(140)
input_box2.setStyleSheet("background-color: white; color: black; padding: 5px; font: 11pt arial;border: 2px solid red;border-radius: 11px; width: 20px; margin-left:20px; ")
input_box2.setText("0")
input_box2.setAlignment(Qt.AlignCenter)
layout.addWidget(input_box2, 1, 2) 


input_box3 = QLineEdit()
input_box3.setFixedWidth(140)
input_box3.setStyleSheet("background-color: white; color: black; padding: 5px; font: 11pt arial;border: 2px solid red;border-radius: 11px; width: 20px; margin-left:20px;  ")
input_box3.setText("0")
input_box3.setAlignment(Qt.AlignCenter)
layout.addWidget(input_box3, 1, 3) 

image_label = QLabel() 
pixmap = QPixmap("kalpana2.png")
pixmap = pixmap.scaled(40,60,Qt.KeepAspectRatio)
image_label.setPixmap(pixmap)  
image_label.setAlignment(Qt.AlignCenter) 
image_label.setStyleSheet("padding: 15px;") 
layout.addWidget(image_label, 1, 1,1,1)
image_label = QLabel()


#Tabs 
tab_widget = QTabWidget(main_frame)
tab_widget.setGeometry(0, 145, main_frame.width(), main_frame.height() - 145)  # Adjust position and size

# Create tabs
tabs=["Telementary Data","Graphs","Location and 3D Plotting","Live Telecast"]
for i in range(0, 4):
    tab = QWidget()
    if tabs[i] == "Graphs":
        create_graph(tab) 
    else :
        tab_label = QLabel(tabs[i])
        tab_label.setAlignment(Qt.AlignCenter)
        tab_label.setStyleSheet("background:'#B191DA';margin:20px;margin-top:0px; height:600px")
        tab_layout = QVBoxLayout(tab)
        tab_layout.setContentsMargins(0, 0, 0, 0)
        tab_layout.setSpacing(0)
        tab_layout.addWidget(tab_label)
    tab_widget.addTab(tab, tabs[i])
    tab_widget.setGeometry(0, 150, tab_widget.width(), 560)
    tab_widget.setStyleSheet("""
    QTabBar::tab {
        background: #A8CED4;
        color: white;
        border-radius: 18px;
        margin-left:2px;
        min-width: 265px;
        padding: 10px 3px;
        font: bold 15pt arial;
        margin-bottom:2px;
        font-weight: bold;
    }
    QTabBar::tab:selected { 
        background:grey;
        color:white;
    }
""")
    
    
#timer 
timer = QTimer()
timer.timeout.connect(update_plot)
timer.start(1000)   
   
    
    
#buttons
button_container = QWidget(main_frame)
button_container.setGeometry(0, 700, main_frame.width(), 60) 
button_layout = QHBoxLayout(button_container)
button_layout.setContentsMargins(15, 0, 15, 0)
button_layout.setSpacing(10)
buttons = ['BOOT','Set Time','Caliberate','ON/OFF','CX','SIM Enable','SIM Activate','SIM Disable']
for name in buttons:
    button = QPushButton(name)
    button.setFixedWidth(110)
    button.setStyleSheet("""
        QPushButton {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #171e3f, stop: 1 #1ee1e5); 
            color: orange; 
            border: 2px solid black; 
            border-radius: 8px; 
            padding: 12px 2px; 
            font: bold 13pt arial;
        } 
    """)
    button.clicked.connect(button_clicked)
    button_layout.addWidget(button)



main_window.show()
sys.exit(app.exec_())