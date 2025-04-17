import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")

    df.drop_duplicates(inplace=True)
    print(f"Removed duplicates. Rows remaining: {df.shape[0]}")

    df.fillna({
        'Price': df['Price'].median(),
        'Mileage': df['Mileage'].median(),
        'Fuel': 'Unknown',
        'Transmission': 'Unknown',
        'Year': df['Year'].mode()[0]
    }, inplace=True)

    df['Price'] = pd.to_numeric(df['Price'])
    df['Mileage'] = pd.to_numeric(df['Mileage'])
    df['Year'] = pd.to_numeric(df['Year'])

    df.rename(columns={
        'Year': 'Manufacture_Year',
        'Description': 'About',
        'Fuel Type': 'Fuel_Type'
    }, inplace=True)

    df = df[~((df['Mileage'] == 0) & (df['Manufacture_Year'] > 2025))]
    df.dropna(inplace=True)

    print("Cleaned Dataset Info:")
    print(df.info())

    return df
