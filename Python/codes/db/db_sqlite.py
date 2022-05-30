import sqlite3 as sql

connection = sql.connect("mydata.db")
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS persons(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
)
"""
)

cursor.execute(
    """
INSERT INTO persons VALUES
(1, 'ANDY', 'Smith', 20)
(2, 'Manu', 'Singh', 30)
(3, 'Juli', 'Smith', 22)
"""
)

cursor.execute(
    """
SELECT * FROM persons WHERE last_name = 'Smith'
"""
)

rows = cursor.fetchall()
print(rows)


class Person:
    def __init__(self, id_num=-1, first="", last="", age=-1):
        self.first = first
        self.age = age
        self.last = last
        self.id_num = id_num

    def load_person(self, id):
        cursor.execute(
            """
            SELECT * FROM persons WHERE id = {}    
            """.format(
                id
            )
        )

        result = cursor.fetchone()

        self.id_num = id
        self.age = result[2]
        self.first = result[0]
        self.last = result[1]


connection.commit()
connection.close()
