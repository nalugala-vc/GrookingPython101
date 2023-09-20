import pandas as pd
import functions
#reading the xlsx file
test_file = pd.ExcelFile("Test Files.xlsx")

#getting the sheets 3b and 3c
class_sheets =test_file.sheet_names
#reading the sheets and print content
for class_sheet in class_sheets:
    class_list = pd.read_excel(test_file, class_sheet)
    print(f"\nReading sheet: {class_sheet}")
    # print(class_list)

    functions.generate_emails(class_list,class_sheet)