import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Price": [100, 102, 104, 103, 105, 107, 110]
}

df = pd.DataFrame(data)

X = df[["Day"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

future_day = np.array([[8]])
predicted_price = model.predict(future_day)

print("Predicted price for day 8:", predicted_price[0])

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Stock Price Prediction")
plt.show()