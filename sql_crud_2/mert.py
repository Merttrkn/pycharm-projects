import sqlite3

db_file = "person.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    last_name TEXT NOT NULL
                    )""")

class Database:
    def __init__(self,table_name):
        self.table_name = table_name

    def create (self,first_name,last_name):
        with sqlite3.connect(db_file) as conn :
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {self.table_name} (name , last_name)VALUES(?,?)",(first_name,last_name))
            conn.commit()

    def read (self,person_id):
        with sqlite3.connect(db_file)as conn :
            cursor = conn.cursor()
            cursor.execute(f"SELECT*FROM {self.table_name} WHERE id = ?",(person_id,))
            person = cursor.fetchone()
            if person:
                person_id ,first_name,last_name = person
                print(f"Kişi id:{person_id}")
                print(f"Adı:{first_name}")
                print(f"Soyadı:{last_name}")

            else:
                print("Kişi bulunamadı")

    def update(self,person_id ,first_name, last_name):
        with sqlite3.connect(db_file) as conn :
            cursor = conn.cursor()
            cursor.execute(f"UPDATE {self.table_name} SET name=? ,last_name=? WHERE id = ?",(first_name,last_name,person_id))
            conn.commit()

    def delete(self,person_id):
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (person_id,))
            conn.commit()

class PersonDatabase(Database):
    def __init__(self):
        super().__init__("person")

if __name__ == "__main__":
    database = PersonDatabase()

    database.create("Mert","Türkan")
    database.create("Berat", "Ünlü")
    database.create("Arda","Sarı")

    print("-----Kişileri oku-----")
    database.read(1)
    database.read(2)
    database.read(3)

    database.update(1,"Metehan ","Kilci")

    database.delete(2)






