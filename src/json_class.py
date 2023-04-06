from abc import ABC, abstractmethod
from src.jobs_classes import Vacancy

import json


class File(ABC):
    def __init__(self, data: list) -> None:
        self._data = data
    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def data_file(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSaver(File):
    def __init__(self, data: list):
        super().__init__(data)

    def add_vacancies(self):
        """
        Функция записи файла с вакансиями
        """
        with open("data_file.json", 'w', encoding='utf-8') as outfile:
            json.dump(self._data, outfile, indent=1, ensure_ascii=False)

    def data_file(self):
        """
        Функция открытия файла с вакансиями
        """
        try:
            with open('data_file.json', 'r', encoding='utf-8') as file:
                raw_json = file.read()
                d_f = json.loads(raw_json)
                return d_f
        except FileNotFoundError:
            print("Файл не найден.")

    def delete_vacancies(self):
        """
        Функция удаления файла с вакансиями
        """
        try:
            with open("data_file.json", "w") as f:
                pass
        except FileNotFoundError:
            print("Файл не найден.")

    def get_user_file(self):
        """
        Функция записи файла с вакансиями, после операций пользователя
        """
        with open("user_data.json", 'w', encoding='utf-8') as outfile:
            json.dump(self._data, outfile, indent=1, ensure_ascii=False)

    def delete_vacancy(self, name):
        with open('data_file.json', 'r') as outfile:
            vacancies = json.load(outfile)
        del vacancies[name]
        with open('data_file.json', 'w') as outfile:
            json.dump(vacancies, outfile, indent=1, ensure_ascii=False)
    def add_vacancy(self, vacancy):
        with open("data_file.json", 'r', encoding='utf-8') as outfile:
            vacancies = json.load(outfile)
        vacancies.append({'name': vacancy.name, 'url': vacancy.url, 'description': vacancy.description, 'payment': vacancy.payment})
        with open('data_file.json', 'w', encoding='utf-8') as outfile:
            json.dump(vacancies, outfile, indent=1, ensure_ascii=False)