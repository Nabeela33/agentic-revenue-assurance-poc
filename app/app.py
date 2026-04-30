from utils.data_loader import load_data

data = load_data()

for key, df in data.items():
    print(f"{key}: {df.shape}")
