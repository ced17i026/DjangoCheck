import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FirstProject.settings')
import django 
django.setup()

import random 
from first_app.models import Topic,webpage,AccessRecord
from faker import Faker

fakedata = Faker()
topics = ["social","politics","world","science","Life"]
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate():
    for entry in range(6):
        top = add_topic()
        name_data = fakedata.company()
        url_data = fakedata.url()
        webpge = webpage.objects.get_or_create(topic=top,name=name_data,url=url_data)[0]

        # AccessRecord population
        date_data = fakedata.date()
        acss_rcrd = AccessRecord.objects.get_or_create(name=webpge,date=date_data)[0]

if __name__=='__main__':
    print("Populating...")
    populate()
    print("Populated Successfully")