			elif Type == "titlebaralisveris":
				parent.Children[Index] = TitleBar()
				parent.Children[Index].SetParent(parent)
				self.LoadElementTitleBar(parent.Children[Index], ElementValue, parent)
			#
			elif Type == "listbox_scrollitem":
				parent.Children[Index] = ListBoxScrollItemEkleme()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)
			

class TitleBarAlisveris(Window):

	BLOCK_WIDTH = 32
	BLOCK_HEIGHT = 23

	def __init__(self):
		Window.__init__(self)
		self.AddFlag("attach")

	def __del__(self):
		Window.__del__(self)

	def MakeTitleBar(self, width, color):

		width = max(64, width)

		imgLeft = ImageBox()
		imgCenter = ExpandedImageBox()
		imgRight = ImageBox()
		imgLeft.AddFlag("not_pick")
		imgCenter.AddFlag("not_pick")
		imgRight.AddFlag("not_pick")
		imgLeft.SetParent(self)
		imgCenter.SetParent(self)
		imgRight.SetParent(self)

		if localeInfo.IsARABIC():
			imgLeft.LoadImage("locale/ae/ui/pattern/titlebar_left.tga")
			imgCenter.LoadImage("locale/ae/ui/pattern/titlebar_center.tga")
			imgRight.LoadImage("locale/ae/ui/pattern/titlebar_right.tga")
		else:
			imgLeft.LoadImage("d:/ymir work/ui/pattern/titlebar_left.tga")
			imgCenter.LoadImage("d:/ymir work/ui/pattern/titlebar_center.tga")
			imgRight.LoadImage("d:/ymir work/ui/pattern/titlebar_right.tga")

		imgLeft.Show()
		imgCenter.Show()
		imgRight.Show()

		self.imgLeft = imgLeft
		self.imgCenter = imgCenter
		self.imgRight = imgRight
		self.btnClose = btnClose

		self.SetWidth(width)

	def SetWidth(self, width):
		self.imgCenter.SetRenderingRect(0.0, 0.0, float((width - self.BLOCK_WIDTH*2) - self.BLOCK_WIDTH) / self.BLOCK_WIDTH, 0.0)
		self.imgCenter.SetPosition(self.BLOCK_WIDTH, 0)
		self.imgRight.SetPosition(width - self.BLOCK_WIDTH, 0)
			
		self.SetSize(width, self.BLOCK_HEIGHT)
