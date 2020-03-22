import csv
from io import StringIO
from operator import methodcaller
from urllib.request import urlopen
import requests

# https://stepik.org/lesson/24473/step/2?thread=solutions&unit=6777
# https://stepik.org/media/attachments/lesson/24473/Crimes.csv

# r = requests.get('https://stepik.org/media/attachments/lesson/24473/Crimes.csv')
# text = r.iter_lines()
from sqlalchemy import Column, Integer, String, DateTime, Boolean

fstream = urlopen('https://stepik.org/media/attachments/lesson/24473/Crimes.csv')

reader = csv.DictReader(StringIO(fstream.read().decode('utf-8')))
# reader = csv.reader(StringIO(fstream.read().decode('utf-8')))
# print(list(map(methodcaller('replace',' ','_'),next(reader))))
print(next(reader))
# print(next(reader))

class Case:
    id = Column(Integer, primary_key=True)
    number = Column(String(60))
    date = Column(DateTime)
    block = Column(String(60))
    description = Column(String(60))
    location_description = Column(String(60))
    arrest = Column(Boolean)
    domestic = Column(Boolean)

class Ivcr:
    id = Column(Integer, primary_key=True)
    code = Column(String(32))

class CrimeType:
    id = Column(Integer, primary_key=True)
    type = Column(String(60))

class beat:
    id = Column(Integer, primary_key=True)
    code = Column(String(32))

class district:
    id = Column(Integer, primary_key=True)
    code = Column(String(32))

class ward:
    id = Column(Integer, primary_key=True)

class CommunityArea:
    id = Column(Integer, primary_key=True)

class FBICode:
    id = Column(Integer, primary_key=True)
    code = Column(String(32))