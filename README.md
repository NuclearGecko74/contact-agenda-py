# 📒 Contact Agenda

A command-line contact manager built with Python. Stores contacts in a CSV file and lets you add, list, and search them from a simple interactive menu.

## Features

- Add contacts with name, phone, and email
- List all contacts in a formatted table
- Search contacts by name (partial match supported)
- Persistent storage using CSV files
- Duplicate detection by name

## Requirements

- Python 3.8+
- Dependencies:

```bash
pip install pandas prettytable
```

## Project Structure

```
contact-agenda/
├── main.py              # Entry point
├── menu.py              # Interactive CLI menu
├── contact.py           # Contact data model
├── contact_agenda.py    # Core logic (add, list, search, load/save)
└── .gitignore
```

## Usage

```bash
python main.py
```

On startup, you will be asked for a filename. The app will create or open a `.csv` file with that name to store your contacts.

```
Enter the name of the file to open or create: my_contacts

====================
   Contact Agenda
====================
1. Add contact
2. List contacts
3. Search contact
4. Exit
====================
Choose an option:
```

## Example

```
Choose an option: 1
Name: Ada Lovelace
Phone: 555-0101
Email: ada@example.com

Choose an option: 2
+──────────────+──────────+───────────────────+
| Name         | Phone    | Email             |
+──────────────+──────────+───────────────────+
| Ada Lovelace | 555-0101 | ada@example.com   |
+──────────────+──────────+───────────────────+
```

## Author

[NuclearGecko74](https://github.com/NuclearGecko74)
