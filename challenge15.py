import webbrowser
import csv
from pathlib import Path

def read_csv(path):
    csv_content = []
    with open(path) as file:
        csvreader = csv.reader(file, delimiter=",")
        for row in csvreader:
            csv_content.append(row)
    return csv_content


def read_html(path):
    with open(path) as file:
        return file.read()


def process(csv, html):
    for x in range(1,6):
        html = html.replace(f"name{x}", csv[x-1][2])
    return html

def write_html(path):
    with open(path) as file:
        return file.write(path)

if __name__ == "__main__":
    csv_file = Path("south.csv")
    html_file = Path("south.html")
    csv_data = read_csv(path=csv_file)
    html_data = read_html(path=html_file)
    print(process(csv=csv_data, html=html_data))
    webbrowser.open("south.html")
