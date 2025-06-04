# Machine Learning Journey

Welcome! This repository documents my personal journey learning Machine Learning from scratch — with theory, examples, and Python code.

---

## 🧠 What is Machine Learning?

Machine Learning (ML) is a way to **teach computers to learn from data** without being explicitly programmed.

For example, instead of writing rules like:

```python
if grade > 90:
    print("Excellent")
```

We give the computer lots of input-output examples. It learns the rules itself by finding patterns in the data.

You're not telling the computer what exactly to do — you're showing it many examples so it can figure it out.

---

## 🌍 Where Do We Use ML?

- YouTube video recommendations  
- Email spam filters  
- Netflix content suggestions  
- ChatGPT helping you learn things

These systems collect huge amounts of data and learn from it to make predictions or decisions.

---

## 💡 Why Use ML?

- Some rules are too complex to program by hand  
- We have lots of data and want insights  
- ML models can keep improving with more data  
- We want predictions or decisions without hardcoding logic

### Example:
Predicting student exam scores using their sleep, study hours, and past scores is hard to write rules for. But ML can learn this from real data.

---

## 🔁 How ML Works (Basic Flow)

1. **Collect data**  
2. **Choose a model**  
3. **Train the model** on the data  
4. **Test the model's performance**  
5. **Use it to make predictions**

```text
Data ➝ Train ➝ Evaluate ➝ Predict
```

---

## 🧪 Types of Machine Learning

### 1. Supervised Learning

- Learns from labeled data (answers are known)
- Like being tutored

**Example:**
- Inputs: study time, sleep hours  
- Label: exam score  
- The model learns to predict new scores

**Used for:**
- Price prediction (regression)  
- Spam detection (classification)  
- Image recognition

---

### 2. Unsupervised Learning

- Learns from data without labels  
- It finds patterns by itself

**Example:**
Customer behavior data ➝ groups like:  
- Group A: Students  
- Group B: Parents  
- Group C: Business buyers

**Used for:**
- Customer segmentation  
- Market basket analysis  
- Topic modeling

---

### 3. Reinforcement Learning

- Learns by trial and error  
- Gets rewarded or punished  

**Example:**
Training a dog:  
"Sit" ➝ treat, "Jump" ➝ no treat.

**Used for:**
- Game AI  
- Self-driving cars  
- Robotics

---

## 🧹 Why Clean Data?

Before running an ML model, we must **transform and clean the dataset** into a usable format.  
Think of it like sieving flour before baking — remove dirt and spread it evenly.

---

## 🔧 Common Data Cleaning Techniques

1. **Check for missing values** – Find null/empty entries  
2. **Drop/Fill missing values** – Use mean, median, or mode  
3. **Remove unnecessary columns** – Drop irrelevant data  
4. **Encode text columns** – Convert to numbers (LabelEncoding, One-Hot)  
5. **Ensure correct data types** – e.g., string stored as int  
6. **Scale numeric data** – Normalize values  
7. **Flag outliers** – Detect extreme values

---

📂 Project Structure:
- `archive/` → Raw dataset (CSV)
- `Loading Dataset/` → Load + Explore dataset
- `Cleaning Dataset/` → Clean and preprocess dataset
- `Machine_Learning.docx` → Personal notes & explanations
- `README.md` → This file!

---

✍️ Author: Jusbeersingh  
🗓️ Started: June 2025

> Feel free to explore, learn, and fork the repo. Happy learning!