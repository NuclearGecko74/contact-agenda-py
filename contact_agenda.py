import pandas as pd
import os
from contact import Contact
from prettytable import PrettyTable

class ContactAgenda:
    def __init__(self, filename="contacts"):
        self.file = filename + ".csv"
        self.columns = ["Name", "Phone", "Email"]
        self.contacts = []

        self.df = self._load_data()

        self._table = PrettyTable()
        self._table.field_names = self.columns

        self._save_data()

    def add_contact(self, name, phone, email):
        if not name or not phone or not email:
            print("All fields are required.")
            return

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Contact '{name}' already exists.")
                return

        new_contact = Contact(name, phone, email)
        contact_dict = new_contact.to_dict()

        new_df = pd.DataFrame([contact_dict], columns=self.columns)
        self.df = pd.concat([self.df, new_df], ignore_index=True)
        self.df.to_csv(self.file, index=False)

        self.contacts.append(new_contact)
        self._table.add_row(contact_dict.values())

    def list_contacts(self):
        print(self._table)

    def search_contact(self, name):
        table = PrettyTable()
        table.field_names = self.columns
        found = False

        for contact in self.contacts:
            contact_name = contact.to_dict()["Name"]
            if name.lower() in contact_name.lower():
                table.add_row(contact.to_dict().values())
                found = True

        if found:
            print(table)
        else:
            print(f"No contacts found for '{name}'.")

    def _load_data(self):
        if not os.path.exists(self.file):
            return pd.DataFrame(columns=self.columns)
        else:
            return pd.read_csv(self.file)

    def _save_data(self):
        for row in self.df.to_dict('records'):
            name = row["Name"]
            phone = row["Phone"]
            email = row["Email"]
            contact = Contact(name, phone, email)

            self.contacts.append(contact)
            self._table.add_row([name, phone, email])
