import csv
from pprint import pprint
import re

def regular(filename):

    contacts_list = []
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        next(rows)
        pprint(contacts_list)

        try:

            for row in rows:

                lastname, firstname, surname = row[0].split(" ")
                if len(row) > 2:
                    surname = row[2]

        except StopIteration:
            print("Файл CSV исчерпан.")

        finally:
                phone = row[5]
                if phone:
                    phone = phone.replace(" ", "")
                    phone = phone.replace("(", "")
                    phone = phone.replace(")", "")
                    phone = phone.replace("-", "")

                match = re.match(r"(\d{10})", phone)

                if match:
                    phone = f"+7({match.group(1)[0:3]})({match.group(1)[3:6]})-({match.group(1)[6:8]})-({match.group(1)[8:10]}))"
                else:
                    match = re.match(r"(\d{11})", phone)
                    if match:
                        phone = f"+7({match.group(1)[1:4]})({match.group(1)[4:7]})-({match.group(1)[7:9]})-({match.group(1)[9:11]}))"
                if "доб" in phone:
                    phone = phone.split("доб")[0] + "доб." + phone.split("доб")[1]

                new = [lastname, firstname, surname, row[3], row[4], phone, row[6]]
                contacts_list.append(new)

        unique = {}
        for rec in unique:
            key = f"{rec[0]} {rec[1]}"
            if key in unique:

                if rec[5]:
                    unique[key][5] = rec[5]
                if rec[6]:
                    unique[key][6] = rec[6]

            else:
                unique[key] = rec

        result = list(unique.values())
        return result

