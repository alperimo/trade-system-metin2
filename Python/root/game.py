	def __ServerCommand_Build(self):
		serverCommandList={
			"LuaToPython"		: self.LuaToPythona,
			"PythonToLua"		: self.PythonToLua,
			"PythonIslem"		: self.PythonIslem,
		}
		
	#----------------------------------------------------#
	
	""" """
	
	"En baþa"
	y = 0
	import riotInfo
	
	""" """
	
	def LuaToPythona(self, LuaToPython):
		global y
		g = LuaToPython
		if g == "alisverisopen":
			import uialisveris
			uialisveris.AlisverisSystem().Open()
		elif g.find("itemler") != -1:
			yap = LuaToPython.split("#")
			item.SelectItem(yap[2])
			ad = item.GetItemName()
			riotInfo.ALISVERIS['itemler'][y] = [ad, yap[1], yap[2], yap[3], yap[4], yap[5], yap[6], yap[7], yap[8], yap[9], yap[10], yap[11], yap[12], yap[13], yap[14], yap[15], yap[16], yap[16], yap[17], yap[18], yap[19], yap[20], yap[21], yap[22], yap[23]]
			self.interface.Alisveris.GetChild("ItemList").InsertItem(1, yap[2], ad, yap[3], yap[1], "#" + yap[4] + "#" + yap[5] +  "#" + yap[6] + "#" + yap[7] + "#" + yap[8] + "#" + yap[9] + "#" + "alisverisbyfatihbab34" + "#" + yap[10] + "#" + yap[11] + "#" + yap[12] + "#" + yap[13] + "#" + yap[14] + "#" + yap[15] + "#" + yap[16] + "#" + yap[16] + "#" + yap[17] + "#" + yap[18] + "#" + yap[19] + "#" + yap[20] + "#" + yap[21] + "#" + yap[22] + "#" + yap[23] + "#")
			y += 1
		elif g.find("myitems") != -1:
			yap = LuaToPython.split("#")
			item.SelectItem(yap[2])
			ad = item.GetItemName()
			riotInfo.ALISVERIS['myitems'][y] = [ad, yap[1], yap[2], yap[3], yap[4], yap[5], yap[6], yap[7], yap[8], yap[9], yap[10], yap[11], yap[12], yap[13], yap[14], yap[15], yap[16], yap[16], yap[17], yap[18], yap[19], yap[20], yap[21], yap[22], yap[23]]
			
	def PythonToLua(self, id):
		riotInfo.ALISVERIS['pythontolua'] = int(id)
		
	def PythonIslem(self):
		net.SendQuestInputStringPacket(riotInfo.ALISVERIS['islem'])