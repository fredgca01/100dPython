
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from club_manager import ClubManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data = DataManager()
club = ClubManager()

# print("Hello\n")
# club.add_member(lastname=input("What is your name ?"), firstname=input("What is your first name ?"),email=input("What is your email ?"))

search =  FlightSearch()
search_result = []
cities = data.get_search_list()
for code in cities:
    search_result.append(search.search("city:PAR",f"city:{code}","1/05/2023","2/05/2023","8/05/2023","9/05/2023"))
flights=[]
for search in search_result:
    for flight in search:
        flights.append(FlightData(flight))

notifier = NotificationManager()

members = club.get_members()
for result in flights:
    if result.is_available() and data.get_lowest_price(result.getPrice(),result.getIataCode()):
        for member in members:
            notifier.send_email(member,result.printSummary(),result.printDetail())
