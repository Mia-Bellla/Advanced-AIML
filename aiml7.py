from faker import Faker

# Create a Faker generator
fake = Faker()

print("Welcome to Fake Human Generator \n")

# Generate a single fake person
print(" Name:", fake.name())
print(" Address:", fake.address())
print(" Email:", fake.email())
print(" Phone:", fake.phone_number())
print(" Job:", fake.job())
print(" Birthday:", fake.date_of_birth(minimum_age=18, maximum_age=80))

print("\n Full Fake Profile ")
profile = fake.simple_profile()
for key, value in profile.items():
    print(f"{key}: {value}")

print("\n 5 Fake Names:")
for i in range(5):
    print("-", fake.name())
