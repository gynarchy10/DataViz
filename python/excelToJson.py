import xlrd
import json
import os
import os.path

# The name of the excel file to use.
# It is assumed that this file is in the /excel directory
excel_filename = "20150613.DataVizData.xlsx"

# The columns that have data.
# It is assumed that the first row is a header, and the remaining rows contain data.
include_cols = [2,3,4]

root_dir = os.path.dirname(os.getcwd())
excel_filepath = os.path.join(root_dir, "excel/{0}".format(excel_filename))

book = xlrd.open_workbook(excel_filepath)
sheet = book.sheet_by_index(0)
print "Number of sheets: {0}".format(book.nsheets)
print "Sheet Name: {0}".format(sheet.name)
print "Rows: {0} Cols: {1}".format(sheet.ncols, sheet.nrows)

dict = {}
dict["groups"] = [[]]
dict["columns"] = []

header_row = sheet.row(0)
for i in include_cols:
    cell = header_row[i]
    dict["groups"][0].append(cell.value)

print "Parsing columns..."
for i in range(0, sheet.ncols):
    if i in include_cols:
        col = sheet.col(i)
        col_data = []

        capture_header = True
        for cell in col:
            if capture_header:
                col_data.append(cell.value)
                capture_header = False
            else:
                col_data.append(float(cell.value))

        dict["columns"].append(col_data)
        print col_data

json_result = json.dumps(dict);
print "Writing json..."
print json_result
f = open(os.path.join(root_dir, 'api/c3Data.json'), 'w')
f.write(json_result)
f.close()
