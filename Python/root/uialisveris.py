import app
import event
import net
import player
import item
import ui
import uiToolTip
import mouseModule
import localeInfo
import uiCommon
import constInfo
import dbg
import math
import shop
import chat
import localeInfo
import snd
import riotInfo

class AlisverisSystem(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.isLoaded = FALSE

	def __Initialize(self):
		self.children = []
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/alisveriswindow.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.board = self.GetChild("Board")
			self.itemler = self.GetChild("ItemList")
			self.param = self.GetChild("Money")
			self.anasayfa = self.GetChild("anasayfabutton")
			self.anasayfa.SetEvent(ui.__mem_func__(self.AnaSayfa))
			self.myitem = self.GetChild("itemlerimbutton")
			self.myitem.SetEvent(ui.__mem_func__(self.MyItems))
			self.GetChild("Money_Slot").SetEvent(ui.__mem_func__(self.ParaAyarlari))
			self.toolTip = uiToolTip.ItemToolTip()
			self.itemler.InsertItem(5, 149, "Muharebe Kilici +9", "250.000.000", "Fatihbab34", "test")
			self.itemler.InsertItem(5, 159, "Hortlak Kilici +5", "100.000.000", "Fatihbab34", "test")
			self.itemler.InsertItem(5, 279, "Sirius Kilici +9", "100.000", "Fatihbab34", "test")
			self.itemler.InsertItem(5, 189, "Zehir Kilici +1", "900.000.000", "Fatihbab34", "test")
			#self.itemler.InsertItem(5, 159, "Hortlak Kilici +5", "100.000.000", "Fatihbab34", "test")
			
		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
		
		self.toolTip = uiToolTip.ItemToolTip()
		self.isLoaded = TRUE

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Hide()
		self.ClearDictionary()
		
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.__Initialize()
		
		if self.IsShow():
			self.Close()
		self.SetTop()
		
		self.Show()
		
	def ParaAyarlari(self):
		riotInfo.ALISVERIS['islem'] = "MoneyAyarlari"
		event.QuestButtonClick(riotInfo.ALISVERIS['pythontolua'])
		
	def AnaSayfa(self):
		self.itemlist.ClearItem()
		for i in range(len(riotInfo.ALISVERIS['itemler'])):
			yap = riotInfo.ALISVERIS['itemler'][i]
			self.itemlist.InsertItem(1, yap[2], yap[0], yap[3], yap[1], "#" + yap[4] + "#" + yap[5] + "#" + yap[6] + "#" + yap[7] + "#" + yap[8] + "#" + yap[9] + "#" + yap[10] + "#" + yap[11] + "#" + yap[12] + "#" + yap[13] + "#" + yap[14] + "#" + yap[15] + "#" + yap[16] + "#" + yap[17] + "#" + yap[18] + "#" + yap[19] + "#" + yap[20] + "#" + yap[21] + "#" + yap[22] + "#" + yap[23] + "#")
		
	def MyItems(self):
		self.itemlist.ClearItem()
		for i in range(len(riotInfo.ALISVERIS['myitems'])):
			yap = riotInfo.ALISVERIS['myitems'][i]
			self.itemlist.InsertItemMy(1, yap[2], yap[0], yap[3], yap[1], "#" + yap[4] + "#" + yap[5] + "#" + yap[6] + "#" + yap[7] + "#" + yap[8] + "#" + yap[9] + "#" + yap[10] + "#" + yap[11] + "#" + yap[12] + "#" + yap[13] + "#" + yap[14] + "#" + yap[15] + "#" + yap[16] + "#" + yap[17] + "#" + yap[18] + "#" + yap[19] + "#" + yap[20] + "#" + yap[21] + "#" + yap[22] + "#" + yap[23] + "#")
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE