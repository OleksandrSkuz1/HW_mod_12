# Додайте методи save_to_file і load_from_file у клас AddressBook для збереження та відновлення адресної книги з файлу:
# Код AddressBook та AddressBookIterator без змін

# Після створення екземпляра AddressBook, використовуйте метод load_from_file для завантаження збережених даних і save_to_file для збереження їх після змін:
book = AddressBook("address_book.pkl")

# Додайте метод search до класу AddressBook, який дозволить шукати контакти за іменем або номером телефону:
# Код AddressBook без змін

# Тепер ви можете шукати контакти за ім'ям або номером телефону за допомогою методу search:
results = book.search("John")  # Шукати за ім'ям або номером телефону
for record in results:
    print(record)

# Не забудьте викликати save_to_file після внесення змін у адресну книгу, щоб зберегти їх на диск:
book.add_record(new_record)
book.save_to_file()



