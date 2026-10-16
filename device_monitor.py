def get_initial_readings():
    return [28, 31, 35, 37, 29]

def display_readings(readings):
    print("\nCURRENT READINGS")
    print("-"*16)
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")
 
def add_reading(readings):
    text = input("\nEnter new reading: ")
    if len(text) == 0:
        print("\nInvalid input. The reading cannot be empty.")
        return
    if not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
        return

    value = int(text)
    if value < 0 or value > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
        return
    readings.append(value)
    print("\nReading added successfully.")

def is_whole_number(text):
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True

def classify_reading(reading):
    if reading < 30:
        return "NORMAL"
    elif reading <= 35:
        return "WARNING"
    else:
        return "CRITICAL"

def display_classification(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        print(f"{reading} °C -> {classify_reading(reading)}")

def compute_total(readings):
    total = 0
    for reading in readings:
        total = total + reading
    return total
 
def compute_average(readings):
    if len(readings) == 0:
        return 0.0
    return compute_total(readings) / len(readings)
 
def find_minimum(readings):
    if len(readings) == 0:
        return 0
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum

def find_maximum(readings):
    if len(readings) == 0:
        return 0
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum

def count_category(readings, category_name):
    count = 0
    for reading in readings:
        if classify_reading(reading) == category_name:
            count = count + 1
    return count

def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"

def display_summary(readings):

    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, "NORMAL")
    warning_count = count_category(readings, "WARNING")
    critical_count = count_category(readings, "CRITICAL")

    overall_status = determine_overall_status(warning_count, critical_count)

    normal_pct = (normal_count / len(readings)) * 100
    warning_pct = (warning_count / len(readings)) * 100
    critical_pct = (critical_count / len(readings)) * 100

    print("\nREADING SUMMARY")
    print("-"*15)
    print(f"Number of readings:  {len(readings)}")
    print(f"Total of readings:   {total}")
    print(f"Average temperature: {average:.2f} °C")
    print(f"Minimum temperature: {minimum} °C")
    print(f"Maximum temperature: {maximum} °C")
    print(f"\nNormal count:        {normal_count} ({normal_pct:.2f}%)")
    print(f"Warning count:       {warning_count} ({warning_pct:.2f}%)")
    print(f"Critical count:      {critical_count} ({critical_pct:.2f}%)")
    print(f"\nOverall status:      {overall_status}")
 
def main():
    readings = get_initial_readings()
    while True:
        print("\nSIMULATED DEVICE MONITORING SYSTEM")
        print("-"*34)
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")

        choice_text = input("\nEnter your choice: ")
        choice = int(choice_text)
        if choice == 1:
            display_readings(readings)
        elif choice == 2:
            add_reading(readings)
        elif choice == 3:
            display_classification(readings)
        elif choice == 4:
            display_summary(readings)
        elif choice == 5:
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()