import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully! Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: File not found. Please check the path.")
        return None

def clean_data(df):
    print("\nCleaning data...")
    before_rows = df.shape[0]
    df = df.drop_duplicates()
    df = df.dropna()
    after_rows = df.shape[0]
    print(f"Removed {before_rows - after_rows} rows (missing or duplicate).")
    return df

def summarize_data(df):
    print("\nDataset Summary:")
    print(df.describe())

def main():
    file_path = "sample_data.csv"
    
    df = load_data(file_path)
    if df is None:
        return
    
    df = clean_data(df)
    
    summarize_data(df)
    
    cleaned_file = "cleaned_data.csv"
    df.to_csv(cleaned_file, index=False)
    print(f"\nCleaned data saved as: {cleaned_file}")

if __name__ == "__main__":
    main()
