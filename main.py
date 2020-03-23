import csv
import os
from datetime import datetime
from io import StringIO
from operator import methodcaller
from urllib.request import urlopen


# https://stepik.org/lesson/24473/step/2?thread=solutions&unit=6777
# https://stepik.org/media/attachments/lesson/24473/Crimes.csv


# fstream = urlopen('https://stepik.org/media/attachments/lesson/24473/Crimes.csv')
# reader = csv.DictReader(StringIO(fstream.read().decode('utf-8')))


# reader = csv.reader(StringIO(fstream.read().decode('utf-8')))
# print(list(map(methodcaller('replace',' ','_'),next(reader))))
# print(next(reader))
# print(next(reader))


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dbfile = os.path.join(os.path.dirname(__file__),'crimes.sqlite3')
engine = create_engine('sqlite:///'+dbfile, echo=False)   # 'sqlite:///:memory:'

from models import Base, Case, Ivcr, CrimeType, Beat, District, Ward, CommunityArea, FBICode

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
df = '%m/%d/%Y %I:%M:%S %p'
data = []

# for d in reader:
#     case = Case(id=d['ID'],
#                 number=d['Case Number'],
#                 date=datetime.strptime(d['Date'],df),
#                 block=d['Block'],
#                 description=d['Description'],
#                 location_description=d['Location Description'],
#                 arrest=d['Arrest']=='true',
#                 domestic=d['Domestic']=='true')
#     data +=[case]
#
# session.add_all(data)
with open('Crimes.csv', 'r') as f:
    reader = csv.DictReader(f)
    # d = next(reader)

    for d in reader:
        case = Case(id=d['ID'],
                    number=d['Case Number'],
                    date=datetime.strptime(d['Date'], df),
                    block=d['Block'],
                    description=d['Description'],
                    location_description=d['Location Description'],
                    arrest=d['Arrest'] == 'true',
                    domestic=d['Domestic'] == 'true',
                    ivcr=session.query(Ivcr).filter_by(code=d['IUCR']).first() or Ivcr(code=d['IUCR']),
                    crimetype=session.query(CrimeType).filter_by(type=d['Primary Type']).first() or CrimeType(type=d['Primary Type']),
                    beat=session.query(Beat).filter_by(code=d['Beat']).first() or Beat(code=d['Beat']),
                    district=session.query(District).filter_by(code=d['District']).first() or District(code=d['District']),
                    ward=session.query(Ward).filter_by(code=d['Ward']).first() or Ward(code=d['Ward']),
                    communityarea=session.query(CommunityArea).filter_by(code=d['Community Area']).first() or CommunityArea(code=d['Community Area']),
                    fbicode=session.query(FBICode).filter_by(code=d['FBI Code']).first() or FBICode(code=d['FBI Code']))
        # data += [case]
        session.add(case)
# session.add(case)
# session.add_all(data)
session.commit()
case = session.query(Case).filter_by(number='HH684629').first()
print(case)
