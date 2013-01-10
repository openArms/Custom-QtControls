from PyQt4 import QtGui,QtCore,uic
import os
import LoadingCircle


class window(QtGui.QMainWindow):
    def __init__(self,parent =None):
        QtGui.QMainWindow.__init__(self,parent)
        
        # Set up the user interface from Designer.
        self.ui = uic.loadUi(os.path.join(os.path.dirname(__file__), "mainwindow.ui"))
        
        self.loadingcircle = LoadingCircle.customProgressBar(self.ui.containerWidget)
        self.loadingcircle.setGeometry(QtCore.QRect(0,0,self.ui.containerWidget.width()/2,self.ui.containerWidget.height()/2))
        self.loadingcircle.setMinimumSize(300,300)
        
        self.loadingcircle.Active =True
        self.loadingcircle.NumberSpoke = 36
        self.loadingcircle.Color = QtGui.QColor.fromRgbF(1,.4,0,1)
        
        
        #Create QButonGroup and add Buttons here
        #Adding Buttons into QButtonGroup does not change anything visually
        #QButtonGroup is just a logical grouping 
        btnGroup = QtGui.QButtonGroup(self.ui.btnGroupLayout);
        btnGroup.addButton(self.ui.btnMacStyle,1)
        btnGroup.addButton(self.ui.btnFireFoxStyle,2)
        btnGroup.addButton(self.ui.btnIEStyle,3)
        btnGroup.addButton(self.ui.btnCustomStyle,4)
        
        self.ui.m_spinSpokeCount.setValue(36)
        self.ui.m_spokeThickness.setValue(2)
        self.ui.m_spinRotation.setValue(80)
        self.ui.m_spinOuterRadius.setValue(7)
        self.ui.m_spinInnerRadius.setValue(6)
        
        #fill the colors list
        self.populateColor()
        
        
        
        #group.setExclusive(True)
        
        self.ui.connect(btnGroup,QtCore.SIGNAL("buttonClicked(int)"),self.onStyleChanged)
        self.ui.connect(self.ui.m_spinSpokeCount,QtCore.SIGNAL("valueChanged(int)"),self.onSpokeCountChanged)
        self.ui.connect(self.ui.m_spokeThickness,QtCore.SIGNAL("valueChanged(int)"),self.onSpokeThicknessChanged)
        self.ui.connect(self.ui.m_spinRotation,QtCore.SIGNAL("valueChanged(int)"),self.onRotationSpeedChanged)
        self.ui.connect(self.ui.m_spinOuterRadius,QtCore.SIGNAL("valueChanged(int)"),self.onOuterRadiusChanged)
        self.ui.connect(self.ui.m_spinInnerRadius,QtCore.SIGNAL("valueChanged(int)"),self.onInnerRadiusChanged)
        
        self.ui.connect(self.ui.cmbColor,QtCore.SIGNAL("activated(int)"),self.onColorChanged)
        self.ui.show()

    def onColorChanged(self,index):
        self.loadingcircle.Color  = QtGui.QColor(self.ui.cmbColor.itemData(index,QtCore.Qt.DecorationRole).toString())
                
    def populateColor(self):
        colorNames = QtGui.QColor.colorNames()
        for index,name in enumerate(colorNames): 
            color = QtGui.QColor(name)
            self.ui.cmbColor.addItem(name)
            self.ui.cmbColor.setItemData(index,color,QtCore.Qt.DecorationRole) 
     
            
    def onStyleChanged(self,value):
        #MacOsStyle 
        if value == 1:
            print "MacOsStyle"
            self.loadingcircle.MacOSXNumberOfSpoke =12
            self.loadingcircle.MacOSXSpokeThickness = 2
            self.loadingcircle.RotationSpeed = 80
            self.loadingcircle.MacOSXOuterCircleRadius = 11
            self.loadingcircle.MacOSXInnerCircleRadius = 5
            
        #FireFox Style
        elif value == 2:
            self.loadingcircle.FireFoxNumberOfSpoke =9
            self.loadingcircle.FireFoxSpokeThickness = 4
            self.loadingcircle.RotationSpeed = 80
            self.loadingcircle.FireFoxOuterCircleRadius = 7
            self.loadingcircle.FireFoxInnerCircleRadius  = 6
            
            
            
        #IE style
        elif value == 3:
            self.loadingcircle.IE7NumberOfSpoke =24
            self.loadingcircle.IE7SpokeThickness = 4
            self.loadingcircle.RotationSpeed = 20
            self.loadingcircle.IE7OuterCircleRadius = 9
            self.loadingcircle.IE7InnerCircleRadius = 8
            
            
        #custom
        else:
            self.loadingcircle.NumberSpoke =self.ui.m_spinSpokeCount.value()
            self.loadingcircle.SpokeThickness = self.ui.m_spokeThickness.value()
            self.loadingcircle.RotationSpeed = self.ui.m_spinRotation.value()
            self.loadingcircle.OuterCircleRadius = self.ui.m_spinOuterRadius.value()
            self.loadingcircle.InnerCircleRadius = self.ui.m_spinInnerRadius.value()
            
        self.loadingcircle.StylePreset = value
   
    def onSpokeCountChanged(self,value):
        self.loadingcircle.NumberSpoke = value
    def onSpokeThicknessChanged(self,value):
        self.loadingcircle.SpokeThickness = value
    def onRotationSpeedChanged(self,value):
        self.loadingcircle.RotationSpeed = value
    def onOuterRadiusChanged(self,value):
        self.loadingcircle.OuterCircleRadius = value
    def onInnerRadiusChanged(self,value):
        self.loadingcircle.InnerCircleRadius = value
    
           
            
            
        
        
        