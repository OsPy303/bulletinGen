"""
	Generer une fichier HTML à partir d'un ExcelToDataFrame
"""
import pdfkit
from utils.exceltodataframe import ExcelToDataFrame
import pandas as pd

class DataFrameToHtml:
	def __init__(self, data):
		self.data = data
		self.htmlString = "<!DOCTYPE html>\n\
							<html>\n\
							<head>\n\
								<title></title>\n\
								<meta charset=\"utf-8\">\n\
								<style>\
								div, table, th, td{\n\
								 border: 1px solid black}\n\
								</style>\
							</head>\n\
							<body>"

	def setHtml(self):
		for index in range(len(self.data.getIndex())):
			self.htmlString += "<div>\n\
								<table>\n\
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
			self.htmlString += "</table>\n</div>\n"



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