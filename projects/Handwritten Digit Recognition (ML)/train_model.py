import joblib
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# Load data from https://www.openml.org/d/554
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)
X = X / 255.  # Normalize pixel values

# Split data for training
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.2)

# Train a simple Multi-layer Perceptron Classifier
mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=20, alpha=1e-4,
                    solver='sgd', verbose=10, random_state=1,
                    learning_rate_init=.1)

print("Training model...")
mlp.fit(X_train, y_train)

print(f"Training set score: {mlp.score(X_train, y_train):.3f}")
print(f"Test set score: {mlp.score(X_test, y_test):.3f}")

# Save the trained model
joblib.dump(mlp, 'mnist_model.pkl')
print("Model saved as mnist_model.pkl")