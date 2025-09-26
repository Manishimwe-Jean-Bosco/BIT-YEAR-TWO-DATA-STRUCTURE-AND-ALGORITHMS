import array

# Integers: Quantities of equipment
equipment_counts = [12, 7, 15, 9, 20]

total = sum(equipment_counts)
average = total / len(equipment_counts)
minimum = min(equipment_counts)
maximum = max(equipment_counts)

# Strings: Formatted report with f-strings
print("Science Lab Equipment Log Report")
print("--------------------------------")
print(f"Total Equipment Items: {total}")
print(f"Average Quantity per Item: {average:.2f}")
print(f"Minimum Quantity: {minimum}")
print(f"Maximum Quantity: {maximum}\n")

# Booleans: Apply threshold condition
threshold = 10
if average > threshold and maximum > threshold:
    print("Status: Above Standard\n")
else:
    print("Status: Below Standard\n")

# Lists: Maintain list of equipment names
equipment_list = ["Microscope", "Test Tubes", "Beakers", "Bunsen Burner", "Thermometer"]
print("Original List:", equipment_list)

equipment_list.append("Centrifuge")   # Add new element
if "Beakers" in equipment_list:       # Remove if exists
    equipment_list.remove("Beakers")

equipment_list.sort()  # Sort in place
print("Modified & Sorted List:", equipment_list, "\n")

# Arrays: Store numeric subset and compare
equipment_array = array.array('i', [12, 7, 15])
print("Array Sum:", sum(equipment_array))
print("List Sum:", sum(equipment_counts), "\n")

# Dictionaries: List of records
records = [
    {"id": 1, "name": "Microscope", "value": 12},
    {"id": 2, "name": "Test Tubes", "value": 7},
    {"id": 3, "name": "Beakers", "value": 15},
    {"id": 4, "name": "Bunsen Burner", "value": 9},
]

records[0]["value"] = 14                     # Update record
records = [r for r in records if r["name"] != "Beakers"]  # Delete record
total_value = sum(r["value"] for r in records)            # Total values

print("Updated Records:", records)
print("Total Value across Records:", total_value)
