import csv
from pprint import pprint
import re


def regular(filename):
    contacts_list = []
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        next(rows)

        for row in rows:
            lastname, firstname = row[0].split(" ", 1)
            surname = row[2] if len(row) > 2 else ""
            phone = row[5].strip() if row[5] else ""
            phone = re.sub(r"[()\- ]", "", phone)

            if re.match(r"^\d{10}$", phone):
                phone = f"+7({phone[:3]})({phone[3:6]})-({phone[6:8]})-({phone[8:10]})"
            elif re.match(r"^\d{11}$", phone):
                phone = f"+7({phone[1:4]})({phone[4:7]})-({phone[7:9]})-({phone[9:11]})"

            if "доб" in phone:
                phone = phone.split("доб")[0] + "доб." + phone.split("доб")[1]

            new = [lastname, firstname, surname, row[3], row[4], phone, row[6]]
            contacts_list.append(new)

    unique = {}
    for contact in contacts_list:
        key = f"{contact[0]} {contact[1]}"
        if key in unique:
            if contact[5]:
                unique[key][5] = contact[5]
            if contact[6]:
                unique[key][6] = contact[6]
        else:
            unique[key] = contact

    result = list(unique.values())
    return result


if __name__ == "__main__":
    filename = "FILE.csv"
    result = regular(filename)
    pprint(result)


    with open("output.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        datawriter.writerows(result)

