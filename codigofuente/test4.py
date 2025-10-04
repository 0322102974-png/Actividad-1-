from faker import Faker

fake=Faker ()

Faker.seed(0)
for _ in range(5):
    print(fake.phone_number())