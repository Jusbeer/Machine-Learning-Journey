# 🧪 Exploratory Data Analysis (EDA)

## 📌 What it is  
Before training a machine learning model, we must first understand the dataset better. 

Think of it like solving a murder case, we are not only solving it yet, we are just studying the clues carefully.

So, the EDA chapter help us visually explore a dataset to understand:
- What the data looks like
- What patterns or trends exist
- What problems the data might have (missing values, outliers, etc.)
- What relationships exist between features (correlations)


---

## 💡 Why we use it  
This chapter is useful because it enables us 
- to see patterns and structure in the dataset instead of just staring at raw numbers
- to choose the right tools or models later by understanding that dataset shape
- to detect any problem in an early phase because it is overwhelming with raw numbers.


Instead of reading rows of numbers in a dataset, we grasp data faster when it’s shown in pictures or diagrams.  It’s like reading a book when we were young, the more visuals it has, the easier it is to follow the story.

For this repo, I’ve chosen a Student Detail dataset (available in archieve), here is how EDA might help us spot that:
- Girls tend to score higher in reading and writing
- Those who completed a test prep course scored better overall
- Some students have unusually low scores (maybe they were missing from class?)
These insights let us clean the data and choose what kind of model we should build later.

---

## 📊 Types of Analysis

### 1. Univariate Analysis  
This type of analysis shows the info about one variable/data at a time. Since “Uni” means one, you are comparing anything, we are just trying to understand one data by itself. This mainly help us with questions like:
- What is the distribution of this variable?
- What values are common or rare?
- Are there any outliers or unusual patterns?
This analysis is crucial since at the start, we can’t build or explain anything without knowing what’s inside each column in our dataset. It’s like checking the ingredients before baking a cake.

For the dataset we have used here in this repository, if you are just one data like **maths scores**, univariate analysis will be used to show how many students scored between 0-100, or are the scores high or low. 


**Examples of univariate charts:**
- Histogram
- Bar chart
- Pie chart
- Box plot

---

### 2. Bivariate Analysis  
This analysis shows the info about two variable/data together and try to see the relationship between both of them. This mainly help us with questions like:
- Does one variable affect another?
- Is there a pattern or connection?
This analysis helps you figure out the cause and effect or comparisons like for this dataset does taking a test prep course lead to higher scores or do boys and girls perform differently in reading?

**Examples of bivariate charts:**
- Scatter plot
- Grouped bar chart or box plot
- Violin plot
- Correlation heatmap

---

### 3. Multivariate Analysis  
In this analysis, we look at 3 or more variables together in a single chart. This mainly help us with questions like:
- Is the relationship between A and B different depending on C?
- Are there deeper patterns involving many factors?
In real world scenarios, problems are never one-dimensional nor always straight forward. This type of analysis helps us to tackle more complex stories hidden in the data.

For the student dataset, using this analysis to assess test preparation + gender + math score; Maybe females with test prep did better, but males didn’t improve as much. 

**Examples of multivariate charts:**
- Grouped bar charts
- Pair plots
- Bubble chart
- 3D scatter plot

---

## 🛠️ Implementation  
Throughout many videos on YouTube, blogs, and using ChatGPT, the best way to implement the EDA efficiently, we need to ask ourself these 3 questions:
- **What is in my dataset?**
- **How are the features related?**
- **What can I ask or test based on real-world logic?**

I’ve come up with a simple 5-step process how to implement the EDA. This helps us move from seeing “just numbers” to actual insights in the dataset.

---

### 1. Summarize the dataset  
The goal here is to get a basic idea of what the data looks like. This is where we mainly answer the first question “**What is in my dataset?**”
- The shape of the dataset (how many rows and columns)
- The column names
- The data types (is it text? number?)
- Missing values or strange data

Normally we can run these functions in Python to get this info:
- 'data_file.info()' – shows column types and non-null counts  
- 'data_file.describe()' – shows summary statistics for numeric columns  
- 'data_file.isnull().sum()' – counts missing values  

---

### 2. Visualize individual columns  
Here, we will use a data visualization tool to plot charts to explore each column alone. This helps us to see distributions, counts, or imbalance in categories. This is where we mainly answer the first question and part of the second question “**How are the features related?**”
- How scores are spread out (e.g. many students scoring around 70?)
- Whether categories are balanced (e.g. more males or females?)

**Some examples are:**  
- Histograms (see distributions like test scores)  
- Count plots (for categories like gender or education)  

---

### 3. Compare features  
Here we will compare two or more columns together. For example:
- Do students who took a prep course score higher?
- Do girls and boys score differently in reading?

**Some examples are:**  
- Boxplots, barplots, violin plots  
- Correlation heatmaps  

---

### 4. Find relationships  
Use plots graph to explore how features relate to each other. This is where we mainly answer the second question like asking deeper questions:
- Does more reading skill mean better writing skill?
- Do math and reading scores increase together?

**Some examples are:**  
- Scatter plots (share relationship between 2 numbers)
- Pairplots (multiple relationships)

---

### 5. Use filters/grouping  
Lastly, we need to break data into parts and study them more closely. We can use:
- Group by categories like gender or education level
- Filters to study only a subset of students (e.g., just those who didn’t take the prep course)

This helps us find patterns within subgroups of the data and this is where we answer the third question “**What can I ask or test based on real-world logic?**”
---

📊 These plots can be made using tools like **Matplotlib**, **Seaborn**, or **Tableau**.
