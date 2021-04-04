import sys
from PyQt5 import QtWidgets
import design, request

class Application(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.day_temp)

    def day_temp(self):
        day_temps = request.respon()
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        morning = f"Утром: {int(day_temps['Morning'])}\u2103"          
        day = f"Днем: {int(day_temps['Day'])}\u2103"            
        evening = f"Вечером: {int(day_temps['Evening'])}\u2103"        
        night = f"Ночью: {int(day_temps['Night'])}\u2103"         
        rf_morn = f"Ощущается как: {int(day_temps['realfeel']['morn'])}\u2103"
        rf_day = f"Ощущается как: {int(day_temps['realfeel']['day'])}\u2103"
        rf_evening = f"Ощущается как: {int(day_temps['realfeel']['eve'])}\u2103"
        rf_night = f"Ощущается как: {int(day_temps['realfeel']['night'])}\u2103"
        self.listWidget_3.addItem("Погода на завтра:")
        self.listWidget.addItem(morning)
        self.listWidget.addItem(day)       
        self.listWidget.addItem(evening)
        self.listWidget.addItem(night)       
        self.listWidget_2.addItem(rf_morn)
        self.listWidget_2.addItem(rf_day)
        self.listWidget_2.addItem(rf_evening)
        self.listWidget_2.addItem(rf_night)   



    

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
    