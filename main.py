from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
import sys, os
import sqlite3
from PIL import Image

con = sqlite3.connect('Employees.db')
cur = con.cursor()
defaultImg = 'person.png'
personId = None

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Employees')
        self.setGeometry(450, 150, 530, 400)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getEmployees()
        self.displayFirstRecord()

    def mainDesign(self):
        self.setStyleSheet('font-size: 12pt; font-family: Arial Bold; background-color:#C4B298;')
        self.employeeList = QListWidget()
        self.employeeList.itemClicked.connect(self.singleClick)
        self.btnNew = QPushButton('New')
        self.btnNew.setStyleSheet('background-color:#858585;')
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.setStyleSheet('background-color:#858585;')
        self.btnUpdate.clicked.connect(self.updateEmployee)
        self.btnDelete = QPushButton('Delete')
        self.btnDelete.setStyleSheet('background-color:#858585;')
        self.btnDelete.clicked.connect(self.deleteEmployee)

    def layouts(self):
        #################LAYOUTS###########################
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rigthTopLayout = QHBoxLayout()
        self.rigthBottomLayout = QHBoxLayout()
        ##############Adding child layout to main layout###
        self.rightMainLayout.addLayout(self.rigthTopLayout)
        self.rightMainLayout.addLayout(self.rigthBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 50)  # 50 - aspect ratio(співвідношення сторін у відсотках)
        self.mainLayout.addLayout(self.rightMainLayout, 50)
        ###########Adding widget main layout################
        self.rigthTopLayout.addWidget(self.employeeList)
        self.rigthBottomLayout.addWidget(self.btnNew)
        self.rigthBottomLayout.addWidget(self.btnUpdate)
        self.rigthBottomLayout.addWidget(self.btnDelete)
        #############Setting main window layout#############
        self.setLayout(self.mainLayout)

    def addEmployee(self):
        self.newEmployee = AddEmployee()
        self.close()

    def getEmployees(self):
        query = ('SELECT ID, Name, Surname FROM Employees;')
        employees = cur.execute(query).fetchall()
        for employee in employees:
            self.employeeList.addItem(str(employee[0])+' - '+employee[1]+' '+employee[2])

    def displayFirstRecord(self):
        global defaultImg
        query = ('SELECT * FROM Employees ORDER BY ROWID ASC LIMIT 1;')
        employee = cur.execute(query).fetchone()
        img = QLabel()
        img.setPixmap(QPixmap('images/'+employee[5]))
        name = QLabel(employee[1])
        surname = QLabel(employee[2])
        phone = QLabel(employee[3])
        email = QLabel(employee[4])
        address = QLabel(employee[6])
        self.leftLayout.setVerticalSpacing(15) # vertical distance by row (15 is pt)
        self.leftLayout.addRow('', img)
        self.leftLayout.addRow('Name: ', name)
        self.leftLayout.addRow('Surname: ', surname)
        self.leftLayout.addRow('Phone: ', phone)
        self.leftLayout.addRow('Email: ', email)
        self.leftLayout.addRow('Address: ', address)

    def singleClick(self):
        for i in reversed(range(self.leftLayout.count())):  # delete leftlayout and change after clicked for new
            widget = self.leftLayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        employee = self.employeeList.currentItem().text()
        id = employee.split(' - ')[0]
        query = ('SELECT * FROM Employees WHERE ID = ?;')
        person = cur.execute(query,(id,)).fetchone() # (id,) - single item tuple
        img = QLabel()
        img.setPixmap(QPixmap('images/'+employee[5]))
        name = QLabel(person[1])
        surname = QLabel(person[2])
        phone = QLabel(person[3])
        email = QLabel(person[4])
        address = QLabel(person[6])
        self.leftLayout.setVerticalSpacing(15)  # vertical distance by row (15 is pt)
        self.leftLayout.addRow("", img)
        self.leftLayout.addRow('Name: ', name)
        self.leftLayout.addRow('Surname: ', surname)
        self.leftLayout.addRow('Phone: ', phone)
        self.leftLayout.addRow('Email: ', email)
        self.leftLayout.addRow('Address: ', address)


    def deleteEmployee(self):
        if self.employeeList.selectedItems():
            person = self.employeeList.currentItem().text()
            id = person.split(' - ')[0]
            mbox = QMessageBox.question(self,'Warning', 'Are you sure to delete this person?', QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query = ('DELETE FROM Employees WHERE ID = ?')
                    cur.execute(query,(id,))
                    con.commit()
                    QMessageBox.information(self, 'Info', 'Done')
                    self.close()
                    self.main = Main()
                except:
                    QMessageBox.information(self, 'Warning!!!', 'Person has not been deleted')
        else:
            QMessageBox.information(self, 'Warning!!!', 'Please select a person to delete')

    def updateEmployee(self):
        global personId
        if self.employeeList.selectedItems():
            person = self.employeeList.currentItem().text()
            personId = person.split(' - ')[0]
            self.updateWindow = UpdateEmployee()
            self.close()
        else:
            QMessageBox.information(self, 'Warning!!!', 'Please select a person to update')

class UpdateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Employee')
        self.setGeometry(450,150,300,300)
        self.UI()
        self.show()

    def UI(self):
        self.getPerson()
        self.mainDesign()
        self.layouts()

    def getPerson(self):
        global personId
        query = ('SELECT * FROM EMPLOYEES WHERE ID = ?;')
        employee = cur.execute(query,(personId,)).fetchone()
        self.name = employee[1]
        self.surname = employee[2]
        self.phone = employee[3]
        self.email = employee[4]
        self.img = employee[5]
        self.address = employee[6]

    def closeEvent(self, event):
        self.main = Main()

    def mainDesign(self):
        ############Top Layout Widgets###############
        self.setStyleSheet('background-color:white;font-size:13pt;font-family:Times')
        self.title = QLabel("Update Person")
        self.title.setStyleSheet('font-size: 20pt; color: black; font-family: Arial Bold')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap('images/{}'.format(self.img)))
        ##############Bottom layout widgets###########
        self.nameLbl = QLabel('Name :')
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.name)
        self.surnameLbl = QLabel('Surname :')
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setText(self.surname)
        self.phoneLbl = QLabel('Phone :')
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setText(self.phone)
        self.emailLbl = QLabel('Email :')
        self.emailEntry = QLineEdit()
        self.emailEntry.setText(self.email)
        self.imgLbl = QLabel('Picture :')
        self.imgBtn = QPushButton('Browse')
        self.imgBtn.clicked.connect(self.uploadImage)
        self.imgBtn.setStyleSheet('background-color:#CB4335 ')
        self.addressLbl = QLabel('Address :')
        self.addressEditor = QTextEdit()
        self.addressEditor.setText(self.address)
        self.addButton = QPushButton('Update')
        self.addButton.setStyleSheet('background-color:#CB4335 ')
        self.addButton.clicked.connect(self.updateEmployee)


    def layouts(self):
        #########Creating main layouts##############
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        #####Adding child layouts to main layouts###
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        #####Adding widget to layout################
              #####Top layout########
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.setContentsMargins(100,10,40,10)
        self.topLayout.addStretch()
            ######Bottom layout#########
        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl, self.emailEntry)
        self.bottomLayout.addRow(self.imgLbl, self.imgBtn)
        self.bottomLayout.addRow(self.addressLbl, self.addressEditor)
        self.bottomLayout.addWidget(self.addButton)
        #self.bottomLayout.addRow("",self.addButton)
        ###Setting main layouts for window##########
        self.setLayout(self.mainLayout)

    def uploadImage(self):
        global defaultImg
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Images Files (*.png *.jpg)')
        if ok:
            defaultImg = os.path.basename(self.fileName) #not an absolute directory
            img = Image.open(self.fileName) #import Image
            img = img.resize(size)
            img.save('images/'+defaultImg)

    def updateEmployee(self):
        global defaultImg
        global personId
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText() # if qtext editor
        if (surname and email !=""):
            try:
               query = ('UPDATE Employees set Name = ?, Surname = ?, Phone = ?, Email = ?, Img = ?, Address = ? WHERE ID = ?; ')
               cur.execute(query,(name,surname,phone,email,img,address,personId))
               con.commit()
               QMessageBox.information(self, 'Success', 'Person has been updated')
               self.close()
               #main = Main()
            except:
                QMessageBox.information(self, 'Warning', 'Person has not been updated')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not be empty')



