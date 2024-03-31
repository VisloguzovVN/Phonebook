
import json

class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, last_name, first_name, middle_name, phone_numbers, email):
        contact = {
            'фамилия': last_name,
            'имя': first_name,
            'отчетсво': middle_name,
            'номер телефона': phone_numbers,
            'электронная почта': email
        }
        self.contacts.append(contact)

    def search_contact(self, query):
        result = []
        for contact in self.contacts:
            if query.lower() in contact['фамилия'].lower() or \
               query.lower() in contact['имя'].lower() or \
               query.lower() in contact['отчество'].lower() or \
               query in contact['номер телефона'] or \
               query.lower() in contact['электронная почта'].lower():
                result.append(contact)
        return result

    def export_contacts(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)

    def import_contacts(self, filename):
        with open(filename, 'r') as file:
            self.contacts = json.load(file)


phonebook = Phonebook()

while True:
    print("\n1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Экспорт контактов")
    print("4. Импорт контактов")
    print("5. Выход")

    choice = input("Введите цифру запроса: ")

    if choice == '1':
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        phone_numbers = input("Введите номера телефонов через запятую: ").split(',')
        email = input("Введите email: ")

        phonebook.add_contact(last_name, first_name, middle_name, phone_numbers, email)

    elif choice == '2':
        query = input("Введите критерий поиска (имя, или фамилия, или номер телефона, или e-mail): ")
        results = phonebook.search_contact(query)
        if results:
            for contact in results:
                print(contact)
        else:
            print("Контакт не найден.")

    elif choice == '3':
        filename = input("Введите название файла для экспорта контактов: ")
        phonebook.export_contacts(filename)
        print("Контакты успешно экспортированы.")

    elif choice == '4':
        filename = input("Введите название файла для импорта контактов: ")
        phonebook.import_contacts(filename)
        print("Контакты успешно импортированы.")

    elif choice == '5':
        print("Выход из программы.")
        break

    else:
        print("Не правильный запрос. Попробуйте еще раз.")
