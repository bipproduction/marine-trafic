from faker import Faker
import random
import time
import os

fake = Faker()

def generate_vessel_data():
    name = fake.company()
    vessel_type = random.choice(['Cargo Ship', 'Fishing Boat', 'Passenger Ship', 'Tanker'])
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    country = fake.country()
    return {'name': name, 'type': vessel_type, 'latitude': latitude, 'longitude': longitude, 'country': country}

def display_vessel_data(vessel_data):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    print("Data Dummy Lalu lintas Kapal Laut:")
    for data in vessel_data:
        print(f"Nama: {data['name']}, Jenis: {data['type']}, Koordinat: ({data['latitude']}, {data['longitude']}), Negara: {data['country']}")

if __name__ == "__main__":
    num_vessels = 1000
    update_interval = 5  # in seconds
    
    vessel_data = [generate_vessel_data() for _ in range(num_vessels)]
    
    while True:
        for i in range(num_vessels):
            vessel_data[i] = generate_vessel_data()
        display_vessel_data(vessel_data)
        time.sleep(update_interval)
