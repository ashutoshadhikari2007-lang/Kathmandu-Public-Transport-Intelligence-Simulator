# Kathmandu Public Transport Intelligence Simulator

A Python-based public transport data analysis and intelligence simulator focused on simulated Kathmandu public transportation data.

This project combines **Object-Oriented Programming, Pandas, NumPy, and Matplotlib** to analyze transport data and generate useful insights about routes, passengers, traffic, fuel usage, revenue, and vehicle performance.

> **Note:** This project uses simulated data for learning and analysis purposes. It is not based on real-time Kathmandu public transport data.

## Project Goals

The main goal of this project is to simulate a public transport analysis system that can answer questions such as:

* Which route has the highest passenger demand?
* Which hours have the highest passenger activity?
* Which routes have higher travel times?
* Which routes are more fuel efficient?
* Which routes generate more revenue?
* Which vehicles perform better?
* Which routes have high demand and high traffic?
* Which trips contain potential anomalies?

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Object-Oriented Programming
* CSV Data

## Project Structure

### Phase 1 — OOP Foundation

The project starts with an object-oriented transport system.

Main classes:

* `Route`
* `Vehicle`
* `Trip`
* `TransportSystem`

These classes are used to manage routes, vehicles, and trips.

### Phase 2 — Data Analysis

The simulated CSV data is analyzed using Pandas and NumPy.

Main analyses include:

* Peak Hour Analysis
* Route Demand Analysis
* Passenger Analysis
* Travel Time Analysis
* Traffic by Hour
* Fuel Efficiency Analysis
* Revenue Analysis
* Vehicle Performance Analysis
* Mean and Median
* Standard Deviation
* Percentage Analysis
* Z-score Analysis
* Anomaly Detection

## Phase 3 — Data Visualization

Matplotlib is used to visualize the analyzed data.

Graphs include:

* Passenger Demand by Route
* Passenger Demand by Hour
* Travel Time by Route
* Fuel Efficiency by Route
* Revenue by Route
* Vehicle Performance
* Passenger Anomaly Detection

## Phase 4 — Intelligence and Ranking

The project goes beyond basic analysis by creating scores and rankings.

### Route Efficiency Score

Routes are evaluated using:

* Passenger Demand
* Revenue
* Fuel Efficiency
* Travel Time

The metrics are normalized and combined using weighted scores.

Weights used:

* Passenger Demand — 30%
* Revenue — 30%
* Fuel Efficiency — 25%
* Travel Time — 15%

This produces a Route Efficiency Score that can be used to rank routes.

### Demand Score

A normalized demand score is calculated to identify routes with higher passenger demand.

### High Demand + High Traffic

The project identifies routes where:

* Passenger demand is relatively high
* Average travel time is relatively high

These routes can be considered higher-priority routes in the simulation.

### Vehicle Ranking

Vehicles are ranked using their calculated performance scores.

## Menu System

The final simulator provides a menu-based interface:

```text
1. Route Analysis
2. Peak Hour Analysis
3. Passenger Analysis
4. Traffic Analysis
5. Fuel Analysis
6. Revenue Analysis
7. Vehicle Performance
8. Route Efficiency
9. Generate Graphs
10. Full Report
0. Exit
```

## Dataset

The project uses a simulated CSV dataset containing fields such as:

* Date
* Route
* Vehicle
* Hour
* Passengers
* Distance
* Travel_Time
* Fuel_Used

Additional calculated columns are generated during analysis, including:

* Fuel_Efficiency
* Revenue
* Z_Score
* Anomaly
* Strong_Anomaly
* Route_Efficiency_Score

The final analyzed dataset can also be exported as a new CSV file.

## Key Concepts Practiced

This project helped practice:

* Python OOP
* Classes and Objects
* Composition
* Lists and Object Management
* Pandas GroupBy
* Aggregation
* Data Cleaning and Inspection
* NumPy Statistics
* Normalization
* Z-score
* Anomaly Detection
* Data Visualization
* Data Ranking
* Weighted Scoring
* CSV File Handling
* Menu-driven Programs

## Learning Outcome

This project was created as a practical learning project to understand how Python, data analysis libraries, statistics, visualization, and OOP can be combined into a single data-driven application.

## Future Improvements

Possible future improvements include:

* Larger and more realistic datasets
* More advanced anomaly detection
* Interactive dashboards
* Database integration
* Real-time transport data
* More detailed vehicle analysis
* Automated report generation

## Author

**Ashutosh Adhikari**

BCA Student | Python | Data Analysis | AI/ML Learning
