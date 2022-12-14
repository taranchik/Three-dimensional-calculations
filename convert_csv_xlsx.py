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

    cell_format_border = workbook.add_format()
    cell_format_border_bold = workbook.add_format()
    cell_format_border.set_border()
    cell_format_border_bold.set_border()
    cell_format_border_bold.set_bold()
    worksheet.write(row, 13, '', cell_format_border)

    # Condition resolves whether there is a header in csv
    if data[0][0] == "Element":
        data_start_row = 1
    else:
        data_start_row = 0

    row_number_counter = 1

    # Print right-side table
    for j in range(data_start_row, len(data)):
        row += 1
        # print data
        worksheet.write(row, column, data[j][6], cell_format_border)

        # print header and move to next column
        if (row_number_counter % 9 == 0):
            row = 3
            if (column > 20):
                tooth = str(column - 20) + 'P'
            else:
                tooth = str((column - 21) * -1) + 'L'
            worksheet.write(3, column, tooth, cell_format_border_bold)
            column += 1

        # print row number
        if (j != 0 and j < 10):
            worksheet.write(j + 3, 13,
                            j, cell_format_border_bold)

        row_number_counter += 1

    workbook.close()


def main():
    xlsx_writer(csv_reader('./src/csv/' + sys.argv[1] + '.csv'))


if __name__ == "__main__":
    main()
