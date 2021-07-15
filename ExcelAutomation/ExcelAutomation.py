import openpyxl as xl
wb = xl.load_workbook("transactions.xlsx");
sheet = wb["Sheet1"];

for i in range(2,sheet.max_row + 1):
    print(sheet.cell(i, 3).value * 0.9);
    sheet.cell(i, 4).value = sheet.cell(i, 3).value * 0.9;

wb.save("transaction2.xlsx")