#2.
class ListBoxScrollVeSiralama2(Window):

	TEMPORARY_PLACE = 3

	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)
		self.overLine = -1
		self.selectedLine = -1
		self.width = 0
		self.height = 0
		self.stepSize = 100
		self.basePos = 0
		self.showLineCount = 0
		self.itemCenterAlign = TRUE
		self.itemList = []
		self.itemlerList = []
		self.itemThinList = []
		self.itemSlotList = []
		self.itemSlotList2 = []
		self.itemResimList = []
		self.itemNameList = []
		self.fiyatList = []
		self.satanNameList = []
		self.satinalList = []
		self.gerialList = []
		
		self.keyDict = {}
		self.textDict = {}
		self.event = lambda *arg: None
		
	def __del__(self):
		Window.__del__(self)

	def SetWidth(self, width):
		self.SetSize(width, self.height)

	def SetSize(self, width, height):
		Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetTextCenterAlign(self, flag):
		self.itemCenterAlign = flag

	def SetBasePos(self, pos):
		self.basePos = pos
		self._LocateItem()

	def ClearItem(self):
		self.keyDict = {}
		self.textDict = {}
		self.itemList = []
		self.itemThinList = []
		self.itemSlotList = []
		self.itemSlotList2 = []
		self.itemResimList = []
		self.itemNameList = []
		self.fiyatList = []
		self.satanNameList = []
		self.satinalList = []
		self.gerialList = []
		self.overLine = -1
		self.selectedLine = -1
	
	#def InsertItem(self, number, resim, text, tooltipText, arg, line):
	def InsertItem(self, number, kodu, itemadi, itemfiyati, itemisatan, uzerinegelince):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = itemadi + itemfiyati + itemisatan + uzerinegelince
		self.textDict[len(self.itemNameList)] = itemadi
		self.textDict[len(self.fiyatList)] = itemfiyati
		self.textDict[len(self.satanNameList)] = itemisatan
		
		thin = ThinBoard()
		thin.SetParent(self)
		thin.SetPosition(6, 40)
		thin.SetSize(744+15+15, 72)
		#thin.SetPosition(20, 117) #Yer
		thin.Show()
		
		slotLine = ImageBox()
		slotLine.SetParent(thin)
		slotLine.SetPosition(30, 5-1)
		slotLine.LoadImage("d:/ymir work/ui/Public/Slot_Base.sub")
		slotLine.Show()
		
		slotLine.SAFE_SetStringEvent("MOUSE_OVER_IN", self.Uzerinde(kodu, uzerinegelince))
		slotLine.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.NoUzerinde)
		
		slotLine2 = ImageBox()
		slotLine2.SetParent(thin)
		slotLine2.SetPosition(30, 20+20-5)
		slotLine2.LoadImage("d:/ymir work/ui/Public/Slot_Base.sub")
		slotLine2.Show()
		
		item.SelectItem(kodu)
		iconu = item.GetIconImageFileName()
		
		resimLine = ImageBox()
		resimLine.SetParent(thin)
		resimLine.SetPosition(30-2, 10-3-1)
		resimLine.LoadImage(iconu)
		resimLine.Show()
		
		itemAdiLine = TextLine()
		itemAdiLine.SetParent(thin)
		itemAdiLine.SetPosition(200-10, 25+2)
		itemAdiLine.SetText(itemadi)
		itemAdiLine.Show()
		
		itemFiyatLine = TextLine()
		itemFiyatLine.SetParent(thin)
		itemFiyatLine.SetPosition(190+180+75-10, 25+2)
		itemFiyatLine.SetText(itemfiyati)
		itemFiyatLine.Show()
		
		itemSatanLine = TextLine()
		itemSatanLine.SetParent(thin)
		itemSatanLine.SetPosition(190+180+80+160-50+10, 25+2)
		itemSatanLine.SetText(itemisatan)
		itemSatanLine.Show()
		
		satinal = Button()
		satinal.SetParent(thin)
		satinal.SetPosition(190+180+80+160+30+10, 25+2-5+1)
		satinal.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		satinal.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		satinal.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		satinal.SetText("Satin Al")
		satinal.SetToolTipText("Itemi satin al")
		satinal.Show()
		#satinal.SetEvent(func)

		self.itemList.append(itemAdiLine)
		self.itemThinList.append(thin)
		self.itemSlotList.append(slotLine)
		self.itemSlotList2.append(slotLine2)
		self.itemResimList.append(resimLine)
		self.itemNameList.append(itemAdiLine)
		self.fiyatList.append(itemFiyatLine)
		self.satanNameList.append(itemSatanLine)
		self.satinalList.append(satinal)

		self._LocateItem()
		
	def InsertItemMy(self, number, kodu, itemadi, itemfiyati, itemisatan, uzerinegelince):
		self.keyDict[len(self.itemList)] = number
		self.textDict[len(self.itemList)] = itemadi + itemfiyati + itemisatan + uzerinegelince
		self.textDict[len(self.itemNameList)] = itemadi
		self.textDict[len(self.fiyatList)] = itemfiyati
		self.textDict[len(self.satanNameList)] = itemisatan
		
		thin = ThinBoard()
		thin.SetParent(self)
		thin.SetPosition(6, 40)
		thin.SetSize(744+15+15, 72)
		#thin.SetPosition(20, 117) #Yer
		thin.Show()
		
		slotLine = ImageBox()
		slotLine.SetParent(thin)
		slotLine.SetPosition(30, 5-1)
		slotLine.LoadImage("d:/ymir work/ui/Public/Slot_Base.sub")
		slotLine.Show()
		
		slotLine.SAFE_SetStringEvent("MOUSE_OVER_IN", self.Uzerinde(kodu, uzerinegelince))
		slotLine.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.NoUzerinde)
		
		slotLine2 = ImageBox()
		slotLine2.SetParent(thin)
		slotLine2.SetPosition(30, 20+20-5)
		slotLine2.LoadImage("d:/ymir work/ui/Public/Slot_Base.sub")
		slotLine2.Show()
		
		item.SelectItem(kodu)
		iconu = item.GetIconImageFileName()
		
		resimLine = ImageBox()
		resimLine.SetParent(thin)
		resimLine.SetPosition(30-2, 10-3-1)
		resimLine.LoadImage(iconu)
		resimLine.Show()
		
		itemAdiLine = TextLine()
		itemAdiLine.SetParent(thin)
		itemAdiLine.SetPosition(200-10, 25+2)
		itemAdiLine.SetText(itemadi)
		itemAdiLine.Show()
		
		itemFiyatLine = TextLine()
		itemFiyatLine.SetParent(thin)
		itemFiyatLine.SetPosition(190+180+75-10, 25+2)
		itemFiyatLine.SetText(itemfiyati)
		itemFiyatLine.Show()
		
		itemSatanLine = TextLine()
		itemSatanLine.SetParent(thin)
		itemSatanLine.SetPosition(190+180+80+160-50+10, 25+2)
		itemSatanLine.SetText(itemisatan)
		itemSatanLine.Show()
		
		gerial = Button()
		gerial.SetParent(thin)
		gerial.SetPosition(190+180+80+160+30+10, 25+2-5+1)
		gerial.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		gerial.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		gerial.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		gerial.SetText("Kaldır")
		gerial.SetToolTipText("Itemi alisveristen kaldir.")
		gerial.Show()
		#satinal.SetEvent(func)

		self.itemList.append(itemAdiLine)
		self.itemThinList.append(thin)
		self.itemSlotList.append(slotLine)
		self.itemSlotList2.append(slotLine2)
		self.itemResimList.append(resimLine)
		self.itemNameList.append(itemAdiLine)
		self.fiyatList.append(itemFiyatLine)
		self.satanNameList.append(itemSatanLine)
		self.gerialList.append(gerial)

		self._LocateItemMy()
		
	def Uzerinde(self, itemkod, text): #gelenler / socket0-5 -> attr0-6
		self.toolTip.ClearToolTip()
		items = text.split("#")
		self.toolTip.AddRefineItemData(itemkod, [items[1],items[2],items[3],items[4],items[5],items[6]], [(items[8],items[9]),(items[10],items[11]),(items[12],items[13]),(items[14],items[15]),(items[16],items[17]),(items[18],items[19]),(items[20],items[21])])
		
	def NoUzerinde(self):
		self.toolTip.Hide()

	def ChangeItem(self, number, text, tooltipText, textlineText, width):
		for key, value in self.keyDict.items():
			if value == number:
				self.textDict[key] = text + tooltipText + textlineText + width

				if number < len(self.itemList):
					self.itemList[key].SetText(text)

				return

	def LocateItem(self):
		self._LocateItem()

	def _LocateItem(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.itemList)):
			thin = self.itemThinList[i]
			slot = self.itemSlotList[i]
			slot2 = self.itemSlotList2[i]
			itemresim = self.itemResimList[i]
			itemadi = self.itemNameList[i]
			itemfiyati = self.fiyatList[i]
			itemisatan = self.satanNameList[i]
			satinal = self.satinalList[i]

			if skipCount > 0:
				skipCount -= 1
				continue

			if localeInfo.IsARABIC():
				w, h = textLine.GetTextSize()
				textLine.SetPosition(w+10, yPos + 3)
			else:
				thin.SetPosition(6, yPos + 40-18+2)
				#slot.SetPosition(68, yPos + 119)
				#slot2.SetPosition(68, yPos + 152)
				#itemresim.SetPosition(72, yPos + 123)
				#itemadi.SetPosition(221+150, yPos + 143)
				#itemfiyati.SetPosition(426+150, yPos + 143)
				#itemisatan.SetPosition(597, yPos + 142)

			yPos += 75

			if yPos <= self.GetHeight():
				#self.showLineCount += 1
				thin.Show()
				slot.Show()
				slot2.Show()
				itemresim.Show()
				itemadi.Show()
				itemfiyati.Show()
				itemisatan.Show()
				satinal.Show()
			else:
				thin.Hide()
				slot.Hide()
				slot2.Hide()
				itemresim.Hide()
				itemadi.Hide()
				itemfiyati.Hide()
				itemisatan.Hide()
				satinal.Hide()
				
	def _LocateItemMy(self):

		skipCount = self.basePos
		yPos = 0
		self.showLineCount = 0

		for i in xrange(0, len(self.itemList)):
			thin = self.itemThinList[i]
			slot = self.itemSlotList[i]
			slot2 = self.itemSlotList2[i]
			itemresim = self.itemResimList[i]
			itemadi = self.itemNameList[i]
			itemfiyati = self.fiyatList[i]
			itemisatan = self.satanNameList[i]
			gerial = self.gerialList[i]

			if skipCount > 0:
				skipCount -= 1
				continue

			if localeInfo.IsARABIC():
				w, h = textLine.GetTextSize()
				textLine.SetPosition(w+10, yPos + 3)
			else:
				thin.SetPosition(6, yPos + 40-18+2)
				#slot.SetPosition(68, yPos + 119)
				#slot2.SetPosition(68, yPos + 152)
				#itemresim.SetPosition(72, yPos + 123)
				#itemadi.SetPosition(221+150, yPos + 143)
				#itemfiyati.SetPosition(426+150, yPos + 143)
				#itemisatan.SetPosition(597, yPos + 142)

			yPos += 75

			if yPos <= self.GetHeight():
				#self.showLineCount += 1
				thin.Show()
				slot.Show()
				slot2.Show()
				itemresim.Show()
				itemadi.Show()
				itemfiyati.Show()
				itemisatan.Show()
				gerial.Show()
			else:
				thin.Hide()
				slot.Hide()
				slot2.Hide()
				itemresim.Hide()
				itemadi.Hide()
				itemfiyati.Hide()
				itemisatan.Hide()
				gerial.Hide()

	def ArrangeItem(self):
		self.SetSize(self.width)
		self.SetSize(self.width, len(self.itemList) * 17)
		self._LocateItem()

	def GetViewItemCount(self):
		return self.showLineCount
		#return int(self.GetHeight() / self.stepSize)

	def GetItemCount(self):
		return len(self.itemList)

	def SetEvent(self, event):
		self.event = event

	def SelectItem(self, line):

		if not self.keyDict.has_key(line):
			return

		if line == self.selectedLine:
			return

		#self.selectedLine = line
		#self.event(self.keyDict.get(line, 0), self.textDict.get(line, "None"))
		
		#x, y = self.GetGlobalPosition()

	def GetSelectedItem(self):
		return self.keyDict.get(self.selectedLine, 0)

	def OnMouseLeftButtonDown(self):
		if self.overLine < 0:
			return

	def OnMouseLeftButtonUp(self):
		if self.overLine >= 0:
			pass
			#self.SelectItem(self.overLine+self.basePos)
	def OnUpdate(self):

		#self.overLine = -1

		if self.IsIn():
			pass
			#self.SelectItem(self.overLine+self.basePos)
			#x, y = self.GetGlobalPosition()
			#height = self.GetHeight()
			#xMouse, yMouse = wndMgr.GetMousePosition()

			#if yMouse - y < height - 1:
			#self.overLine = (yMouse - y) / self.stepSize

				#if self.overLine < 0:
					#self.overLine = -1
				#if self.overLine >= len(self.itemList):
					#self.overLine = -1

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()
		yRender -= self.TEMPORARY_PLACE
		widthRender = self.width
		heightRender = self.height + self.TEMPORARY_PLACE*2

		if localeInfo.IsCIBN10:
			if -1 != self.overLine and self.keyDict[self.overLine] != -1:
				grp.SetColor(HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)

			if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
				if self.selectedLine >= self.basePos:
					if self.selectedLine - self.basePos < self.showLineCount:
						grp.SetColor(SELECT_COLOR)
						grp.RenderBar(xRender + 2 - 50, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize - 50)

		else:		
			if -1 != self.overLine:
				pass
				#grp.SetColor(HALF_WHITE_COLOR)
				#grp.RenderBar(xRender + 2 - 50, yRender + self.overLine*self.stepSize + 4, self.width - 3 - 50, self.stepSize - 50)				

			if -1 != self.selectedLine:
				pass
				#if self.selectedLine >= self.basePos:
					#if self.selectedLine - self.basePos < self.showLineCount:
						#grp.SetColor(SELECT_COLOR)
						#grp.RenderBar(xRender + 2 - 50, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4 - 50, self.width - 3, self.stepSize - 50)
						
