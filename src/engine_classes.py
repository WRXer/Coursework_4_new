from abc import ABC, abstractmethod
from src.auth_data import token
import requests


class Engine(ABC):
    def __init__(self, search_text='python', per_page=3):
        self.search_text = search_text
        self.per_page = per_page

    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def get_request(self):
        vacancies_data = []
        url = "https://api.hh.ru/vacancies"
        params = {"text": self.search_text,"per_page": self.per_page}
        response = requests.get(url, params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                if vacancy['salary'] is not None:
                    vacancy_data = {'name': vacancy['name'], 'url': vacancy['url'],
                                    'description': vacancy['snippet']['requirement'], 'payment': vacancy['salary']}
                    vacancies_data.append(vacancy_data)
                else:
                    continue
        else:
            print("Error:", response.status_code)
        return vacancies_data
        #vacancy['salary'] зарплата
        #vacancy['snippet'] описание

class SuperJob(Engine):
     def get_request(self):
        vacancies_data = []
        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {'X-Api-App-Id': token}
        params = {'keyword': self.search_text, 'page': 1, 'count': self.per_page}
        response = requests.get(url,headers=headers, params=params)
        if response.status_code == 200:
            vacancies = response.json()["objects"]
            for vacancy in vacancies:
                vacancy_data = {'sj': {'name': vacancy['profession'], 'url': vacancy['link'], 'description': vacancy['candidat'], 'payment': vacancy['payment_from']}}
                vacancies_data.append(vacancy_data)
        #vacancy['candidat'] описание
        #vacancy['payment_from'] зарплата
        else:
            print("Error:", response.status_code)
        return vacancies_data
