import uart_data_handler_form
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor
import sys
from str_hex import str_hex
import para_cmd


class uart_data_handler_UI(QtWidgets.QWidget, uart_data_handler_form.Ui_MainWindow):
    def __init__(self, parent=None):
        super(uart_data_handler_UI, self).__init__(parent)
        self.setupUi(self)

        self.cmd_para = para_cmd.PARA_CMD()

        # 增加槽函数
        self.pushButton_add.clicked.connect(self.clicked_add_para_button)
        self.pushButton_clear.clicked.connect(self.clicked_clear_button)
        self.pushButton_del.clicked.connect(self.clicked_del_button)

    def clicked_add_para_button(self):
        '''
        点击添加按键的操作
        '''
        # 获取编辑框的字符串
        cmd_str = self.lineEdit_CMD.text()
        para_type_str = self.lineEdit_para_type.text()
        para_data_str = self.lineEdit_Para_data.text()

        # 判断内容有无，决定当前添加命令还是添加参数
        if len(para_type_str) == 0 and len(para_data_str) == 0:
            if len(cmd_str) != 0:
                # 只添加命令
                mode = 0
            else:
                # 都没有
                return
        elif len(para_type_str) == 0 or len(para_data_str) == 0:
            QtWidgets.QMessageBox.warning(self,'缺少参数', '请正确输入。', QtWidgets.QMessageBox.Ok)
            return
        else:
            if len(cmd_str) != 0:
                mode = 1
            else:
                QtWidgets.QMessageBox.warning(self,'缺少命令', '请正确输入。', QtWidgets.QMessageBox.Ok)
                return
        
        if mode == 0:
            # 只添加命令
            # 将命令字符串转换成int列表
            self.list_cmd = self.__GetStrlist(cmd_str)
        
            if len(self.list_cmd) == 0:
                # 出错
                QtWidgets.QMessageBox.warning(self,'命令输入错误', '请正确输入。', QtWidgets.QMessageBox.Ok)
                return

            if self.cmd_para.add_cmd(self.list_cmd) == False:
                QtWidgets.QMessageBox.warning(self,'命令输入错误', '请正确输入。', QtWidgets.QMessageBox.Ok)
                return

        elif mode == 1:
            # 添加命令和参数
            # 将命令字符串转换成int列表
            self.list_cmd = self.__GetStrlist(cmd_str)
        
            if len(self.list_cmd) == 0:
                # 出错
                QtWidgets.QMessageBox.warning(self,'命令输入错误', '请正确输入。', QtWidgets.QMessageBox.Ok)
                return
        
            # 将参数类型字符串转换成int列表
            self.list_para_type = self.__GetStrlist(para_type_str)

            if len(self.list_para_type) == 0:
                # 出错
                QtWidgets.QMessageBox.warning(self,'参数类型输入错误', '请正确输入。', QtWidgets.QMessageBox.Ok)
                return

            # 将参数数据字符串转换成int列表
            self.list_para_data = self.__GetStrlist(para_data_str)

            if len(self.list_para_data) == 0:
                # 出错
                QtWidgets.QMessageBox.warning(self,'参数数据输入错误', '请正确输入。', QtWidgets.QMessageBox.Ok)
                return

            if self.cmd_para.add_cmd(self.list_cmd) == False:
                QtWidgets.QMessageBox.warning(self,'命令输入错误', '请正确输入。', QtWidgets.QMessageBox.Ok)
                return

            if self.cmd_para.add_para(self.list_para_type, self.list_para_data) == False:
                QtWidgets.QMessageBox.warning(self,'参数输入错误', '请正确输入。', QtWidgets.QMessageBox.Ok)
                return

        self.show_str()

    def clicked_clear_button(self):
        # 清空参数字节
        self.cmd_para = para_cmd.PARA_CMD()
        
        # 清空显示
        self.lineEdit_CMD.setText('')
        self.lineEdit_Para_data.setText('')
        self.lineEdit_para_type.setText('')
        self.textBrowser_display.setText('')
    
    def clicked_del_button(self):
        self.cmd_para.del_para()
        self.show_str()

    def show_str(self):
        #命令和参数均添加完毕
        int_list_para_cmd = self.cmd_para.completeCmdPara()

        if int_list_para_cmd == None:
            return

        show_str = ''
        
        for val in int_list_para_cmd:
            show_str += '%02X'%val
            show_str += ' '
        
        self.textBrowser_display.setText(show_str)

    def __GetStrlist(self,hexstr):
        list_str = str_hex().isHexStr(hexstr)

        if list_str == 'Split':
            list_str = str_hex().SplitStr2list(hexstr)
        elif list_str == 'NoSplit':
            list_str = str_hex().NoSplitStr2list(hexstr)
        else:
            return None

        if list_str == None:
            return None

        return list_str

def mywindow():
    mywindow = uart_data_handler_UI()
    mywindow.show()
    return mywindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myobj = mywindow()
    sys.exit(app.exec_())
