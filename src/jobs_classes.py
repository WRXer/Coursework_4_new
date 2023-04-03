import json


class Vacancy:
    __slots__ = ('name', 'url', 'description', 'payment')
    def __init__(self, name: str, url: str, description: str, payment):
        self.name = name
        self.url = url
        self.description = description    #Описание вакансии
        self.payment = payment

    def __str__(self):
        return f"Name: {self.name}, Url: {self.url}, Description: {self.description}, Payment: {self.payment}"



def filter_vacancies(vacancies, filter_words):
    """
    Функция фильтрации вакансий по ключевым словам пользователя
    :param hh_vacancies:
    :param sj_vacancies:
    :param filter_words:
    :return:
    """
    list_vacancies = []
    for i in vacancies:
        if i['description'] is not None:
            if filter_words.lower() in i['description'].lower():
                list_vacancies.append(i)
    return list_vacancies

def get_avg_salary_range(payment):
    """
    Функция для получения среднего значения зарплаты из диапазона
    """
    if type(payment) != int:
        if payment['currency'] == 'USD':    #Переводим доллар в рубли(пока так)
            if payment['to'] is not None:
                payment['to'] *= 80
            if payment['from'] is not None:
                payment['from'] *= 80
            payment['currency'] = 'RUR(from USD(80))'
        if payment['to'] == None:
            return payment['from']
        if payment['from'] == None:
            return payment['to']
        return (payment['to'] + payment['from']) / 2    # Считаем среднее значение зарплаты из значений to и from
    else:
        return payment

def sorting(filtered_vacancies):
    """
    Сортировка вакансий по зарплате
    :param vacancies:
    :return:
    """
    sorted_data = sorted(filtered_vacancies, key=lambda x: get_avg_salary_range(x['payment']), reverse=True)
    return sorted_data

def get_top(sorted_vacancies, top_count):
    """
    Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods)
    """
    top = []
    counter = 0
    for v in sorted_vacancies:
        if counter < top_count:
            top.append(v)
            counter +=1
        else:
            break
    return top
