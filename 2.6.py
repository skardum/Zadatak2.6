import requests
from tabulate import tabulate

pj = '4986-1'
username = 'luceed_mb'
password = '7e5y2Uza'

urlTemplate = 'http://apidemo.luceed.hr/datasnap/rest/mpobracun/placanja/{pj}/{dateFrom}/{dateTo}'

while True:
	dateFrom = input("unesite datum od (dd.MM.yyyy): ")
	if dateFrom != '':
		break
	print('morate unijeti datum od')

dateTo = input("unesite datum do (dd.MM.yyyy): ")

url = urlTemplate.format(
	pj = pj,
	dateFrom = dateFrom,
	dateTo = dateTo,
)

request = requests.get(url, auth = (username, password))
response = request.json()

if 'error' in response:
	print('')
	print(response['error'].strip())
	print('')
	exit()

stavke = response['result'][0]['obracun_placanja']

if len(stavke) == 0:
	print('')
	print('Nema stavki za prikazati')
	print('')
	exit()

header = stavke[0].keys()
rows =  [x.values() for x in stavke]

print(tabulate(rows, header))