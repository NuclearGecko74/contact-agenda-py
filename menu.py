from contact_agenda import ContactAgenda

def show_menu():
    print("\n====================")
    print("   Contact Agenda")
    print("====================")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Exit")
    print("====================")


class Menu:
    def __init__(self):
        filename = input("Enter the name of the file to open or create: ")
        self.agenda = ContactAgenda(filename)

    def run(self):
        while True:
            show_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                self.agenda.add_contact(name, phone, email)

            elif choice == "2":
                self.agenda.list_contacts()

            elif choice == "3":
                name = input("Search by name: ")
                self.agenda.search_contact(name)

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option, try again.")