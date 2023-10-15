# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFontComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QListView, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)
from static import resouces

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(688, 601)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.588015, y1:0.328, x2:1, y2:0, stop:0 rgba(210, 213, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"*{\n"
"border:none;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"padding:0;\n"
"margin:0;\n"
"}\n"
"QPushButton{\n"
"text-align:center;\n"
"padding: 0.5em 1em;\n"
"background-color: transparent;\n"
"color: #000000;\n"
"}\n"
"#stackedWidget {\n"
"background-color: #ffffff;\n"
"}\n"
"#home_btn {\n"
"background-color: #ffffff;\n"
"border-left: 3px solid #eee;\n"
"}\n"
"\n"
"#left_menu QPushButton:hover{\n"
"background-color:  rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"	padding: 3;\n"
"	border: 1px solid #000000;\n"
"	border-radius: 3;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"	padding: 3;\n"
"	border: 1px solid #000000;\n"
"	border-radius: 3;\n"
"}\n"
"\n"
""
                        "Line {\n"
"	background-color: rgb(168, 168, 168);\n"
"}\n"
" QToolTip {\n"
"        background-color: #FFFFFF;\n"
"        color: #000000;\n"
"        border: 1px solid #000000;\n"
" }\n"
"QDateEdit {\n"
" 	border: 1px solid #000000; \n"
"	padding: 0.5em;\n"
"}\n"
"#page_setting  QPushButton, #page_report  QPushButton, #page_chart  QPushButton, #page_result QPushButton {\n"
"background-color: rgb(197, 197, 197);\n"
"}\n"
"#page_setting  QPushButton:hover, #page_report  QPushButton:hover, #page_chart  QPushButton:hover, #page_result QPushButton:hover {\n"
"background-color: rgb(220, 220, 220);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.main_body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QWidget(self.main_body)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy2)
        self.left_menu.setMinimumSize(QSize(70, 0))
        self.left_menu.setMaximumSize(QSize(250, 16777215))
        self.left_menu.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.left_menu)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_btn_burger = QFrame(self.widget)
        self.frame_menu_btn_burger.setObjectName(u"frame_menu_btn_burger")
        self.verticalLayout_7 = QVBoxLayout(self.frame_menu_btn_burger)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.burger_btn = QPushButton(self.frame_menu_btn_burger)
        self.burger_btn.setObjectName(u"burger_btn")
        self.burger_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.burger_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/arrow_rigth.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.burger_btn.setIcon(icon)
        self.burger_btn.setIconSize(QSize(36, 36))
        self.burger_btn.setCheckable(True)
        self.burger_btn.setChecked(False)

        self.verticalLayout_7.addWidget(self.burger_btn, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_menu_btn_burger)

        self.frame_menu_btns = QFrame(self.widget)
        self.frame_menu_btns.setObjectName(u"frame_menu_btns")
        self.verticalLayout_6 = QVBoxLayout(self.frame_menu_btns)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_btn_navigation = QFrame(self.frame_menu_btns)
        self.frame_menu_btn_navigation.setObjectName(u"frame_menu_btn_navigation")
        self.verticalLayout_5 = QVBoxLayout(self.frame_menu_btn_navigation)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.report_btn = QPushButton(self.frame_menu_btn_navigation)
        self.report_btn.setObjectName(u"report_btn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.report_btn.setFont(font)
        self.report_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.report_btn.setToolTipDuration(-1)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/document.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.report_btn.setIcon(icon1)
        self.report_btn.setIconSize(QSize(34, 34))

        self.verticalLayout_5.addWidget(self.report_btn)

        self.chart_btn = QPushButton(self.frame_menu_btn_navigation)
        self.chart_btn.setObjectName(u"chart_btn")
        self.chart_btn.setFont(font)
        self.chart_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.chart_btn.setToolTipDuration(-1)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/bar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chart_btn.setIcon(icon2)
        self.chart_btn.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.chart_btn)

        self.result_btn = QPushButton(self.frame_menu_btn_navigation)
        self.result_btn.setObjectName(u"result_btn")
        self.result_btn.setFont(font)
        self.result_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.result_btn.setToolTipDuration(-1)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.result_btn.setIcon(icon3)
        self.result_btn.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.result_btn)


        self.verticalLayout_6.addWidget(self.frame_menu_btn_navigation)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.frame_menu_btn_setting = QFrame(self.frame_menu_btns)
        self.frame_menu_btn_setting.setObjectName(u"frame_menu_btn_setting")
        self.frame_menu_btn_setting.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_btn_setting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_menu_btn_setting)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.setting_btn = QPushButton(self.frame_menu_btn_setting)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy2.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy2)
        self.setting_btn.setFont(font)
        self.setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_btn.setToolTipDuration(-1)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon4)
        self.setting_btn.setIconSize(QSize(36, 36))

        self.verticalLayout_8.addWidget(self.setting_btn)


        self.verticalLayout_6.addWidget(self.frame_menu_btn_setting)


        self.verticalLayout_4.addWidget(self.frame_menu_btns)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.main_body_content = QFrame(self.main_body)
        self.main_body_content.setObjectName(u"main_body_content")
        sizePolicy.setHeightForWidth(self.main_body_content.sizePolicy().hasHeightForWidth())
        self.main_body_content.setSizePolicy(sizePolicy)
        self.main_body_content.setMinimumSize(QSize(600, 600))
        self.main_body_content.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.main_body_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.verticalLayout_10 = QVBoxLayout(self.page_report)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_page_report = QLabel(self.page_report)
        self.label_page_report.setObjectName(u"label_page_report")
        sizePolicy.setHeightForWidth(self.label_page_report.sizePolicy().hasHeightForWidth())
        self.label_page_report.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.label_page_report, 0, Qt.AlignTop)

        self.line_3 = QFrame(self.page_report)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_3)

        self.frame = QFrame(self.page_report)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_2)

        self.listView = QListView(self.frame)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_8.addWidget(self.listView)


        self.verticalLayout_10.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_report)
        self.page_chart = QWidget()
        self.page_chart.setObjectName(u"page_chart")
        self.verticalLayout_11 = QVBoxLayout(self.page_chart)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.page_chart)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignTop)

        self.line_4 = QFrame(self.page_chart)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_4)

        self.frame_19 = QFrame(self.page_chart)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.page_chart)
        self.page_result = QWidget()
        self.page_result.setObjectName(u"page_result")
        self.verticalLayout_12 = QVBoxLayout(self.page_result)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_4 = QLabel(self.page_result)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_12.addWidget(self.label_4, 0, Qt.AlignTop)

        self.line = QFrame(self.page_result)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.frame_11 = QFrame(self.page_result)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_11)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_result = QFrame(self.frame_11)
        self.frame_result.setObjectName(u"frame_result")
        self.frame_result.setFrameShape(QFrame.StyledPanel)
        self.frame_result.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_result)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.change_test = QComboBox(self.frame_result)
        self.change_test.addItem("")
        self.change_test.addItem("")
        self.change_test.addItem("")
        self.change_test.addItem("")
        self.change_test.addItem("")
        self.change_test.addItem("")
        self.change_test.addItem("")
        self.change_test.addItem("")
        self.change_test.addItem("")
        self.change_test.setObjectName(u"change_test")
        sizePolicy1.setHeightForWidth(self.change_test.sizePolicy().hasHeightForWidth())
        self.change_test.setSizePolicy(sizePolicy1)
        self.change_test.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.change_test)

        self.label_15 = QLabel(self.frame_result)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_5.addWidget(self.label_15, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.dateEdit_from = QDateEdit(self.frame_result)
        self.dateEdit_from.setObjectName(u"dateEdit_from")
        self.dateEdit_from.setCursor(QCursor(Qt.PointingHandCursor))
        self.dateEdit_from.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dateEdit_from.setDateTime(QDateTime(QDate(2023, 9, 9), QTime(21, 0, 0)))
        self.dateEdit_from.setMinimumDateTime(QDateTime(QDate(2023, 9, 9), QTime(21, 0, 0)))
        self.dateEdit_from.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dateEdit_from, 0, Qt.AlignVCenter)

        self.label_16 = QLabel(self.frame_result)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_5.addWidget(self.label_16, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.dateEdit_until = QDateEdit(self.frame_result)
        self.dateEdit_until.setObjectName(u"dateEdit_until")
        self.dateEdit_until.setCursor(QCursor(Qt.PointingHandCursor))
        self.dateEdit_until.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dateEdit_until.setMinimumDateTime(QDateTime(QDate(2023, 9, 13), QTime(21, 0, 0)))
        self.dateEdit_until.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dateEdit_until, 0, Qt.AlignVCenter)

        self.btn_complete_filter_result = QPushButton(self.frame_result)
        self.btn_complete_filter_result.setObjectName(u"btn_complete_filter_result")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_complete_filter_result.sizePolicy().hasHeightForWidth())
        self.btn_complete_filter_result.setSizePolicy(sizePolicy3)
        self.btn_complete_filter_result.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.btn_complete_filter_result)

        self.btn_open_extension_search = QPushButton(self.frame_result)
        self.btn_open_extension_search.setObjectName(u"btn_open_extension_search")
        sizePolicy3.setHeightForWidth(self.btn_open_extension_search.sizePolicy().hasHeightForWidth())
        self.btn_open_extension_search.setSizePolicy(sizePolicy3)
        self.btn_open_extension_search.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.btn_open_extension_search)


        self.verticalLayout_20.addWidget(self.frame_result, 0, Qt.AlignVCenter)

        self.tableView = QTableView(self.frame_11)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSortingEnabled(True)

        self.verticalLayout_20.addWidget(self.tableView)

        self.frame_change_model_result_2 = QFrame(self.frame_11)
        self.frame_change_model_result_2.setObjectName(u"frame_change_model_result_2")
        sizePolicy.setHeightForWidth(self.frame_change_model_result_2.sizePolicy().hasHeightForWidth())
        self.frame_change_model_result_2.setSizePolicy(sizePolicy)
        self.frame_change_model_result_2.setFrameShape(QFrame.StyledPanel)
        self.frame_change_model_result_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_change_model_result_2)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_delete_row_result = QPushButton(self.frame_change_model_result_2)
        self.btn_delete_row_result.setObjectName(u"btn_delete_row_result")
        sizePolicy3.setHeightForWidth(self.btn_delete_row_result.sizePolicy().hasHeightForWidth())
        self.btn_delete_row_result.setSizePolicy(sizePolicy3)
        self.btn_delete_row_result.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_delete_row_result)

        self.btn_generate_row = QPushButton(self.frame_change_model_result_2)
        self.btn_generate_row.setObjectName(u"btn_generate_row")
        sizePolicy3.setHeightForWidth(self.btn_generate_row.sizePolicy().hasHeightForWidth())
        self.btn_generate_row.setSizePolicy(sizePolicy3)
        self.btn_generate_row.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.btn_generate_row)

        self.btn_setting_result = QPushButton(self.frame_change_model_result_2)
        self.btn_setting_result.setObjectName(u"btn_setting_result")
        sizePolicy3.setHeightForWidth(self.btn_setting_result.sizePolicy().hasHeightForWidth())
        self.btn_setting_result.setSizePolicy(sizePolicy3)
        self.btn_setting_result.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/filter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting_result.setIcon(icon5)
        self.btn_setting_result.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.btn_setting_result)


        self.verticalLayout_20.addWidget(self.frame_change_model_result_2, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.page_result)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_13 = QVBoxLayout(self.page_setting)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_5 = QLabel(self.page_setting)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_13.addWidget(self.label_5, 0, Qt.AlignTop)

        self.line_2 = QFrame(self.page_setting)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.frame_scale = QFrame(self.page_setting)
        self.frame_scale.setObjectName(u"frame_scale")
        self.frame_scale.setFrameShape(QFrame.StyledPanel)
        self.frame_scale.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_scale)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.frame_scale)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.comboBox_scale = QComboBox(self.frame_scale)
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.setObjectName(u"comboBox_scale")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox_scale.sizePolicy().hasHeightForWidth())
        self.comboBox_scale.setSizePolicy(sizePolicy4)
        self.comboBox_scale.setMinimumSize(QSize(0, 0))
        self.comboBox_scale.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_scale.setAutoFillBackground(False)
        self.comboBox_scale.setEditable(False)
        self.comboBox_scale.setFrame(True)

        self.horizontalLayout_11.addWidget(self.comboBox_scale)


        self.verticalLayout_13.addWidget(self.frame_scale)

        self.frame_3 = QFrame(self.page_setting)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 8, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_settings_about_app = QPushButton(self.frame_10)
        self.btn_settings_about_app.setObjectName(u"btn_settings_about_app")
        sizePolicy3.setHeightForWidth(self.btn_settings_about_app.sizePolicy().hasHeightForWidth())
        self.btn_settings_about_app.setSizePolicy(sizePolicy3)
        self.btn_settings_about_app.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_settings_about_app)

        self.btn_setting_save = QPushButton(self.frame_10)
        self.btn_setting_save.setObjectName(u"btn_setting_save")
        sizePolicy3.setHeightForWidth(self.btn_setting_save.sizePolicy().hasHeightForWidth())
        self.btn_setting_save.setSizePolicy(sizePolicy3)
        self.btn_setting_save.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_setting_save)


        self.horizontalLayout.addWidget(self.frame_10, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.frame_6, 9, 0, 1, 1)

        self.frame_18 = QFrame(self.frame_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_18)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_13, 0, Qt.AlignBottom)

        self.btn_setting_user_guide = QPushButton(self.frame_18)
        self.btn_setting_user_guide.setObjectName(u"btn_setting_user_guide")
        self.btn_setting_user_guide.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.btn_setting_user_guide)


        self.gridLayout.addWidget(self.frame_18, 2, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_7)

        self.btn_check_conn_database = QPushButton(self.frame_8)
        self.btn_check_conn_database.setObjectName(u"btn_check_conn_database")
        self.btn_check_conn_database.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_9.addWidget(self.btn_check_conn_database)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_11, 0, Qt.AlignTop)

        self.btn_config_database = QPushButton(self.frame_7)
        self.btn_config_database.setObjectName(u"btn_config_database")
        self.btn_config_database.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.btn_config_database)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.gridLayout.addWidget(self.frame_5, 7, 0, 1, 1)

        self.frame_language = QFrame(self.frame_3)
        self.frame_language.setObjectName(u"frame_language")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_language.sizePolicy().hasHeightForWidth())
        self.frame_language.setSizePolicy(sizePolicy5)
        self.frame_language.setFrameShape(QFrame.StyledPanel)
        self.frame_language.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_language)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_language)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.comboBox_language = QComboBox(self.frame_language)
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.setObjectName(u"comboBox_language")
        sizePolicy5.setHeightForWidth(self.comboBox_language.sizePolicy().hasHeightForWidth())
        self.comboBox_language.setSizePolicy(sizePolicy5)
        self.comboBox_language.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.comboBox_language)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.frame_theme = QFrame(self.frame_language)
        self.frame_theme.setObjectName(u"frame_theme")
        self.frame_theme.setFrameShape(QFrame.StyledPanel)
        self.frame_theme.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_theme)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.frame_theme)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.comboBox_theme = QComboBox(self.frame_theme)
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        sizePolicy5.setHeightForWidth(self.comboBox_theme.sizePolicy().hasHeightForWidth())
        self.comboBox_theme.setSizePolicy(sizePolicy5)
        self.comboBox_theme.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.comboBox_theme)


        self.horizontalLayout_10.addWidget(self.frame_theme)


        self.gridLayout.addWidget(self.frame_language, 0, 0, 1, 1)

        self.frame_17 = QFrame(self.frame_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")

        self.horizontalLayout_14.addWidget(self.label, 0, Qt.AlignLeft)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.fontComboBox = QFontComboBox(self.frame_17)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy5.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy5)
        self.fontComboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.fontComboBox)

        self.frame_16 = QFrame(self.frame_17)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.horizontalLayout_13.addWidget(self.label_6)

        self.spinBox = QSpinBox(self.frame_16)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox.setMinimum(5)

        self.horizontalLayout_13.addWidget(self.spinBox)


        self.horizontalLayout_14.addWidget(self.frame_16)


        self.gridLayout.addWidget(self.frame_17, 1, 0, 1, 1)

        self.btn_open_hot_keys_2 = QPushButton(self.frame_3)
        self.btn_open_hot_keys_2.setObjectName(u"btn_open_hot_keys_2")
        self.btn_open_hot_keys_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_open_hot_keys_2, 4, 0, 1, 1)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(True)

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_9, 6, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 10)

        self.verticalLayout_13.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_setting)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.main_body_content)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.burger_btn.setText("")
