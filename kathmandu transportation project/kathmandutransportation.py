import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
class route:
    def __init__(self,route_id,route_name,start_point,destination,distance):
        self.route_id=route_id
        self.route_name=route_name
        self.start_point=start_point
        self.destination=destination
        self.distance=float(distance)

    def display_route(self):
        print("The route id is: ",self.route_id)
        print("Route name is: ",self.route_name)
        print("Start point: ",self.start_point)
        print("Destination:",self.destination)
        print("Distance of travel: ",self.distance)

    def update_distance(self):
        new_distance=float(input("Enter the new distance: "))
        if new_distance==self.distance or new_distance<0:
            print("Same distance or invalid distance entered")
        else:
            self.distance=new_distance
            print("New distance added successfully")

    def get_route_info(self):
        return self.route_id,self.route_name,self.start_point,self.distance,self.destination
      

    def get_route_length(self):
        return self.distance

class vechile:
    def __init__(self,vechile_id,vechile_type,capacity,fuel_capacity,fuel_type):
        self.vechile_id=vechile_id
        self.vechile_type=vechile_type
        self.capacity=int(capacity)
        self.fuel_capacity=fuel_capacity
        self.fuel_type=fuel_type

    def display_vechile(self):
        print("Vechile id: ",self.vechile_id)
        print("Vechile type: ",self.vechile_type)
        print("Capacity: ",self.capacity)
        print("Fuel capacity: ",self.fuel_capacity)
        print("Fuel Type: ",self.fuel_type)

    def update_capacity(self):
        new_capacity=int(input("Enter the new capacity: "))
        if new_capacity==self.capacity or new_capacity<0:
            print("Same capacity or invalid capacity")
        else:
            self.capacity=new_capacity
            print("Updated")

    def get_vechile_info(self):
        return self.vechile_id,self.vechile_type,self.capacity,self.fuel_capacity,self.fuel_type

    def get_capacity(self):
        return self.capacity

class trip:
    def __init__(self,trip_id,trip_date,route,vechile,hour,passengers,travel_time,fuel_used):
        self.trip_id=trip_id
        self.trip_date=trip_date
        self.route=route
        self.vechile=vechile
        self.hour=float(hour)
        self.passengers=int(passengers)
        self.travel_time=float(travel_time)
        self.fuel_used=float(fuel_used)

    def display_trip(self):
        print("Trip id: ",self.trip_id)
        print("Trip date: ",self.trip_date)
        print("Route:")
        self.route.display_route()
        print("Vechile:")
        self.vechile.display_vechile()
        print("Hour: ",self.hour)
        print("Passengers count: ",self.passengers)
        print("Travel time: ",self.travel_time)
        print("Fuel used: ",self.fuel_used)

    
    def get_trip_info(self):
        return self.trip_id,self.trip_date,self.route,self.vechile,self.hour,self.passengers,self.travel_time,self.fuel_used

    def get_passenger_count(self):
        return self.passengers

    def get_fuel_used(self):
        return self.fuel_used
    
class trasnportsystem:
    def __init__(self):
        self.routes=[]
        self.vechiles=[]
        self.trips=[]

    def add_route(self,route):
        self.routes.append(route)
        print("Route added successfully")

    def add_vechile(self,vechile):
        self.vechiles.append(vechile)
        print("Vechile added scuccesfully")

    def add_trip(self,trip):
        self.trips.append(trip)
        print("Trip added successfully")

    def remove_route(self):
        route=input("Enter the route id: ")
        found=False
        for x in self.routes:
            if x.route_id==route:
                self.routes.remove(x)
                print("Removed")
                found=True
                break
        if not found:
            print("Invaid id entered")       

    def remove_vechile(self):
        vechile_=input("Enter the vechile id: ")
        found=False
        for x in self.vechiles:
            if x.vechile_id==vechile_:
                self.vechiles.remove(x)
                print("Removed")
                found=True
                break
        if not found:
            print("Invaid id entered")       

    def get_route(self):
        id=input("Enter route id: ")
        for x in self.routes:
            if x.route_id==id:
                return x
        else:
            return None

    def get_vechile(self):
        id=input("Enter the vechile id: ")
        for x in self.vechiles:
            if x.vechile_id==id:
                return x
        else:
            return None

    def display_all_routes(self):
        for x in self.routes:
            x.display_route()

    def display_all_vechiles(self):
        for x in self.vechiles:
            x.display_vechile()

    def display_all_trips(self):
        for x in self.trips:
            x.display_trip()

    def add_trip(self):
        tripid = input("Enter the trip id: ")
        routeid = input("Enter the route id: ")

        route = None
        for x in self.routes:
            if x.route_id == routeid:
                route = x
                break
        if route is None:
            print("Invalid route id")
            return
        
        vehicleid = input("Enter the vehicle id: ")
        vehicle = None
        for x in self.vechiles:
            if x.vechile_id == vehicleid:
                vehicle = x
                break
        if vehicle is None:
            print("Invalid vehicle id")
            return
        trip_date = input("Enter the trip date: ")
        hour = float(input("Enter the trip hour: "))
        passengers = int(input("Enter the number of passengers: "))
        travel_time = float(input("Enter the travel time: "))
        fuel_used = float(input("Enter the fuel used: "))

        for x in self.vechiles:
            if passengers>vechile.capacity:
                print("More than capacity")
                return
        trip1=trip( tripid,
                trip_date,
                route,
                vehicle,
                hour,
                passengers,
                travel_time,
                fuel_used)
        self.trips.append(trip1)
        print("Trip added successfully")

