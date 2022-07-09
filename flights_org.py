from urllib.request import urlopen
import json

class Flight:
    def __init__(self, flights:dict):
        self.id = flights["CHFLTN"]
        self.airline = flights["CHOPERD"]
        self.dest = flights["CHLOCCT"]
        self.time = flights["CHSTOL"]
        self.status = flights["CHRMINE"]
    
    def html_row(self):
        row = "<tr>"
        for i in self.__dict__.values():
            row += f"<tr>{i}</td>"
        row += "</tr>"
        return row 

    def html_table(self, flights):
        html = "<table>"
        html += f"""<tr>
                        <td> id 
                        </td>
                        <td> company
                        </td>
                        <td> departure
                        </td>
                        <td> destination
                        </td>
                        <td> time 
                        </td>
                    </tr>"""
        for flight in flights:
            html+= Flight(flight).html_row
        html+= "</table>"
        return html
    

    
def api_to_dict():
    """Gets api and returns a dict of the data"""
    f = urlopen("https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=5")
    api_dict = json.loads(f.read().decode())["result"]["records"]
    return api_dict
flights = api_to_dict()

def write_to_html(flights):
    g = open("flights_organisation.html","w")
    g.write(Flight(flights).html_table)
    g.close()
    return

write_to_html(flights)

:(

    