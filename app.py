import requests
import datetime


quarantine_data = requests.get('https://api.quarantine.country/api/v1/summary/latest').json()
total_cases_switzerland = quarantine_data['data']['regions']['switzerland']['total_cases']

with open("total_cases_switzerland.csv", 'a') as file:
    file.write(
        f'{datetime.datetime.now().isoformat()}, {total_cases_switzerland} \n')
