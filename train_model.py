import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import pickle

# Dataset Diabetes
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
cols = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
df = pd.read_csv(url, names=cols)

X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_dt = DecisionTreeClassifier()
model_svc = SVC()

model_dt.fit(X_train_scaled, y_train)
model_svc.fit(X_train_scaled, y_train)

models = [model_dt, model_svc]

# Simpan model dan scaler
pickle.dump(models, open('model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))