system=trasnportsystem()
print(system.routes)
print(system.vechiles)
print(system.trips)

route1=route("R001", "Koteshwor-Kalanki", "Koteshwor", "Kalanki", 14)
route1.display_route()
route1.update_distance()
route1.get_route_info()
route1.get_route_length()

vechile1=vechile("V001","Bus",40,60,"Disel")
vechile1.display_vechile()
vechile1.update_capacity()
vechile1.get_vechile_info()
vechile1.get_capacity()

trip1=trip("T001","2026-10-05",route1,vechile1,6,35,35,4.2)
trip1.display_trip()
trip1.get_trip_info()
trip1.get_passenger_count()
trip1.get_fuel_used()


df = pd.read_csv("kathmandu transportation project/transport_data1.csv")
print("The first data",df.head())
print("The shape of data",df.shape)
print("Info of data frame: ",df.info())
print("Missing values in data frame are: ",df.isnull().sum())
print("The duplicated value is: ",df.duplicated().sum())

df["Date"] = pd.to_datetime(df["Date"])
print(df.describe())
group=df.groupby("Hour")["Passengers"].mean()
print("The peak hour is: ",group)
print("Peak hour:", group.idxmax())
print("Average passengers:", group.max())

passenger_grp=df.groupby("Route")["Passengers"].mean()
print(passenger_grp)
print("Highest demand route:", passenger_grp.idxmax())
print("Average passengers:", passenger_grp.max())

total_passenger=df.groupby("Route")["Passengers"].sum()
print(total_passenger)
print(total_passenger.idxmax())
print(total_passenger.max())

traffic_analysis=df.groupby("Route")["Travel_Time"].mean()
print("Traffic analysis: ",traffic_analysis)
print("Slowest route: ",traffic_analysis.idxmax())
print("Average travel time:", traffic_analysis.max())
print("Fastest route:", traffic_analysis.idxmin())
print("Average travel time:", traffic_analysis.min())

avg_hour=df.groupby("Hour")["Travel_Time"].mean()
print(avg_hour)
print("Highest traffic hour:", avg_hour.idxmax())
print("Average travel time:", avg_hour.max())
print("Lowest traffic hour:", avg_hour.idxmin())
print("Average travel time:", avg_hour.min())

df["Fuel_Efficiency"]=df["Distance"]/df["Fuel_Used"]
route_efficiency=df.groupby("Route")["Fuel_Efficiency"].mean()
print(route_efficiency)
print("Best fuel efficiency: ",route_efficiency.idxmax())
print("Worst fuel efficiency: ",route_efficiency.idxmin())

vechile_efficiency=df.groupby("Vehicle")["Fuel_Efficiency"].mean()
print(vechile_efficiency)
print("Best fuel efficiency: ",vechile_efficiency.idxmax())
print("Worst fuel efficiency: ",vechile_efficiency.idxmin())

df["Revenue"]=df["Distance"]*5* df["Passengers"]

route_revenue=df.groupby("Route")["Revenue"].sum()
print(route_revenue)

vechile_revenue=df.groupby("Vehicle")["Revenue"].sum()
print(vechile_revenue)

print("Heighst revenue route: ",route_revenue.idxmax())
print("Heighst revenue vechile: ",vechile_revenue.idxmax())
print("Lowest revenue route:", route_revenue.idxmin())

average_revenue = df["Revenue"].mean()
print("Average revenue per trip:", average_revenue)

