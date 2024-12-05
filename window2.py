# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form2hOJLhW.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QLineEdit, QSizePolicy, QToolButton,
    QWidget)

class Ui_designer(object):
    def setupUi(self, designer):
        if not designer.objectName():
            designer.setObjectName(u"designer")
        designer.resize(980, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(designer.sizePolicy().hasHeightForWidth())
        designer.setSizePolicy(sizePolicy)
        designer.setStyleSheet(u"selection-background-color: rgb(85, 85, 85);\n"
"\n"
"selection-color: rgb(75, 251, 175);\n"
"color: rgb(75, 251, 175);\n"
"background-color: rgb(0, 0, 0);")
        self.webEngineView_5 = QWebEngineView(designer)
        self.webEngineView_5.setObjectName(u"webEngineView_5")
        self.webEngineView_5.setGeometry(QRect(0, 0, 980, 680))
        self.webEngineView_5.setUrl(QUrl(u"https://www.google.co.in/"))
        self.webEngineView_5.setZoomFactor(0.800000000000000)
        self.lineEdit = QLineEdit(designer)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(64, 36, 1743, 20))
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,0.8);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setFrame(False)
        self.toolButton_aerrow_left = QToolButton(designer)
        self.toolButton_aerrow_left.setObjectName(u"toolButton_aerrow_left")
        self.toolButton_aerrow_left.setGeometry(QRect(379, 5, 22, 22))
        self.toolButton_aerrow_left.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_aerrow_left.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon = QIcon()
        icon.addFile(u"aerrow_left1.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_aerrow_left.setIcon(icon)
        self.toolButton_aerrow_left.setIconSize(QSize(20, 20))
        self.toolButton_aerrow_left.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.toolButton_aerrow_left.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_aerrow_right = QToolButton(designer)
        self.toolButton_aerrow_right.setObjectName(u"toolButton_aerrow_right")
        self.toolButton_aerrow_right.setGeometry(QRect(404, 5, 22, 22))
        self.toolButton_aerrow_right.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_aerrow_right.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u"aerrow_right1.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_aerrow_right.setIcon(icon1)
        self.toolButton_aerrow_right.setIconSize(QSize(20, 20))
        self.toolButton_aerrow_right.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.toolButton_aerrow_right.setArrowType(Qt.ArrowType.NoArrow)
        self.pushButton_go = QToolButton(designer)
        self.pushButton_go.setObjectName(u"pushButton_go")
        self.pushButton_go.setGeometry(QRect(456, 5, 22, 22))
        self.pushButton_go.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u"redirect1.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_go.setIcon(icon2)
        self.pushButton_go.setIconSize(QSize(20, 20))
        self.pushButton_go.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.pushButton_go.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_refresh = QToolButton(designer)
        self.toolButton_refresh.setObjectName(u"toolButton_refresh")
        self.toolButton_refresh.setGeometry(QRect(429, 4, 25, 25))
        self.toolButton_refresh.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon3 = QIcon()
        icon3.addFile(u"refresh1.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_refresh.setIcon(icon3)
        self.toolButton_refresh.setIconSize(QSize(20, 20))
        self.toolButton_refresh.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.toolButton_refresh.setArrowType(Qt.ArrowType.NoArrow)
        self.widget_toolbar = QWidget(designer)
        self.widget_toolbar.setObjectName(u"widget_toolbar")
        self.widget_toolbar.setGeometry(QRect(373, 6, 211, 22))
        self.widget_toolbar.setStyleSheet(u"background-color: rgb(32, 32, 32);")
        self.pushButton_maximise = QToolButton(self.widget_toolbar)
        self.pushButton_maximise.setObjectName(u"pushButton_maximise")
        self.pushButton_maximise.setGeometry(QRect(160, 0, 22, 22))
        self.pushButton_maximise.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon4 = QIcon()
        icon4.addFile(u"../../../Octopus v1.71/images/maximise.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_maximise.setIcon(icon4)
        self.pushButton_maximise.setIconSize(QSize(20, 20))
        self.pushButton_maximise.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.pushButton_maximise.setArrowType(Qt.ArrowType.NoArrow)
        self.pushButton_save_page = QToolButton(designer)
        self.pushButton_save_page.setObjectName(u"pushButton_save_page")
        self.pushButton_save_page.setGeometry(QRect(502, 7, 22, 22))
        self.pushButton_save_page.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon5 = QIcon()
        icon5.addFile(u"maximise1.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_save_page.setIcon(icon5)
        self.pushButton_save_page.setIconSize(QSize(20, 20))
        self.pushButton_save_page.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.pushButton_save_page.setArrowType(Qt.ArrowType.NoArrow)
        self.widget_toolbar.raise_()
        self.webEngineView_5.raise_()
        self.toolButton_aerrow_left.raise_()
        self.toolButton_aerrow_right.raise_()
        self.toolButton_refresh.raise_()
        self.pushButton_go.raise_()
        self.lineEdit.raise_()
        self.pushButton_save_page.raise_()

        self.retranslateUi(designer)

        QMetaObject.connectSlotsByName(designer)
    # setupUi

    def retranslateUi(self, designer):
        designer.setWindowTitle(QCoreApplication.translate("designer", u"Form", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("designer", u"Enter Custom URL in this Format ex :-    https://www.google.com/search?q={query}", None))
#if QT_CONFIG(tooltip)
        self.toolButton_aerrow_left.setToolTip(QCoreApplication.translate("designer", u"<html><head/><body><p>Go to Previous Page</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_aerrow_left.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_aerrow_right.setToolTip(QCoreApplication.translate("designer", u"<html><head/><body><p>Go to Forward Page</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_aerrow_right.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_go.setToolTip(QCoreApplication.translate("designer", u"<html><head/><body><p>Redirect to Browser</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_go.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_refresh.setToolTip(QCoreApplication.translate("designer", u"<html><head/><body><p>Reload</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_refresh.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_maximise.setToolTip(QCoreApplication.translate("designer", u"<html><head/><body><p>FullScreen / Normal</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_maximise.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_save_page.setToolTip(QCoreApplication.translate("designer", u"<html><head/><body><p>Save Current Page</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_save_page.setText("")
    # retranslateUi

