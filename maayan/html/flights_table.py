from urllib.request import urlopen
import json
import time
from datetime import datetime

class Flight:
    def __init__(self, id, airline, dest, time, status):
        self.id = id
        self.airline = airline
        self.dest = dest
        self.time = time
        self.status = status

    def html_header(self):
        html = """
            <tr>
                <td> id </td>
                <td> airline </td>
                <td> destination </td>
                <td> time </td>
                <td> status </td>
            </tr>
        """
        return html

    def html_row(self):
        row = "<tr>"
        for i in self.__dict__.values():
            if i == "":
                i = "Updating data..."
            row += f"<td>{i}</td>"
        row += "</tr>"
        return row

    def __repr__(self):
        return f"<Flight {self.id}>"

def html_page(flights: list[Flight]):
    """Create an html table out of list of flights"""
    if not flights:
        return ""
    html = "<html><body>"
    html += "<header><h1>Flights table:</h1></header>"
    html += f"<h2>Last update: {datetime.now().strftime('%H:%M:%S')}</h2>"
    html += "<table id = 'table'>"
    html += flights[0].html_header()

    for flight in flights:
        row = flight.html_row()
        html += row

    html += "</table>"
    html += "<script src='flights.js'></script></body></html>"
    return html


def write_to_html(flights: list[Flight]):
    html = html_page(flights)
    with open("flights_organisation.html", "w") as f:
        f.write(html)
    return

def get_flights_data() -> list[dict]:
    """Gets api and returns a dict of the data"""
    f = urlopen(
        "https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=1")
    api_result = json.loads(f.read().decode())["result"]
    total = int(api_result["total"])
    f = urlopen(f"https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit={total}")
    api_records = json.loads(f.read().decode())["result"]["records"]

    return api_records

flights_data: list[dict] = get_flights_data()
flights: list[Flight] = []

for flight_dict in flights_data:
    flight = Flight(
        id = flight_dict["CHFLTN"],
        airline = flight_dict["CHOPERD"],
        dest = flight_dict["CHLOCCT"],
        time = flight_dict["CHSTOL"],
        status = flight_dict["CHRMINE"],
    )
    flights.append(flight)

while True:
    print("Refreshing html...")
    write_to_html(flights)
    time.sleep(60*15)


