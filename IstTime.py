def convert_ist_time(ist_hour, ist_minute, offset):
    total_minutes = ist_hour * 60 + ist_minute + int(offset * 60)
    total_minutes %= 1440
    return divmod(total_minutes, 60)

time_differences = {
    "USA (New York)": -9.5,
    "UK (London)": -4.5,
    "Germany": -3.5,
    "Japan": 3.5,
    "Australia (Sydney)": 5.5,
    "UAE (Dubai)": -1.5,
    "China": 2.5
}

while True:
    print("\nEnter IST time (HH MM): ")
    ist_hour, ist_minute = map(int, input().split())

    print("\nChoose a country:")
    countries = list(time_differences.keys())
    for idx, country in enumerate(countries, 1):
        print(f"{idx}. {country}")

    choice = int(input("Enter choice number: ")) - 1
    selected_country = countries[choice]
    offset = time_differences[selected_country]

    new_hour, new_minute = convert_ist_time(ist_hour, ist_minute, offset)
    print(f"\nTime in {selected_country}: {new_hour:02}:{new_minute:02}")

    again = input("\nDo you want to use the program again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break
