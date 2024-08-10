from PyQt5.QtWidgets import QMessageBox
import sqlite3

class DatabaseManager:
    def __init__(self, db_file="database.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS person_crud(
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                surname TEXT NOT NULL
                                )""")
        self.conn.commit()

    def insert_person(self, person):
        try:
            self.cursor.execute("SELECT * FROM person_crud WHERE id = ?", (person.id,))
            existing_person = self.cursor.fetchone()
            if existing_person:
                QMessageBox.warning(None, "Hata", "Bu id numarası zaten var")
            else:
                self.cursor.execute("INSERT INTO person_crud (id, name, surname) VALUES (?, ?, ?)", (person.id, person.name, person.surname))
                self.conn.commit()
                return True
        except ValueError:
            QMessageBox.warning(None, "Hata", "ID alanına geçerli bir sayı girin.")
            return False

    def update_person(self, person):
        try:
            self.cursor.execute("UPDATE person_crud SET name=?, surname=? WHERE id=?", (person.name, person.surname, person.id))
            self.conn.commit()
            return True
        except ValueError:
            QMessageBox.warning(None, "Hata", "ID alanına geçerli bir sayı girin.")
            return False

    def delete_person(self, id):
        self.cursor.execute("DELETE FROM person_crud WHERE id=?", (id,))
        self.conn.commit()