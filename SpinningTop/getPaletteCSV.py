import csv
import grapefruit

def getPaletteCSV(fname):
    palette = []
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            palette.append(grapefruit.Color.NewFromHtml(row[0]))
    f.close()
    return palette
