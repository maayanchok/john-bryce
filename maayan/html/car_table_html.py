from urllib.request import urlopen
import json


class Car:
    def __init__(self,imp_id, imp_name, model_type, prod_year, price):
        self.imp_id = imp_id
        self.imp_name = imp_name
        self.model_type = model_type
        self.prod_year = prod_year
        self.price = price

    def html_header(self):
        html = """
            <tr>
                <td> importer id </td>
                <td> importer name </td>
                <td> model type </td>
                <td> production year </td>
                <td> price </td>
            </tr>
        """
        return html

    def to_html_row(self):
        html = "<tr>"
        for val in self.__dict__.values():
            html += f"<td>{val}</td>"
        html += "</tr>"
        return html
    


def get_data() -> list[dict]:
    f = urlopen(
        "https://data.gov.il/api/3/action/datastore_search?resource_id=39f455bf-6db0-4926-859d-017f34eacbcb&limit=5")
    api_result = json.loads(f.read().decode())["result"]
    total = int(api_result["total"])
    f = urlopen(
        f"https://data.gov.il/api/3/action/datastore_search?resource_id=39f455bf-6db0-4926-859d-017f34eacbcb&limit={total}")
    api_records = json.loads(f.read().decode())["result"]["records"]
    return api_records

def html_page(cars):
    html ="<html><body><table>"
    html += cars[0].html_header()
    for car in cars:
        html += car.to_html_row()
    html +=  "</table></body></html>"
    return html
    
def write_to_html(cars: list[Car]):
    html = html_page(cars)
    with open("cars_table.html", "w") as f:
        f.write(html)
    return

car_data = get_data()
cars = []
for car_dict in car_data:
    car = Car(
        imp_id = car_dict["semel_yevuan"],
        imp_name = car_dict["shem_yevuan"],
        model_type = car_dict["sug_degem"],
        prod_year = car_dict["shnat_yitzur"],
        price = car_dict["mehir"]
    )
    cars.append(car)

write_to_html(cars)
