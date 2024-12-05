# Here's an example of how you could use Python to scrape bus schedule information from the Rockingham Transit website

import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.transperth.wa.gov.au/timetablepdfs/Bus%20Timetable%20127%2020240715.pdf"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# # Find the table containing the bus schedule
# table = soup.find("table", {"class": "table-striped"})

# # Extract the bus times from the table
# bus_times = []
# for row in table.find_all("tr"):
#     cells = row.find_all("td")
#     if len(cells) > 0:
#         time = cells[0].text.strip()
#         bus_times.append(time)

# # Print the bus times
# print("Rockingham Transit Route 555 Bus Times:")
# for time in bus_times:
#     print(time)
