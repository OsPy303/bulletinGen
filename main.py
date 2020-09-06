from utils.template import DataFrameToHtml
from utils.exceltodataframe import ExcelToDataFrame

data = ExcelToDataFrame("note_premiere_a1", 21)
#print(data.getFilesName())
#data.setDataframe()
html = DataFrameToHtml(data)
html.setHtml()
html.saveHtml()
html.savePdf()