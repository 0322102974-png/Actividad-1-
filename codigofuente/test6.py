from faker import Faker

fake=Faker ()

Faker.seed(0)
for _ in range(1):
    print(fake.simple_profile())