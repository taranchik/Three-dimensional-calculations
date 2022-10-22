import csv
import xlsxwriter


def csv_reader(path):
    file = open(path)

    type(file)
    csvreader = csv.reader(file)

    rows = []

    for row in csvreader:
        rows.append(row)

    return rows


def xlsx_writer(data):
    workbook = xlsxwriter.Workbook('3mL.xlsx')
    worksheet = workbook.add_worksheet()

    for j in range(len(data)):
        for i in range(len(data[j])):
            worksheet.write(j, i, data[j][i])

    workbook.close()


xlsx_writer(csv_reader('./src/csv/3mL.csv'))
