import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

df = pd.read_csv("iris.csv")

features = df[['petal.length', 'petal.width']]
labels = df.variety

features = features.to_numpy()
labels = labels.to_numpy()

np.set_printoptions(suppress=True)

def distance(p0, p1):
  'Computes squared euclidean distance'
  return np.sum( (p0-p1)**2 )

test_feature = np.array([1.9,0.9]) #A hypothetcal seed's feature
known_features = features[:,0:2] #grab first two features
dists = np.array([distance(t, test_feature) for t in known_features])

nearest = dists.argmin()

def nn_classify_sample(training_set, training_labels, new_example):
  dists = np.array([distance(t, new_example) for t in training_set])
  nearest = dists.argmin()
  return training_labels[nearest]

def nn_classify(train_data, train_features, features):
  num_result = features[:,0].size
  result = np.ones(num_result)
  for i in range(0,num_result):
    result[i] = nn_classify_sample(train_data[:,0:2], train_features, features[i])
  return result


h = 0.1 #step size in the mesh
x_min, x_max = features[:, 0].min() - 0.2, features[:, 0].max() + 0.2
y_min, y_max = features[:, 1].min() - 0.2, features[:, 1].max() + 0.2
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
test_features = np.array([xx.ravel(), yy.ravel()]).transpose()

#map string labels to numerical
label_to_int = {'Setosa': 0, 'Versicolor': 1, 'Virginica': 2}
numerical_labels = [label_to_int[label] for label in labels]

z = nn_classify(features, numerical_labels, test_features)

z = z.reshape(xx.shape)
fig = plt.figure()
plt.pcolormesh(xx, yy, z)

plt.scatter(features[:, 0], features[:, 1], c=numerical_labels, edgecolor='k', s=60)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Outcome classification")
plt.xlabel("Area")
plt.ylabel("Compactness")

z = z.reshape(xx.shape)
fig = plt.figure()
plt.pcolormesh(xx, yy, z)

plt.scatter(features[:, 0], features[:, 1], c=numerical_labels, edgecolor='k', s=20)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Outcome classification (nearest neighbor)")

def graphClassifier2D(X,Y, classifier):

  cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF', '#AAFFFF'])
  cmap_bold  = ListedColormap(['#FF0000', '#0000FF', '#00FFFF'])

  h = 0.1
  x_min, x_max = X[:, 0].min() - 0.2, X[:, 0].max() + 0.2
  y_min, y_max = X[:, 1].min() - 0.2, X[:, 1].max() + 0.2
  xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
  test_features = np.array([xx.ravel(), yy.ravel()]).transpose()
  z = classifier(X, Y, test_features)

  z = z.reshape(xx.shape)
  fig = plt.figure()
  plt.pcolormesh(xx, yy, z, cmap=cmap_light)

  plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_bold, edgecolor='k', s=20)
  plt.xlim(xx.min(), xx.max())
  plt.ylim(yy.min(), yy.max())
  plt.title("Outcome classification (nearest neighbor)")
  plt.show()

graphClassifier2D(features, numerical_labels, nn_classify)


#Function that wraps up the classification and graphing with nicer colors
def graphClassifier2D(X,Y, classifier, normalize=False):
  # Create color maps
  cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF', '#AAFFFF'])
  cmap_bold  = ListedColormap(['#FF0000', '#0000FF', '#00FFFF'])

  if normalize:
    X -= X.mean(axis=0) # subtract the mean for each feature
    X /= X.std(axis=0)  # divide each feature by its standard deviation

  h = 0.1  # step size in the mesh
  x_min, x_max = X[:, 0].min() - 0.2, X[:, 0].max() + 0.2
  y_min, y_max = X[:, 1].min() - 0.2, X[:, 1].max() + 0.2
  xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
  test_features = np.array([xx.ravel(), yy.ravel()]).transpose()
  z = classifier(X, Y, test_features)

  z = z.reshape(xx.shape)
  fig = plt.figure()
  plt.pcolormesh(xx, yy, z, cmap=cmap_light)

  plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_bold, edgecolor='k', s=20)
  plt.xlim(xx.min(), xx.max())
  plt.ylim(yy.min(), yy.max())
  plt.title("Outcome classification (nearest neighbor)")
  plt.xlabel("Area (Normalized)")
  plt.ylabel("Compactness (Normalized)")
  plt.show()

graphClassifier2D(features, numerical_labels, nn_classify, True)