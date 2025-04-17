from Data_loader import load_and_clean_data
from Visualization import analyze_data
from Connector import insert_to_mysql

def main():
    file_path = "uae_used_cars_10k.csv"
    df = load_and_clean_data(file_path)
    analyze_data(df)
    insert_to_mysql(df)

if __name__ == "__main__":
    main()
