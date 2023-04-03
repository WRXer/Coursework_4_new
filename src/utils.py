from src.engine_classes import HH, SuperJob
from src.jobs_classes import Vacancy, HHVacancy, sorting, get_top,filter_vacancies

import json


class JSONSaver:
    def add_vacancy(self, vacancies_data):
        """
        Функция записи файла с вакансиями
        """
        with open("data_file.json", 'w', encoding='utf-8') as outfile:
            json.dump(vacancies_data, outfile, indent=1, ensure_ascii=False)

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

    def delete_vacancy(self):
        """
        Функция удаления файла с вакансиями
        """
        try:
            with open("data_file.json", "w") as f:
                pass
        except FileNotFoundError:
            print("Файл не найден.")




def main():
    #platforms = all
    search_query = 'python'
    hh = HH(search_query)
    sj = SuperJob(search_query)
    hh_vacancies = hh.get_request()
    sj_vacancies = sj.get_request()
    json_saver = JSONSaver()
    all = hh_vacancies + sj_vacancies
    json_saver.add_vacancy(all)
    vacancies = json_saver.data_file()
    filter_words = "sql"
    filtered_vacancies = filter_vacancies(vacancies, filter_words)
    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return


    z = Vacancy(vacancies)
    #for v in vacancies:
        #vacancy = Vacancy(v['name'], v['url'], v['description'], v['payment'])
        #print(v)
    sorted_vacancies = sorting(filtered_vacancies)
    top_count = 30
    top_vacancies  = get_top(sorted_vacancies, top_count)
    for t in top_vacancies:
        print(t)
