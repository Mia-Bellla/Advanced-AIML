# K-Nearest Neighbors on Iris Dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Split dataset into training (70%) and testing (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Create KNN model (k=5)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predictions
y_pred = knn.predict(X_test)

# Print predictions with correctness check
print("=== Prediction Results ===")
for i in range(len(y_test)):
    actual = target_names[y_test[i]]
    predicted = target_names[y_pred[i]]
    if y_test[i] == y_pred[i]:
        print(f"Sample {i}:  Correct | Predicted: {predicted}, Actual: {actual}")
    else:
        print(f"Sample {i}:  Wrong | Predicted: {predicted}, Actual: {actual}")

# Accuracy
accuracy = knn.score(X_test, y_test)
print(f"\nOverall Accuracy: {accuracy * 100:.2f}%")
