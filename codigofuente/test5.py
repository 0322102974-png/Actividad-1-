from faker import Faker

fake=Faker ()

Faker.seed(0)
for _ in range(15):
    print("Puesdes aplicar a:",fake.job_male())