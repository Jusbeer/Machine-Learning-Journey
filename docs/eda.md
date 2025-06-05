# 🧪 Exploratory Data Analysis (EDA)

## 📌 What it is  
Before training a machine learning model, we must first understand the dataset better. E.g. We must search what's inside, what it might be hiding, and how everything is connected. Imagine of it like we are detective solving a case, we are not only solving the problem yet, we are just studying the clues carefully.

So, in this chapter, we explore a dataset to understand:
- What the data looks like
- What patterns or trends exist
- What problems the data might have (missing values, outliers, etc.)
- What relationships exist between features (correlations)


---

## 💡 Why we use it  
This chapter is useful because it enables us 
- to understand with what we are working with because it is hard to see patterns.
- to choose the right one or transformations because it is easy to miss trends.
- to detect any problem in an early phase because it is overwhelming with raw numbers.


Instead of reading rows of numbers in a dataset, we grasp data faster when it’s shown in pictures or diagrams.  It’s like reading a book when we were young, the more visuals it has, the easier it is to follow the story.

---

## 🛠️ Implementation  
Throughout many videos on YouTube, blogs, and using ChatGPT, I’ve came up with a process how to implement the EDA process in a simple way. Here are the steps I’ve came up with to help us move from “just numbers” to actual insights we can act on:

---

### 1. Summarize the dataset  
Look at the shape (rows & columns) of the dataset. e.g. column names, data types, and a few top rows.  
This helps us to get a “quick look” at what the dataset contains.  
Normally we can run these functions in Python to get this info:
- 'data_file.info()' – shows column types and non-null counts  
- 'data_file.describe()' – shows summary statistics for numeric columns  
- 'data_file.isnull().sum()' – counts missing values  

---

### 2. Visualize individual columns  
We will use a data visualization tool to plot charts to explore each column alone. This helps us to see distributions, counts, or imbalance in categories. 

**Some examples are:**  
- Histograms (see distributions)  
- Count plots (for categories)  

---

### 3. Compare features  
Here we will compare two or more columns together. For example, “Does gender affect test scores in a school?”

**Some examples are:**  
- Boxplots, barplots, violin plots  
- Correlation heatmaps  

---

### 4. Find relationships  
Use plots graph to explore how features relate to each other (e.g., does more study time mean better scores?).

**Some examples are:**  
- Scatter plots (X vs Y)  
- Pairplots (multiple relationships)  

---

### 5. Use filters/grouping  
Lastly, we will break the data into smaller parts using groupby or filters. This helps us to study differences between categories like gender, education level, etc.

---

📊 These plots can be made using tools like **Matplotlib**, **Seaborn**, or **Tableau**.
