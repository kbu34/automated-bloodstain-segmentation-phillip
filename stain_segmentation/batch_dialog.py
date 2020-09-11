# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch_process.ui'
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

class Ui_BatchProcessing(object):
    def setupUi(self, BatchProcessing):
        BatchProcessing.setObjectName(_fromUtf8("BatchProcessing"))
        BatchProcessing.resize(284, 319)
        self.buttonBox = QtWidgets.QDialogButtonBox(BatchProcessing)
        self.buttonBox.setGeometry(QtCore.QRect(40, 270, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtWidgets.QLabel(BatchProcessing)
        self.label.setGeometry(QtCore.QRect(30, 20, 46, 13))
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(BatchProcessing)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 46, 13))
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.folder_path_edit = QtWidgets.QLineEdit(BatchProcessing)
        self.folder_path_edit.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.folder_path_edit.setObjectName(_fromUtf8("folder_path_edit"))
        self.output_path_edit = QtWidgets.QLineEdit(BatchProcessing)
        self.output_path_edit.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.output_path_edit.setObjectName(_fromUtf8("output_path_edit"))
        self.folder_path = QtWidgets.QPushButton(BatchProcessing)
        self.folder_path.setGeometry(QtCore.QRect(200, 20, 51, 23))
        self.folder_path.setObjectName(_fromUtf8("folder_path"))
        self.output_path = QtWidgets.QPushButton(BatchProcessing)
        self.output_path.setGeometry(QtCore.QRect(200, 50, 51, 23))
        self.output_path.setObjectName(_fromUtf8("output_path"))
        self.verticalLayoutWidget = QtWidgets.QWidget(BatchProcessing)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 100, 201, 111))
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
        self.label_5 = QtWidgets.QLabel(BatchProcessing)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 111, 21))
        self.label_5.setMaximumSize(QtCore.QSize(16777191, 16777215))
        font = QtWidgets.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(BatchProcessing)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 220, 160, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtWidgets.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.scale_spin = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_2)
        self.scale_spin.setObjectName(_fromUtf8("scale_spin"))
        self.horizontalLayout_2.addWidget(self.scale_spin)
        self.line_3 = QtWidgets.QFrame(BatchProcessing)
        self.line_3.setGeometry(QtCore.QRect(30, 70, 221, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtWidgets.QFrame(BatchProcessing)
        self.line_4.setGeometry(QtCore.QRect(30, 210, 221, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))

        self.retranslateUi(BatchProcessing)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BatchProcessing.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BatchProcessing.reject)
        QtCore.QMetaObject.connectSlotsByName(BatchProcessing)

    def retranslateUi(self, BatchProcessing):
        BatchProcessing.setWindowTitle(_translate("BatchProcessing", "Dialog", None))
        self.label.setText(_translate("BatchProcessing", "Folder", None))
        self.label_2.setText(_translate("BatchProcessing", "Output", None))
        self.folder_path.setText(_translate("BatchProcessing", "Choose", None))
        self.output_path.setText(_translate("BatchProcessing", "Choose", None))
        self.linearity_check.setText(_translate("BatchProcessing", "Linearity", None))
        self.convergence_check.setText(_translate("BatchProcessing", "Convergence", None))
        self.distribution_check.setText(_translate("BatchProcessing", "Distribution of Elements", None))
        self.label_5.setText(_translate("BatchProcessing", "Pattern Metrics", None))
        self.label_6.setText(_translate("BatchProcessing", "Scale", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BatchProcessing = QtWidgets.QDialog()
    ui = Ui_BatchProcessing()
    ui.setupUi(BatchProcessing)
    BatchProcessing.show()
    sys.exit(app.exec_())

