from src.engine_classes import HH, SuperJob
from src.jobs_classes import Vacancy, HHVacancy, sorting

import json


class JSONSaver:
    def add_vacancy(self, vacancies_data):
        with open("data_file.json", 'w', encoding='utf-8') as outfile:
            json.dump(vacancies_data, outfile, indent=1, ensure_ascii=False)

    def data_file(self):
        with open('data_file.json', 'r', encoding='utf-8') as file:
            raw_json = file.read()
            d_f = json.loads(raw_json)
            return d_f

    def delete_vacancy(self):
        with open("data_file.json", "w") as f:
            pass


def main():
    hh = HH('python', 35)
    sj = SuperJob('java', 2)
    hh_vacancies = hh.get_request()
    sj_vacancies = sj.get_request()
    json_saver = JSONSaver()
    json_saver.add_vacancy(hh_vacancies)
    vacancies = json_saver.data_file()
    for v in vacancies:
        vacancy = Vacancy(v['name'], v['url'], v['description'], v['payment'])
    #print(vacancy)
    sorted_vacancies = sorting(vacancies)
    for v in sorted_vacancies:
        print(v['payment'])
