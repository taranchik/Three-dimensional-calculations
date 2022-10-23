import csv
import xlsxwriter
import sys


def csv_reader(path):
    file = open(path)

    type(file)
    csvreader = csv.reader(file)

    rows = []

    for row in csvreader:
        rows.append(row)

    return rows


def xlsx_writer(data):
    workbook = xlsxwriter.Workbook('./src/xlsx/' + sys.argv[1] + '.xlsx')
    worksheet = workbook.add_worksheet()

    # Filling main talbe
    for j in range(len(data)):
        for i in range(len(data[j])):
            worksheet.write(j, i, data[j][i])

    row = 3
    column = 14
    tooth = None

    # Filling right-side table
    for j in range(1, 127):
        row += 1
        worksheet.write(row, column, data[j][6])

        if (j % 9 == 0):
            row = 3
            if (column > 20):
                tooth = str(column - 20) + 'P'
            else:
                tooth = str((column - 21) * -1) + 'L'
            worksheet.write(3, column, tooth)
            column += 1

        if (j < 10):
            worksheet.write(j + 3, 13, j)

    workbook.close()


def main():
    xlsx_writer(csv_reader('./src/csv/' + sys.argv[1] + '.csv'))


if __name__ == "__main__":
    main()
