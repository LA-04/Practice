import openpyxl

wb = openpyxl.reader.excel.load_workbook("nmrv.xlsx")
print(wb.sheetnames)
