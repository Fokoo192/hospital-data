from Hospitals import Hospital 
from random import randint

names = ["Central Newfoundland Regional Health Centre","Health Sciences Centre","Western Memorial Regional Hospital","Waterford Hospital, Eastern Health","St. Clare's Mercy Hospital","Dr. G. B. Cross Memorial Hospital","Sir Thomas Roddick Hospital","Bonavista Peninsula Health Centre","James Paton Memorial Regional Health Centre","St Clare's Hospital Chaplain","Carbonear General Hospital","Baie Verte Peninsula Health Centre","Fogo Island Health Centre","Notre Dame Bay Memorial Health Centre","Bonne Bay Health Centre","Burin Peninsula Health Care Centre","Labrador Health Centre","Labrador West Health Centre","Dr. Charles S. Curtis Memorial Hospital","U S Memorial Health Centre","Brookfield Hospital Dr","Dr. A.A. Wilkinson Memorial Health Centre","Labrador South Health Centre - Labrador-Grenfell Health","Strait of Belle Isle Health Centre","Janeway Children's Health and Rehabilitation Centre","Labrador Health Svc","Brookfield Hospital","Corner Brook Acute Care Hospital","Eastern Health Long Term Care","Dr. Hugh Twomey Health Centre","Corner Brook Long Term Care Centre","Calder Health Centre - Western Health","Janeway Childrens Hospital","st.marry","Brookfield Health Centre","Dr.Charles L.Legrow Health Centre","Dr. S Beckley Health Center","Green Bay Community Health Centre","Dr. Walter Templeman Health Care Centre","Dr. S Beckley Health Center","Eastport Community Health Center"]

data = {}
for x in names:
    a = Hospital(x,randint(20,100),randint(0,100),randint(0,50),randint(200,500),randint(20,100))
    data[x]=a._information
print(data)