import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import main_window
from photo_viewer import PhotoViewer
import stain_segmentation as Seg
import cv2
from PIL import Image
import os

class BPA_App(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(BPA_App, self).__init__(parent)
        self.setupUi(self)
        self.viewer = PhotoViewer(self.centralwidget)
        self.viewer.setMinimumSize(500, 500)
        self.horizontalLayout.addWidget(self.viewer)
        self.actionLoad.triggered.connect(self.load_image)
        self.actionExport.triggered.connect(self.export)
        self.actionSegment_Image.triggered.connect(self.segment_image)
        self.file_name = ""
        self.populate_table()
        self.result = None

    def load_image(self):
        self.file_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif *.png *.tif)")
        if self.file_name:
            self.viewer.setPhoto(pixmap=QtGui.QPixmap(self.file_name))

    def export(self):
        save_path = QtGui.QFileDialog.getSaveFileName(self, 'Open file', 
         'c:\\')
        if save_path:
            Seg.export_stain_data(save_path)
            # Seg.export_pattern_data(save_path)
            save_path = os.path.splitext(save_path)[0]
            cv2.cvtColor(self.result, cv2.COLOR_BGR2RGB, self.result)
            cv2.imwrite(save_path + "-result.jpg", self.result)

    def segment_image(self):
        if self.file_name != "":
            image = cv2.imread(str(self.file_name))
            orginal = cv2.imread(str(self.file_name))
            self.result = Seg.stain_segmentation(image, orginal)
            result = self.result
            height, width, byteValue = self.result.shape
            bytesPerLine = 3 * width
            cv2.cvtColor(result, cv2.COLOR_BGR2RGB, result)
            qImg = QtGui.QImage(result.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
            self.viewer.setPhoto(pixmap=QtGui.QPixmap.fromImage(qImg))
            self.populate_table()
    
    def populate_table(self):
        self.clear_table()
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(len(Seg.pattern.stains))
        headers = "id;position x;position y;area px;area_mm;width ellipse;height ellipse;angle;gamma;direction;solidity;circularity;intensity"
        self.tableWidget.setHorizontalHeaderLabels(headers.split(";"))
        j = 0
        for stain in Seg.pattern.stains:
            print("getting summary data for stain", stain.id, stain.id / len(Seg.pattern.stains) * 100, "%")
            stain_data = stain.get_summary_data()            
            for i in range(13):
                self.tableWidget.setItem(j,i, QtGui.QTableWidgetItem(str(stain_data[i])))
            j += 1
        self.tableWidget.show()

    def clear_table(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()

def main():
    app = QtGui.QApplication(sys.argv)
    gui = BPA_App()
    gui.show()
    app.exec_()

if __name__ == '__main__':
   main()
