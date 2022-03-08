import uialisveris
	
	def __MakeDialogs(self):
		self.AlisverisWindow = uiAlisveris.AlisverisSystem()
		self.AlisverisWindow.Hide
		
	def Close(self):
		if self.AlisverisWindow:
			self.AlisverisWindow.Destroy()
			
		del self.AlisverisWindow