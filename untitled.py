# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1621, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabPages = QtWidgets.QTabWidget(self.centralwidget)
        self.tabPages.setGeometry(QtCore.QRect(20, 10, 1581, 801))
        self.tabPages.setObjectName("tabPages")
        self.tabPage1 = QtWidgets.QWidget()
        self.tabPage1.setObjectName("tabPage1")
        self.layoutWidget = QtWidgets.QWidget(self.tabPage1)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 161, 185))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.host_label = QtWidgets.QLabel(self.layoutWidget)
        self.host_label.setObjectName("host_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.host_label)
        self.host_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.host_edit.setObjectName("host_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.host_edit)
        self.port_label = QtWidgets.QLabel(self.layoutWidget)
        self.port_label.setObjectName("port_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.port_label)
        self.port_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.port_edit.setObjectName("port_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.port_edit)
        self.user_label = QtWidgets.QLabel(self.layoutWidget)
        self.user_label.setObjectName("user_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.user_label)
        self.user_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_edit.setObjectName("user_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.user_edit)
        self.password_label = QtWidgets.QLabel(self.layoutWidget)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.password_label)
        self.password_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_edit.setInputMask("")
        self.password_edit.setText("")
        self.password_edit.setObjectName("password_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password_edit)
        self.mysql_connection_test = QtWidgets.QPushButton(self.layoutWidget)
        self.mysql_connection_test.setObjectName("mysql_connection_test")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.mysql_connection_test)
        self.widget_mysqlTestMsgBox = QtWidgets.QTextBrowser(self.tabPage1)
        self.widget_mysqlTestMsgBox.setGeometry(QtCore.QRect(900, 10, 661, 171))
        self.widget_mysqlTestMsgBox.setObjectName("widget_mysqlTestMsgBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tabPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 210, 1551, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.retrieveData = QtWidgets.QPushButton(self.tabPage1)
        self.retrieveData.setGeometry(QtCore.QRect(790, 170, 80, 24))
        self.retrieveData.setObjectName("retrieveData")
        self.filters = QtWidgets.QLineEdit(self.tabPage1)
        self.filters.setGeometry(QtCore.QRect(241, 128, 631, 41))
        self.filters.setText("")
        self.filters.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.filters.setObjectName("filters")
        self.layoutWidget1 = QtWidgets.QWidget(self.tabPage1)
        self.layoutWidget1.setGeometry(QtCore.QRect(241, 12, 631, 85))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.databaseName_label = QtWidgets.QLabel(self.layoutWidget1)
        self.databaseName_label.setObjectName("databaseName_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.databaseName_label)
        self.databaseName_edit = QtWidgets.QComboBox(self.layoutWidget1)
        self.databaseName_edit.setObjectName("databaseName_edit")
        self.databaseName_edit.addItem("")
        self.databaseName_edit.addItem("")
        self.databaseName_edit.addItem("")
        self.databaseName_edit.addItem("")
        self.databaseName_edit.addItem("")
        self.databaseName_edit.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.databaseName_edit)
        self.gridLayout.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.tableName_label = QtWidgets.QLabel(self.layoutWidget1)
        self.tableName_label.setObjectName("tableName_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.tableName_label)
        self.tableName_edit = QtWidgets.QComboBox(self.layoutWidget1)
        self.tableName_edit.setObjectName("tableName_edit")
        self.tableName_edit.addItem("")
        self.tableName_edit.addItem("")
        self.tableName_edit.addItem("")
        self.tableName_edit.addItem("")
        self.tableName_edit.addItem("")
        self.tableName_edit.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tableName_edit)
        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableName_label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.tableName_label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableName_label_2.sizePolicy().hasHeightForWidth())
        self.tableName_label_2.setSizePolicy(sizePolicy)
        self.tableName_label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.tableName_label_2.setObjectName("tableName_label_2")
        self.horizontalLayout.addWidget(self.tableName_label_2)
        self.startDate = QtWidgets.QDateEdit(self.layoutWidget1)
        self.startDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 3, 1), QtCore.QTime(0, 0, 0)))
        self.startDate.setObjectName("startDate")
        self.horizontalLayout.addWidget(self.startDate)
        self.startTime = QtWidgets.QTimeEdit(self.layoutWidget1)
        self.startTime.setObjectName("startTime")
        self.horizontalLayout.addWidget(self.startTime)
        self.tableName_label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.tableName_label_4.setObjectName("tableName_label_4")
        self.horizontalLayout.addWidget(self.tableName_label_4)
        self.endDate = QtWidgets.QDateEdit(self.layoutWidget1)
        self.endDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 6, 1), QtCore.QTime(0, 0, 0)))
        self.endDate.setObjectName("endDate")
        self.horizontalLayout.addWidget(self.endDate)
        self.endTime = QtWidgets.QTimeEdit(self.layoutWidget1)
        self.endTime.setObjectName("endTime")
        self.horizontalLayout.addWidget(self.endTime)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.mysqlRetrieveContent = QtWidgets.QLineEdit(self.tabPage1)
        self.mysqlRetrieveContent.setGeometry(QtCore.QRect(241, 101, 631, 21))
        self.mysqlRetrieveContent.setText("")
        self.mysqlRetrieveContent.setObjectName("mysqlRetrieveContent")
        self.tabPages.addTab(self.tabPage1, "")
        self.tabPage2 = QtWidgets.QWidget()
        self.tabPage2.setObjectName("tabPage2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabPage2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(520, 10, 461, 721))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.layout_hists = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.layout_hists.setContentsMargins(0, 0, 0, 0)
        self.layout_hists.setObjectName("layout_hists")
        self.layoutWidget2 = QtWidgets.QWidget(self.tabPage2)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 511, 721))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layout_lines = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.layout_lines.setContentsMargins(0, 0, 0, 0)
        self.layout_lines.setObjectName("layout_lines")
        self.layoutWidget3 = QtWidgets.QWidget(self.tabPage2)
        self.layoutWidget3.setGeometry(QtCore.QRect(990, 10, 141, 721))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.extreamSliderLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.extreamSliderLayout.setContentsMargins(0, 0, 0, 0)
        self.extreamSliderLayout.setObjectName("extreamSliderLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabPage2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 730, 1041, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabPage2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1140, 10, 431, 671))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser_dataTransfer = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser_dataTransfer.setObjectName("textBrowser_dataTransfer")
        self.verticalLayout_2.addWidget(self.textBrowser_dataTransfer)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tabPage2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1430, 690, 141, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.genSqlCriticalParamBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.genSqlCriticalParamBtn.setObjectName("genSqlCriticalParamBtn")
        self.gridLayout_4.addWidget(self.genSqlCriticalParamBtn, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.tabPages.addTab(self.tabPage2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabPages.setCurrentIndex(0)
        self.databaseName_edit.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.host_label.setText(_translate("MainWindow", "HOST"))
        self.host_edit.setPlaceholderText(_translate("MainWindow", "127.0.0.1"))
        self.port_label.setText(_translate("MainWindow", "PORT"))
        self.port_edit.setPlaceholderText(_translate("MainWindow", "3306"))
        self.user_label.setText(_translate("MainWindow", "USER"))
        self.user_edit.setPlaceholderText(_translate("MainWindow", "root"))
        self.password_label.setText(_translate("MainWindow", "PWD"))
        self.password_edit.setPlaceholderText(_translate("MainWindow", "000000"))
        self.mysql_connection_test.setText(_translate("MainWindow", "连接测试"))
        self.retrieveData.setText(_translate("MainWindow", "数据查询测试"))
        self.filters.setPlaceholderText(_translate("MainWindow", "筛选条件，默认: 空，形如：and (发电机定子铁芯铜屏蔽温度1_汽端 <= 100)"))
        self.databaseName_label.setText(_translate("MainWindow", "数据库名称"))
        self.databaseName_edit.setCurrentText(_translate("MainWindow", "stator_core_temper_copperisolate"))
        self.databaseName_edit.setItemText(0, _translate("MainWindow", "stator_core_temper_copperisolate"))
        self.databaseName_edit.setItemText(1, _translate("MainWindow", "stator_core_temper_fingerpress"))
        self.databaseName_edit.setItemText(2, _translate("MainWindow", "stator_core_temper_ringpress"))
        self.databaseName_edit.setItemText(3, _translate("MainWindow", "stator_core_temper_teeth"))
        self.databaseName_edit.setItemText(4, _translate("MainWindow", "stator_core_temper_yoke"))
        self.databaseName_edit.setItemText(5, _translate("MainWindow", "laizhou_2021"))
        self.tableName_label.setText(_translate("MainWindow", "表名称"))
        self.tableName_edit.setItemText(0, _translate("MainWindow", "20210301_20210531莱州铁芯铜屏蔽调整结构"))
        self.tableName_edit.setItemText(1, _translate("MainWindow", "20210301_20210531莱州铁芯压指调整结构"))
        self.tableName_edit.setItemText(2, _translate("MainWindow", "20210301_20210531莱州铁芯压圈调整结构"))
        self.tableName_edit.setItemText(3, _translate("MainWindow", "20210301_20210531莱州铁芯齿部调整结构"))
        self.tableName_edit.setItemText(4, _translate("MainWindow", "20210301_20210531莱州铁芯轭部调整结构"))
        self.tableName_edit.setItemText(5, _translate("MainWindow", "莱州1号机组2022年01月18号发电机相关数据"))
        self.tableName_label_2.setText(_translate("MainWindow", "开始时间"))
        self.startDate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.startTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.tableName_label_4.setText(_translate("MainWindow", "截止时间"))
        self.endDate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.endTime.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.mysqlRetrieveContent.setPlaceholderText(_translate("MainWindow", "查询命令，默认:\'时间戳,发电机定子铁芯铜屏蔽温度1_汽端...\',可选count(*),不允许‘*’"))
        self.tabPages.setTabText(self.tabPages.indexOf(self.tabPage1), _translate("MainWindow", "数据库测试"))
        self.label.setText(_translate("MainWindow", "    注意：对单个测点数据进行筛选时，其它测点样本会联动（数据一致性保证）"))
        self.genSqlCriticalParamBtn.setText(_translate("MainWindow", "打印SQL关键参数"))
        self.tabPages.setTabText(self.tabPages.indexOf(self.tabPage2), _translate("MainWindow", "数据处理"))
