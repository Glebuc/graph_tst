# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
from static import resouces

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
"text-align:left;\n"
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
"QLabel{\n"
"font-size: 20px;\n"
"}\n"
"#left_menu QPushButton:hover{\n"
"background-color:  rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(255, 255, 255);\n"
"    selection-color: rgb(200, 200, 200);\n"
"}\n"
" QToolTip {\n"
"        background-color: #FFFFFF; /* \u0416\u0435\u043b\u0442\u044b\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"        color: #000000; /* \u0427\u0435"
                        "\u0440\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"        border: 1px solid #000000; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
" }")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.main_body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QWidget(self.main_body)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy1)
        self.left_menu.setMinimumSize(QSize(60, 0))
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
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.burger_btn = QPushButton(self.widget_4)
        self.burger_btn.setObjectName(u"burger_btn")
        self.burger_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.burger_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/arrow_rigth.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.burger_btn.setIcon(icon)
        self.burger_btn.setIconSize(QSize(36, 36))
        self.burger_btn.setCheckable(True)

        self.verticalLayout_7.addWidget(self.burger_btn, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.widget_4, 0, Qt.AlignLeft)

        self.widget_menu = QWidget(self.widget)
        self.widget_menu.setObjectName(u"widget_menu")
        self.verticalLayout_6 = QVBoxLayout(self.widget_menu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.report_btn = QPushButton(self.frame_2)
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

        self.chart_btn = QPushButton(self.frame_2)
        self.chart_btn.setObjectName(u"chart_btn")
        self.chart_btn.setFont(font)
        self.chart_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.chart_btn.setToolTipDuration(-1)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/bar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chart_btn.setIcon(icon2)
        self.chart_btn.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.chart_btn)

        self.result_btn = QPushButton(self.frame_2)
        self.result_btn.setObjectName(u"result_btn")
        self.result_btn.setFont(font)
        self.result_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.result_btn.setToolTipDuration(-1)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.result_btn.setIcon(icon3)
        self.result_btn.setIconSize(QSize(36, 36))

        self.verticalLayout_5.addWidget(self.result_btn)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.frame = QFrame(self.widget_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.setting_btn = QPushButton(self.frame)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy1.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy1)
        self.setting_btn.setFont(font)
        self.setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_btn.setToolTipDuration(-1)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon4)
        self.setting_btn.setIconSize(QSize(36, 36))

        self.verticalLayout_8.addWidget(self.setting_btn)


        self.verticalLayout_6.addWidget(self.frame)


        self.verticalLayout_4.addWidget(self.widget_menu)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.left_menu)

        self.main_body_content = QWidget(self.main_body)
        self.main_body_content.setObjectName(u"main_body_content")
        self.main_body_content.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.main_body_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setMinimumSize(QSize(400, 600))
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.verticalLayout_10 = QVBoxLayout(self.page_report)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.page_report)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_report)
        self.page_chart = QWidget()
        self.page_chart.setObjectName(u"page_chart")
        self.verticalLayout_11 = QVBoxLayout(self.page_chart)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.page_chart)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_chart)
        self.page_result = QWidget()
        self.page_result.setObjectName(u"page_result")
        self.verticalLayout_12 = QVBoxLayout(self.page_result)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_4 = QLabel(self.page_result)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_12.addWidget(self.label_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_result)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_13 = QVBoxLayout(self.page_setting)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_5 = QLabel(self.page_setting)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_13.addWidget(self.label_5)

        self.frame_3 = QFrame(self.page_setting)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMaximumSize(QSize(160000, 160000))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_scale = QFrame(self.frame_4)
        self.frame_scale.setObjectName(u"frame_scale")
        self.frame_scale.setFrameShape(QFrame.StyledPanel)
        self.frame_scale.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_scale)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_8 = QLabel(self.frame_scale)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.verticalLayout_17.addWidget(self.label_8, 0, Qt.AlignTop)

        self.comboBox_scale = QComboBox(self.frame_scale)
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.addItem("")
        self.comboBox_scale.setObjectName(u"comboBox_scale")
        sizePolicy1.setHeightForWidth(self.comboBox_scale.sizePolicy().hasHeightForWidth())
        self.comboBox_scale.setSizePolicy(sizePolicy1)
        self.comboBox_scale.setAutoFillBackground(False)
        self.comboBox_scale.setEditable(False)
        self.comboBox_scale.setFrame(True)

        self.verticalLayout_17.addWidget(self.comboBox_scale, 0, Qt.AlignTop)


        self.gridLayout.addWidget(self.frame_scale, 0, 0, 1, 1, Qt.AlignTop)

        self.frame_theme = QFrame(self.frame_4)
        self.frame_theme.setObjectName(u"frame_theme")
        self.frame_theme.setFrameShape(QFrame.StyledPanel)
        self.frame_theme.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_theme)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_9 = QLabel(self.frame_theme)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_18.addWidget(self.label_9, 0, Qt.AlignTop)

        self.comboBox_theme = QComboBox(self.frame_theme)
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        sizePolicy1.setHeightForWidth(self.comboBox_theme.sizePolicy().hasHeightForWidth())
        self.comboBox_theme.setSizePolicy(sizePolicy1)

        self.verticalLayout_18.addWidget(self.comboBox_theme, 0, Qt.AlignTop)


        self.gridLayout.addWidget(self.frame_theme, 0, 1, 1, 1, Qt.AlignTop)

        self.frame_language = QFrame(self.frame_4)
        self.frame_language.setObjectName(u"frame_language")
        self.frame_language.setFrameShape(QFrame.StyledPanel)
        self.frame_language.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_language)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_10 = QLabel(self.frame_language)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_19.addWidget(self.label_10, 0, Qt.AlignTop)

        self.comboBox_language = QComboBox(self.frame_language)
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.setObjectName(u"comboBox_language")

        self.verticalLayout_19.addWidget(self.comboBox_language, 0, Qt.AlignTop)


        self.gridLayout.addWidget(self.frame_language, 0, 2, 1, 1, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_16.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_10, 0, Qt.AlignBottom)


        self.verticalLayout_16.addWidget(self.frame_6)


        self.verticalLayout_13.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_setting)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.main_body_content)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0438 \u0434\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431", None))
        self.comboBox_scale.setItemText(0, QCoreApplication.translate("MainWindow", u"50%", None))
        self.comboBox_scale.setItemText(1, QCoreApplication.translate("MainWindow", u"80%", None))
        self.comboBox_scale.setItemText(2, QCoreApplication.translate("MainWindow", u"100%", None))
        self.comboBox_scale.setItemText(3, QCoreApplication.translate("MainWindow", u"120%", None))
        self.comboBox_scale.setItemText(4, QCoreApplication.translate("MainWindow", u"150%", None))
        self.comboBox_scale.setItemText(5, QCoreApplication.translate("MainWindow", u"200%", None))

        self.comboBox_scale.setCurrentText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
        self.comboBox_theme.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430\u044f", None))
        self.comboBox_theme.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.comboBox_theme.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a", None))
        self.comboBox_language.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.comboBox_language.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

