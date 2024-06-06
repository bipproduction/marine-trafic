import numpy as np
import signal
import sys
from asciichartpy import plot
import time
from colorama import Fore, Style
import random

# Fungsi untuk menangani penekanan ctrl+c
def signal_handler(sig, frame):
    print('\nTerminating...')
    sys.exit(0)

# Fungsi untuk menghasilkan data harga saham palsu
def generate_fake_stock_prices():
    return np.random.randint(50, 200, size=100)

# Fungsi untuk mendapatkan kode warna acak
def random_color():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    return np.random.choice(colors)

# Fungsi untuk menghasilkan data longitude, latitude, dan nama negara palsu
def generate_fake_coordinates():
    longitude = round(random.uniform(-180, 180), 2)
    latitude = round(random.uniform(-90, 90), 2)
    countries = ["Indonesia", "Australia", "United States", "China", "Brazil", "Russia"]
    country = random.choice(countries)
    return longitude, latitude, country

# Inisialisasi grafik
stock_prices = generate_fake_stock_prices()
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        # Perbarui harga saham palsu
        stock_prices = np.roll(stock_prices, -1)
        stock_prices[-1] = np.random.randint(50, 200)

        chart = plot(stock_prices, {'height': 15, 'offset': 3})
        colored_chart = random_color() + chart + Style.RESET_ALL

        # Clear terminal screen
        print("\033[H\033[J")

        # Print colored chart
        print(colored_chart)

        # Generate and print running text
        for _ in range(6):
            longitude, latitude, country = generate_fake_coordinates()
            print(f"Location: Longitude {longitude}, Latitude {latitude}, Country: {country}")

        time.sleep(2)  # Menunda pembaruan selama 2 detik
except KeyboardInterrupt:
    pass
