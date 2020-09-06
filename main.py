import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from utils.template import DataFrameToHtml
from utils.exceltodataframe import ExcelToDataFrame

class EntriesContainer(Gtk.Box):
	def __init__(self, parentDialog):
		Gtk.Box.__init__(self, spacing=6)

		self.parentDialog = parentDialog

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
			data = ExcelToDataFrame(dialog.get_filename())

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