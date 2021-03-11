import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.itproger
collection = db.employees

personId = None


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Employees')
        self.setGeometry(450, 180, 530, 400)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getEmployees()
        self.displayFirstRecord()
        style = open('css/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def mainDesign(self):
        self.employeeList = QListWidget()
        self.employeeList.itemClicked.connect(self.singleClick)
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText('Search For Employee')
        self.searchBtn = QPushButton('Search')
        self.searchBtn.clicked.connect(self.searchEmployee)
        self.btnNew = QPushButton('New')
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.clicked.connect(self.updateEmployee)
        self.btnDelete = QPushButton('Delete')
        self.btnDelete.clicked.connect(self.deleteEmployee)

    def layouts(self):
        #################LAYOUTS###########################
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rigthTopLayout = QHBoxLayout()
        self.rigthMiddleLayout = QHBoxLayout()
        self.rigthBottomLayout = QHBoxLayout()
        ##############Adding child layout to main layout###
        self.rightMainLayout.addLayout(self.rigthTopLayout)
        self.rightMainLayout.addLayout(self.rigthMiddleLayout)
        self.rightMainLayout.addLayout(self.rigthBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 50)  # 50 - aspect ratio(співвідношення сторін у відсотках)
        self.mainLayout.addLayout(self.rightMainLayout, 50)
        ###########Adding widget main layout################
        self.rigthTopLayout.addWidget(self.employeeList)
        self.rigthMiddleLayout.addWidget(self.searchEntry)
        self.rigthMiddleLayout.addWidget(self.searchBtn)
        self.rigthBottomLayout.addWidget(self.btnNew)
        self.rigthBottomLayout.addWidget(self.btnUpdate)
        self.rigthBottomLayout.addWidget(self.btnDelete)
        #############Setting main window layout#############
        self.setLayout(self.mainLayout)


    def searchEmployee(self):
        if self.searchEntry.text() == "":
            QMessageBox.information(self, 'Warning', 'Search query cant be empty!')
            self.employeeList.clear()
            self.getEmployees()
        else:
            try:
                nameValue = self.searchEntry.text().title()
                name = nameValue.split(' ')[0]
                surnameValue = self.searchEntry.text().title()
                surname = surnameValue.split(' ')[1]
                query = collection.find({"name": name, "surname": surname})
                for emp in query:
                    if emp['name'] == name and surname == emp['surname']:
                        self.employeeList.clear()
                        self.searchEntry.setText("")
                        self.employeeList.addItem(str('1') + ' - ' + str(emp['name']) + ' ' + emp['surname'])
                        for i in reversed(range(self.leftLayout.count())):
                            widget = self.leftLayout.takeAt(i).widget()
                        if widget is not None:
                            widget.deleteLater()
                        name = QLabel(emp['name'])
                        surname = QLabel(emp['surname'])
                        phone = QLabel(emp['phone'])
                        email = QLabel(emp['email'])
                        address = QLabel(emp['address'])
                        self.leftLayout.setVerticalSpacing(15)
                        self.leftLayout.addRow('Name: ', name)
                        self.leftLayout.addRow('Surname: ', surname)
                        self.leftLayout.addRow('Phone: ', phone)
                        self.leftLayout.addRow('Email: ', email)
                        self.leftLayout.addRow('Address: ', address)
                    else:
                        QMessageBox.information(self, 'Info', 'There is no such Employee!')
            except:
                QMessageBox.information(self, 'Info', 'Try to enter full name and surname to search!')


    def addEmployee(self):
        self.newEmployee = AddEmployee()
        self.close()

    def getEmployees(self):
        query = collection.find({}, {'_id': 0})
        count = 0
        for employee in query:
            count += 1
            self.employeeList.addItem(str(count) + ' - ' + str(employee['name']) + ' ' + employee['surname'])

    def displayFirstRecord(self):
        query = collection.find({}, {'_id': 0}).limit(1)
        for employee in query:
            name = QLabel(employee['name'])
            surname = QLabel(employee['surname'])
            phone = QLabel(employee['phone'])
            email = QLabel(employee['email'])
            address = QLabel(employee['address'])
            self.leftLayout.setVerticalSpacing(15)  # vertical distance by row (15 is pt)
            self.leftLayout.addRow('Name: ', name)
            self.leftLayout.addRow('Surname: ', surname)
            self.leftLayout.addRow('Phone: ', phone)
            self.leftLayout.addRow('Email: ', email)
            self.leftLayout.addRow('Address: ', address)

    def singleClick(self):
        for i in reversed(range(self.leftLayout.count())):
            widget = self.leftLayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        employee = self.employeeList.currentItem().text()
        nameId = employee.split(' ')[2]
        surnameId = employee.split(' ')[3]
        query = collection.find({'name': nameId, 'surname': surnameId}, {'_id': 0}).limit(1)
        for emp in query:
            name = QLabel(emp['name'])
            surname = QLabel(emp['surname'])
            phone = QLabel(emp['phone'])
            email = QLabel(emp['email'])
            address = QLabel(emp['address'])
            self.leftLayout.setVerticalSpacing(15)  # vertical distance by row (15 pt)
            self.leftLayout.addRow('Name: ', name)
            self.leftLayout.addRow('Surname: ', surname)
            self.leftLayout.addRow('Phone: ', phone)
            self.leftLayout.addRow('Email: ', email)
            self.leftLayout.addRow('Address: ', address)

    def deleteEmployee(self):
        if self.employeeList.selectedItems():
            person = self.employeeList.currentItem().text()
            nameId = person.split(' ')[2]
            surnameId = person.split(' ')[3]
            mbox = QMessageBox.question(self, 'Warning', 'Are you sure to delete this person?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query = collection.delete_one({'name': nameId, 'surname': surnameId})
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
            personId = person.split(' ')[3]
            self.updateWindow = UpdateEmployee()
            self.close()
        else:
            QMessageBox.information(self, 'Warning!!!', 'Please select a person to update')


class UpdateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Employee')
        self.setGeometry(450, 150, 300, 300)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.getPerson()
        self.mainDesign()
        self.layouts()
        style = open('css/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def getPerson(self):
        global personId
        query = collection.find({'surname': personId}).limit(1)
        for employee in query:
            self.name = employee['name']
            self.surname = employee['surname']
            self.phone = employee['phone']
            self.email = employee['email']
            self.address = employee['address']

    def closeEvent(self, event):
        self.main = Main()

    def mainDesign(self):
        ############Top Layout Widgets###############
        self.title = QLabel("Update Person")
        # self.title.setStyleSheet('font-size: 20pt; color: black; font-family: Arial Bold')
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
        self.addressLbl = QLabel('Address :')
        self.addressEditor = QTextEdit()
        self.addressEditor.setText(self.address)
        self.addButton = QPushButton('Update')
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
        self.topLayout.setContentsMargins(100, 10, 40, 10)
        self.topLayout.addStretch()
        ######Bottom layout#########
        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl, self.emailEntry)
        self.bottomLayout.addRow(self.addressLbl, self.addressEditor)
        self.bottomLayout.addWidget(self.addButton)
        ###Setting main layouts for window##########
        self.setLayout(self.mainLayout)

    def updateEmployee(self):
        global personId
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        address = self.addressEditor.toPlainText()  # if qtext editor: toPlainText()
        if (surname and email != ""):
            try:
                query = collection.replace_one({'surname': personId},
                                               {'name': name, 'surname': surname, 'phone': phone, 'email': email,
                                                'address': address})
                QMessageBox.information(self, 'Success', 'Person has been updated')
                self.close()
            # main = Main()
            except:
                QMessageBox.information(self, 'Warning', 'Person has not been updated')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not be empty')


class AddEmployee(QWidget):  # inheirt
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Employee')
        self.setGeometry(450, 150, 300, 300)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        style = open('css/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def closeEvent(self, event):
        self.main = Main()

    def mainDesign(self):
        ############Top Layout Widgets###############
        self.title = QLabel("Add Person")
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
        self.addressLbl = QLabel('Address :')
        self.addressEditor = QTextEdit()
        self.addButton = QPushButton('Add')
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
        self.topLayout.setContentsMargins(100, 10, 40, 10)
        self.topLayout.addStretch()
        ######Bottom layout#########
        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl, self.emailEntry)
        self.bottomLayout.addRow(self.addressLbl, self.addressEditor)
        self.bottomLayout.addWidget(self.addButton)
        ###Setting main layouts for window##########
        self.setLayout(self.mainLayout)

    def addEmployee(self):
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        address = self.addressEditor.toPlainText()
        if (surname and email != ""):
            try:
                post = {'name': name.title(), 'surname': surname.title(), 'phone': phone, 'email': email, 'address': address.title()}
                query = collection.insert_one(post)
                QMessageBox.information(self, 'Success', 'Person has been added')
                self.close()
                # main = Main()
            except:
                QMessageBox.information(self, 'Warning', 'Person has not been added')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not be empty')


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())


if __name__ == '__main__':
    main()
