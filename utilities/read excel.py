from openpyxl import workbook,load_workbook
wb = load_workbook("C:\\Users\\uif48567\\PycharmProjects\\PythonFramework\\testdata\\tdataexcel.xlsx")
sh = wb.active
print(sh['A2'].value)