#if QT_CONFIG(shortcut)
        self.burger_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.report_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.report_btn.setText("")
#if QT_CONFIG(shortcut)
        self.report_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.chart_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.chart_btn.setText("")
#if QT_CONFIG(shortcut)
        self.chart_btn.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.result_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.result_btn.setText("")
#if QT_CONFIG(shortcut)
        self.result_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.setting_btn.setText("")
#if QT_CONFIG(shortcut)
        self.setting_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_page_report.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.change_test.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))
        self.change_test.setItemText(1, QCoreApplication.translate("MainWindow", u"HPCG", None))
        self.change_test.setItemText(2, QCoreApplication.translate("MainWindow", u"HPL", None))
        self.change_test.setItemText(3, QCoreApplication.translate("MainWindow", u"IMB", None))
        self.change_test.setItemText(4, QCoreApplication.translate("MainWindow", u"MPIGraph", None))
        self.change_test.setItemText(5, QCoreApplication.translate("MainWindow", u"b_eff", None))
        self.change_test.setItemText(6, QCoreApplication.translate("MainWindow", u"NFStest", None))
        self.change_test.setItemText(7, QCoreApplication.translate("MainWindow", u"STREAM", None))
        self.change_test.setItemText(8, QCoreApplication.translate("MainWindow", u"IOZONE", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e", None))
        self.btn_complete_filter_result.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_open_extension_search.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.btn_delete_row_result.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_generate_row.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.btn_setting_result.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438 \u0434\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431", None))
        self.comboBox_scale.setItemText(0, QCoreApplication.translate("MainWindow", u"50%", None))
        self.comboBox_scale.setItemText(1, QCoreApplication.translate("MainWindow", u"80%", None))
        self.comboBox_scale.setItemText(2, QCoreApplication.translate("MainWindow", u"100%", None))
        self.comboBox_scale.setItemText(3, QCoreApplication.translate("MainWindow", u"120%", None))
        self.comboBox_scale.setItemText(4, QCoreApplication.translate("MainWindow", u"150%", None))
        self.comboBox_scale.setItemText(5, QCoreApplication.translate("MainWindow", u"200%", None))

        self.comboBox_scale.setCurrentText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.btn_settings_about_app.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.btn_setting_save.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f TsT Graph", None))
        self.btn_setting_user_guide.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435 \u0441 \u0411\u0414", None))
        self.btn_check_conn_database.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044e \u0411\u0414", None))
        self.btn_config_database.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a", None))
        self.comboBox_language.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.comboBox_language.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
        self.comboBox_theme.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.comboBox_theme.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.btn_open_hot_keys_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u044f\u0447\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0432 TsT Graph", None))
    # retranslateUi

