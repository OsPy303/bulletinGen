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

class ExcelToDict:
	def __init__(self, fileName):
		# <fileName> : le nom ou le chemain du fichier excel
		self.fileName = fileName
		# Lire le fichier excel avec pandas
		self.noteDataFrame = pd.read_excel(self.fileName)
		# Stocker les colonnes
		self.column = self.noteDataFrame.columns
		# lire les index
		self.index = self.noteDataFrame.index

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