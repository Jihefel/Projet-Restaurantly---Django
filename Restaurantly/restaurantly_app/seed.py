from django_seed import Seed    
from restaurantly_app.models import Member
import random

def run():
    seeder = Seed.seeder()
    genders = ['male','female','autre']
    seeder.add_entity(Member, 20, {
        'age' : lambda x: random.randint(0,100),
        'name' : lambda x: seeder.faker.name(),
        'gender' : lambda x: genders[random.randint(0,2)],
    })
    inserted_pks = seeder.execute()
    print(inserted_pks)