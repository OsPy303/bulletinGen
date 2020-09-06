"""
	Generer une fichier HTML à partir d'un dictionnaire de dictionnaire
"""
import pdfkit
from utils.exceltodict import ExcelToDict
import pandas as pd

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

	def setHtml1(self):
		for index in range(len(self.data.getIndex())):
			self.htmlString += "<table>\n\
								<tr>\n\
								<th>Discipline</th>\n\
								<th>Notes</th>\n\
								</tr>\n"
			row = self.data.getOneRow(index)

			for elt in row.index[2:]:
				self.htmlString += f"<tr>\n\
									<td>{elt}</td>\n\
									<td>{row.loc[elt]}</td>\n\
									</tr>\n"
			self.htmlString += "</table>\n"



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