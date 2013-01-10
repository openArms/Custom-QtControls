from PyQt4 import QtGui,QtCore
import math


class StylePreset():
	MacOSX,Firefox,IE7,Custom =  range(4)
	

class customProgressBar(QtGui.QProgressBar):
	def __init__(self,parent=None):
		QtGui.QProgressBar.__init__(self,parent)
		
		#Constants =========================================================
		self.NumberOfDegreesInCircle = 360
		self.NumberOfDegreesInHalfCircle = self.NumberOfDegreesInCircle / 2
		self.DefaultOuterCircleRadius = 8
		self.DefaultInnerCircleRadius = 10;
		self.DefaultNumberOfSpoke = 36;
		self.DefaultSpokeThickness = 4;
		self.DefaultColor = QtCore.Qt.darkGray
		self.MacOSXInnerCircleRadius = 5
		self.MacOSXOuterCircleRadius = 11
		self.MacOSXNumberOfSpoke = 12
		self.MacOSXSpokeThickness = 2
		self.FireFoxInnerCircleRadius = 6
		self.FireFoxOuterCircleRadius = 7
		self.FireFoxNumberOfSpoke = 9
		self.FireFoxSpokeThickness = 4
		self.IE7InnerCircleRadius = 8
		self.IE7OuterCircleRadius = 9
		self.IE7NumberOfSpoke = 24
		self.IE7SpokeThickness = 4
		#Enumeration =======================================================
		self.StylePresets = StylePreset()
		#Attributes ========================================================
		self.m_Timer  = QtCore.QTimer()
		self.m_IsTimerActive = True
		
		self.m_NumberOfSpoke = 10
		self.m_SpokeThickness =2
		self.m_ProgressValue = 0
		self.m_OuterCircleRadius = 7
		self.m_InnerCircleRadius = 6
		self.m_CenterPoint = QtCore.QPointF(self.width()/2,self.height()/2)
		self.m_Color = QtGui.QColor.fromRgbF(0, 0,1,1)
		self.m_Colors = list()
		self.m_Angles = list()
		self.BYTEMAXSIZE = 255
		
		self.connect(self.m_Timer,QtCore.SIGNAL("timeout()"),self.Tick)
		#self.ActiveTimer()
		
	
	#Properties ========================================================
	#<summary>
	#Gets or sets the lightest color of the circle.
	#</summary>
	#<value>The lightest color of the circle.</value>
	
	@property
	def Color(self):
		return self.m_Color
	@Color.setter
	def Color(self,value):
		self.m_Color = value
		self.GenerateColorsPallet()
		self.update()
		
	#<summary>
	#Gets or sets the outer circle radius.
	#</summary>
	#<value>The outer circle radius.</value>
	@property
	def OuterCircleRadius(self):
		if (self.m_OuterCircleRadius == 0):
			self.m_OuterCircleRadius = self.DefaultOuterCircleRadius
			return self.m_OuterCircleRadius
	@OuterCircleRadius.setter
	def OuterCircleRadius(self,value):
		self.m_OuterCircleRadius = value
		self.update()

	#<summary>
	#Gets or sets the inner circle radius.
	#</summary>
	#<value>The inner circle radius.</value>
	@property
	def InnerCircleRadius(self,value):
		if (self.m_InnerCircleRadius == 0):
			self.m_InnerCircleRadius = self.DefaultOuterCircleRadius
			return self.m_InnerCircleRadius
	@InnerCircleRadius.setter
	def InnerCircleRadius(self,value): 
		self.m_InnerCircleRadius = value
		self.update()

	#<summary>
	#Gets or sets the number of spoke.
	#</summary>
	#<value>The number of spoke.</value>
	@property
	def NumberSpoke(self):
		if (self.m_NumberOfSpoke == 0):
			self.m_NumberOfSpoke = self.DefaultOuterCircleRadius
			
		return self.m_NumberOfSpoke
	@NumberSpoke.setter        
	def NumberSpoke(self,value): 
		if (self.m_NumberOfSpoke != value and self.m_NumberOfSpoke > 0):
			self.m_NumberOfSpoke = value
			self.GenerateColorsPallet()
			self.GetSpokesAngles()
			self.update()

	#<summary>
	#Gets or sets a value indicating whether this <see cref="T:LoadingCircle"/> is active.
	#</summary>
	#<value><c>true</c> if active; otherwise, <c>false</c>.</value>
	@property
	def Active(self):
		return self.m_IsTimerActive
	@Active.setter 
	def Active(self,value):
		self.m_IsTimerActive = value
		self.ActiveTimer()
		

	#<summary>
	#Gets or sets the spoke thickness.
	#</summary>
	#<value>The spoke thickness.</value>
	@property
	def SpokeThickness(self):
		if (self.m_SpokeThickness <= 0):
			self.m_SpokeThickness = self.DefaultSpokeThickness
			return self.m_SpokeThickness
		
	@SpokeThickness.setter		
	def SpokeThickness(self,value): 
		self.m_SpokeThickness = value
		self.update()
		
	#<summary>
	#Gets or sets the rotation speed.
	#</summary>
	#<value>The rotation speed.</value>
	@property
	def RotationSpeed(self):
		return self.m_Timer.interval()
	@RotationSpeed.setter
	def RotationSpeed(self,value): 
		if value > 0:
			self.m_Timer.setInterval(value)

	#<summary>
	#Quickly sets the style to one of these presets, or a custom style if desired
	#</summary>
	#<value>The style preset.</value>
	#[Category("LoadingCircle"),
	#Description("Quickly sets the style to one of these presets, or a custom style if desired"),
	#DefaultValue(typeof(StylePresets), "Custom")]
	@property
	def StylePreset(self,value):
		return self.m_StylePreset
	
	@StylePreset.setter
	def StylePreset(self,value):
		self.m_StylePreset = value
		if self.m_StylePreset == self.StylePresets.MacOSX:
			self.SetCircleAppearance(self.MacOSXNumberOfSpoke,self.MacOSXSpokeThickness, self.MacOSXInnerCircleRadius,self.MacOSXOuterCircleRadius)

		elif self.m_StylePreset == self.StylePresets.Firefox:
			self.SetCircleAppearance(self.FireFoxNumberOfSpoke,\
                    self.FireFoxSpokeThickness, self.FireFoxInnerCircleRadius,\
                    self.FireFoxOuterCircleRadius)

		elif self.m_StylePreset == self.StylePresets.IE7:
			self.SetCircleAppearance(self.IE7NumberOfSpoke,\
                    self.IE7SpokeThickness, self.IE7InnerCircleRadius,\
                    self.IE7OuterCircleRadius)

		elif self.m_StylePreset == self.StylePresets.Custom:
			self.SetCircleAppearance(self.DefaultNumberOfSpoke,self.DefaultSpokeThickness,self.DefaultInnerCircleRadius,self.DefaultOuterCircleRadius) 
	#Events ============================================================
	#<summary>
	#Handles the Resize event of the LoadingCircle control.
	#</summary>
	#<param name="sender">The source of the event.</param>
	#<param name="e">The <see cref="T:System.EventArgs"/> instance containing the event data.</param>
	def LoadingCircle_Resize(self,sender,e):
		self.GetControlCenterPoint()
		pass


	#<summary>
	#Handles the Tick event of the aTimer control.
	#</summary>
	#<param name="sender">The source of the event.</param>
	#<param name="e">The <see cref="T:System.EventArgs"/> instance containing the event data.</param>
	
	def Tick(self):
		self.m_ProgressValue =  (self.m_ProgressValue + 1)% self.m_NumberOfSpoke
		self.update()


	
				
	#Overridden Methods ================================================
	#<summary>
	#Retrieves the size of a rectangular area into which a control can be fitted.
	#</summary>
	#<param name="proposedSize">The custom-sized area for a control.</param>
	#<returns>
	#An ordered pair of type <see cref="T:System.Drawing.Size"></see> representing the width and height of a rectangle.
	#</returns>
	
	def GetPreferredSize(self,proposedSize):
		proposedSize.Width =(self.m_OuterCircleRadius + self.m_SpokeThickness) * 2
		return proposedSize
	
	#Methods ===========================================================
	#<summary>
	#Darkens a specified color.
	#</summary>
	#<param name="_objColor">Color to darken.</param>
	#<param name="_intPercent">The percent of darken.</param>
	#<returns>The new color generated.</returns>
	def Darken(self,_objColor,_intPercent):
		
		intRed = _objColor.red()
		intGreen = _objColor.green()
		intBlue = _objColor.blue()
		return QtGui.QColor.fromRgba(QtGui.qRgba(min(intRed, self.BYTEMAXSIZE),min(intGreen, self.BYTEMAXSIZE),min(intBlue, self.BYTEMAXSIZE),_intPercent))
		
	# <summary>
	# Generates the colors pallet.
	#args (QColor _objColor, bool _blnShadeColor, int _intNbSpoke)
	# </summary>
	def GenerateColorsPallet(self):
		
		if self.m_NumberOfSpoke > 0 :
			self.m_Colors = []
			_objColor ,_blnShadeColor,_intNbSpoke  = [self.m_Color, self.m_IsTimerActive, self.m_NumberOfSpoke]  
			
			#Value is used to simulate a gradient feel... For each spoke, the 
			#color will be darken by value in intIncrement.
			bytIncrement = (self.BYTEMAXSIZE / self.m_NumberOfSpoke)
			#Reset variable in case of multiple passes
			PERCENTAGE_OF_DARKEN = 0
			for intCursor in range(self.m_NumberOfSpoke):
				if _blnShadeColor:
					if intCursor == 0 or intCursor < (self.m_NumberOfSpoke - _intNbSpoke):
						self.m_Colors.append(_objColor)
					else:
						#Increment alpha channel color
						PERCENTAGE_OF_DARKEN += bytIncrement
						#Ensure that we don't exceed the maximum alpha
						#channel value (255)
						if(PERCENTAGE_OF_DARKEN > self.BYTEMAXSIZE):
							PERCENTAGE_OF_DARKEN = self.BYTEMAXSIZE
							
						#Determine the spoke forecolor
						self.m_Colors.append(self.Darken(_objColor, PERCENTAGE_OF_DARKEN))
				else:
					self.m_Colors.append(_objColor)
				
			
		
		
	# <summary>
	# Gets the control center point.
	# args (Control _objControl)
	# </summary>
	def GetControlCenterPoint(self,*args):
		if len(args)== 0:
			self.m_CenterPoint = self.GetControlCenterPoint(self);
		else:
			return args[0].Width / 2, args[0].Height / 2 - 1
	
	
	#Events ============================================================
	#<summary>
	#Handles the Resize event of the LoadingCircle control.
	#</summary>
	#<param name="sender">The source of the event.</param>
	#<param name="e">The <see cref="T:System.EventArgs"/> instance containing the event data.</param>
	def Resize(self,sender,e):
		self.GetControlCenterPoint()
	
			
	#<summary>
	#Gets the coordinate.
	#</summary>
	#<param name="_objCircleCenter">The Circle center.</param>
	#<param name="_intRadius">The radius.</param>
	#<param name="_dblAngle">The angle.</param>
	#<returns></returns
	def GetCoordinate(self,objCircleCenter,intRadius,dblAngle):
		dblAngle = math.pi * dblAngle / self.NumberOfDegreesInHalfCircle
		return QtCore.QPointF(objCircleCenter.x() +intRadius * math.cos(dblAngle),objCircleCenter.y() + intRadius * math.sin(dblAngle))
	

	#<summary>
	#Gets the spokes angles.
	#</summary>
	def GetSpokesAngles(self,*args):
		self.m_Angles=[]
		numberofspokes = self.m_NumberOfSpoke if len(args) == 0 else args[0]
		dblAngle = (self.NumberOfDegreesInCircle / numberofspokes)
		for shtCounter in range( numberofspokes ):
			self.m_Angles.append( dblAngle if shtCounter == 0 else self.m_Angles[shtCounter - 1] + dblAngle)
	#<summary>
	#Actives the timer.
	#</summary>
	def ActiveTimer(self):
		if self.m_IsTimerActive:
			self.m_Timer.start()
		else:
			self.m_Timer.stop()
			self.m_ProgressValue = 0
		
		self.GenerateColorsPallet()
		self.update()
	

	#<summary>
	#Sets the circle appearance.
	#</summary>
	#<param name="numberSpoke">The number spoke.</param>
	#<param name="spokeThickness">The spoke thickness.</param>
	#<param name="innerCircleRadius">The inner circle radius.</param>
	#<param name="outerCircleRadius">The outer circle radius.</param>
	def SetCircleAppearance(self,numberSpoke,spokeThickness,innerCircleRadius,outerCircleRadius):
		self.m_NumberOfSpoke = numberSpoke
		self.m_SpokeThickness = spokeThickness
		self.m_InnerCircleRadius = innerCircleRadius
		self.m_OuterCircleRadius = outerCircleRadius
		
		self.update()
			
	#<summary>
	#Raises the <see cref="E:System.Windows.Forms.Control.Paint"></see> event.
	#</summary>
	#<param name="e">A <see cref="T:System.Windows.Forms.PaintEventArgs"></see> that contains the event data.</param>
	def paintEvent(self,e):
		p = QtGui.QPainter(self)
		p.setRenderHints(QtGui.QPainter.Antialiasing)
		if self.m_NumberOfSpoke > 0:
			intPosition = self.m_ProgressValue
			for intCounter in range(self.m_NumberOfSpoke):
				intPosition = intPosition % self.m_NumberOfSpoke
				pen = QtGui.QPen()  #creates a default pen
				pen.setStyle(QtCore.Qt.SolidLine)
				pen.setWidth(self.m_SpokeThickness)
				
				gradient = QtGui.QLinearGradient()
				gradient.setColorAt(0,self.m_Colors[intCounter].darker(200))
				gradient.setColorAt(0,self.m_Colors[intCounter].lighter(100))
				
				pen.setBrush(gradient)
				pen.setCapStyle(QtCore.Qt.RoundCap);
				pen.setJoinStyle(QtCore.Qt.RoundJoin)
				p.setPen(pen)
								
					
				p.drawLine(self.GetCoordinate(self.m_CenterPoint, self.m_InnerCircleRadius, self.m_Angles[intPosition]),\
							   self.GetCoordinate(self.m_CenterPoint, self.m_OuterCircleRadius,self.m_Angles[intPosition]))
		
				intPosition+= 1
			
			
