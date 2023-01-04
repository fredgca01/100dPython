
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data = DataManager()
#print(data.get_search_list())

search =  FlightSearch()
flights = []
for code in data.get_search_list():
    flights = search.search("city:PAR",f"city:{code}","20/05/2023","20/05/2023","25/05/2023","25/05/2023")
search_result=[]
for flight in flights:
    search_result.append(FlightData(flight))

notifier = NotificationManager()

for result in search_result:
    #result.is_available() and
    if data.get_lowest_price(result.getPrice(),result.getIataCode()):
        notifier.send_email("xxxx",result.printSummary(),result.printDetail())
