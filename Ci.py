import sys 
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Ci(QDialog):
    
    def __init__(self, parent = None):
        
        super(Ci,self).__init__(parent)
        
        princLabel = QLabel("Principal: ")
        rateLabel = QLabel("Rate: ")
        yearLabel = QLabel("Year: ")
        AmountLabel = QLabel("Amount ")
        
        yrs = ["1 year", "2 years" , "3 years"]
        
        self.pSpinBox = QDoubleSpinBox()
        self.pSpinBox.setRange(0.00,100000000.00)
        self.pSpinBox.setValue(2000.00)
        self.pSpinBox.setPrefix("Rs. ")
        self.rSpinBox = QDoubleSpinBox()
        self.rSpinBox.setRange(0.00,100.00)
        self.rSpinBox.setValue(5.00)
        self.rSpinBox.setSuffix(" %")
        self.yComboBox = QComboBox()
        self.yComboBox.addItems(yrs)
        
        self.amount = QLabel()
        
        grid = QGridLayout()
        grid.addWidget(princLabel, 0,0)
        grid.addWidget(self.pSpinBox, 0, 1)
        grid.addWidget(rateLabel, 1, 0)
        grid.addWidget(self.rSpinBox, 1, 1)
        grid.addWidget(yearLabel, 2,0)
        grid.addWidget(self.yComboBox, 2, 1)
        grid.addWidget(AmountLabel, 3,0)
        grid.addWidget(self.amount, 3,1)
        
        self.connect(self.pSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.rSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.yComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        
        
        self.setLayout(grid)
        self.setWindowTitle("Compound Interest")
        self.setGeometry(500,300,400,100)
        
    def updateUi(self):
        
        pr = float(self.pSpinBox.value())
        rat = float(self.rSpinBox.value())
        yr = int(self.yComboBox.currentText()[0:1])
        am = pr*((1+(rat/100.0))**yr)
        self.amount.setText("Rs. %0.2f" % am)
        
        
app = QApplication(sys.argv)
ci = Ci()
ci.show()
app.exec_()
        
        
        
        
        
        