import requests
from colorama import Fore, Style
import creds

class Converter:

    @staticmethod
    def fetch_exchange_rates():
        """Fetch the latest exchange rates from the API."""
        try:
            response = requests.get(creds.api_key)
            response.raise_for_status()  # raise an error for http issues
            data = response.json()
            if data["result"] == "success":
                return data["conversion_rates"]
            else:
                print("Failed to fetch exchange rates:", data.get("error-type", "Unknown error"))
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None

    @staticmethod
    def convert_currency(amount, target_currency):
        """Convert an amount in EUR to the target currency."""
        rates = Converter.fetch_exchange_rates()
        if rates and target_currency in rates:
            return amount * rates[target_currency]
        else:
            print(f"Conversion rate for {target_currency} not found.")
            return None

    @staticmethod
    def eur_to_usd(amount):
        return Converter.convert_currency(amount, "USD")

    @staticmethod
    def eur_to_gbp(amount):
        return Converter.convert_currency(amount, "GBP")

    @staticmethod
    def eur_to_inr(amount):
        return Converter.convert_currency(amount, "INR")

    @staticmethod
    def eur_to_jpy(amount):
        return Converter.convert_currency(amount, "JPY")

    @staticmethod
    def eur_to_aud(amount):
        return Converter.convert_currency(amount, "AUD")

    @staticmethod
    def eur_to_cad(amount):
        return Converter.convert_currency(amount, "CAD")

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

    @staticmethod
    def validate_temperature_input(value):
        """Validate that the temperature input is a realistic numeric value."""
        if not isinstance(value, (int, float)):
            raise ValueError("The temperature value must be a numeric value.")
        if not (-273.15 <= value <= 1000):  # Allow values between absolute zero and 1000°C
            raise ValueError("Temperature must be between -273.15°C and 1000°C.")
        return value


    @staticmethod
    def validate_currency_input(value):
        """Validate that the currency input is a valid positive numeric value."""
        if not isinstance(value, (int, float)):
            raise ValueError("The amount must be a numeric value.")
        if not (0 < value <= 1e12):  # Ensure the value is within a realistic range
            raise ValueError("Amount must be positive and less than 1 trillion.")
        return value

def get_valid_menu_choice(prompt, valid_choices):
    """Prompt the user for a valid menu choice."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

# Menu Functions
def temperature_menu():
    converter = Converter()

    while True:
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.MAGENTA + "     🌡️  Temperature Conversions 🌡️     ".center(40) + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.GREEN + "1. Celsius to Fahrenheit" + Style.RESET_ALL)
        print(Fore.GREEN + "2. Celsius to Kelvin" + Style.RESET_ALL)
        print(Fore.GREEN + "3. Fahrenheit to Celsius" + Style.RESET_ALL)
        print(Fore.GREEN + "4. Fahrenheit to Kelvin" + Style.RESET_ALL)
        print(Fore.GREEN + "5. Kelvin to Celsius" + Style.RESET_ALL)
        print(Fore.GREEN + "6. Kelvin to Fahrenheit" + Style.RESET_ALL)
        print(Fore.RED + "7. Back to Main Menu 🚪 " + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)

        temp_choice = get_valid_menu_choice("Choose an option (1-7): ", ["1", "2", "3", "4", "5", "6", "7"])
        if temp_choice == "7":
            break

        try:
            value = float(input("Enter the temperature value: "))
            value = converter.validate_temperature_input(value)  # Validate the input

            if temp_choice == "1":
                result = converter.celsius_to_fahrenheit(value)
                print(f"{value} Celsius is {result:.2f} Fahrenheit.")
            elif temp_choice == "2":
                result = converter.celsius_to_kelvin(value)
                print(f"{value} Celsius is {result:.2f} Kelvin.")
            elif temp_choice == "3":
                result = converter.fahrenheit_to_celsius(value)
                print(f"{value} Fahrenheit is {result:.2f} Celsius.")
            elif temp_choice == "4":
                result = converter.fahrenheit_to_kelvin(value)
                print(f"{value} Fahrenheit is {result:.2f} Kelvin.")
            elif temp_choice == "5":
                result = converter.kelvin_to_celsius(value)
                print(f"{value} Kelvin is {result:.2f} Celsius.")
            elif temp_choice == "6":
                result = converter.kelvin_to_fahrenheit(value)
                print(f"{value} Kelvin is {result:.2f} Fahrenheit.")
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)

def currency_menu():
    converter = Converter()

    while True:
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.MAGENTA + "     💵  Currency Conversions 💵       ".center(40) + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.GREEN + "1. EUR to USD" + Style.RESET_ALL)
        print(Fore.GREEN + "2. EUR to GBP" + Style.RESET_ALL)
        print(Fore.GREEN + "3. EUR to INR" + Style.RESET_ALL)
        print(Fore.GREEN + "4. EUR to JPY" + Style.RESET_ALL)
        print(Fore.GREEN + "5. EUR to AUD" + Style.RESET_ALL)
        print(Fore.GREEN + "6. EUR to CAD" + Style.RESET_ALL)
        print(Fore.RED + "7. Back to Main Menu 🚪" + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)

        currency_choice = get_valid_menu_choice("Choose an option (1-7): ", ["1", "2", "3", "4", "5", "6", "7"])
        if currency_choice == "7":
            break

        try:
            value = float(input("Enter the amount in EUR: "))
            value = converter.validate_currency_input(value)  # Validate the input

            if currency_choice == "1":
                result = converter.eur_to_usd(value)
                print(f"{value} EUR is {result:.2f} USD")
            elif currency_choice == "2":
                result = converter.eur_to_gbp(value)
                print(f"{value} EUR is {result:.2f} GBP")
            elif currency_choice == "3":
                result = converter.eur_to_inr(value)
                print(f"{value} EUR is {result:.2f} INR")
            elif currency_choice == "4":
                result = converter.eur_to_jpy(value)
                print(f"{value} EUR is {result:.2f} JPY")
            elif currency_choice == "5":
                result = converter.eur_to_aud(value)
                print(f"{value} EUR is {result:.2f} AUD")
            elif currency_choice == "6":
                result = converter.eur_to_cad(value)
                print(f"{value} EUR is {result:.2f} CAD")
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)

def main_menu():
    while True:
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.MAGENTA + "          Conversion Menu          ".center(40) + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)
        print(Fore.GREEN + "1. Temperature Conversions 🌡️ " + Style.RESET_ALL)
        print(Fore.GREEN + "2. Currency Conversions 💱 " + Style.RESET_ALL)
        print(Fore.RED + "3. Exit " + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 40 + Style.RESET_ALL)

        choice = get_valid_menu_choice("Choose an option (1-3): ", ["1", "2", "3"])

        if choice == "1":
            temperature_menu()
        elif choice == "2":
            currency_menu()
        elif choice == "3":
            break

if __name__ == "__main__":
    main_menu()