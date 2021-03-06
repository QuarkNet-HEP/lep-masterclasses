import csv
import os.path as path

# Check that the files listed in the csv are
# present in the images dir

with open('Z_exercise.csv', 'r') as z_csv:
    csv_reader = csv.reader(z_csv)
    next(csv_reader, None)
    for row in csv_reader:
        try:
            assert(path.isfile(f'./images/{row[0]}'))
        except AssertionError:
            print(f'{row[0]},{row[1]} not found')
 
with open('W_exercise.csv', 'r') as w_csv:
    csv_reader = csv.reader(w_csv)
    next(csv_reader, None)
    for row in csv_reader:
        try:
            assert(path.isfile(f'./images/{row[0]}'))
        except AssertionError:
            print(f'{row[0]},{row[1]} not found')
