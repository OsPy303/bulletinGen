from utils.template import CreateHtml
from utils.exceltodict import ExcelToDict

data = ExcelToDict("terminale_D.xlsx")
dic = data.getAllNoteDico()
html = CreateHtml(dic)
html.setHtml()
html.saveHtml()
html.savePdf()