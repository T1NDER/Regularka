from regularka import regular
import csv
from pprint import pprint

filename = "FILE.csv"

result = regular(filename)
pprint(result)

with open(filename, "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result)



