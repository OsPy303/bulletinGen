"""
* Lire les fichiers excels dans un dossier en supposant que
* Ce sont des notes des eleve d'une classe separé par matiere
"""
import pandas as pd
import os
import fnmatch

class ExcelToDict:
	def __init__(self, fileName, coefficient):
		# <fileName> : est un dossier ou liste des fichier excel
		self.fileName = fileName
		self.noteDataFrame = None
		self.coefficient = coefficient
		# Liste des fichier dans le dossier
		self.listFile = self.getFilesName() if self.fileName is not list() else self.fileName
		self.setDataframe()
		# Stocker les colonnes
		self.column = self.noteDataFrame.columns
		# lire les index
		self.index = self.noteDataFrame.index
		print(self.noteDataFrame)

	def getFilesName(self):
		"""
			Renvoie les nom des fichiers dans les dossier
			Supposant que le dossier ne contient que des
			notes des eleve d'une classe dans des ficchiers
			excel separé par matiere
		"""
		listFile = list()
		with os.scandir(self.fileName) as dirContent:
			for content in dirContent:
				 if content.is_file() and fnmatch.fnmatch((fName := content.name), '*.xlsx'):
				 	listFile.append(self.fileName +'/' + fName)
		listFile.sort()

		return listFile

	def setDataframe(self):
		"""
			lis tous les fichiers fichier excel et les
			fusionner dans une seule dataframe
		"""
		listdDataframe = [pd.read_excel(self.listFile[0], usecols=[0, 1, 2])]

		for excelFile in self.listFile[1:]:
			# On extrait seulement la colonne contenat les notes
			dataframe = pd.read_excel(excelFile, usecols=[2])
			listdDataframe.append(dataframe)

		# On fusionne les dataframes
		combinedDataframe = pd.concat(listdDataframe, axis=1)

		# Calculer la totale des notes
		# Ajouter une nouvelle colonne contenant la totale
		combinedDataframe['Total'] = combinedDataframe[combinedDataframe.columns[2:]].sum(axis=1)

		self.noteDataFrame = combinedDataframe
		self.calculateMeans()

	def calculateMeans(self):
		# Calcule la moyenne de tous les eleve sur la liste
		# et cree une nouvell colonne <Moyenne>
		self.noteDataFrame["Moyenne"] = self.noteDataFrame["Total"].div(self.coefficient).round(2)

		# Ranger par ordre de merite
		self.noteDataFrame.sort_values(by=['Moyenne'], ascending=False, inplace=True)

	def getOneRow(self, index):
		#Retourne une ligne dans le dataframe a pertir du numero d'index donnee 
		
		return self.noteDataFrame.iloc[index]

	def getComlumn(self):
		return self.column

	def getIndex(self):
		return self.index