# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_view.ui'
#
# Created: Fri Jul  2 10:57:54 2021
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import xlrd
import xl_read
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1212, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(5, 1, 581, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 255, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.treeWidget.setPalette(palette)
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
      
        self.textEdit.setGeometry(QtCore.QRect(10, 302, 581, 300))


        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(187, 203, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(187, 203, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(593, 310, 621, 297))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(236, 231, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 231, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textEdit_2.setPalette(palette)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))

        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(595, 10, 621, 300))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 215, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tableWidget.setPalette(palette)

        #self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        #self.tableWidget_2.setGeometry(QtCore.QRect(10, 220, 581, 321))
        #palette = QtGui.QPalette()
        #brush = QtGui.QBrush(QtGui.QColor(212, 255, 252))
        #brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        #brush = QtGui.QBrush(QtGui.QColor(212, 255, 252))
        #brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        #brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        #brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        #self.tableWidget_2.setPalette(palette)
        #self.tableWidget_2.setPalette(palette)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        #XStream.stdout().messageWritten.connect( self.textEdit.append)
        #XStream.stderr().messageWritten.connect( self.textEdit.append)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.all_tests = []
        
        #return self.textEdit

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "BD_ADDRESS", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Current_id", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Start Time", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "State", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        # ---------------------------------------------------------------------------------------------------------------------------------------------
        #self.textEdit.setPlainText("hello")
        #self.textEdit = QtGui.QTextEdit(self.centralwidget)
        #self.textEdit.setGeometry(QtCore.QRect(10, 230, 571, 201))
        #self.textEdit.setPalette(palette)
        #self.textEdit.setObjectName(_fromUtf8("textEdit"))
       
        # Read excel
        inputWorkbook = xlrd.open_workbook('C:/Users/ptlab1/Documents/sp_zagkou/TestPlan_tests.xlsx')
        inputWorksheet = inputWorkbook.sheet_by_name('TestSetup')
        dev_row, dev_col = xl_read.find_params_position(inputWorksheet, 'Device Setup')
        # Find position of db address attribute
        title_bd_address_col = xl_read.find_title_index(inputWorksheet, 'DB_Address', dev_row, dev_col)
        # Find position of test set up attribute
        title_test_index_col = xl_read.find_title_index(inputWorksheet, 'Test Setup Index', dev_row, dev_col)

        self.all_tests = xl_read.make_list_of_tests(inputWorksheet, dev_row, dev_col, title_bd_address_col,
                                                    title_test_index_col)

        # set tree widget
        for i in range(len(self.all_tests)):
            item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
            self.treeWidget.topLevelItem(i).setText(0, _translate("MainWindow", self.all_tests[i].bd_address, None))
            for j in range(len(self.all_tests[i].ble_params)):
                item_1 = QtGui.QTreeWidgetItem(item_0)
                self.treeWidget.topLevelItem(i).child(j).setText(1, _translate("MainWindow",
                                                                               str(self.all_tests[i].ble_params[j][0]),
                                                                               None))

            self.treeWidget.setSortingEnabled(__sortingEnabled)

        #    excel
        ble_row, ble_col = xl_read.find_params_position(inputWorksheet, 'BLE Params')
        # # Find position of connection interval attribute
        # ci_col = xl_read.find_title_index(inputWorksheet, 'CI', ble_row, ble_col)
        # # Find position of latency attribute
        # latency_col = xl_read.find_title_index(inputWorksheet, 'Latency', ble_row, ble_col)
        # # Find position of to attribute
        # tout_col = xl_read.find_title_index(inputWorksheet, 'Tout', ble_row, ble_col)

        # __sortingEnabled = self.tableWidget.isSortingEnabled()
        # self.tableWidget.setSortingEnabled(False)

        # set rows and columns of ble params
        column_count = len(self.all_tests[0].ble_params[0])
        row_count = len(self.all_tests) * len(self.all_tests[0].ble_params)
        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(column_count)
        self.tableWidget.setRowCount(row_count)

        # add title ble params
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Index", None))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Retry", None))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CI", None))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Latency", None))
        item = QtGui.QTableWidgetItem()
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tout", None))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Timeout", None))

        # add ble params
        circle=0
        for i in range(len(self.all_tests)):
            for j in range(len(self.all_tests[i].ble_params)):
                for k in range(len(self.all_tests[i].ble_params[j])):
                    item = QtGui.QTableWidgetItem()
                    self.tableWidget.setItem(i + j+circle, k, item)
                    item = self.tableWidget.item(i + j+circle, k)
                    item.setText(_translate("MainWindow", str(self.all_tests[i].ble_params[j][k]), None))
            circle+=len(self.all_tests[i].ble_params)-1
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #self.tableWidget_2.setRowCount(1)
        #self.tableWidget_2.setColumnCount(1)
        #self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
		#
        #item = QtGui.QTableWidgetItem()                
        #self.tableWidget_2.setVerticalHeaderItem(0, item) 
        #item = self.tableWidget_2.verticalHeaderItem(0)        
        #self.tableWidget_2.verticalHeader().setDefaultSectionSize(300)
        #item.setText(_translate("MainWindow", "CMD/CMF/LRX", None))
        #item = QtGui.QTableWidgetItem()   
        #self.tableWidget_2.setHorizontalHeaderItem(0, item)
        #item = self.tableWidget_2.horizontalHeaderItem(0)        
        #self.tableWidget_2.horizontalHeader().setDefaultSectionSize(500)
        #item.setText(_translate("MainWindow", "LOGGER", None))
        #XStream.stdout().messageWritten.connect( self.textEdit.append)
        #XStream.stderr().messageWritten.connect( self.textEdit.append)

    def write_text_editor(self):
        self.textEdit.setPlainText("Logging..")


#if __name__ == "__main__":
#    import sys
#
#    app = QtGui.QApplication(sys.argv)
#    MainWindow = QtGui.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())
