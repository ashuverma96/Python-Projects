import os 
import csv
from datetime import datetime
import requests

FILENAME ="weather_logs.csv"
API_KEY = "*****"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

city = ""

def log_weather():
    city = input("Enter your city name: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(FILENAME, "r", newline='', encoding="utf-8") as f:
        for row in reader:
            if row["Date"]== date and row['City'].lower() == city.lower():
                print("Entry for this city and date exits")
                return
            
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            print(f"API error")
            return
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        
        with open(FILENAME, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.twriterow([date,city.title(), temp, condition])
            print(f"Logged: {temp} {condition} in {city.title()} on {date}")
            
    except Exception as e:
        print("failed to make api call")
        
def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <=1:
            print("No Entery")
            return
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")
        
def main():
    while True:
        print("real time weather logger")
        print("1. Add weather log")
        print("2. View weather log")
        
        choice = input("choose an option: ").strip()
        
        match choice:
            case "1": log_weather()
            case "2": view_logs()
            case __: print("Invalid option")
            
if __name__ == "__main__":
    main()
        

