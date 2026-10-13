

chosen_year = int(input("Enter a year to analyze: "))

lowest_life = None
highest_life = None

year_total = 0
year_count = 0

year_lowest = None
year_highest = None

with open("life-expectancy.csv", "r", encoding="utf-8") as file:

    # Skip the first line because it contains the column headings.
    file.readline()

    # Read and analyze the remaining lines.
    for line in file:
        parts = line.strip().split(",")

        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        # Ignore regional records that do not have a country code.
        if code == "":
            continue

        # Find the lowest life expectancy in the dataset.
        if lowest_life is None or life_expectancy < lowest_life:
            lowest_life = life_expectancy
            lowest_country = country
            lowest_year = year

        # Find the highest life expectancy in the dataset.
        if highest_life is None or life_expectancy > highest_life:
            highest_life = life_expectancy
            highest_country = country
            highest_year = year

        # Calculate statistics for the year entered by the user.
        if year == chosen_year:
            year_total += life_expectancy
            year_count += 1

            if year_lowest is None or life_expectancy < year_lowest:
                year_lowest = life_expectancy
                year_lowest_country = country

            if year_highest is None or life_expectancy > year_highest:
                year_highest = life_expectancy
                year_highest_country = country


# Display the overall results.
print("\n--- Overall Life Expectancy Results ---")
print(
    f"Lowest: {lowest_life:.3f} years in "
    f"{lowest_country}, {lowest_year}"
)
print(
    f"Highest: {highest_life:.3f} years in "
    f"{highest_country}, {highest_year}"
)

# Display results for the selected year.
print(f"\n--- Results for {chosen_year} ---")

# if year_count > 0:
#     average = year_total / year_count

#     print(f"Average life expectancy: {average:.3f} years")
#     print(
#         f"Lowest: {year_lowest:.3f} years in "
#         f"{year_lowest_country}"
#     )
#     print(
#         f"Highest: {year_highest:.3f} years in "
#         f"{year_highest_country}"
#     )
# else:
#     print(f"No country data was found for the year {chosen_year}.")

# Display the overall results.
print("\n" + "=" * 45)
print(" THE WORLD'S LIFE EXPECTANCY DISCOVERY")
print("=" * 45)

print(
    f" Lowest life expectancy: {lowest_life:.3f} years"
    f" — {lowest_country} ({lowest_year})"
)

print(
    f" Highest life expectancy: {highest_life:.3f} years"
    f" — {highest_country} ({highest_year})"
)

# Display results for the selected year.
print("\n" + "=" * 45)
print(f" YOUR YEAR-IN-FOCUS: {chosen_year}")
print("=" * 45)

if year_count > 0:
    average = year_total / year_count

    print(f" Average life expectancy: {average:.3f} years")
    print(
        f" Lowest: {year_lowest:.3f} years"
        f" — {year_lowest_country}"
    )
    print(
        f" Highest: {year_highest:.3f} years"
        f" — {year_highest_country}"
    )
    print("\n Every number tells a story about human life!")
else:
    print(f"Sorry! No country data was found for {chosen_year}.")
    print("Try another year to continue your discovery.")

print("\nThank you for exploring the world with us! ")
