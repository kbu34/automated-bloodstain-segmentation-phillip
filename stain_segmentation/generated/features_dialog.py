# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/features_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SegmenationMetrics(object):
    def setupUi(self, SegmenationMetrics):
        SegmenationMetrics.setObjectName("SegmenationMetrics")
        SegmenationMetrics.resize(353, 274)
        self.gridLayout = QtWidgets.QGridLayout(SegmenationMetrics)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(SegmenationMetrics)
        self.label_2.setMaximumSize(QtCore.QSize(16777191, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(SegmenationMetrics)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(SegmenationMetrics)
        self.label.setMaximumSize(QtCore.QSize(16777191, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.id = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id.setFont(font)
        self.id.setChecked(True)
        self.id.setObjectName("id")
        self.verticalLayout_2.addWidget(self.id)
        self.ellipse = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ellipse.setFont(font)
        self.ellipse.setChecked(True)
        self.ellipse.setObjectName("ellipse")
        self.verticalLayout_2.addWidget(self.ellipse)
        self.outline = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outline.setFont(font)
        self.outline.setChecked(True)
        self.outline.setObjectName("outline")
        self.verticalLayout_2.addWidget(self.outline)
        self.center = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.center.setFont(font)
        self.center.setChecked(True)
        self.center.setObjectName("center")
        self.verticalLayout_2.addWidget(self.center)
        self.directionality = QtWidgets.QCheckBox(SegmenationMetrics)
        self.directionality.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.directionality.setFont(font)
        self.directionality.setChecked(False)
        self.directionality.setObjectName("directionality")
        self.verticalLayout_2.addWidget(self.directionality)
        self.direction_line = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.direction_line.setFont(font)
        self.direction_line.setChecked(False)
        self.direction_line.setObjectName("direction_line")
        self.verticalLayout_2.addWidget(self.direction_line)
        self.gamma = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gamma.setFont(font)
        self.gamma.setChecked(False)
        self.gamma.setObjectName("gamma")
        self.verticalLayout_2.addWidget(self.gamma)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 4, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.linearity_check = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.linearity_check.setFont(font)
        self.linearity_check.setChecked(True)
        self.linearity_check.setObjectName("linearity_check")
        self.verticalLayout.addWidget(self.linearity_check)
        self.convergence_check = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convergence_check.setFont(font)
        self.convergence_check.setChecked(True)
        self.convergence_check.setObjectName("convergence_check")
        self.verticalLayout.addWidget(self.convergence_check)
        self.distribution_check = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distribution_check.setFont(font)
        self.distribution_check.setChecked(True)
        self.distribution_check.setObjectName("distribution_check")
        
        self.centroid_check = QtWidgets.QCheckBox(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centroid_check.setFont(font)
        # self.centroid_check.setChecked(True)
        self.centroid_check.setObjectName("centroid_check")
        self.verticalLayout.addWidget(self.centroid_check)

        self.verticalLayout.addWidget(self.distribution_check)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(SegmenationMetrics)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(SegmenationMetrics)
        self.label_3.setMaximumSize(QtCore.QSize(16777191, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(SegmenationMetrics)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.scale_spin = QtWidgets.QDoubleSpinBox(SegmenationMetrics)
        self.scale_spin.setObjectName("scale_spin")
        self.horizontalLayout.addWidget(self.scale_spin)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SegmenationMetrics)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 3)

        self.retranslateUi(SegmenationMetrics)
        self.buttonBox.accepted.connect(SegmenationMetrics.accept)
        self.buttonBox.rejected.connect(SegmenationMetrics.reject)
        QtCore.QMetaObject.connectSlotsByName(SegmenationMetrics)

    def retranslateUi(self, SegmenationMetrics):
        _translate = QtCore.QCoreApplication.translate
        SegmenationMetrics.setWindowTitle(_translate("SegmenationMetrics", "Dialog"))
        self.label_2.setText(_translate("SegmenationMetrics", "Annotations"))
        self.label.setText(_translate("SegmenationMetrics", "Pattern Metrics"))
        self.id.setText(_translate("SegmenationMetrics", "ID"))
        self.ellipse.setText(_translate("SegmenationMetrics", "Ellipse"))
        self.outline.setText(_translate("SegmenationMetrics", "Outline"))
        self.center.setText(_translate("SegmenationMetrics", "Center"))
        self.directionality.setText(_translate("SegmenationMetrics", "Directionality text"))
        self.direction_line.setText(_translate("SegmenationMetrics", "Direction line"))
        self.gamma.setText(_translate("SegmenationMetrics", "Gamma"))
        self.linearity_check.setText(_translate("SegmenationMetrics", "Linearity"))
        self.convergence_check.setText(_translate("SegmenationMetrics", "Convergence"))
        self.distribution_check.setText(_translate("SegmenationMetrics", "Distribution of Elements"))
        self.centroid_check.setText(_translate("SegmenationMetrics", "Centroid"))
        self.label_3.setText(_translate("SegmenationMetrics", "Scale"))
        self.label_4.setText(_translate("SegmenationMetrics", "Scale"))

