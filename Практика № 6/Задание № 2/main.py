import json
import sqlite3


con = sqlite3.connect("data.db")
cur = con.execute("CREATE TABLE tasks(userId, taskID, completed)")

with open("data2.json") as file:
    tasks = json.load(file)

for task in tasks:
    if "userId" not in task:
        task["userId"] = None

cur.executemany("INSERT INTO tasks VALUES (:userId, :taskID, :completed)", tasks)
con.commit()

cur.execute("SELECT * FROM tasks")
print(*cur.fetchall(), sep="\n")

con.close()