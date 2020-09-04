"""
	Generer une fichier HTML à partir d'un dictionnaire de dictionnaire
"""
import pdfkit

class CreateHtml:
	def __init__(self, data):
		self.data = data
		self.htmlString = "<!DOCTYPE html>\n\
							<html>\n\
							<head>\n\
								<title></title>\n\
								<meta charset=\"utf-8\">\n\
							</head>\n\
							<body>"

	def setHtml(self):
		"""
			Cree dynamiquement un synthaxe html à partire des données 
			du dictionnaire
		"""
		self.htmlString += "<ol>\n"
		for key in self.data.keys():
			tempDict = self.data[key]
			self.htmlString += "<li>\n"
			self.htmlString += "<ul>\n"

			for notes in tempDict.keys():
				print(tempDict[notes])
				self.htmlString += f"<li>{str(notes)} --> {str(tempDict[notes])}</li>\n"

			self.htmlString += "</ul>\n"
			self.htmlString += "</li>"

		self.htmlString += "</ol>\n"
		self.htmlString += "</body>\n\
							</html>"

	def saveHtml(self):
		"""
			Enregistrer le synthaxe dans un fichier html
		"""
		with open("test.html", "w") as toHtml:
			toHtml.write(self.htmlString)

	def savePdf(self):
		"""
			Crée un fichier pdf à partir du fichier html enregistré
		"""
		option = {
		'encoding':'UTF-8'
		}
		pdfkit.from_file("test.html", "out.pdf", options=option)