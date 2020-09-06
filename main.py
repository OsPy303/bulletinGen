from utils.template import CreateHtml
from utils.exceltodict import ExcelToDict

data = ExcelToDict("note_premiere_a1", 21)
#print(data.getFilesName())
#data.setDataframe()
html = CreateHtml(data)
html.setHtml()
html.saveHtml()
html.savePdf()