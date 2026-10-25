## second model: random forest
import pandas as pd
from sklearn.model_selection import train_test_split

nls = pd.read_csv("Data/nls.csv")

X = nls[['HP', 'Torque (Nm)', 'Engine Size (L)']]
y = nls['Time']

X = X.fillna(X['Engine Size (L)'].median())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

## Now we can train a random forest regressor model on the training data
from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor(n_estimators = 100, random_state = 42).fit(X_train, y_train)

## Now we can evaluate the model on the test data
y_rf_pred = rf_model.predict(X_test)

## We use MAE, RMSE, and R^2 to evaluate the model performance
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mae_rf = mean_absolute_error(y_test, y_rf_pred)
from sklearn.metrics import root_mean_squared_error

rmse_rf = root_mean_squared_error(y_test, y_rf_pred)
r2_rf = r2_score(y_test, y_rf_pred)
print(f'Random Forest Model - MAE: {mae_rf:.4f}, RMSE: {rmse_rf:.4f}, R^2: {r2_rf:.4f}')    