class ListBoxScrollItemEkleme(ListBoxScrollVeSiralama2):
	def __init__(self):
		ListBoxScrollVeSiralama2.__init__(self)
		
		self.viewItemCount=15
		self.basePos=0
		self.itemHeight=15
		self.itemStep=20
		self.showLineCount = 0
		self.scrollBar = ScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetScrollEvent(self.__OnScroll)
		self.scrollBar.Hide()

	def SetSize(self, width, height):
		ListBoxScrollVeSiralama2.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
		Window.SetSize(self, width, height)
		
		#self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH + 5 - 15 - 7, 0)
		##self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH, 0)
		self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH - 8 - 3 - 9, 0)
		self.scrollBar.SetScrollBarSize(height)

	def ClearItem(self):
		ListBoxScrollVeSiralama2.ClearItem(self)
		self.scrollBar.SetPos(0)

	def _LocateItem(self):
		ListBoxScrollVeSiralama2._LocateItem(self)
		
		if self.showLineCount < len(self.itemList):
			self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()
		
	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar
		
	def __OnScroll(self):
		scrollLen = self.GetItemCount()-self.GetViewItemCount()
		if scrollLen < 0:
			scrollLen = 0
		self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return len(self.itemList)

	def GetItemViewCoord(self, pos, itemWidth):
		if localeInfo.IsARABIC():
			return (self.GetWidth()-itemWidth-10, (pos-self.basePos)*self.itemStep)
		else:
			return (0, (pos-self.basePos)*self.itemStep)
			
	def __IsInViewRange(self, pos): #-> ARG: Liste'yi tekrar döndür,elemanlari al.Pos = 0
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1
						
