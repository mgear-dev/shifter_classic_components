# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/repo/mgear_dist/framework/shifter_classic_components/scripts/mgear/shifter_classic_components/chain_net_01/settingsUI.ui'
#
# Created: Wed Mar 27 16:41:46 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 244)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.neighbor_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.neighbor_lineEdit.setObjectName("neighbor_lineEdit")
        self.horizontalLayout_2.addWidget(self.neighbor_lineEdit)
        self.neighbor_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.neighbor_pushButton.setObjectName("neighbor_pushButton")
        self.horizontalLayout_2.addWidget(self.neighbor_pushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.inbetween_label = QtWidgets.QLabel(self.groupBox_3)
        self.inbetween_label.setObjectName("inbetween_label")
        self.horizontalLayout_6.addWidget(self.inbetween_label)
        self.inbetweenChains_spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.inbetweenChains_spinBox.setMinimum(1)
        self.inbetweenChains_spinBox.setMaximum(9999)
        self.inbetweenChains_spinBox.setProperty("value", 1)
        self.inbetweenChains_spinBox.setObjectName("inbetweenChains_spinBox")
        self.horizontalLayout_6.addWidget(self.inbetweenChains_spinBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.neutralPose_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.neutralPose_checkBox.setText("Neutral Pose")
        self.neutralPose_checkBox.setObjectName("neutralPose_checkBox")
        self.verticalLayout.addWidget(self.neutralPose_checkBox)
        self.overrideNegate_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.overrideNegate_checkBox.setText("Override Negate Axis Direction For \"R\" Side")
        self.overrideNegate_checkBox.setObjectName("overrideNegate_checkBox")
        self.verticalLayout.addWidget(self.overrideNegate_checkBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("Form", "Net config", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Neighbor", None, -1))
        self.neighbor_pushButton.setText(QtWidgets.QApplication.translate("Form", "<<", None, -1))
        self.inbetween_label.setText(QtWidgets.QApplication.translate("Form", "Inbetween chains", None, -1))
        self.inbetweenChains_spinBox.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p><br/></p></body></html>", None, -1))

