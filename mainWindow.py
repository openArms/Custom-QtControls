from PyQt4 import QtGui,QtCore
import sys
import LoadingCircle
import WidgetUI
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    w = WidgetUI.window()
    
    """
    w = QtGui.QMainWindow()
    w.resize(500,500)
    
    w.setWindowTitle('Progress Bar')
    
    loadingcircle = LoadingCircle.customProgressBar()
    loadingcircle.setGeometry(QtCore.QRect(0,0,500,200))
    loadingcircle.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
    loadingcircle.Active  =True
    loadingcircle.NumberSpoke =36
    loadingcircle.Color = QtGui.QColor.fromRgbF(1,.4,0,1)
    loadingcircle.SpokeThickness = 4
    loadingcircle.RotationSpeed = 80
    loadingcircle.OuterCircleRadius = 50
    loadingcircle.InnerCircleRadius = 45
    loadingcircle.StylePreset = 4 #Custom
    
    w.setCentralWidget(loadingcircle)
    w.show()
    
    """
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()