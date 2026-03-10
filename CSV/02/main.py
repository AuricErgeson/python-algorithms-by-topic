import csv

data= [
    {
        "Name":"Auric",
        "City":"Twinkhof",
        "Age":25
    },
    {
        "Age":26,
        "Name": "Hakim",
        "City":"Islamabad"
    },
    {
        "City":"Tehran",
        "Age": "35",
        "Name":"Ashana"      
    }    
]

with open("CSV/02/friends.csv", "w",encoding="utf-8",newline="") as file:
    w= csv.DictWriter(file,
                      fieldnames=["Name","Age","City"],
                      delimiter=",")
    w.writerows(data)
    
