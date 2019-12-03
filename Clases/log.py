import os

class Log:
	def __init__(self, path = "C:\Users\Administrador\Desktop\pooo\poo\poo"):
		self.path = path

	def Log():
		return self

	def Add(sLog):
		self.CreateDirectory();
		nombre = self.GetNameFile()
		cadena = ""

		cadena += datetime.now() + sLog + "\n"

		sw = new StreamWriter(self.path + "/" + nombre)
		sw.write(cadena)
		sw.close()

	def GetNameFile():
		nombre = ""

		now = datetime.now()
		nombre = "log_" + now.year + "_" + now.month + "_" + now.day + ".txt"

		return nombre

	def CreateDirectory():
		try:
			if not os.path.exists(self.path):
		    	os.mkdir(self.path)
		except OSError:
			throw new Exception("No se pudo crear el directorio")
