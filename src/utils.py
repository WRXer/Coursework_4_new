from src.engine_classes import HH, SuperJob
from src.jobs_classes import Vacancy, HHVacancy, sorting, get_top

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
    hh = HH('python', 100)
    sj = SuperJob('python', 100)
    hh_vacancies = hh.get_request()
    sj_vacancies = sj.get_request()
    all = hh_vacancies + sj_vacancies
    json_saver = JSONSaver()
    json_saver.add_vacancy(all)
    vacancies = json_saver.data_file()
    #for v in vacancies:
        #vacancy = Vacancy(v['name'], v['url'], v['description'], v['payment'])
        #print(v)
    sorted_vacancies = sorting(vacancies)
    top_count = 10
    top_vacancies  = get_top(sorted_vacancies, top_count)
    for t in top_vacancies:
        print(t)
