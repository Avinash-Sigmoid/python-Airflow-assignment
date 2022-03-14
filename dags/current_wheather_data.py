import requests
import datetime
import csv
def write_csv():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "14008bcf0dmsh53056f154f78195p12b0a5jsn55387aeff04f"
        }

    #cities = ["Bhopal","Delhi","chandigarh","Goa","Mumbai","Jaipur","Gandhinagar","Pune","Hyderabad","Surat"]
    cities = ["Patna", "Delhi", "Bangalore",
              "Goa", "Mumbai", "Jaipur", "Hyderabad",
              "Pune", "Hyderabad", "chandigarh"]

    data_to_write = []
    #print("ndfjbihbfei")

    for city in cities:
        querystring = {"q":f"{city},india","lat":"0","lon":"0","id":"2172797","lang":"null","units":"imperial","mode":"JSON"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        print(data)
        list_item = [data["name"],data["weather"][0]["description"],data["main"]["temp"], data["main"]["feels_like"],
                     data["main"]["temp_min"], data["main"]["temp_max"], data["main"]["humidity"], data["clouds"]["all"] ]

        data_to_write.append(list_item)

    header = ['State', 'Description', 'Temperature', 'Feels_Like_Temperature', 'Min_Temperature', 'Max_Temperature', 'Humidity', 'Clouds']
    try:
        with open('Weather_Data.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data_to_write)
        print("Done Successfully")
    except:
        print("connection error...")

if __name__=="__main__":
    write_csv()









