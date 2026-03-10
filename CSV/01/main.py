import csv

with open("CSV/01/country_full.csv", "r",encoding="utf-8") as file:
    for row in csv.DictReader(file):
        #print(row["name"],row["region"])
        pass


data = [["a.e.nitonde","2000","Auric","Ergeson"],
        ["l.caspari","1998","Lukas","Caspari"]
        ]

with open("CSV/01/username.csv", "a",encoding="utf-8",newline="") as file:
    w = csv.writer(file,delimiter=";")
    w.writerows(data)

