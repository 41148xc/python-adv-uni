import requests

class Fetcher:
    def __init__(self):
        url = "https://cdn.ituring.ir/ex/users.json"
        response = requests.get(url)
        self.__students = response.json() if response.status_code == 200 else []

    def nerds(self):
        return {f"{s['first_name']} {s['last_name']}" for s in self.__students if s['score'] > 18.5}

    def sultans(self):
        max_score = max(s['score'] for s in self.__students)
        return tuple(f"{s['first_name']} {s['last_name']}" for s in self.__students if s['score'] == max_score)

    def mean(self):
        scores = [s['score'] for s in self.__students]
        return sum(scores) / len(scores) if scores else 0

    def get_students(self):
        return [{'first_name': s['first_name'], 'last_name': s['last_name'], 'score': s['score']} for s in self.__students]

fetcher = Fetcher()

print("Nerds:", fetcher.nerds())
print("Sultans:", fetcher.sultans())
print("Mean score:", fetcher.mean())
print("Filtered students:", fetcher.get_students())
