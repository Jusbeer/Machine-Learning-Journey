# 🧠 What is Machine Learning?

Machine Learning (ML) is a way to **teach/instruct computers to learn (obviously) from data** without having to explicitly program it.

Take this example, imagine we are writing a code where we output a comment base on the mark a student has obtain. Instead of writing rules like this:

```python
if grade > 90:
    print("Excellent")
```

We give the computer examples of inputs and correct outputs; it figures out the rules itself by learning patterns from the data we gave it.

You’re not telling the computer what exactly to do. You’re showing it lots of examples so it can guess the rules.

---

## 🌍 Where Do We Use ML?
You may be asking where do we use this type of technology; Here are some examples:
- YouTube video recommendations  
- Email spam filters  
- Netflix showing you what to watch next
- Most well known, ChatGPT helping you learn things.

Behind the scenes, these companies collect massive data and use ML to predict or recommend based on it.

---

## 💡 Why Use ML?

The reason why we use ML is simply when the instruction/rules are too complex to write by hand. Another reason why we use ML is because there’s a lot of data and we want insights/prediction on what may happen. Also, by setting up this type of system, we aim that the system keeps improving without having too much of our input, but with it’s our experience. 

Like for e.g. if we have a dataset full of student’s data gathered in a survey, and we want to predict a student’s exam score based on their study time, sleep, and past grades. This relationships/links are too complex to be hard coded and that’s where we will train a model on real student data.

---

## 🔁 How ML Works (Basic Flow)

1. **Firstly, we will collect data, simply think about have a dataset full of relevant data.**
2. **Then, we will choose the type of model we will use (will explain below)**
3. **After choosing the model, we will train it with available data**
4. **While testing we will test how well it works and its efficiency**
5. **At this stage the algorithm will be ready, and we will use it to make predictions.**

Imagine this flow:

```text
Data ➝ Train ➝ Evaluate ➝ Predict
```

---

## 🧪 Types of Machine Learning
As mention above when describing how ML works, we’ve talk about models. There are 3 types of ML models:

### 1. Supervised Learning
This model learns from labelled data, meaning the data has already the correct answer. Think of it like I’m tutoring you, so I’m showing you the correct answer while you learn.

**Example:**
You have a dataset of students with:
- Features: study time, sleep hours, attendance
- Label: exam score
You “train” the model by giving it inputs (X) and correct outputs (y). Then you test if it can predict scores for new students.

**Use for:**
- Predicting prices (regression)
- Spam detection (classification)
- Image recognition (classification)

---

### 2. Unsupervised Learning
This model learns from unlabelled data, meaning there are no answers. It just looks for patterns or groups in the data. Think of it like I let you to do your research without telling you what to find.

**Example:**
You give it a list of customer behaviours (what they click, buy, view), and it finds clusters like:
- Group A: Students  
- Group B: Parents  
- Group C: Business buyers
You never told it what the groups are. It discovered them.

**Used for:**
- Customer segmentation  
- Market basket analysis  
- Topic modeling (NLP)

---

### 3. Reinforcement Learning
This model learns by doing trial & error. It takes actions and gets rewards or penalties. Over time, it learns what actions give the most reward.
Think: training a dog. “Sit” -> treat. “Jump” -> no treat.

**Example:**
Teaching a robot to walk, or an AI to play chess or video games. It gets points when it does well, and adjusts strategy.

**Used for:**
- Game AI  
- Self-driving cars  
- Robotics

---

✍️ Author: Jusbeer Ramo
🗓️ Started: 06 June 2025

> Feel free to explore, learn, and fork the repo. Happy learning!