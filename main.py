from application.cls_phonebook import PhoneBook

def main():
    raw_data_path = 'application/data/phonebook_raw.csv'
    phone_book = PhoneBook(raw_data_path)

    pure_data_path = 'application/data/phonebook_pure.csv'
    phone_book.fix(pure_data_path)


if __name__ == '__main__':
    main()
