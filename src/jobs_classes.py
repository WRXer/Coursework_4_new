class Vacancy:
    __slots__ = ('name', 'url', 'description', 'payment')
    def __init__(self, name: str, url: str, description: str, payment: str):
        self.name = name
        self.url = url
        self.description = description    #Описание вакансии
        self.payment = payment

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.payment}, Description: {self.description}, Url: {self.url}"


class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: {self.description}, зарплата: {self.payment} руб/мес'


class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.description}, зарплата: {self.payment} руб/мес'


def get_avg_salary_range(payment):
    """
    Функция для получения среднего значения зарплаты из диапазона
    """
    if payment is not None:
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

def sorting(vacancies):
    """
    Сортировка вакансий по зарплате
    :param vacancies:
    :return:
    """
    sorted_data = sorted(vacancies, key=lambda x: get_avg_salary_range(x['payment']), reverse=True)
    return sorted_data

def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass