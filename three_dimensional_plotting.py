
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import xlrd


def threedim_plot(title, dataY):
    groups = ("start", "3 month", "6 month")
    colors = ("red", "green", "blue")

    fig = plt.figure(figsize=(16.0, 8.0))
    ax = plt.axes(projection='3d')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for data, color, group in zip(dataY, colors, groups):
        ax.scatter(0, data, 0, alpha=0.8, c=color,
                   edgecolors='none', s=30, label=group)

    ax.set_title(title)
    ax.legend(loc=1)

    ax.view_init(30, 0)

    # plt.savefig('./src/img/' + title + '.png', bbox_inches='tight')
    plt.show()


def read_xlsx(path):
    # Open the Workbook
    workbook = xlrd.open_workbook(path)

    # Open the worksheet
    worksheet = workbook.sheet_by_index(0)

    # Define variables
    thees = {}
    tooth = None
    left_tooth_counter = 7
    right_tooth_counter = 1

    for i in range(1, 127):
        # Read the cell values
        if ((i - 1) % 9 == 0):
            if (left_tooth_counter == 0):
                tooth = str(right_tooth_counter) + 'P'
                thees[tooth] = []
                right_tooth_counter += 1
            else:
                tooth = str(left_tooth_counter) + 'L'
                thees[tooth] = []
                left_tooth_counter -= 1

        thees[tooth].append(float(worksheet.cell_value(i, 6)))

    return thees


thees_frames_start = read_xlsx("./src/xlsx/Kopia-pliku-rozgrupowanie.xlsx")
thees_frames_three_months = read_xlsx("./src/xlsx/3mU.xlsx")
thees_frames_six_months = read_xlsx("./src/xlsx/6mU.xlsx")

for key, _ in thees_frames_start.items():
    threedim_plot('Upper Jaw - ' + key,
                  (thees_frames_start[key], thees_frames_three_months[key], thees_frames_six_months[key]))
