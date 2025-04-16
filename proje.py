import pandas as pd
import mysql.connector  # Required later if inserting into MySQL
import matplotlib.pyplot as plt
import seaborn as sns
#  Load dataset
df = pd.read_csv("uae_used_cars_10k.csv")
print(" Dataset loaded successfully.")

#  Remove duplicate rows
df.drop_duplicates(inplace=True)
print(f" Removed duplicates. Rows remaining: {df.shape[0]}")

#  Fill missing values with appropriate defaults
df.fillna({
    'Price': df['Price'].median(),                # Replace missing prices with median
    'Mileage': df['Mileage'].median(),            # Replace missing mileage with median
    'Fuel': 'Unknown',                            # Replace missing fuel type with 'Unknown'
    'Transmission': 'Unknown',                    # Replace missing transmission with 'Unknown'
    'Year': df['Year'].mode()[0]                  # Replace missing year with most common year
}, inplace=True)

#  Normalize data types
df['Price'] = pd.to_numeric(df['Price'])
df['Mileage'] = pd.to_numeric(df['Mileage'])
df['Year'] = pd.to_numeric(df['Year'])

#  Rename columns for clarity and consistency
df.rename(columns={
    'Year': 'Manufacture_Year',
    'Description': 'About',
    'Fuel Type': 'Fuel_Type'
}, inplace=True)

#  Filter out unrealistic data
# Remove cars with 0 mileage and year > 2025 (future data or errors)
df = df[~((df['Mileage'] == 0) & (df['Manufacture_Year'] > 2025))]

#  Drop any remaining rows with missing values
df.dropna(inplace=True)

#  Optional: View cleaned DataFrame info
print(" Cleaned Dataset Info:")
print(df.info())

#  Preview the cleaned dataset
# print(" Cleaned Dataset Sample:")
# print(df.head())

print(df[['Price', 'Mileage', 'Manufacture_Year']].describe())

# Count of unique car brands and models
print(f" Total Unique Brands: {df['Make'].nunique()}")
print(f" Total Unique Models: {df['Model'].nunique()}")

#  Top 10 Most Listed Car Models
print(" Top 10 Most Listed Car Models:")
top_models = df.groupby(['Make', 'Model']).size().sort_values(ascending=False).head(10)
print(top_models)

#  Cars Offering the Best Resale Value (Lowest Price-to-Mileage Ratio)
df['Resale_Value_Score'] = df['Price'] / df['Mileage']
best_resale_value = df[df['Mileage'] > 0].sort_values(by='Resale_Value_Score').head(10)
print(" Top 10 Best Resale Value Cars (Lowest Price/Mileage):")
print(best_resale_value[['Make', 'Model', 'Price', 'Mileage', 'Resale_Value_Score']])

#  Transmission distribution
trans_dist = df['Transmission'].value_counts()
print(" Transmission Type Distribution:")
print(trans_dist)

#  Fuel type distribution
fuel_dist = df['Fuel_Type'].value_counts()
print(" Fuel Type Distribution:")
print(fuel_dist)

# Top 10 car models bar plot
plt.figure(figsize=(10, 6))
top_models.plot(kind='barh', color='skyblue')
plt.title('Top 10 Most Listed Car Models')
plt.xlabel('Number of Listings')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Transmission Pie Chart
plt.figure(figsize=(6, 6))
trans_dist.plot(kind='pie', autopct='%1.1f%%')
plt.title('Transmission Type Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Fuel Type Pie Chart
plt.figure(figsize=(6, 6))
fuel_dist.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title('Fuel Type Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()


conn = mysql.connector.connect(
    host="localhost",         # or your database IP address
    user="root",     # MySQL username
    password="Uday", # MySQL password
    database="uday"  # Optional: If you want to connect to a specific database
)


cursor=conn.cursor()

insert_query="""
INSERT INTO used_cars (Make, Model, Manufacture_year, Price, Mileage, Fuel_type, Transmission,Color,Location,About)
VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)
"""
data_to_insert=[
    (
        row['Make'],
        row['Model'],
        int(row['Manufacture_Year']),
        float(row['Price']),
        int(row['Mileage']),
        row['Fuel_Type'],
        row['Transmission'],
        row['Color'],
        row['Location'],
        row['About']
    )
    for _,row in df.iterrows()
]
cursor.executemany(insert_query,data_to_insert)
cursor.close()
conn.commit()