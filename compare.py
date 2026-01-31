from sklearn.tree import DecisionTreeClassifier
from decision_tree import DecisionTree
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar dados
df = pd.read_csv('data/diabetes.csv')
X = df.drop('Outcome', axis=1).values
y = df['Outcome'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sua implementação
print("🌲 SUA IMPLEMENTAÇÃO:")
my_tree = DecisionTree(max_depth=5, min_samples_split=10, min_samples_leaf=5)
my_tree.fit(X_train, y_train)
my_pred = my_tree.predict(X_test)
my_accuracy = accuracy_score(y_test, my_pred)
print(f"Acurácia: {my_accuracy:.4f}\n")

# Scikit-learn
print("🔬 SCIKIT-LEARN:")
sk_tree = DecisionTreeClassifier(max_depth=5, min_samples_split=10, 
                                 min_samples_leaf=5, random_state=42)
sk_tree.fit(X_train, y_train)
sk_pred = sk_tree.predict(X_test)
sk_accuracy = accuracy_score(y_test, sk_pred)
print(f"Acurácia: {sk_accuracy:.4f}\n")

print(f"📊 Diferença: {abs(my_accuracy - sk_accuracy):.4f}")