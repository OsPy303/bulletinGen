"""
* Ce module lit un fichier excel contenant les notes
* et totales des notes des eleves est genere un  
* dictionaire de dictionnaire de forme:
* {
	0: {
		  'num': 2,
		  'nom': 'ANDRIANARINIVO Joyce Ckadly',
		  'malagasy': 30.0,
		  'histo_geo': 21.5,
		  'anglais': 1.0,
		  'français': 18.0,
		  'physique': 44.0,
		  'mathématiques': 54.0,
		  'philosophie': 18.0,
		  'SVT': 75.0,
		  'total': 260.5
		},
 	1: {
 		  'num': 2,
		  'nom': 'ANDRIANARINIVO Joyce Ckadly',
		  'malagasy': 30.0,
		  'histo_geo': 21.5,
		  'anglais': 1.0,
		  'français': 18.0,
		  'physique': 44.0,
		  'mathématiques': 54.0,
		  'philosophie': 18.0,
		  'SVT': 75.0,
		  'total': 260.5
		},
 	2: {
 		  'num': 2,
		  'nom': 'ANDRIANARINIVO Joyce Ckadly',
		  'malagasy': 30.0,
		  'histo_geo': 21.5,
		  'anglais': 1.0,
		  'français': 18.0,
		  'physique': 44.0,
		  'mathématiques': 54.0,
		  'philosophie': 18.0,
		  'SVT': 75.0,
		  'total': 260.5
		}
  }
"""
import pandas as pd
import os
import fnmatch

class ExcelToDict:
	def __init__(self, fileName, coefficient, isDirectory=False):
		# <fileName> : le nom ou le chemain du fichier excel
		self.fileName = fileName
		self.isDirectory = isDirectory
		self.noteDataFrame = None
		self.coefficient = coefficient

		if self.isDirectory:
			self.listFile = self.getFilesName()
			self.setDataframe()

		else:
			# Lire le fichier excel avec pandas
			self.noteDataFrame = pd.read_excel(self.fileName)
		# Stocker les colonnes
		self.column = self.noteDataFrame.columns
		# lire les index
		self.index = self.noteDataFrame.index
		print(self.noteDataFrame)


	def readNoteSeries(self, pdSeries):
		"""
		Lire le note d'une eleve re renvoie un dictionnaire
		comme: 
		{
		  'num': 2,
		  'nom': 'ANDRIANARINIVO Joyce Ckadly',
		  'malagasy': 30.0,
		  'histo_geo': 21.5,
		  'anglais': 1.0,
		  'français': 18.0,
		  'physique': 44.0,
		  'mathématiques': 54.0,
		  'philosophie': 18.0,
		  'SVT': 75.0,
		  'total': 260.5
		}
		"""
		noteDico = dict()
		for col in self.column:
			noteDico[col] = pdSeries[col]

		return noteDico

	def getAllNoteDico(self):
		"""
		Lire la totalite du dataframe et renvoie la dictionnaire de 
		dictionnaire
		"""
		allNote = dict()
		# parcourir le dataframe
		for i in self.index:
			temp = self.noteDataFrame.iloc[i]
			noteTemp = self.readNoteSeries(temp)
			allNote[i] = noteTemp

		return allNote

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