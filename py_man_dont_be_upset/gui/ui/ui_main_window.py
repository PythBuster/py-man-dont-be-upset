# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 658)
        MainWindow.setMinimumSize(QSize(30, 30))
        MainWindow.setMaximumSize(QSize(677, 658))
        self.action_About_Qt = QAction(MainWindow)
        self.action_About_Qt.setObjectName("action_About_Qt")
        self.actionAbout_the_Game = QAction(MainWindow)
        self.actionAbout_the_Game.setObjectName("actionAbout_the_Game")
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.pushButton_home_a_yellow = QPushButton(self.centralwidget)
        self.pushButton_home_a_yellow.setObjectName("pushButton_home_a_yellow")
        self.pushButton_home_a_yellow.setMinimumSize(QSize(38, 38))
        self.pushButton_home_a_yellow.setMaximumSize(QSize(38, 38))
        self.pushButton_home_a_yellow.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: yellow;\n"
            ""
        )

        self.horizontalLayout.addWidget(self.pushButton_home_a_yellow)

        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_home_d_yellow = QPushButton(self.centralwidget)
        self.pushButton_home_d_yellow.setObjectName("pushButton_home_d_yellow")
        self.pushButton_home_d_yellow.setMinimumSize(QSize(38, 38))
        self.pushButton_home_d_yellow.setMaximumSize(QSize(38, 38))
        self.pushButton_home_d_yellow.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: yellow;\n"
            ""
        )

        self.horizontalLayout_4.addWidget(self.pushButton_home_d_yellow)

        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 4, 1, 1)

        self.pushButton_field_36 = QPushButton(self.centralwidget)
        self.pushButton_field_36.setObjectName("pushButton_field_36")
        self.pushButton_field_36.setMinimumSize(QSize(50, 50))
        self.pushButton_field_36.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton_field_36.setFont(font)
        self.pushButton_field_36.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_36, 9, 3, 1, 1)

        self.pushButton_dice_yellow = QPushButton(self.centralwidget)
        self.pushButton_dice_yellow.setObjectName("pushButton_dice_yellow")
        self.pushButton_dice_yellow.setMinimumSize(QSize(50, 50))
        self.pushButton_dice_yellow.setMaximumSize(QSize(50, 50))
        self.pushButton_dice_yellow.setFont(font)
        self.pushButton_dice_yellow.setStyleSheet(
            "border: 2px outset black; border-radius: 8px; background-color:yellow;"
        )

        self.gridLayout.addWidget(self.pushButton_dice_yellow, 4, 2, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_home_a_green = QPushButton(self.centralwidget)
        self.pushButton_home_a_green.setObjectName("pushButton_home_a_green")
        self.pushButton_home_a_green.setMinimumSize(QSize(38, 38))
        self.pushButton_home_a_green.setMaximumSize(QSize(38, 38))
        self.pushButton_home_a_green.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: #33ff33;"
        )

        self.horizontalLayout_13.addWidget(self.pushButton_home_a_green)

        self.gridLayout.addLayout(self.horizontalLayout_13, 3, 5, 1, 1)

        self.pushButton_base_1_red = QPushButton(self.centralwidget)
        self.pushButton_base_1_red.setObjectName("pushButton_base_1_red")
        self.pushButton_base_1_red.setMinimumSize(QSize(50, 50))
        self.pushButton_base_1_red.setMaximumSize(QSize(50, 50))
        self.pushButton_base_1_red.setFont(font)
        self.pushButton_base_1_red.setStyleSheet(
            "background-color: red;border: 2px solid black;border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_base_1_red, 12, 9, 1, 1)

        self.pushButton_base_3_red = QPushButton(self.centralwidget)
        self.pushButton_base_3_red.setObjectName("pushButton_base_3_red")
        self.pushButton_base_3_red.setMinimumSize(QSize(50, 50))
        self.pushButton_base_3_red.setMaximumSize(QSize(50, 50))
        self.pushButton_base_3_red.setFont(font)
        self.pushButton_base_3_red.setStyleSheet(
            "background-color: red;border: 2px solid black;border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_base_3_red, 14, 9, 1, 1)

        self.pushButton_field_8 = QPushButton(self.centralwidget)
        self.pushButton_field_8.setObjectName("pushButton_field_8")
        self.pushButton_field_8.setMinimumSize(QSize(50, 50))
        self.pushButton_field_8.setMaximumSize(QSize(50, 50))
        self.pushButton_field_8.setFont(font)
        self.pushButton_field_8.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_8, 3, 4, 1, 1)

        self.pushButton_base_4_blue = QPushButton(self.centralwidget)
        self.pushButton_base_4_blue.setObjectName("pushButton_base_4_blue")
        self.pushButton_base_4_blue.setMinimumSize(QSize(50, 50))
        self.pushButton_base_4_blue.setMaximumSize(QSize(50, 50))
        self.pushButton_base_4_blue.setFont(font)
        self.pushButton_base_4_blue.setStyleSheet(
            "background-color: #5080ff; border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_4_blue, 14, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_home_b_blue = QPushButton(self.centralwidget)
        self.pushButton_home_b_blue.setObjectName("pushButton_home_b_blue")
        self.pushButton_home_b_blue.setMinimumSize(QSize(38, 38))
        self.pushButton_home_b_blue.setMaximumSize(QSize(38, 38))
        self.pushButton_home_b_blue.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: #5080ff;"
        )

        self.horizontalLayout_11.addWidget(self.pushButton_home_b_blue)

        self.gridLayout.addLayout(self.horizontalLayout_11, 11, 5, 1, 1)

        self.pushButton_base_4_yellow = QPushButton(self.centralwidget)
        self.pushButton_base_4_yellow.setObjectName("pushButton_base_4_yellow")
        self.pushButton_base_4_yellow.setMinimumSize(QSize(50, 50))
        self.pushButton_base_4_yellow.setMaximumSize(QSize(50, 50))
        self.pushButton_base_4_yellow.setFont(font)
        self.pushButton_base_4_yellow.setStyleSheet(
            "background-color: yellow; \n"
            "border: 2px solid black;\n"
            "border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_4_yellow, 3, 1, 1, 1)

        self.pushButton_field_28 = QPushButton(self.centralwidget)
        self.pushButton_field_28.setObjectName("pushButton_field_28")
        self.pushButton_field_28.setMinimumSize(QSize(50, 50))
        self.pushButton_field_28.setMaximumSize(QSize(50, 50))
        self.pushButton_field_28.setFont(font)
        self.pushButton_field_28.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_28, 12, 6, 1, 1)

        self.pushButton_base_1_green = QPushButton(self.centralwidget)
        self.pushButton_base_1_green.setObjectName("pushButton_base_1_green")
        self.pushButton_base_1_green.setMinimumSize(QSize(50, 50))
        self.pushButton_base_1_green.setMaximumSize(QSize(50, 50))
        self.pushButton_base_1_green.setFont(font)
        self.pushButton_base_1_green.setStyleSheet(
            "background-color: #33ff33;border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_1_green, 1, 9, 1, 1)

        self.pushButton_base_3_green = QPushButton(self.centralwidget)
        self.pushButton_base_3_green.setObjectName("pushButton_base_3_green")
        self.pushButton_base_3_green.setMinimumSize(QSize(50, 50))
        self.pushButton_base_3_green.setMaximumSize(QSize(50, 50))
        self.pushButton_base_3_green.setFont(font)
        self.pushButton_base_3_green.setStyleSheet(
            "background-color: #33ff33;border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_3_green, 3, 9, 1, 1)

        self.pushButton_field_5 = QPushButton(self.centralwidget)
        self.pushButton_field_5.setObjectName("pushButton_field_5")
        self.pushButton_field_5.setMinimumSize(QSize(50, 50))
        self.pushButton_field_5.setMaximumSize(QSize(50, 50))
        self.pushButton_field_5.setFont(font)
        self.pushButton_field_5.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_5, 6, 4, 1, 1)

        self.pushButton_field_15 = QPushButton(self.centralwidget)
        self.pushButton_field_15.setObjectName("pushButton_field_15")
        self.pushButton_field_15.setMinimumSize(QSize(50, 50))
        self.pushButton_field_15.setMaximumSize(QSize(50, 50))
        self.pushButton_field_15.setFont(font)
        self.pushButton_field_15.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_15, 6, 6, 1, 1)

        self.pushButton_field_37 = QPushButton(self.centralwidget)
        self.pushButton_field_37.setObjectName("pushButton_field_37")
        self.pushButton_field_37.setMinimumSize(QSize(50, 50))
        self.pushButton_field_37.setMaximumSize(QSize(50, 50))
        self.pushButton_field_37.setFont(font)
        self.pushButton_field_37.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_37, 9, 2, 1, 1)

        self.pushButton_field_29 = QPushButton(self.centralwidget)
        self.pushButton_field_29.setObjectName("pushButton_field_29")
        self.pushButton_field_29.setMinimumSize(QSize(50, 50))
        self.pushButton_field_29.setMaximumSize(QSize(50, 50))
        self.pushButton_field_29.setFont(font)
        self.pushButton_field_29.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_29, 14, 6, 1, 1)

        self.pushButton_field_38 = QPushButton(self.centralwidget)
        self.pushButton_field_38.setObjectName("pushButton_field_38")
        self.pushButton_field_38.setMinimumSize(QSize(50, 50))
        self.pushButton_field_38.setMaximumSize(QSize(50, 50))
        self.pushButton_field_38.setFont(font)
        self.pushButton_field_38.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_38, 9, 1, 1, 1)

        self.pushButton_base_1_yellow = QPushButton(self.centralwidget)
        self.pushButton_base_1_yellow.setObjectName("pushButton_base_1_yellow")
        self.pushButton_base_1_yellow.setMinimumSize(QSize(50, 50))
        self.pushButton_base_1_yellow.setMaximumSize(QSize(50, 50))
        self.pushButton_base_1_yellow.setFont(font)
        self.pushButton_base_1_yellow.setStyleSheet(
            "background-color: yellow; \n"
            "border: 2px solid black;\n"
            "border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_1_yellow, 1, 0, 1, 1)

        self.pushButton_base_1_blue = QPushButton(self.centralwidget)
        self.pushButton_base_1_blue.setObjectName("pushButton_base_1_blue")
        self.pushButton_base_1_blue.setMinimumSize(QSize(50, 50))
        self.pushButton_base_1_blue.setMaximumSize(QSize(50, 50))
        self.pushButton_base_1_blue.setFont(font)
        self.pushButton_base_1_blue.setStyleSheet(
            "background-color: #5080ff; border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_1_blue, 12, 0, 1, 1)

        self.pushButton_field_27 = QPushButton(self.centralwidget)
        self.pushButton_field_27.setObjectName("pushButton_field_27")
        self.pushButton_field_27.setMinimumSize(QSize(50, 50))
        self.pushButton_field_27.setMaximumSize(QSize(50, 50))
        self.pushButton_field_27.setFont(font)
        self.pushButton_field_27.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_27, 11, 6, 1, 1)

        self.pushButton_dice_green = QPushButton(self.centralwidget)
        self.pushButton_dice_green.setObjectName("pushButton_dice_green")
        self.pushButton_dice_green.setMinimumSize(QSize(50, 50))
        self.pushButton_dice_green.setMaximumSize(QSize(50, 50))
        self.pushButton_dice_green.setFont(font)
        self.pushButton_dice_green.setStyleSheet(
            "border: 2px outset black; border-radius: 8px; background-color: #33ff33;"
        )

        self.gridLayout.addWidget(self.pushButton_dice_green, 4, 8, 1, 1)

        self.pushButton_field_2 = QPushButton(self.centralwidget)
        self.pushButton_field_2.setObjectName("pushButton_field_2")
        self.pushButton_field_2.setMinimumSize(QSize(50, 50))
        self.pushButton_field_2.setMaximumSize(QSize(50, 50))
        self.pushButton_field_2.setFont(font)
        self.pushButton_field_2.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;"
        )

        self.gridLayout.addWidget(self.pushButton_field_2, 6, 1, 1, 1)

        self.pushButton_base_2_yellow = QPushButton(self.centralwidget)
        self.pushButton_base_2_yellow.setObjectName("pushButton_base_2_yellow")
        self.pushButton_base_2_yellow.setMinimumSize(QSize(50, 50))
        self.pushButton_base_2_yellow.setMaximumSize(QSize(50, 50))
        self.pushButton_base_2_yellow.setFont(font)
        self.pushButton_base_2_yellow.setStyleSheet(
            "background-color: yellow; \n"
            "border: 2px solid black;\n"
            "border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_2_yellow, 1, 1, 1, 1)

        self.pushButton_field_10 = QPushButton(self.centralwidget)
        self.pushButton_field_10.setObjectName("pushButton_field_10")
        self.pushButton_field_10.setMinimumSize(QSize(50, 50))
        self.pushButton_field_10.setMaximumSize(QSize(50, 50))
        self.pushButton_field_10.setFont(font)
        self.pushButton_field_10.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_10, 1, 5, 1, 1)

        self.pushButton_field_25 = QPushButton(self.centralwidget)
        self.pushButton_field_25.setObjectName("pushButton_field_25")
        self.pushButton_field_25.setMinimumSize(QSize(50, 50))
        self.pushButton_field_25.setMaximumSize(QSize(50, 50))
        self.pushButton_field_25.setFont(font)
        self.pushButton_field_25.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_25, 9, 6, 1, 1)

        self.pushButton_field_19 = QPushButton(self.centralwidget)
        self.pushButton_field_19.setObjectName("pushButton_field_19")
        self.pushButton_field_19.setMinimumSize(QSize(50, 50))
        self.pushButton_field_19.setMaximumSize(QSize(50, 50))
        self.pushButton_field_19.setFont(font)
        self.pushButton_field_19.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_19, 6, 10, 1, 1)

        self.pushButton_field_32 = QPushButton(self.centralwidget)
        self.pushButton_field_32.setObjectName("pushButton_field_32")
        self.pushButton_field_32.setMinimumSize(QSize(50, 50))
        self.pushButton_field_32.setMaximumSize(QSize(50, 50))
        self.pushButton_field_32.setFont(font)
        self.pushButton_field_32.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_32, 12, 4, 1, 1)

        self.pushButton_field_33 = QPushButton(self.centralwidget)
        self.pushButton_field_33.setObjectName("pushButton_field_33")
        self.pushButton_field_33.setMinimumSize(QSize(50, 50))
        self.pushButton_field_33.setMaximumSize(QSize(50, 50))
        self.pushButton_field_33.setFont(font)
        self.pushButton_field_33.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_33, 11, 4, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.pushButton_home_a_red = QPushButton(self.centralwidget)
        self.pushButton_home_a_red.setObjectName("pushButton_home_a_red")
        self.pushButton_home_a_red.setMinimumSize(QSize(38, 38))
        self.pushButton_home_a_red.setMaximumSize(QSize(38, 38))
        self.pushButton_home_a_red.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: red;"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_home_a_red)

        self.gridLayout.addLayout(self.horizontalLayout_5, 7, 9, 1, 1)

        self.pushButton_base_4_green = QPushButton(self.centralwidget)
        self.pushButton_base_4_green.setObjectName("pushButton_base_4_green")
        self.pushButton_base_4_green.setMinimumSize(QSize(50, 50))
        self.pushButton_base_4_green.setMaximumSize(QSize(50, 50))
        self.pushButton_base_4_green.setFont(font)
        self.pushButton_base_4_green.setStyleSheet(
            "background-color: #33ff33;border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_4_green, 3, 10, 1, 1)

        self.pushButton_field_24 = QPushButton(self.centralwidget)
        self.pushButton_field_24.setObjectName("pushButton_field_24")
        self.pushButton_field_24.setMinimumSize(QSize(50, 50))
        self.pushButton_field_24.setMaximumSize(QSize(50, 50))
        self.pushButton_field_24.setFont(font)
        self.pushButton_field_24.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_24, 9, 7, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_home_c_yellow = QPushButton(self.centralwidget)
        self.pushButton_home_c_yellow.setObjectName("pushButton_home_c_yellow")
        self.pushButton_home_c_yellow.setMinimumSize(QSize(38, 38))
        self.pushButton_home_c_yellow.setMaximumSize(QSize(38, 38))
        self.pushButton_home_c_yellow.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: yellow;\n"
            ""
        )

        self.horizontalLayout_3.addWidget(self.pushButton_home_c_yellow)

        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 3, 1, 1)

        self.pushButton_field_34 = QPushButton(self.centralwidget)
        self.pushButton_field_34.setObjectName("pushButton_field_34")
        self.pushButton_field_34.setMinimumSize(QSize(50, 50))
        self.pushButton_field_34.setMaximumSize(QSize(50, 50))
        self.pushButton_field_34.setFont(font)
        self.pushButton_field_34.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_34, 10, 4, 1, 1)

        self.pushButton_field_39 = QPushButton(self.centralwidget)
        self.pushButton_field_39.setObjectName("pushButton_field_39")
        self.pushButton_field_39.setMinimumSize(QSize(50, 50))
        self.pushButton_field_39.setMaximumSize(QSize(50, 50))
        self.pushButton_field_39.setFont(font)
        self.pushButton_field_39.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_39, 9, 0, 1, 1)

        self.pushButton_field_11 = QPushButton(self.centralwidget)
        self.pushButton_field_11.setObjectName("pushButton_field_11")
        self.pushButton_field_11.setMinimumSize(QSize(50, 50))
        self.pushButton_field_11.setMaximumSize(QSize(50, 50))
        self.pushButton_field_11.setFont(font)
        self.pushButton_field_11.setStyleSheet(
            "background-color: #33ff33;border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_field_11, 1, 6, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_home_a_blue = QPushButton(self.centralwidget)
        self.pushButton_home_a_blue.setObjectName("pushButton_home_a_blue")
        self.pushButton_home_a_blue.setMinimumSize(QSize(38, 38))
        self.pushButton_home_a_blue.setMaximumSize(QSize(38, 38))
        self.pushButton_home_a_blue.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: #5080ff;"
        )

        self.horizontalLayout_12.addWidget(self.pushButton_home_a_blue)

        self.gridLayout.addLayout(self.horizontalLayout_12, 12, 5, 1, 1)

        self.pushButton_field_13 = QPushButton(self.centralwidget)
        self.pushButton_field_13.setObjectName("pushButton_field_13")
        self.pushButton_field_13.setMinimumSize(QSize(50, 50))
        self.pushButton_field_13.setMaximumSize(QSize(50, 50))
        self.pushButton_field_13.setFont(font)
        self.pushButton_field_13.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_13, 4, 6, 1, 1)

        self.label_counter = QLabel(self.centralwidget)
        self.label_counter.setObjectName("label_counter")
        font1 = QFont()
        font1.setPointSize(28)
        self.label_counter.setFont(font1)
        self.label_counter.setStyleSheet(
            "background-color: black; color: white; border-radius: 8px;"
        )
        self.label_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_counter, 7, 5, 1, 1)

        self.pushButton_field_35 = QPushButton(self.centralwidget)
        self.pushButton_field_35.setObjectName("pushButton_field_35")
        self.pushButton_field_35.setMinimumSize(QSize(50, 50))
        self.pushButton_field_35.setMaximumSize(QSize(50, 50))
        self.pushButton_field_35.setFont(font)
        self.pushButton_field_35.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_35, 9, 4, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_home_b_yellow = QPushButton(self.centralwidget)
        self.pushButton_home_b_yellow.setObjectName("pushButton_home_b_yellow")
        self.pushButton_home_b_yellow.setMinimumSize(QSize(38, 38))
        self.pushButton_home_b_yellow.setMaximumSize(QSize(38, 38))
        self.pushButton_home_b_yellow.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: yellow;\n"
            ""
        )

        self.horizontalLayout_2.addWidget(self.pushButton_home_b_yellow)

        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 2, 1, 1)

        self.pushButton_field_6 = QPushButton(self.centralwidget)
        self.pushButton_field_6.setObjectName("pushButton_field_6")
        self.pushButton_field_6.setMinimumSize(QSize(50, 50))
        self.pushButton_field_6.setMaximumSize(QSize(50, 50))
        self.pushButton_field_6.setFont(font)
        self.pushButton_field_6.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_6, 5, 4, 1, 1)

        self.pushButton_dice_blue = QPushButton(self.centralwidget)
        self.pushButton_dice_blue.setObjectName("pushButton_dice_blue")
        self.pushButton_dice_blue.setMinimumSize(QSize(50, 50))
        self.pushButton_dice_blue.setMaximumSize(QSize(50, 50))
        self.pushButton_dice_blue.setFont(font)
        self.pushButton_dice_blue.setStyleSheet(
            "border: 2px outset black; border-radius: 8px; background-color: #5080ff;"
        )

        self.gridLayout.addWidget(self.pushButton_dice_blue, 11, 2, 1, 1)

        self.pushButton_field_23 = QPushButton(self.centralwidget)
        self.pushButton_field_23.setObjectName("pushButton_field_23")
        self.pushButton_field_23.setMinimumSize(QSize(50, 50))
        self.pushButton_field_23.setMaximumSize(QSize(50, 50))
        self.pushButton_field_23.setFont(font)
        self.pushButton_field_23.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_23, 9, 8, 1, 1)

        self.pushButton_field_3 = QPushButton(self.centralwidget)
        self.pushButton_field_3.setObjectName("pushButton_field_3")
        self.pushButton_field_3.setMinimumSize(QSize(50, 50))
        self.pushButton_field_3.setMaximumSize(QSize(50, 50))
        self.pushButton_field_3.setFont(font)
        self.pushButton_field_3.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_3, 6, 2, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_home_c_green = QPushButton(self.centralwidget)
        self.pushButton_home_c_green.setObjectName("pushButton_home_c_green")
        self.pushButton_home_c_green.setMinimumSize(QSize(38, 38))
        self.pushButton_home_c_green.setMaximumSize(QSize(38, 38))
        self.pushButton_home_c_green.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: #33ff33;"
        )

        self.horizontalLayout_15.addWidget(self.pushButton_home_c_green)

        self.gridLayout.addLayout(self.horizontalLayout_15, 5, 5, 1, 1)

        self.pushButton_field_18 = QPushButton(self.centralwidget)
        self.pushButton_field_18.setObjectName("pushButton_field_18")
        self.pushButton_field_18.setMinimumSize(QSize(50, 50))
        self.pushButton_field_18.setMaximumSize(QSize(50, 50))
        self.pushButton_field_18.setFont(font)
        self.pushButton_field_18.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_18, 6, 9, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_home_d_green = QPushButton(self.centralwidget)
        self.pushButton_home_d_green.setObjectName("pushButton_home_d_green")
        self.pushButton_home_d_green.setMinimumSize(QSize(38, 38))
        self.pushButton_home_d_green.setMaximumSize(QSize(38, 38))
        self.pushButton_home_d_green.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: #33ff33;"
        )

        self.horizontalLayout_16.addWidget(self.pushButton_home_d_green)

        self.gridLayout.addLayout(self.horizontalLayout_16, 6, 5, 1, 1)

        self.pushButton_field_20 = QPushButton(self.centralwidget)
        self.pushButton_field_20.setObjectName("pushButton_field_20")
        self.pushButton_field_20.setMinimumSize(QSize(50, 50))
        self.pushButton_field_20.setMaximumSize(QSize(50, 50))
        self.pushButton_field_20.setFont(font)
        self.pushButton_field_20.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_20, 7, 10, 1, 1)

        self.pushButton_field_40 = QPushButton(self.centralwidget)
        self.pushButton_field_40.setObjectName("pushButton_field_40")
        self.pushButton_field_40.setMinimumSize(QSize(50, 50))
        self.pushButton_field_40.setMaximumSize(QSize(50, 50))
        self.pushButton_field_40.setFont(font)
        self.pushButton_field_40.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_40, 7, 0, 1, 1)

        self.pushButton_dice_red = QPushButton(self.centralwidget)
        self.pushButton_dice_red.setObjectName("pushButton_dice_red")
        self.pushButton_dice_red.setMinimumSize(QSize(50, 50))
        self.pushButton_dice_red.setMaximumSize(QSize(50, 50))
        self.pushButton_dice_red.setFont(font)
        self.pushButton_dice_red.setStyleSheet(
            "border: 2px outset black; border-radius: 8px; background-color: red;"
        )

        self.gridLayout.addWidget(self.pushButton_dice_red, 11, 8, 1, 1)

        self.pushButton_base_3_blue = QPushButton(self.centralwidget)
        self.pushButton_base_3_blue.setObjectName("pushButton_base_3_blue")
        self.pushButton_base_3_blue.setMinimumSize(QSize(50, 50))
        self.pushButton_base_3_blue.setMaximumSize(QSize(50, 50))
        self.pushButton_base_3_blue.setFont(font)
        self.pushButton_base_3_blue.setStyleSheet(
            "background-color: #5080ff; border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_3_blue, 14, 0, 1, 1)

        self.pushButton_field_7 = QPushButton(self.centralwidget)
        self.pushButton_field_7.setObjectName("pushButton_field_7")
        self.pushButton_field_7.setMinimumSize(QSize(50, 50))
        self.pushButton_field_7.setMaximumSize(QSize(50, 50))
        self.pushButton_field_7.setFont(font)
        self.pushButton_field_7.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_7, 4, 4, 1, 1)

        self.pushButton_field_16 = QPushButton(self.centralwidget)
        self.pushButton_field_16.setObjectName("pushButton_field_16")
        self.pushButton_field_16.setMinimumSize(QSize(50, 50))
        self.pushButton_field_16.setMaximumSize(QSize(50, 50))
        self.pushButton_field_16.setFont(font)
        self.pushButton_field_16.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_16, 6, 7, 1, 1)

        self.pushButton_field_22 = QPushButton(self.centralwidget)
        self.pushButton_field_22.setObjectName("pushButton_field_22")
        self.pushButton_field_22.setMinimumSize(QSize(50, 50))
        self.pushButton_field_22.setMaximumSize(QSize(50, 50))
        self.pushButton_field_22.setFont(font)
        self.pushButton_field_22.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_22, 9, 9, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_home_b_red = QPushButton(self.centralwidget)
        self.pushButton_home_b_red.setObjectName("pushButton_home_b_red")
        self.pushButton_home_b_red.setMinimumSize(QSize(38, 38))
        self.pushButton_home_b_red.setMaximumSize(QSize(38, 38))
        self.pushButton_home_b_red.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: red;"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_home_b_red)

        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 8, 1, 1)

        self.pushButton_field_26 = QPushButton(self.centralwidget)
        self.pushButton_field_26.setObjectName("pushButton_field_26")
        self.pushButton_field_26.setMinimumSize(QSize(50, 50))
        self.pushButton_field_26.setMaximumSize(QSize(50, 50))
        self.pushButton_field_26.setFont(font)
        self.pushButton_field_26.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_26, 10, 6, 1, 1)

        self.pushButton_field_12 = QPushButton(self.centralwidget)
        self.pushButton_field_12.setObjectName("pushButton_field_12")
        self.pushButton_field_12.setMinimumSize(QSize(50, 50))
        self.pushButton_field_12.setMaximumSize(QSize(50, 50))
        self.pushButton_field_12.setFont(font)
        self.pushButton_field_12.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_12, 3, 6, 1, 1)

        self.pushButton_field_1 = QPushButton(self.centralwidget)
        self.pushButton_field_1.setObjectName("pushButton_field_1")
        self.pushButton_field_1.setMinimumSize(QSize(50, 50))
        self.pushButton_field_1.setMaximumSize(QSize(50, 50))
        self.pushButton_field_1.setFont(font)
        self.pushButton_field_1.setStyleSheet(
            "background-color: yellow; \n"
            "border: 2px solid black;\n"
            "border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_field_1, 6, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_home_c_red = QPushButton(self.centralwidget)
        self.pushButton_home_c_red.setObjectName("pushButton_home_c_red")
        self.pushButton_home_c_red.setMinimumSize(QSize(38, 38))
        self.pushButton_home_c_red.setMaximumSize(QSize(38, 38))
        self.pushButton_home_c_red.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: red;"
        )

        self.horizontalLayout_7.addWidget(self.pushButton_home_c_red)

        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 7, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_home_b_green = QPushButton(self.centralwidget)
        self.pushButton_home_b_green.setObjectName("pushButton_home_b_green")
        self.pushButton_home_b_green.setMinimumSize(QSize(38, 38))
        self.pushButton_home_b_green.setMaximumSize(QSize(38, 38))
        self.pushButton_home_b_green.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: #33ff33;"
        )

        self.horizontalLayout_14.addWidget(self.pushButton_home_b_green)

        self.gridLayout.addLayout(self.horizontalLayout_14, 4, 5, 1, 1)

        self.pushButton_base_2_blue = QPushButton(self.centralwidget)
        self.pushButton_base_2_blue.setObjectName("pushButton_base_2_blue")
        self.pushButton_base_2_blue.setMinimumSize(QSize(50, 50))
        self.pushButton_base_2_blue.setMaximumSize(QSize(50, 50))
        self.pushButton_base_2_blue.setFont(font)
        self.pushButton_base_2_blue.setStyleSheet(
            "background-color: #5080ff; border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_2_blue, 12, 1, 1, 1)

        self.pushButton_field_30 = QPushButton(self.centralwidget)
        self.pushButton_field_30.setObjectName("pushButton_field_30")
        self.pushButton_field_30.setMinimumSize(QSize(50, 50))
        self.pushButton_field_30.setMaximumSize(QSize(50, 50))
        self.pushButton_field_30.setFont(font)
        self.pushButton_field_30.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_30, 14, 5, 1, 1)

        self.pushButton_field_21 = QPushButton(self.centralwidget)
        self.pushButton_field_21.setObjectName("pushButton_field_21")
        self.pushButton_field_21.setMinimumSize(QSize(50, 50))
        self.pushButton_field_21.setMaximumSize(QSize(50, 50))
        self.pushButton_field_21.setFont(font)
        self.pushButton_field_21.setStyleSheet(
            "background-color: red;border: 2px solid black;border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_21, 9, 10, 1, 1)

        self.pushButton_base_3_yellow = QPushButton(self.centralwidget)
        self.pushButton_base_3_yellow.setObjectName("pushButton_base_3_yellow")
        self.pushButton_base_3_yellow.setMinimumSize(QSize(50, 50))
        self.pushButton_base_3_yellow.setMaximumSize(QSize(50, 50))
        self.pushButton_base_3_yellow.setFont(font)
        self.pushButton_base_3_yellow.setStyleSheet(
            "background-color: yellow; \n"
            "border: 2px solid black;\n"
            "border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_3_yellow, 3, 0, 1, 1)

        self.pushButton_base_2_green = QPushButton(self.centralwidget)
        self.pushButton_base_2_green.setObjectName("pushButton_base_2_green")
        self.pushButton_base_2_green.setMinimumSize(QSize(50, 50))
        self.pushButton_base_2_green.setMaximumSize(QSize(50, 50))
        self.pushButton_base_2_green.setFont(font)
        self.pushButton_base_2_green.setStyleSheet(
            "background-color: #33ff33;border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_base_2_green, 1, 10, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_home_c_blue = QPushButton(self.centralwidget)
        self.pushButton_home_c_blue.setObjectName("pushButton_home_c_blue")
        self.pushButton_home_c_blue.setMinimumSize(QSize(38, 38))
        self.pushButton_home_c_blue.setMaximumSize(QSize(38, 38))
        self.pushButton_home_c_blue.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: #5080ff;"
        )

        self.horizontalLayout_10.addWidget(self.pushButton_home_c_blue)

        self.gridLayout.addLayout(self.horizontalLayout_10, 10, 5, 1, 1)

        self.pushButton_field_4 = QPushButton(self.centralwidget)
        self.pushButton_field_4.setObjectName("pushButton_field_4")
        self.pushButton_field_4.setMinimumSize(QSize(50, 50))
        self.pushButton_field_4.setMaximumSize(QSize(50, 50))
        self.pushButton_field_4.setFont(font)
        self.pushButton_field_4.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_4, 6, 3, 1, 1)

        self.pushButton_field_31 = QPushButton(self.centralwidget)
        self.pushButton_field_31.setObjectName("pushButton_field_31")
        self.pushButton_field_31.setMinimumSize(QSize(50, 50))
        self.pushButton_field_31.setMaximumSize(QSize(50, 50))
        self.pushButton_field_31.setFont(font)
        self.pushButton_field_31.setStyleSheet(
            "background-color: #5080ff; border: 2px solid black;border-radius: 25px;\n"
            ""
        )

        self.gridLayout.addWidget(self.pushButton_field_31, 14, 4, 1, 1)

        self.pushButton_field_9 = QPushButton(self.centralwidget)
        self.pushButton_field_9.setObjectName("pushButton_field_9")
        self.pushButton_field_9.setMinimumSize(QSize(50, 50))
        self.pushButton_field_9.setMaximumSize(QSize(50, 50))
        self.pushButton_field_9.setFont(font)
        self.pushButton_field_9.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_9, 1, 4, 1, 1)

        self.pushButton_field_17 = QPushButton(self.centralwidget)
        self.pushButton_field_17.setObjectName("pushButton_field_17")
        self.pushButton_field_17.setMinimumSize(QSize(50, 50))
        self.pushButton_field_17.setMaximumSize(QSize(50, 50))
        self.pushButton_field_17.setFont(font)
        self.pushButton_field_17.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_17, 6, 8, 1, 1)

        self.pushButton_base_2_red = QPushButton(self.centralwidget)
        self.pushButton_base_2_red.setObjectName("pushButton_base_2_red")
        self.pushButton_base_2_red.setMinimumSize(QSize(50, 50))
        self.pushButton_base_2_red.setMaximumSize(QSize(50, 50))
        self.pushButton_base_2_red.setFont(font)
        self.pushButton_base_2_red.setStyleSheet(
            "background-color: red;border: 2px solid black;border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_base_2_red, 12, 10, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_home_d_red = QPushButton(self.centralwidget)
        self.pushButton_home_d_red.setObjectName("pushButton_home_d_red")
        self.pushButton_home_d_red.setMinimumSize(QSize(38, 38))
        self.pushButton_home_d_red.setMaximumSize(QSize(38, 38))
        self.pushButton_home_d_red.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: red;"
        )

        self.horizontalLayout_8.addWidget(self.pushButton_home_d_red)

        self.gridLayout.addLayout(self.horizontalLayout_8, 7, 6, 1, 1)

        self.pushButton_field_14 = QPushButton(self.centralwidget)
        self.pushButton_field_14.setObjectName("pushButton_field_14")
        self.pushButton_field_14.setMinimumSize(QSize(50, 50))
        self.pushButton_field_14.setMaximumSize(QSize(50, 50))
        self.pushButton_field_14.setFont(font)
        self.pushButton_field_14.setStyleSheet(
            "border: 2px solid black; border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_field_14, 5, 6, 1, 1)

        self.pushButton_base_4_red = QPushButton(self.centralwidget)
        self.pushButton_base_4_red.setObjectName("pushButton_base_4_red")
        self.pushButton_base_4_red.setMinimumSize(QSize(50, 50))
        self.pushButton_base_4_red.setMaximumSize(QSize(50, 50))
        self.pushButton_base_4_red.setFont(font)
        self.pushButton_base_4_red.setStyleSheet(
            "background-color: red;border: 2px solid black;border-radius: 25px;\n" ""
        )

        self.gridLayout.addWidget(self.pushButton_base_4_red, 14, 10, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_home_d_blue = QPushButton(self.centralwidget)
        self.pushButton_home_d_blue.setObjectName("pushButton_home_d_blue")
        self.pushButton_home_d_blue.setMinimumSize(QSize(38, 38))
        self.pushButton_home_d_blue.setMaximumSize(QSize(38, 38))
        self.pushButton_home_d_blue.setStyleSheet(
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "border: 2px solid black;\n"
            "border-radius: 19px;\n"
            "background-color: #5080ff;"
        )

        self.horizontalLayout_9.addWidget(self.pushButton_home_d_blue)

        self.gridLayout.addLayout(self.horizontalLayout_9, 9, 5, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 677, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menu_File.addAction(self.action_Exit)
        self.menu_About.addAction(self.action_About_Qt)
        self.menu_About.addAction(self.actionAbout_the_Game)

        self.retranslateUi(MainWindow)
        self.action_Exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.action_About_Qt.setText(
            QCoreApplication.translate("MainWindow", "About &Qt", None)
        )
        self.actionAbout_the_Game.setText(
            QCoreApplication.translate("MainWindow", "About the &Game", None)
        )
        self.action_Exit.setText(
            QCoreApplication.translate("MainWindow", "&Exit", None)
        )
        self.pushButton_home_a_yellow.setText(
            QCoreApplication.translate("MainWindow", "a", None)
        )
        self.pushButton_home_d_yellow.setText(
            QCoreApplication.translate("MainWindow", "d", None)
        )
        self.pushButton_field_36.setText("")
        self.pushButton_dice_yellow.setText(
            QCoreApplication.translate("MainWindow", "6", None)
        )
        self.pushButton_home_a_green.setText(
            QCoreApplication.translate("MainWindow", "a", None)
        )
        self.pushButton_base_1_red.setText(
            QCoreApplication.translate("MainWindow", "1", None)
        )
        self.pushButton_base_3_red.setText(
            QCoreApplication.translate("MainWindow", "3", None)
        )
        self.pushButton_field_8.setText("")
        self.pushButton_base_4_blue.setText(
            QCoreApplication.translate("MainWindow", "4", None)
        )
        self.pushButton_home_b_blue.setText(
            QCoreApplication.translate("MainWindow", "b", None)
        )
        self.pushButton_base_4_yellow.setText(
            QCoreApplication.translate("MainWindow", "4", None)
        )
        self.pushButton_field_28.setText("")
        self.pushButton_base_1_green.setText(
            QCoreApplication.translate("MainWindow", "1", None)
        )
        self.pushButton_base_3_green.setText(
            QCoreApplication.translate("MainWindow", "3", None)
        )
        self.pushButton_field_5.setText("")
        self.pushButton_field_15.setText("")
        self.pushButton_field_37.setText("")
        self.pushButton_field_29.setText("")
        self.pushButton_field_38.setText("")
        self.pushButton_base_1_yellow.setText(
            QCoreApplication.translate("MainWindow", "1", None)
        )
        self.pushButton_base_1_blue.setText(
            QCoreApplication.translate("MainWindow", "1", None)
        )
        self.pushButton_field_27.setText("")
        self.pushButton_dice_green.setText(
            QCoreApplication.translate("MainWindow", "6", None)
        )
        self.pushButton_field_2.setText("")
        self.pushButton_base_2_yellow.setText(
            QCoreApplication.translate("MainWindow", "2", None)
        )
        self.pushButton_field_10.setText("")
        self.pushButton_field_25.setText("")
        self.pushButton_field_19.setText("")
        self.pushButton_field_32.setText("")
        self.pushButton_field_33.setText("")
        self.pushButton_home_a_red.setText(
            QCoreApplication.translate("MainWindow", "a", None)
        )
        self.pushButton_base_4_green.setText(
            QCoreApplication.translate("MainWindow", "4", None)
        )
        self.pushButton_field_24.setText("")
        self.pushButton_home_c_yellow.setText(
            QCoreApplication.translate("MainWindow", "c", None)
        )
        self.pushButton_field_34.setText("")
        self.pushButton_field_39.setText("")
        self.pushButton_field_11.setText("")
        self.pushButton_home_a_blue.setText(
            QCoreApplication.translate("MainWindow", "a", None)
        )
        self.pushButton_field_13.setText("")
        self.label_counter.setText(QCoreApplication.translate("MainWindow", "60", None))
        self.pushButton_field_35.setText("")
        self.pushButton_home_b_yellow.setText(
            QCoreApplication.translate("MainWindow", "b", None)
        )
        self.pushButton_field_6.setText("")
        self.pushButton_dice_blue.setText(
            QCoreApplication.translate("MainWindow", "6", None)
        )
        self.pushButton_field_23.setText("")
        self.pushButton_field_3.setText("")
        self.pushButton_home_c_green.setText(
            QCoreApplication.translate("MainWindow", "c", None)
        )
        self.pushButton_field_18.setText("")
        self.pushButton_home_d_green.setText(
            QCoreApplication.translate("MainWindow", "d", None)
        )
        self.pushButton_field_20.setText("")
        self.pushButton_field_40.setText("")
        self.pushButton_dice_red.setText(
            QCoreApplication.translate("MainWindow", "6", None)
        )
        self.pushButton_base_3_blue.setText(
            QCoreApplication.translate("MainWindow", "3", None)
        )
        self.pushButton_field_7.setText("")
        self.pushButton_field_16.setText("")
        self.pushButton_field_22.setText("")
        self.pushButton_home_b_red.setText(
            QCoreApplication.translate("MainWindow", "b", None)
        )
        self.pushButton_field_26.setText("")
        self.pushButton_field_12.setText("")
        self.pushButton_field_1.setText("")
        self.pushButton_home_c_red.setText(
            QCoreApplication.translate("MainWindow", "c", None)
        )
        self.pushButton_home_b_green.setText(
            QCoreApplication.translate("MainWindow", "b", None)
        )
        self.pushButton_base_2_blue.setText(
            QCoreApplication.translate("MainWindow", "2", None)
        )
        self.pushButton_field_30.setText("")
        self.pushButton_field_21.setText("")
        self.pushButton_base_3_yellow.setText(
            QCoreApplication.translate("MainWindow", "3", None)
        )
        self.pushButton_base_2_green.setText(
            QCoreApplication.translate("MainWindow", "2", None)
        )
        self.pushButton_home_c_blue.setText(
            QCoreApplication.translate("MainWindow", "c", None)
        )
        self.pushButton_field_4.setText("")
        self.pushButton_field_31.setText("")
        self.pushButton_field_9.setText("")
        self.pushButton_field_17.setText("")
        self.pushButton_base_2_red.setText(
            QCoreApplication.translate("MainWindow", "2", None)
        )
        self.pushButton_home_d_red.setText(
            QCoreApplication.translate("MainWindow", "d", None)
        )
        self.pushButton_field_14.setText("")
        self.pushButton_base_4_red.setText(
            QCoreApplication.translate("MainWindow", "4", None)
        )
        self.pushButton_home_d_blue.setText(
            QCoreApplication.translate("MainWindow", "d", None)
        )
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", "&File", None))
        self.menu_About.setTitle(
            QCoreApplication.translate("MainWindow", "&About", None)
        )

    # retranslateUi
