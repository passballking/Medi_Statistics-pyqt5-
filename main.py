import sys, logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog
from demo_main_window import *
from demo_company_list import *
from demo_check_item_list import *


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        # 初始化数据
        self.checkItemPriceDict = {'检查项目A': 101, '检查项目B': 200,
                             '检查项目C': 300, '检查项目D': 200, '检查项目E': 300, '检查项目F': 50234, '检查项目G': 120}
        self.companyPriceDict = dict()
        self.patientsList = []
        self.main_ui.choose_company_button.clicked.connect(self.getCompanyList)
        self.main_ui.choose_items_button.clicked.connect(self.getCheckItemsList)
        self.main_ui.add_one_unit_button.clicked.connect(self.add_one_unit)
        self.main_ui.delete_one_unit_button.clicked.connect(self.delete_one_unit)
        self.main_ui.save_to_file_button.clicked.connect(self.save_to_file)

    def getCompanyList(self):
        self.companyWin = companyWindow()
        self.companyWin.show()
        self.companyWin.company_list_ui.company_list_widget.itemDoubleClicked.connect(self.get_company_name)

    def get_company_name(self, item):
        self.main_ui.checked_comapny_label.setText(item.text())
        self.companyWin.close()

    def getCheckItemsList(self):
        self.checkItemListWin = checkItemWindow()
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

class companyWindow(QDialog, Ui_company_list):
    def __init__(self):
        QDialog.__init__(self)
        self.company_list_ui = Ui_company_list()
        self.company_list_ui.setupUi(self)
        companyList = ['公司Asfhajskdfjkshdfjkahksdjfhjashdjfkhalksjdfhalsdjkfhajskdlfaksjdhfjaslkhf', '公司12', '公司A432', '公司Afasd', '公司fas', '公司234fw', '公司bfg', '公司hrs']
        for i in companyList:
            self.company_list_ui.company_list_widget.addItem(i)

class checkItemWindow(QDialog, Ui_item_list_dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.check_item_list_ui = Ui_item_list_dialog()
        self.check_item_list_ui.setupUi(self)
        checkItemList = ['检查项目A', '检查项目B',
                       '检查项目C', '检查项目D', '检查项目E', '检查项目F', '检查项目G']
        for i in checkItemList:
            self.check_item_list_ui.item_check_listWidget.addItem(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = mainWindow()
    mainWin.show()
    sys.exit(app.exec_())
