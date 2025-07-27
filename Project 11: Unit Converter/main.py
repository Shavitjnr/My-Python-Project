def length_converter():
    print("\nLength Conversion:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = input("Choose an option: ")
    if choice == "1":
        meters = float(input("Enter meters: "))
        print(f"{meters} meters = {meters * 3.28084:.2f} feet")
    elif choice == "2":
        feet = float(input("Enter feet: "))
        print(f"{feet} feet = {feet / 3.28084:.2f} meters")
    else:
        print("Invalid choice.")

def weight_converter():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose an option: ")
    if choice == "1":
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kg = {kg * 2.20462:.2f} lbs")
    elif choice == "2":
        lbs = float(input("Enter pounds: "))
        print(f"{lbs} lbs = {lbs / 2.20462:.2f} kg")
    else:
        print("Invalid choice.")

def temperature_converter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option: ")
    if choice == "1":
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {c * 9/5 + 32:.2f}°F")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print(f"{f}°F = {(f - 32) * 5/9:.2f}°C")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = input("Select conversion type: ")
        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()