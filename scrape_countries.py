import requests
from bs4 import BeautifulSoup

# Part a: Fetch HTML
url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)

if response.status_code != 200:
    print("Error fetching page:", response.status_code)
    exit()

html = response.text

# Part b: Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Part c: Extract Name, Capital, Population, Area
countries = soup.find_all("div", class_="country")

# Part d: Store in structured format (list of dictionaries)
country_data = []
for country in countries:
    name = country.find("h3", class_="country-name").get_text(strip=True)
    capital = country.find("span", class_="country-capital").get_text(strip=True)
    population = country.find("span", class_="country-population").get_text(strip=True)
    area = country.find("span", class_="country-area").get_text(strip=True)

    country_data.append({
        "Name": name,
        "Capital": capital,
        "Population": population,
        "Area": area
    })

# Part e: Print as a simple table
print(f"{'Name':<30} {'Capital':<20} {'Population':<15} {'Area (km²)':<10}")
print("-" * 80)

for c in country_data[:30]:  # print only first 30 for preview
    print(f"{c['Name']:<30} {c['Capital']:<20} {c['Population']:<15} {c['Area']:<10}")

#Create a CSV file
import csv
filename = "countries.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Capital", "Population", "Area"])
    writer.writeheader()
    writer.writerows(country_data)