import csv
import re

PHONE_SEARCH_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB_PATTERN = r'+7(\2)-\3-\4-\5 \6\7'

class PhoneBook:
    def __init__(self, raw_data_path):
        raw_contact_list = self._get_raw(raw_data_path)
        contact_list_with_doubles = self._process_raw_data(raw_contact_list)
        self.pure_contact_list = self._make_pure_contact_list(contact_list_with_doubles)

    @staticmethod
    def _get_raw(data):
        with open(data, encoding='utf-8') as file:
            rows = csv.reader(file, delimiter=",")
            result = list(rows)
        return result

    @staticmethod
    def _process_raw_data(data):
        result = list()
        for row in data:
            record = list()
            full_name = re.findall(r'(\w+)', ' '.join(row[:3]))
            full_name.append('') if len(full_name) < 3 else ...
            record += full_name
            record.append(row[3])
            record.append(row[4])
            record.append(re.sub(PHONE_SEARCH_PATTERN, PHONE_SUB_PATTERN, row[5]).strip())
            record.append(row[6])
            result.append(record)
        return result

    def _make_pure_contact_list(self, data):
        result = dict()
        for item in data:
            result[item[0]] = self._merge_doubles(item, result[item[0]]) if item[0] in result else item
        return result.values()

    @staticmethod
    def _merge_doubles(record_one, record_two):
        result = list()
        for index in range(len(record_one)):
            result.append(record_one[index]) if record_one[index] else result.append(record_two[index])
        return result

    def fix(self, pure_data_path):
        with open(pure_data_path, "w", encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(self.pure_contact_list)
        print('Phonebook fixed, data saved in application/data/phonebook_pure.csv')
