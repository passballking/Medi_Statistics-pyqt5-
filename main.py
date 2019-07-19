import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog
from PyQt5.QtCore import QSettings, QTextCodec
from demo_main_window import *
from demo_company_list import *
from demo_check_item_list import *


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        # 初始化数据
        settings = QSettings("ZhongLiuYiYuanConfig.ini", QSettings.IniFormat)
        for i in settings.allKeys():
            print(i)
        self.checkItemPriceDict = {'检查项目A': 101, '检查项目B': 200,
                             '检查项目C': 300, '检查项目D': 200, '检查项目E': 300, '检查项目F': 50234, '检查项目G': 120}
        self.checkItemList = ['检查项目A', '检查项目B',
                         '检查项目C', '检查项目D', '检查项目E', '检查项目F', '检查项目G']
        self.companyList = ['公司VVVh', '公司12', '公司A432', '公司Afasd', '公司fas', '公司234fw', '公司bfg']
        self.companyPriceDict = dict()
        self.patientsList = []
        self.main_ui.choose_company_button.clicked.connect(self.openCompanyWindow)
        self.main_ui.choose_items_button.clicked.connect(self.opencheckItemWindow)
        self.main_ui.add_one_unit_button.clicked.connect(self.add_one_unit)
        self.main_ui.delete_one_unit_button.clicked.connect(self.delete_one_unit)
        self.main_ui.save_to_file_button.clicked.connect(self.save_to_file)
        self.main_ui.com_add_pushButton.clicked.connect(self.add_com_to_list)
        self.main_ui.com_del_pushButton.clicked.connect(self.del_com_to_list)
        self.main_ui.item_price_add_pushButton.clicked.connect(self.add_item_price_to_list)
        self.main_ui.item_price_del_pushButton.clicked.connect(self.del_item_price_to_list)
        self.main_ui.save_to_ini_button.clicked.connect(self.save_to_ini_file)

        #初始化页面
        for i in self.companyList:
            self.main_ui.page2_com_listWidget.addItem(i)
        for j in self.checkItemPriceDict:
            self.main_ui.page2_item_price_listWidget.addItem(j + ':' + str(self.checkItemPriceDict[j]))

    def openCompanyWindow(self):
        self.companyWin = companyWindow()
        for i in self.companyList:
            self.companyWin.company_list_ui.company_list_widget.addItem(i)
        self.companyWin.show()
        self.companyWin.company_list_ui.company_list_widget.itemDoubleClicked.connect(self.get_company_name)
        self.main_ui.checked_comapny_label.clear()

    def get_company_name(self, item):
        self.main_ui.checked_comapny_label.setText(item.text())
        self.companyWin.close()

    def opencheckItemWindow(self):
        self.checkItemListWin = checkItemWindow()
        for i in self.checkItemList:
            self.checkItemListWin.check_item_list_ui.item_check_listWidget.addItem(i)
        self.checkItemListWin.show()
        self.checkItemListWin.accepted.connect(self.get_check_items_names)
        self.main_ui.checked_items_listWidget.clear()

    def get_check_items_names(self):
        items_list = self.checkItemListWin.check_item_list_ui.item_check_listWidget.selectedItems()
        for i in list(items_list):
            self.main_ui.checked_items_listWidget.addItem(i.text())
        self.checkItemListWin.close()

    def add_one_unit(self):
        count = self.main_ui.checked_items_listWidget.count()
        this_com_name = self.main_ui.checked_comapny_label.text()
        if count == 0 or this_com_name == '':
            QMessageBox.information(self, 'Warning', self.tr('请添加公司或添加检查项目！！！'))
            return
        add_text = '公司: ' + this_com_name + ', '
        one_company_price = 0
        for i in range(count):
            add_text += self.main_ui.checked_items_listWidget.item(i).text() + ' '
            one_company_price += self.checkItemPriceDict[self.main_ui.checked_items_listWidget.item(i).text()]
        if this_com_name in self.companyPriceDict:
            self.companyPriceDict[this_com_name] += one_company_price
        else:
            self.companyPriceDict[this_com_name] = one_company_price
        self.main_ui.units_list_listWidget.addItem(add_text)
        self.main_ui.all_company_price_listWidgets.clear()
        for j in self.companyPriceDict:
            self.main_ui.all_company_price_listWidgets.addItem('公司： ' + j + '  价格: ' + str(self.companyPriceDict[j]))
        self.patientsList.append({this_com_name: one_company_price})
        self.main_ui.checked_items_listWidget.clear()
        self.main_ui.checked_comapny_label.clear()

    def delete_one_unit(self):
        row = self.main_ui.units_list_listWidget.currentRow()
        if row != -1:
            com_name = list(self.patientsList[row].keys())[0]
            com_price = self.patientsList[row][com_name]
        self.companyPriceDict[com_name] -= com_price
        del self.patientsList[row]
        self.main_ui.all_company_price_listWidgets.clear()
        for j in self.companyPriceDict:
            self.main_ui.all_company_price_listWidgets.addItem('公司： ' + j + '  价格: ' + str(self.companyPriceDict[j]))
        self.main_ui.units_list_listWidget.takeItem(row)

    def save_to_file(self):
        file_path = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "C:\\")
        print(file_path)
        with open(file_path + '\今日统计结果.txt', 'w') as f:
            f.write("总计:\n")
            for one_company in self.companyPriceDict:
                f.write(one_company + ' : ' + str(self.companyPriceDict[one_company]) + "\n")
            f.write("\n明细:\n")
            for item in self.patientsList:
                f.write("%s\n" % item)
            f.close()

    def add_com_to_list(self):
        if hasattr(self, 'companyWin'):
            self.companyWin.close()
        this_com_name = self.main_ui.com_lineEdit.text()
        if this_com_name == '':
            QMessageBox.information(self, 'Warning', self.tr('请添加公司！！！'))
            return
        if this_com_name in self.companyList:
            QMessageBox.information(self, 'Warning', self.tr('该公司已经添加！！！'))
            return
        self.companyList.append(this_com_name)
        self.main_ui.page2_com_listWidget.addItem(this_com_name)
        self.main_ui.com_lineEdit.clear()

    def add_item_price_to_list(self):
        if hasattr(self, 'checkItemListWin'):
            self.checkItemListWin.close()
        this_item_name = self.main_ui.item_lineEdit.text()
        this_item_price = self.main_ui.item_price_spinBox.value()
        if this_item_name == '':
            QMessageBox.information(self, 'Warning', self.tr('请添加项目名称！！！'))
            return
        if this_item_name in self.companyPriceDict:
            QMessageBox.information(self, 'Warning', self.tr('该项目已经添加！！！'))
            return
        self.checkItemList.append(this_item_name)
        self.checkItemPriceDict[this_item_name] = this_item_price
        self.main_ui.page2_item_price_listWidget.addItem(this_item_name + ':' + str(this_item_price))
        self.main_ui.com_lineEdit.clear()
        self.main_ui.item_price_spinBox.setValue(0)

    def del_com_to_list(self):
        if hasattr(self, 'companyWin'):
            self.companyWin.close()
        row = self.main_ui.page2_com_listWidget.currentRow()
        del self.companyList[row]
        self.main_ui.page2_com_listWidget.takeItem(row)

    def del_item_price_to_list(self):
        if hasattr(self, 'checkItemListWin'):
            self.checkItemListWin.close()
        row = self.main_ui.page2_item_price_listWidget.currentRow()
        del self.checkItemPriceDict[self.checkItemList[row]]
        del self.checkItemList[row]
        self.main_ui.page2_item_price_listWidget.takeItem(row)

    def save_to_ini_file(self):
        settings = QSettings("ZhongLiuYiYuanConfig.ini", QSettings.IniFormat)
        settings.setIniCodec(QTextCodec.codecForName("GB2312"))
        settings.beginGroup("CompanyList")
        for i in range(len(self.companyList)):
            settings.setValue("companyName" + str(i), self.companyList[i])
        settings.endGroup()
        settings.beginGroup("ItemPriceList")
        for j in self.checkItemPriceDict:
            settings.setValue(j, str(self.checkItemPriceDict[j]))
        settings.endGroup()


class companyWindow(QDialog, Ui_company_list):
    def __init__(self):
        QDialog.__init__(self)
        self.company_list_ui = Ui_company_list()
        self.company_list_ui.setupUi(self)

class checkItemWindow(QDialog, Ui_item_list_dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.check_item_list_ui = Ui_item_list_dialog()
        self.check_item_list_ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = mainWindow()
    mainWin.show()
    sys.exit(app.exec_())
