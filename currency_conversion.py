import sys 
import urllib2
# urllib2 is to grab files over the internet, for the currency conversion rates
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Form(QDialog):
    
    def __init__(self,parent = None):
        super(Form,self).__init__(parent)
        
        date = self.getdata()
        # The getData() function gets all the exchange rates and populates self.rates dictionary
        # It also returns a string holding a date when the rates were in force
        
        #ITS NOT AN INBUILT FUNCTION
        
        #The dictionary keys are the currency names
        # The dictionary values are the conversion rates
        rates = sorted(self.rates.keys())
        
        # we sort it to provided a sorted list to the user in the combo boxes
        
        #WE DO NOT NEED REFERENCES TO dataLabel AND rates, HENCE WE DO NOT USE self
        # FOR THE OTHER COMBOBOX AND LABELS, WE NEED THEM OUTSIDE THE FUNCTION, HENCE WE USE self
        
        
        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox() # to handle floating point
        self.fromSpinBox.setRange(0.01,10000000.00)
        # for a spinBox always set the range first and then the value, to prevent errors and possible 
        # loss of precision if the value is outside the range later
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")
        
        # here we use a grid layout
        
        grid = QGridLayout()
        # we lay out the widgets in grid layout
        # all we have to do is specify the row and column, which is zero indexed
        
        grid.addWidget(dateLabel,0,0)
        grid.addWidget(self.fromComboBox,1,0)
        grid.addWidget(self.fromSpinBox,1,1)
        grid.addWidget(self.toComboBox,2,0)
        grid.addWidget(self.toLabel,2,1)
        self.setLayout(grid)
        
        # the layouts are smart, hence the column 0 would occupy more width than
        # the column 1 as we need more space for the display in column 0
        # all this is automatically taken care of
        
        #again we use the connect() function to get a hold of the signals of widgets
        #when their states change and act accordingly
        
        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"),self.updateUi)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"),self.updateUi)
        self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        self.setWindowTitle("Currency Converter")
        
        
    def updateUi(self):
        
        to = unicode(self.toComboBox.currentText())
        from_ = unicode(self.fromComboBox.currentText())
        amount = (self.rates[from_]/self.rates[to])*self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" % amount)
        
    def getdata(self):
        
        #Look at the bank file to get to know the file details
        
        self.rates = {}
        try:
            date = "Unknown"
            
            fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
            
            for line in fh:
                if not line or line.startswith('#') or line.startswith("Closing "):
                    continue
                fields = line.split(", ")
                if line.startswith("Date "):
                    date = fields[-1] #The latest date is the last on the row
                else:
                    try: #for invalid numbers
                        value = float(fields[-1])
                        self.rates[unicode(fields[0])] = value  
                        #making the dictionary
                    except ValueError:
                        pass
            
            return "Exchange Rates Date: "+date #returns the date
        except Exception, e:
            return "Failed  to download:\n%s" % e #returns error
        
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        