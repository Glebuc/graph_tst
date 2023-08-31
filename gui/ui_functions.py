from PySide6.QtGui import QIcon

from ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSize
from PySide6.QtWidgets import QPushButton

class UIFunctions(Ui_MainWindow):


    def reset_style(self):
        child_button_menu = self.ui.widget_menu.findChildren(QPushButton)
        for btn in child_button_menu:
            btn.setStyleSheet("")

    # def set_active_btn(self):
    #     child_widgets = self.ui.frame_2.findChildren(QPushButton)
    #     for child_widget in child_widgets:
    #         child_widget.setStyleSheet()

    def toggle_text(self):
        checked = self.ui.burger_btn.isChecked()  # Проверяем состояние кнопки меню
        if checked:
            self.ui.report_btn.setText("Отчеты")
            self.ui.report_btn.setToolTip("")
            self.ui.result_btn.setText("Результаты")
            self.ui.result_btn.setToolTip("")
            self.ui.setting_btn.setText("Настройки")
            self.ui.setting_btn.setToolTip("")
            self.ui.chart_btn.setText("Графики")
            self.ui.chart_btn.setToolTip("")
            icon = QIcon()
            icon.addFile(u":/Icons/arrow_left.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.burger_btn.setIcon(icon)
            self.ui.burger_btn.setIconSize(QSize(36, 36))
        else:
            self.ui.report_btn.setText("")
            self.ui.report_btn.setToolTip("Отчеты")
            self.ui.result_btn.setText("")
            self.ui.result_btn.setToolTip("Результаты")
            self.ui.setting_btn.setText("")
            self.ui.setting_btn.setToolTip("Настройки")
            self.ui.chart_btn.setText("")
            self.ui.chart_btn.setToolTip("Графики")
            icon = QIcon()
            icon.addFile(u":/Icons/arrow_rigth.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.burger_btn.setIcon(icon)
            self.ui.burger_btn.setIconSize(QSize(36, 36))




    def toggleMenu(self, maxWidth, enable):
        if enable:

            width = self.ui.left_menu.width()
            width_btn_toggle = self.ui.burger_btn.width()
            maxExtend = maxWidth

            if  60<= width <= 90:
                widthExtended = maxExtend
            else:
                widthExtended = width_btn_toggle


            self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()