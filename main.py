from application.cls_phonebook import PhoneBook

def main():
    phonebook = PhoneBook('application/data/phonebook_raw.csv')
    phonebook.fix('application/data/phonebook_pure.csv')


if __name__ == '__main__':
    main()