vehicle_travel_time = df.groupby("Vehicle")["Travel_Time"].mean()
print(vehicle_travel_time)
print("Slowest vehicle:", vehicle_travel_time.idxmax())
print("Average travel time:", vehicle_travel_time.max())
print("Fastest vehicle:", vehicle_travel_time.idxmin())
print("Average travel time:", vehicle_travel_time.min())

df["Passenger_Score"]=(df["Passengers"]-df["Passengers"].min())/(df["Passengers"].max()-df["Passengers"].min())
df["Revenue_Score"]=(df["Revenue"]-df["Revenue"].min())/(df["Revenue"].max()-df["Revenue"].min())
df["Fuel_Efficiency_Score"]=(df["Fuel_Efficiency"]-df["Fuel_Efficiency"].min())/(df["Fuel_Efficiency"].max()-df["Fuel_Efficiency"].min())
df["Travel_Time_Score"]=(df["Travel_Time"].max()-df["Travel_Time"])/(df["Travel_Time"].max()-df["Travel_Time"].min())

passenger_score=df["Passenger_Score"]*0.30
revenue_score=df["Revenue_Score"]*0.30
fuel_efficiency_score=df["Fuel_Efficiency_Score"]*0.25
travel_time_score=df["Travel_Time_Score"]*0.15

vechile_performance_score=passenger_score+revenue_score+fuel_efficiency_score+travel_time_score
df["Vehicle_Performance_Score"] = vechile_performance_score
vehicle_performance = df.groupby("Vehicle")["Vehicle_Performance_Score"].mean()
print(vehicle_performance)
print("Best performing vehicle:", vehicle_performance.idxmax())
print("Best performance score:", vehicle_performance.max())
print("Worst performing vehicle:", vehicle_performance.idxmin())
print("Worst performance score:", vehicle_performance.min())

passenger_mean=np.mean(df["Passengers"])
print("Passenger mean: ",passenger_mean)
passenger_std=np.std(df["Passengers"])
print("Passenger standard deviation: ",passenger_std)

route_standartd=df.groupby("Route")["Passengers"].std()
print(route_standartd)
print("Relatively Stable Route is: ",route_standartd.idxmin())
print("Highly variable route is: ",route_standartd.idxmax())

route_passengers=df.groupby("Route")["Passengers"].sum()
total_passengers = df["Passengers"].sum()
route_percentage=(route_passengers/total_passenger)*100
print(route_percentage)
print("Total percentage:", route_percentage.sum())

mean_passnenger=np.mean(df["Passengers"])
std_passenger=np.std(df["Passengers"])
x=df["Passengers"]
z=(x-mean_passnenger)/std_passenger
for i in range(len(z)):
    if abs(z.iloc[i]) > 3:
        print("Row", i, "Strong anomaly")
    elif abs(z.iloc[i]) > 2:
        print("Row", i, "Potential anomaly")

route_passneger=df.groupby("Route")["Passengers"].mean()
plt.bar(route_passneger.index,route_passneger.values)
plt.xlabel("Passengers")
plt.ylabel("Mean_Passengers")
plt.title("Average Passengers By route demamad")
plt.tight_layout()
plt.show()

peak_passenger_demand=df.groupby("Hour")["Passengers"].mean()
x = peak_passenger_demand.index
y = peak_passenger_demand.values
plt.plot(x,y)
plt.xlabel("Hour")
plt.ylabel("Peak passenger demand")
plt.title("Hour vs peak passenger demand")
plt.show()

travel_time_route=df.groupby("Route")["Travel_Time"].mean()
x=travel_time_route.index
y=travel_time_route.values
plt.barh(x,y)
plt.xlabel("Route")
plt.ylabel("Travel TIme")
plt.title("Route Vs Travel Time")
plt.show()

fuel_efficiency=df.groupby("Route")["Fuel_Efficiency"].mean()
x=fuel_efficiency.index
y=fuel_efficiency.values
plt.barh(x,y)
plt.xlabel("Fuel Efficiency")
plt.ylabel("Route")
plt.title("Fuel Efficiency vs Route")
plt.show()

revenue_route=df.groupby("Route")["Revenue"].mean()
x=revenue_route.index
y=revenue_route.values
plt.barh(x,y)
plt.xlabel("Revenue")
plt.ylabel("Route")
plt.title("Revenue Vs Route")
plt.show()

vechile_performance=df.groupby("Vehicle")["Vehicle_Performance_Score"].mean()
x=vechile_performance_score.index
y=vechile_performance_score.values
plt.barh(x,y)
plt.xlabel("Vechiles")
plt.ylabel("Vechile performance score")
plt.title("Vechile vs Vechile Performance Score")
plt.show()

