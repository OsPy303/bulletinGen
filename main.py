import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from utils.template import DataFrameToHtml
from utils.exceltodataframe import ExcelToDataFrame

class Store(Gtk.ListStore):
	# Crée un liste store model à patir des colonne
	# d'Une dataframe 
	def __init__(self, dataHeader):
		Gtk.ListStore.__init__(self)

		self.dataHeader = dataHeader
		self.listTypeHeader = [str, str]
		for i in range(len(self.dataHeader[2:])):
			self.listTypeHeader.append(str)

		print(self.listTypeHeader)

		self.column_types = self.listTypeHeader
		self.set_column_types(self.column_types)

class ListView(Gtk.Box):
	# Create listview from ExcelToDataFrame oject
	def __init__(self, data):
		Gtk.Box.__init__(self, spacing=6)

		self.data = data

		#Cree un liststore Model
		self.notesListStore = Store(self.data.getComlumn())
		print('>>>',self.notesListStore.column_types)

		# Add data on list model
		for i in range(self.data.getDataFrame().shape[0]):
			row = self.data.getDataFrame().iloc[i]
			print(row)
			index = [x for x in row.index]
			listToModel = list()
			for elt in index:
				#listToModel.append(row[elt] if type(row[elt]) is str else float(row[elt]))
				listToModel.append(str(row[elt]))
			print(listToModel)
			self.notesListStore.append(listToModel)

		# Create TreeView with model
		self.tree = Gtk.TreeView(self.notesListStore)

		# Ajouter les en-tete de colonne
		columnHead = self.data.getComlumn()
		for i, title in enumerate(columnHead):
			renderer = Gtk.CellRendererText()
			col = Gtk.TreeViewColumn(title, renderer, text=i)
			self.tree.append_column(col)

		listNoteContainer = Gtk.ScrolledWindow()
		listNoteContainer.set_vexpand(True)
		listNoteContainer.add(self.tree)

		self.pack_start(listNoteContainer, True, True, 0)


class EntriesContainer(Gtk.Box):
	def __init__(self, parentDialog):
		Gtk.Box.__init__(self, spacing=6)

		self.parentDialog = parentDialog
		self.calculatedData = None

		self.classLabel = Gtk.Label(label='Classe')
		self.classEntry = Gtk.Entry()

		self.chooseFolder = Gtk.Button(label='Choisir un dossier')
		self.chooseFolder.connect('clicked', self.fileChooser)

		self.pack_start(self.classLabel, True, True, 0)
		self.pack_start(self.classEntry, True, True, 0)
		self.pack_start(self.chooseFolder, True, True, 0)

	def fileChooser(self, widget):
		dialog = Gtk.FileChooserDialog(title="Choisir un dossier",
				parent=self.parentDialog,
				action=Gtk.FileChooserAction.SELECT_FOLDER)
		dialog.add_buttons(
			'Annuler', Gtk.ResponseType.CANCEL,
			'Choisir', Gtk.ResponseType.OK)

		folder = dialog.run()
		if folder == Gtk.ResponseType.OK:
			self.calculatedData = ExcelToDataFrame(dialog.get_filename())
			dialog.destroy()
			listView = ListView(self.calculatedData)
			fen = Gtk.Window(title='Liste', border_width=8)
			fen.set_default_size(1000, 600)
			fen.connect('delete-event', Gtk.main_quit)
			fen.add(listView)
			fen.show_all()
			Gtk.main()

		elif folder == Gtk.ResponseType.CANCEL:
			dialog.destroy()



class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title='Calcul Notes')
		self.connect('delete-event', Gtk.main_quit)
		self.set_border_width(8)

		# Main contenair
		self.mainContainer = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)

		# Les entrer...
		self.entry = EntriesContainer(self)
		self.mainContainer.pack_start(self.entry, True, True, 0)

		self.add(self.mainContainer)
		self.show_all()

window = MainWindow()
Gtk.main()