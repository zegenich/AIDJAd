from enum import Enum
from faker import Faker

fake = Faker()
fake_ru = Faker('ru_RU')

namefamil = fake_ru.name().split()
name = namefamil[0]
lastname = namefamil[1]

class BookingData(Enum):
    FIRSTNAME = name
    LASTNAME = lastname

