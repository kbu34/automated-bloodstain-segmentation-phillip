# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'features_dialog.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_SegmenationMetrics(object):
    def setupUi(self, SegmenationMetrics):
        SegmenationMetrics.setObjectName(_fromUtf8("SegmenationMetrics"))
        SegmenationMetrics.resize(402, 319)
        self.buttonBox = QtWidgets.QDialogButtonBox(SegmenationMetrics)
        self.buttonBox.setGeometry(QtCore.QRect(30, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(SegmenationMetrics)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 141, 229))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.id = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.id.setFont(font)
        self.id.setChecked(True)
        self.id.setObjectName(_fromUtf8("id"))
        self.verticalLayout_2.addWidget(self.id)
        self.ellipse = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.ellipse.setFont(font)
        self.ellipse.setChecked(True)
        self.ellipse.setObjectName(_fromUtf8("ellipse"))
        self.verticalLayout_2.addWidget(self.ellipse)
        self.outline = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.outline.setFont(font)
        self.outline.setChecked(True)
        self.outline.setObjectName(_fromUtf8("outline"))
        self.verticalLayout_2.addWidget(self.outline)
        self.center = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.center.setFont(font)
        self.center.setChecked(True)
        self.center.setObjectName(_fromUtf8("center"))
        self.verticalLayout_2.addWidget(self.center)
        self.directionality = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.directionality.setEnabled(True)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.directionality.setFont(font)
        self.directionality.setChecked(False)
        self.directionality.setObjectName(_fromUtf8("directionality"))
        self.verticalLayout_2.addWidget(self.directionality)
        self.direction_line = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.direction_line.setFont(font)
        self.direction_line.setChecked(False)
        self.direction_line.setObjectName(_fromUtf8("direction_line"))
        self.verticalLayout_2.addWidget(self.direction_line)
        self.gamma = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.gamma.setFont(font)
        self.gamma.setChecked(False)
        self.gamma.setObjectName(_fromUtf8("gamma"))
        self.verticalLayout_2.addWidget(self.gamma)
        self.verticalLayoutWidget = QtWidgets.QWidget(SegmenationMetrics)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 40, 171, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.linearity_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.linearity_check.setFont(font)
        self.linearity_check.setChecked(True)
        self.linearity_check.setObjectName(_fromUtf8("linearity_check"))
        self.verticalLayout.addWidget(self.linearity_check)
        self.convergence_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.convergence_check.setFont(font)
        self.convergence_check.setChecked(True)
        self.convergence_check.setObjectName(_fromUtf8("convergence_check"))
        self.verticalLayout.addWidget(self.convergence_check)
        self.distribution_check = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.distribution_check.setFont(font)
        self.distribution_check.setChecked(True)
        self.distribution_check.setObjectName(_fromUtf8("distribution_check"))
        self.verticalLayout.addWidget(self.distribution_check)
        self.label = QtWidgets.QLabel(SegmenationMetrics)
        self.label.setGeometry(QtCore.QRect(230, 20, 111, 21))
        self.label.setMaximumSize(QtCore.QSize(16777191, 16777215))
        font = QtWidgets.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(SegmenationMetrics)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 91, 21))
        self.label_2.setMaximumSize(QtCore.QSize(16777191, 16777215))
        font = QtWidgets.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(SegmenationMetrics)
        self.label_3.setGeometry(QtCore.QRect(260, 170, 51, 21))
        self.label_3.setMaximumSize(QtCore.QSize(16777191, 16777215))
        font = QtWidgets.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayoutWidget = QtWidgets.QWidget(SegmenationMetrics)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 190, 160, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.scale_spin = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.scale_spin.setObjectName(_fromUtf8("scale_spin"))
        self.horizontalLayout.addWidget(self.scale_spin)
        self.line = QtWidgets.QFrame(SegmenationMetrics)
        self.line.setGeometry(QtCore.QRect(200, 150, 161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtWidgets.QFrame(SegmenationMetrics)
        self.line_2.setGeometry(QtCore.QRect(170, 30, 20, 241))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(SegmenationMetrics)
        self.buttonBox_2.setGeometry(QtCore.QRect(300, 290, 341, 32))
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName(_fromUtf8("buttonBox_2"))

        self.retranslateUi(SegmenationMetrics)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SegmenationMetrics.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SegmenationMetrics.reject)
        QtCore.QMetaObject.connectSlotsByName(SegmenationMetrics)

    def retranslateUi(self, SegmenationMetrics):
        SegmenationMetrics.setWindowTitle(_translate("SegmenationMetrics", "Dialog", None))
        self.id.setText(_translate("SegmenationMetrics", "ID", None))
        self.ellipse.setText(_translate("SegmenationMetrics", "Ellipse", None))
        self.outline.setText(_translate("SegmenationMetrics", "Outline", None))
        self.center.setText(_translate("SegmenationMetrics", "Center", None))
        self.directionality.setText(_translate("SegmenationMetrics", "Directionality text", None))
        self.direction_line.setText(_translate("SegmenationMetrics", "Direction line", None))
        self.gamma.setText(_translate("SegmenationMetrics", "Gamma", None))
        self.linearity_check.setText(_translate("SegmenationMetrics", "Linearity", None))
        self.convergence_check.setText(_translate("SegmenationMetrics", "Convergence", None))
        self.distribution_check.setText(_translate("SegmenationMetrics", "Distribution of Elements", None))
        self.label.setText(_translate("SegmenationMetrics", "Pattern Metrics", None))
        self.label_2.setText(_translate("SegmenationMetrics", "Annotations", None))
        self.label_3.setText(_translate("SegmenationMetrics", "Scale", None))
        self.label_4.setText(_translate("SegmenationMetrics", "Scale", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SegmenationMetrics = QtWidgets.QDialog()
    ui = Ui_SegmenationMetrics()
    ui.setupUi(SegmenationMetrics)
    SegmenationMetrics.show()
    sys.exit(app.exec_())

