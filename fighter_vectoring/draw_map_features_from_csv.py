import csv


def read_coord_from_csv(file_name):
    coord_list = []
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            x = int(row[0].strip("("))
            y = int(row[1].strip(")"))
            coord = (x, y)
            print(coord)
            coord_list.append(coord)
    return coord_list
