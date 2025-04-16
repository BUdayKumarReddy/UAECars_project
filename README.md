# UAECars_project
# UAE Used Cars Data Analysis 📊🚗

This project focuses on the **analysis and visualization** of a real-world dataset containing details of **10,000+ used cars in the UAE**. It also demonstrates **data cleaning**, **statistical analysis**, **visualization**, and **data migration to a MySQL database** using Python.

## 📁 Dataset
The dataset used is: **uae_used_cars_10k.csv**  
It contains fields like:
- `Make` – Car brand
- `Model` – Car model
- `Year` – Year of manufacture
- `Price` – Price of the car
- `Mileage` – Distance driven
- `Fuel Type` – Fuel category
- `Transmission` – Manual/Automatic

## 🔧 Technologies Used
- **Python** – Data analysis & scripting
- **Pandas** – Data processing
- **Matplotlib & Seaborn** – Data visualization
- **MySQL** – Database for storing cleaned data
- **mysql-connector-python** – Python-MySQL integration
  
## 📊 Features & Analysis Performed

✅ **Data Cleaning:**
- Removed duplicates
- Handled missing values using median/mode/defaults
- Normalized column names and data types
- Filtered out unrealistic values (e.g. 0 mileage with future years)

✅ **Descriptive Statistics:**
- Summary statistics of price, mileage, and manufacture year
- Count of unique brands and models

✅ **Insights Extracted:**
- 🔝 Top 10 Most Listed Car Models
- 💰 Top 10 Best Resale Value Cars (Lowest Price-to-Mileage Ratio)
- ⚙️ Transmission Type Distribution
- ⛽ Fuel Type Distribution

✅ **Visualizations:**
- Bar chart of most listed car models
- Pie charts for transmission and fuel type distribution

✅ **MySQL Integration:**
- Connected to a local MySQL database
- Inserted cleaned data into the `used_cars` table using `executemany()`

## 🗃️ Database Schema

Table: `used_cars`

| Column            | Data Type   |
|------------------|-------------|
| Make             | VARCHAR     |
| Model            | VARCHAR     |
| Manufacture_year | INT         |
| Price            | FLOAT       |
| Mileage          | INT         |
| Fuel_type        | VARCHAR     |
| Transmission     | VARCHAR     |
| Color            | VARCHAR     |
| Location         | VARCHAR     |
| About            | TEXT        |

