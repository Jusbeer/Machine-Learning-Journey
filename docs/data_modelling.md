# 📊 Chapter: Data Modeling

After visualizing and cleaning the dataset, the next step in our machine learning journey is choosing the right **machine learning model**.

Think of a model like a recipe or blueprint — it helps the system understand patterns in the data and make predictions or decisions. But just like building a house, we do not jump straight into action. We first need to understand what we are building, why, and how.

---

## 🎯 What Is a Machine Learning Model?

A machine learning model is a mathematical system that maps **inputs** to **outputs**. It's trained using historical data so it can learn patterns and make future predictions.

Depending on the kind of data and task, there are **three main types** of machine learning approaches:

---

## 1. Supervised Learning

As we know Supervised learning, maps an input to an output based on a series of example **input-output** pairs. To understand this chapter better, supervised learning is when we have a dataset with any number of independent variables also called feature or input variables and a dependent variable also called Target or output variable that is supposed to be predicted

### Example:
Predicting the price of a house, the output variable here is the price which is based on features of the house like the square footage, location, and construction year.

![Picture1](./Data%20Modeling%20pictures/Picture1.jpg)

For this chapter, supervised learning has 2 sub-categorised:
### 🔹 Regression (Predicting Numbers):
In the Regression model, we want to predict a **continuous numeric** target variable from a given input variable. Using the example before, this could be predicting the price of a house by giving any number of features of the house. Then, we can determine their relationship to predict the final price of the house. Some of the most common types of regression model include:
#### 🔹 Linear & Polynomial Regression:
This is simply finding a line that fits the data its extensions include multiple linear regression that is finding a plane of best fit and polynomial regression that is finding a curve for best fit.

![Picture2](./Data%20Modeling%20pictures/Picture2.jpg)
We could use this model to predict the price of a house. The output variable 

#### 🔹 Decision Tree:
It looks something like the diagram below where each square is called a node. The more node you have, the more accurate your decision tree will be in general.

![Picture3](./Data%20Modeling%20pictures/Picture3.jpg)

#### 🔹 Random Forest:
These are assembling learning techniques that builds off over decision tree. It involves creating multiple decision trees using bootstrap data sets of original data and randomly selecting a subset of variables at each step of the decision tree. The model then selects the mode of all the predictions of each decision trees and by relying on the majority wins model it reduces the risk of error from individual tree.

![Picture4](./Data%20Modeling%20pictures/Picture4.jpg)

#### 🔹 Neural Networks:
This technique is quite popular and it is a multi layered model inspired by a human mind. Just like the neurons in our brain, the circle represents a node.  The left circles represent an input layer, the circles in the middle represents a hidden layer, and the right circles represents an output layer. Each node in the hidden layer represents a function that input goes through ultimately leading to the output circles.

![Picture5](./Data%20Modeling%20pictures/Picture5.jpg)

### 🔹 Classification (Predicting Categories):
In the Classification model we try to assign a **discrete** categorical label also called a class to a data point.
E.g. We may want to assign the label spam or no spam to an email based on its content or sender. But we can have 2 classes e.g. junk, primary, social, promotions, and updates.
Some of the most common types of classification models include:
#### 🔹 Logistic Regression:
This technique is similar to linear regression but it is used to model the probability of finite number of outcomes typically two.

![Picture6](./Data%20Modeling%20pictures/Picture6.jpg)

#### 🔹 Support Vector Machines:
It is a supervised classification technique that carries an objective to find a hyper lane in n-dimensional space that can distinctly classify the data points

![Picture7](./Data%20Modeling%20pictures/Picture7.jpg)

#### 🔹 Naive Bayes:
It is a classifier which acts as a probabilistic machine learning model used for classification tasks. The crux of the classifier is based on the Bayes theorem.

![Picture8](./Data%20Modeling%20pictures/Picture8.jpg)

#### 🔹 Decision Tree, Random Forest, Neural Network:
These models are the same as previously explained, and the only difference here is that the output is discrete rather than continuous.

---

## 2. Unsupervised Learning

Unlike supervised learning, unsupervised learning is used to draw inferences and find patterns from input data **without references to label** the outcome. Also, we can refer unsupervised learning as any learning problem that is not supervised. It is mainly used where no truth about the data is know.

### Example:
Supervised learning is like showing a little kid what a typical cat looks like and what a typical dog look like and giving him/her a new picture and asking them what animal they see. But unsupervised learning is like giving a kid no idea what a cat or dog looks like and giving them a pile of pictures of animals and asking them to group them by similarity without further instructions.

The main method in unsupervised learning include:
### 🔹 Clustering:
Clustering involves grouping of data points. This method is mainly used when we do not have any labels and want to find unknown clusters/group just by looking at the overall structure of the data and trying to find potential clusters in the data.
It is frequently used for scenarios like customer segmentation, fraud detection and document classification.

![Picture9](./Data%20Modeling%20pictures/Picture9.jpg)
The important with the different methods in finding clusters, they all aim to achieve the same thing. The most important clustering algorithm is called K-Means clustering, where K represents the number of clusters we are looking for.

![Picture10](./Data%20Modeling%20pictures/Picture10.jpg)
To implement k-means, we start by randomly selecting centers for your k clusters and assigning all data points to the cluster centre closest to them. From the example here, the clusters here are shown in blue and green, then we recalculate the cluster centers based on the data point assign to them. 

### 🔹 Dimensionality Reduction:
The idea of this method is to reduce the number of feature or dimensions of your data set while keeping as much information as possible. Most dimensionality reduction techniques can be categorized as either feature elimination or feature extraction.

![Picture11](./Data%20Modeling%20pictures/Picture11.jpg)

Usually, this group of algorithms does this by finding correlations between existing features and removing potentially redundant Dimensions without losing much information.

![Picture12](./Data%20Modeling%20pictures/Picture12.jpg)

#### Example:
![Picture13](./Data%20Modeling%20pictures/Picture13.jpg)

Do you need a picture with high resolution to recognize the plane in the picture below or can you reduce the number of pixels in the image.
A popular method of dimensionality reduction is called principal component analysis or PCA (more explanation coming soon)

---

## 3. Reinforcement Learning *(Coming Soon)*

This technique is based on **learning by trial and error**.  
It’s used in areas like game AI, robotics, and recommendation systems.

*(More on this will be added later!)*

---

## ✅ Summary

- Supervised = Learn with labels (predict values or categories).
- Unsupervised = Learn without labels (find structure or reduce dimensions).
- Reinforcement = Learn by interacting with an environment (coming soon!).

---

## 📁 Next Steps

➡️ In the next chapter, we’ll begin exploring **how to select and evaluate the best model** for our chosen dataset.