x = range(len(z))
y = z
plt.scatter(x, y)
plt.axhline(2, linestyle="--")
plt.axhline(-2, linestyle="--")
plt.axhline(3, linestyle="--")
plt.axhline(-3, linestyle="--")
plt.axhline(0, linestyle="-")
plt.xlabel("Trip / Row")
plt.ylabel("Z-score")
plt.title("Passenger Anomaly Detection using Z-score")
plt.show()

passenger_demand = df.groupby("Route")["Passengers"].mean()
fuel_efficiency = df.groupby("Route")["Fuel_Efficiency"].mean()
travel_time = df.groupby("Route")["Travel_Time"].mean()
revenue = df.groupby("Route")["Revenue"].sum()

passenger_norm=(passenger_demand-passenger_demand.min())/(passenger_demand.max()-passenger_demand.min())
fuel_efficiency_norm=(fuel_efficiency-fuel_efficiency.min())/(fuel_efficiency.max()-fuel_efficiency.min())
revenue_norm=(revenue-revenue.min())/(revenue.max()-revenue.min())
travel_time_norm=(travel_time.max()-travel_time)/(travel_time.max()-travel_time.min())

new_score = (passenger_norm * 0.30) + (revenue_norm * 0.30) + (fuel_efficiency_norm * 0.25) + (travel_time_norm * 0.15)

route_ranking = new_score.sort_values(ascending=False)
print(route_ranking)
print("Best route:", route_ranking.idxmax())
print("Best score:", route_ranking.max())
print("Worst route:", route_ranking.idxmin())
print("Worst score:", route_ranking.min())

demand_score=(passenger_demand-passenger_demand.min())/(passenger_demand.max()-passenger_demand.min())

demand_ranking=demand_score.sort_values(ascending=False)

print(demand_score)
print(demand_ranking)
print("Highest demand route:",demand_ranking.idxmax())
print("Highest demand score:",demand_ranking.max())
print("Lowest demand route:",demand_ranking.idxmin())
print("Lowest demand score:",demand_ranking.min())

route_analysis=pd.DataFrame({
    "Passenger_Demand":passenger_demand,
    "Travel_Time":travel_time,
    "Demand_Score":demand_score
})
high_demand_traffic=route_analysis[
    (route_analysis["Demand_Score"]>=0.5) &
    (route_analysis["Travel_Time"]>=route_analysis["Travel_Time"].mean())
]

print(high_demand_traffic)
high_demand_traffic=high_demand_traffic.sort_values(by="Demand_Score",ascending=False)
print(high_demand_traffic)
vehicle_ranking=vehicle_performance.sort_values(ascending=False)
print(vehicle_ranking)
print("Best performing vehicle:",vehicle_ranking.idxmax())
print("Best performance score:",vehicle_ranking.max())
print("Worst performing vehicle:",vehicle_ranking.idxmin())
print("Worst performance score:",vehicle_ranking.min())
vehicle_priority=pd.DataFrame({
    "Performance_Score":vehicle_performance,
    "Average_Travel_Time":vehicle_travel_time,
    "Fuel_Efficiency":vechile_efficiency
})
vehicle_priority=vehicle_priority.sort_values(by="Performance_Score",ascending=False)

print(vehicle_priority)

