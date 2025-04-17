import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(df):
    print(df[['Price', 'Mileage', 'Manufacture_Year']].describe())

    print(f"Total Unique Brands: {df['Make'].nunique()}")
    print(f"Total Unique Models: {df['Model'].nunique()}")

    print("Top 10 Most Listed Car Models:")
    top_models = df.groupby(['Make', 'Model']).size().sort_values(ascending=False).head(10)
    print(top_models)

    df['Resale_Value_Score'] = df['Price'] / df['Mileage']
    best_resale = df[df['Mileage'] > 0].sort_values(by='Resale_Value_Score').head(10)

    print("Top 10 Best Resale Value Cars (Lowest Price/Mileage):")
    print(best_resale[['Make', 'Model', 'Price', 'Mileage', 'Resale_Value_Score']])

    print("Transmission Type Distribution:")
    trans_dist = df['Transmission'].value_counts()
    print(trans_dist)

    print("Fuel Type Distribution:")
    fuel_dist = df['Fuel_Type'].value_counts()
    print(fuel_dist)

    # Plots
    plt.figure(figsize=(10, 6))
    top_models.plot(kind='barh', color='skyblue')
    plt.title('Top 10 Most Listed Car Models')
    plt.xlabel('Number of Listings')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 6))
    trans_dist.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Transmission Type Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 6))
    fuel_dist.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    plt.title('Fuel Type Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
