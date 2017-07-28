import xlrd
from COM_work import COM_worker
from GSM_Connection import GSM
class Parsing_xls():

    def parse(self):
        rb = xlrd.open_workbook('C:/Buyak/Projects/VZEPAddr/Могилевская область_2017-12-06 21-30-00.xls')
        sheet = rb.sheet_by_index(0)
        dict = {}
        s = set()
        row = sheet.row_values(0)
        for c_el in range(row.__len__()):
            if row[c_el] == "номер для дозвона к УСПД":
                dict["Телефон"] = c_el
            elif row[c_el] == "Тип УСПД":
                dict["УСПД"] = c_el

        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            if row[dict["УСПД"]] == "ЕА8086" or row[dict["УСПД"]] == "EA8086": #для русской и английской записи строки EA8086
                s.add(row[dict["Телефон"]])
        return s
