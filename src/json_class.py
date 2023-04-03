from abc import ABC, abstractmethod


import json


class File(ABC):
    def __init__(self, vacancies_data: list) -> None:
        self._vacancies_data = vacancies_data
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
    def __init__(self, vacancies_data: list):
        super().__init__(vacancies_data)

    def add_vacancies(self):
        """
        Функция записи файла с вакансиями
        """
        with open("data_file.json", 'w', encoding='utf-8') as outfile:
            json.dump(self._vacancies_data, outfile, indent=1, ensure_ascii=False)

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