while True:
    print("1.Route Analysis")
    print("2.Peak Hour Analysis")
    print("3.Passenger Analysis")
    print("4.Traffic Analysis")
    print("5.Fuel Aanalysis")
    print("6.Revenuw Analysis")
    print("7.Vechile Performance")
    print("8.Route Efficiency")
    print("9.Generate Graphs")
    print("10.Full Report")
    print("0.Exit")

    choice=int(input("Enter your choice from (0-10)"))
    if choice==1:
        print(passenger_demand)
        print("Highest demand route:",passenger_demand.idxmax())
        print("Highest average passengers:",passenger_demand.max())
        print("Lowest demand route:",passenger_demand.idxmin())
        print("Lowest average passengers:",passenger_demand.min())

    elif choice==2:
        print(peak_passenger_demand)
        print("Peak passenger hour:",peak_passenger_demand.idxmax())
        print("Average passengers:",peak_passenger_demand.max())

    elif choice==3:
        print("Mean passengers:",passenger_mean)
        print("Standard deviation:",passenger_std)

    elif choice==4:
        print(travel_time)
        print("Slowest route:",travel_time.idxmax())
        print("Slowest average travel time:",travel_time.max())
        print("Fastest route:",travel_time.idxmin())
        print("Fastest average travel time:",travel_time.min())

    elif choice==5:
        print(fuel_efficiency)
        print("Best fuel efficient route:",fuel_efficiency.idxmax())
        print("Best fuel efficiency:",fuel_efficiency.max())
        print("Worst fuel efficient route:",fuel_efficiency.idxmin())
        print("Worst fuel efficiency:",fuel_efficiency.min())
        print(vechile_efficiency)
        print("Best fuel efficient vehicle:",vechile_efficiency.idxmax())
        print("Worst fuel efficient vehicle:",vechile_efficiency.idxmin())

    elif choice==6:
        print(route_revenue)
        print("Highest revenue route:",route_revenue.idxmax())
        print("Highest route revenue:",route_revenue.max())
        print("Lowest revenue route:",route_revenue.idxmin())
        print("Lowest route revenue:",route_revenue.min())
        
    elif choice==7:
        print(vehicle_performance)
        print("Best performing vehicle:",vehicle_performance.idxmax())
        print("Best performance score:",vehicle_performance.max())
        print("Worst performing vehicle:",vehicle_performance.idxmin())
        print("Worst performance score:",vehicle_performance.min())

    elif choice==8:
        print(route_ranking)
        print("Best route:",route_ranking.idxmax())
        print("Best route score:",route_ranking.max())
        print("Worst route:",route_ranking.idxmin())
        print("Worst route score:",route_ranking.min())
        

    elif choice==9:
        x=route_passengers.index
        y=route_passengers.values
        plt.figure(figsize=(10,6))
        plt.bar(x,y)
        plt.xlabel("Route")
        plt.ylabel("Average Passengers")
        plt.title("Average Passenger Demand by Route")
        plt.xticks(rotation=45,ha="right")
        plt.tight_layout()
        plt.show()

        x=peak_passenger_demand.index
        y=peak_passenger_demand.values
        plt.figure(figsize=(10,6))
        plt.plot(x,y)
        plt.xlabel("Hour")
        plt.ylabel("Average Passenger Demand")
        plt.title("Hour vs Average Passenger Demand")
        plt.show()

        x=travel_time.index
        y=travel_time.values
        plt.figure(figsize=(10,6))
        plt.barh(x,y)
        plt.xlabel("Travel Time")
        plt.ylabel("Route")
        plt.title("Route vs Travel Time")
        plt.tight_layout()
        plt.show()

        x=fuel_efficiency.index
        y=fuel_efficiency.values
        plt.figure(figsize=(10,6))
        plt.barh(x,y)
        plt.xlabel("Fuel Efficiency")
        plt.ylabel("Route")
        plt.title("Fuel Efficiency vs Route")
        plt.tight_layout()
        plt.show()

        x=route_revenue.index
        y=route_revenue.values
        plt.figure(figsize=(10,6))
        plt.barh(x,y)
        plt.xlabel("Revenue")
        plt.ylabel("Route")
        plt.title("Revenue vs Route")
        plt.tight_layout()
        plt.show()

        x=vehicle_performance.index
        y=vehicle_performance.values
        plt.figure(figsize=(10,6))
        plt.bar(x,y)
        plt.xlabel("Vehicle")
        plt.ylabel("Performance Score")
        plt.title("Average Vehicle Performance Score")
        plt.xticks(rotation=45,ha="right")
        plt.tight_layout()
        plt.show()

        x=range(len(z))
        y=z
        plt.figure(figsize=(10,6))
        plt.scatter(x,y)
        plt.axhline(2,linestyle="--")
        plt.axhline(-2,linestyle="--")
        plt.axhline(3,linestyle="--")
        plt.axhline(-3,linestyle="--")
        plt.axhline(0,linestyle="-")
        plt.xlabel("Trip / Row")
        plt.ylabel("Z-score")
        plt.title("Passenger Anomaly Detection using Z-score")
        plt.show()

    elif choice==10:
        print("========== TRANSPORT INTELLIGENCE ==========")
        print("Best route:",route_ranking.idxmax())
        print("Best route score:",route_ranking.max())
        print("Highest demand route:",demand_ranking.idxmax())
        print("Peak passenger hour:",peak_passenger_demand.idxmax())
        print("Slowest route:",travel_time.idxmax())
        print("Best fuel efficient route:",fuel_efficiency.idxmax())
        print("Highest revenue route:",route_revenue.idxmax())
        print("Best performing vehicle:",vehicle_ranking.idxmax())
        print("Worst performing vehicle:",vehicle_ranking.idxmin())
        print("High demand + high traffic routes:",high_demand_traffic.index.tolist())

    elif choice==0:
        print("Program exited")
        break

    else:
        print("Invalid choice")
df.to_csv("kathmandu_transport_analysis.csv", index=False)