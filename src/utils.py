from src.engine_classes import HH, SuperJob
from src.jobs_classes import Vacancy, FileOperations
from src.json_class import JSONSaver


def platforms():
    pass





def main():
    print("Привествую! Это программа по парсингу и обработке данных с сайта вакансий hh.ru  superjob.ru")
    #platforms = all
    top_count = 0
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
    #fo = FileOperations(vacancies, filter_words)
    user_vacancies = FileOperations(vacancies, filter_words, top_count).filter_vacancies()
    if not user_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return
    user_vacancies = FileOperations(vacancies).sorting()
    top_count = 10
    user_vacancies = FileOperations(vacancies, top_count).get_top()

    #for t in user_vacancies:
    #    print(t['payment'])

