from faker import Faker
import csv

fake = Faker()

with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email", "Job"])

    for _ in range(10):
        name = fake.name()
        email = fake.email()
        job = fake.job()
        writer.writerow([name, email, job])
