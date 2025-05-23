import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")  # Suppress warnings for cleaner output

# Step 1: Create a synthetic dataset (mimicking BPS rice price trends)
data = {
    'Month Index': [1, 2, 3, 4, 5],  # Represents months (e.g., Jan-May)
    'Price (Rp/kg)': [12000, 12500, 13000, 13500, 14000]  # Realistic rice prices
}
df = pd.DataFrame(data)

# Step 2: Prepare data for training
X = df[['Month Index']].values  # Input feature (month index)
y = df['Price (Rp/kg)'].values   # Target (rice price)

# Step 3: Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Function to predict rice price based on user input
def predict_rice_price(month_index):
    month_index = np.array([[month_index]])  # Reshape for sklearn
    predicted_price = model.predict(month_index)[0]
    return predicted_price

# Step 5: Interactive loop for predictions
print("Prediksi Harga Beras (Rice Price Predictor)")
while True:
    user_input = input("Masukkan indeks bulan (1-12) atau 'keluar' untuk berhenti: ")
    if user_input.lower() == 'keluar':
        print("Keluar dari program...")
        break
    try:
        month_index = float(user_input)
        if month_index <= 0 or month_index > 12:
            print("Masukkan angka antara 1 dan 12.")
            continue
        price = predict_rice_price(month_index)
        print(f"Prediksi harga beras untuk bulan {month_index:.0f}: Rp {price:.2f}/kg")
    except ValueError:
        print("Input tidak valid. Masukkan angka atau 'keluar'.")