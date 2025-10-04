from faker import Faker

fake=Faker ()

Faker.seed(0)
for _ in range(10):
    print("Numero de pasaporte", fake.passport_number())
