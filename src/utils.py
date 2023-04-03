from src.engine_classes import HH, SuperJob
from src.jobs_classes import Vacancy, sorting, get_top,filter_vacancies
from src.json_class import JSONSaver


def main():
    #platforms = all
    search_query = 'python'
    hh = HH(search_query)
    sj = SuperJob(search_query)
    hh_vacancies = hh.get_request()
    sj_vacancies = sj.get_request()
    vacancies_data = hh_vacancies + sj_vacancies
    json_saver = JSONSaver(vacancies_data)
    #json_saver.add_vacancies()
    vacancies = json_saver.data_file()
    filter_words = "django"
    filtered_vacancies = filter_vacancies(vacancies, filter_words)
    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    #for v in filtered_vacancies:
    #    vacancy = Vacancy(v['name'], v['url'], v['description'], v['payment'])
    #    print(str(vacancy))
    sorted_vacancies = sorting(filtered_vacancies)
    top_count = 30
    top_vacancies  = get_top(sorted_vacancies, top_count)
    for t in top_vacancies:
        print(t)
