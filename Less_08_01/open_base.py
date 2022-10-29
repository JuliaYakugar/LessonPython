import csv
import json
from pathlib import Path

def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee

def write_csv(employee: list):
    with open(Path.cwd() / 'database.csv', 'a', encoding='utf-8') as data:
	    data.write(employee)

def new_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as data:
        for employee in employees:
	        data.write((f"{employee['id']},{employee['last_name']},{employee['first_name']},{employee['position']},{employee['phone_number']},{employee['salary']}\n"))


def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee

def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')