class AddEmployee(QWidget): #inheirt
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Employee')
        self.setGeometry(450,150,300,300)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def closeEvent(self, event):
        self.main = Main()

    def mainDesign(self):
        ############Top Layout Widgets###############
        self.setStyleSheet('background-color:white;font-size:13pt;font-family:Times')
        self.title = QLabel("Add Person")
        self.title.setStyleSheet('font-size: 20pt; color: black; font-family: Arial Bold')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap('icons/person.png'))
        ##############Bottom layout widgets###########
        self.nameLbl = QLabel('Name :')
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText('Enter Employee Name')
        self.surnameLbl = QLabel('Surname :')
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText('Enter Employee Surname')
        self.phoneLbl = QLabel('Phone :')
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText('Enter Employee Phone Number')
        self.emailLbl = QLabel('Email :')
        self.emailEntry = QLineEdit()
        self.emailEntry.setPlaceholderText('Enter Employee Email')
        self.imgLbl = QLabel('Picture :')
        self.imgBtn = QPushButton('Browse')
        self.imgBtn.clicked.connect(self.uploadImage)
        self.imgBtn.setStyleSheet('background-color:#CB4335 ')
        self.addressLbl = QLabel('Address :')
        self.addressEditor = QTextEdit()
        self.addButton = QPushButton('Add')
        self.addButton.setStyleSheet('background-color:#CB4335 ')
        self.addButton.clicked.connect(self.addEmployee)


    def layouts(self):
        #########Creating main layouts##############
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        #####Adding child layouts to main layouts###
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        #####Adding widget to layout################
              #####Top layout########
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.setContentsMargins(100,10,40,10)
        self.topLayout.addStretch()
            ######Bottom layout#########
        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl, self.emailEntry)
        self.bottomLayout.addRow(self.imgLbl, self.imgBtn)
        self.bottomLayout.addRow(self.addressLbl, self.addressEditor)
        self.bottomLayout.addWidget(self.addButton)
        #self.bottomLayout.addRow("",self.addButton)
        ###Setting main layouts for window##########
        self.setLayout(self.mainLayout)

    def uploadImage(self):
        global defaultImg
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self,'Upload Image','','Images Files (*.png *.jpg)')
        if ok:
            defaultImg = os.path.basename(self.fileName) #not an absolute directory
            img = Image.open(self.fileName) #import Image
            img = img.resize(size)
            img.save('images/{}'.format(defaultImg))


    def addEmployee(self):
        global defaultImg
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText() # if qtext editor
        if (surname and email !=""):
            try:
               query = ('INSERT INTO Employees (Name, Surname, Phone, Email, Img, Address) VALUES (?,?,?,?,?,?);')
               cur.execute(query,(name,surname,phone,email,img,address))
               con.commit()
               QMessageBox.information(self, 'Success', 'Person has been added')
               self.close()
               #main = Main()
            except:
                QMessageBox.information(self, 'Warning', 'Person has not been added')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not be empty')

def main():
    APP= QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()

