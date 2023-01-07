from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from club_manager import ClubManager

data = DataManager()
club = ClubManager()
search = FlightSearch()

search_result = []
cities = data.get_search_list()
for code in cities:
    search_result.extend(search.search("city:PAR", f"city:{code}", "1/05/2023", "2/05/2023", "8/05/2023", "9/05/2023"))

flights = [FlightData(flight) for flight in search_result]
notifier = NotificationManager()
members = club.get_members()

for result in flights:
    if result.is_available() and data.get_lowest_price(result.get_price(), result.get_iata_code()):
        for member in members:
            notifier.send_email(member, result.print_summary(), result.print_detail())