class ScrollBarAlisveris(Window):

	SCROLLBAR_WIDTH = 35
	SCROLLBAR_MIDDLE_HEIGHT = 9
	SCROLLBAR_BUTTON_WIDTH = 35
	SCROLLBAR_BUTTON_HEIGHT = 35
	MIDDLE_BAR_POS = 5
	MIDDLE_BAR_UPPER_PLACE = 3
	MIDDLE_BAR_DOWNER_PLACE = 4
	TEMP_SPACE = MIDDLE_BAR_UPPER_PLACE + MIDDLE_BAR_DOWNER_PLACE

	class MiddleBar(DragButton):
		def __init__(self):
			DragButton.__init__(self)
			self.AddFlag("movable")
			#self.AddFlag("restrict_x")

		def MakeImage(self):
			top = ImageBox()
			top.SetParent(self)
			top.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Top.tga")
			top.SetPosition(0, 0)
			top.AddFlag("not_pick")
			top.Show()
			bottom = ImageBox()
			bottom.SetParent(self)
			bottom.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Bottom.tga")
			bottom.AddFlag("not_pick")
			bottom.Show()

			middle = ExpandedImageBox()
			middle.SetParent(self)
			middle.LoadImage("d:/ymir work/ui/pattern/ScrollBar_Middle.tga")
			middle.SetPosition(0, 4)
			middle.AddFlag("not_pick")
			middle.Show()

			self.top = top
			self.bottom = bottom
			self.middle = middle

		def SetSize(self, height):
			height = max(12, height)
			DragButton.SetSize(self, 10, height)
			self.bottom.SetPosition(0, height-4)

			height -= 4*3
			self.middle.SetRenderingRect(0, 0, 0, float(height)/4.0)

	def __init__(self):
		Window.__init__(self)

		self.pageSize = 1
		self.curPos = 0.0
		self.eventScroll = lambda *arg: None
		self.lockFlag = FALSE
		self.scrollStep = 0.20


		self.CreateScrollBar()

	def __del__(self):
		Window.__del__(self)

	def CreateScrollBar(self):
		barSlot = Bar3D()
		barSlot.SetParent(self)
		barSlot.AddFlag("not_pick")
		barSlot.Show()

		middleBar = self.MiddleBar()
		middleBar.SetParent(self)
		middleBar.SetMoveEvent(__mem_func__(self.OnMove))
		middleBar.Show()
		middleBar.MakeImage()
		middleBar.SetSize(12)

		upButton = Button()
		upButton.SetParent(self)
		upButton.SetEvent(__mem_func__(self.OnUp))
		upButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_up_button_01.sub")
		upButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_up_button_02.sub")
		upButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_up_button_03.sub")
		upButton.Show()

		downButton = Button()
		downButton.SetParent(self)
		downButton.SetEvent(__mem_func__(self.OnDown))
		downButton.SetUpVisual("d:/ymir work/ui/public/scrollbar_down_button_01.sub")
		downButton.SetOverVisual("d:/ymir work/ui/public/scrollbar_down_button_02.sub")
		downButton.SetDownVisual("d:/ymir work/ui/public/scrollbar_down_button_03.sub")
		downButton.Show()

		self.upButton = upButton
		self.downButton = downButton
		self.middleBar = middleBar
		self.barSlot = barSlot

		self.SCROLLBAR_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_MIDDLE_HEIGHT = self.middleBar.GetHeight()
		self.SCROLLBAR_BUTTON_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_BUTTON_HEIGHT = self.upButton.GetHeight()

	def Destroy(self):
		self.middleBar = None
		self.upButton = None
		self.downButton = None
		self.eventScroll = lambda *arg: None

	def SetScrollEvent(self, event):
		self.eventScroll = event

	def SetMiddleBarSize(self, pageScale):
		realHeight = self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2
		self.SCROLLBAR_MIDDLE_HEIGHT = int(pageScale * float(realHeight))
		self.middleBar.SetSize(self.SCROLLBAR_MIDDLE_HEIGHT)
		self.pageSize = (self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)

	def SetScrollBarSize(self, height):
		self.pageSize = (height - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)
		self.SetSize(self.SCROLLBAR_WIDTH, height)
		self.upButton.SetPosition(0, 0)
		self.downButton.SetPosition(0, height - self.SCROLLBAR_BUTTON_HEIGHT)
		self.middleBar.SetRestrictMovementArea(self.MIDDLE_BAR_POS, self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE, self.MIDDLE_BAR_POS+2, height - self.SCROLLBAR_BUTTON_HEIGHT*2 - self.TEMP_SPACE)
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, 0)

		self.UpdateBarSlot()

	def UpdateBarSlot(self):
		self.barSlot.SetPosition(0, self.SCROLLBAR_BUTTON_HEIGHT)
		self.barSlot.SetSize(self.GetWidth() - 2, self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2 - 2)

	def GetPos(self):
		return self.curPos

	def SetPos(self, pos):
		pos = max(0.0, pos)
		pos = min(1.0, pos)

		newPos = float(self.pageSize) * pos
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, int(newPos) + self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE)
		self.OnMove()

	def SetScrollStep(self, step):
		self.scrollStep = step
	
	def GetScrollStep(self):
		return self.scrollStep
		
	def OnUp(self):
		self.SetPos(self.curPos-self.scrollStep)

	def OnDown(self):
		self.SetPos(self.curPos+self.scrollStep)

	def OnMove(self):

		if self.lockFlag:
			return

		if 0 == self.pageSize:
			return

		(xLocal, yLocal) = self.middleBar.GetLocalPosition()
		self.curPos = float(yLocal - self.SCROLLBAR_BUTTON_HEIGHT - self.MIDDLE_BAR_UPPER_PLACE) / float(self.pageSize)

		self.eventScroll()

	def OnMouseLeftButtonDown(self):
		(xMouseLocalPosition, yMouseLocalPosition) = self.GetMouseLocalPosition()
		pickedPos = yMouseLocalPosition - self.SCROLLBAR_BUTTON_HEIGHT - self.SCROLLBAR_MIDDLE_HEIGHT/2
		newPos = float(pickedPos) / float(self.pageSize)
		self.SetPos(newPos)

	def LockScroll(self):
		self.lockFlag = TRUE

	def UnlockScroll(self):
		self.lockFlag = FALSE