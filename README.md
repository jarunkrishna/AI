# Building a Simple Chatbot from Scratch in Python (using NLTK)

![Alt text](https://cdn-images-1.medium.com/max/800/1*pPcVfZ7i-gLMabUol3zezA.gif)

History of chatbots dates back to 1966 when a computer program called ELIZA was invented by Weizenbaum. It imitated the language of a psychotherapist from only 200 lines of code. 

On similar lines let's create a very basic chatbot utlising the Python's NLTK library.It's a very simple bot with hardly any cognitive skills,but still a good way to get into NLP and get to know about chatbots.

## Overview

This project demonstrates the creation of a chatbot using Python and Natural Language Processing (NLP). The chatbot is designed to interact with users, understand their natural language input, and provide relevant responses.

## Table of Contents
* [Prerequisites](#pre-requisites)
* [Installation](#installation-of-nltk)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Technologies Used](#technologies-used)
* [How to run](#how-to-run)
* [Contributing](#contributing)
* [License](#license)




## Pre-requisites

Before getting started with this project, ensure that you have the following prerequisites:

Python (3.x recommended)
Required Python libraries (e.g., spaCy, NLTK, or other NLP libraries)
Text data for training and testing
A basic understanding of NLP concepts



### Installation of NLTK
```
pip install nltk
```
### Installing required packages
After NLTK has been downloaded, install required packages
```
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.layers import TextVectorization
import re,string
from tensorflow.keras.layers import LSTM,Dense,Embedding,Dropout,LayerNormalization
```
## Usage

### 1. Data Preprocessing: 
If required, preprocess your training and testing data, which may involve text cleaning, tokenization, and feature engineering.

### 2. Training: 
Train your chatbot using your preferred NLP model. You may use pre-trained models, fine-tune them, or create custom models.

### 3. Chatbot Interface: 
Implement the chatbot interface using a web application or command-line interface. Users can interact with the chatbot by providing text input.

### 4. User Interaction: 
Users can send text messages to the chatbot, and the chatbot will process these messages, understand user intent, and provide appropriate responses.

### 5. Deployment: 
Deploy your chatbot as needed, whether it's a web-based chatbot, a chatbot API, or an integration with messaging platforms.

### 6. Continuous Improvement: 
Continuously improve your chatbot by refining the NLP model, enhancing the user experience, and expanding its capabilities.

# Project Structure

#### flask/templates, flask/static, flask/app.py
#### flask/templates/index.html
#### flask/static/style.css
#### flask/app.py

## Technologies Used

Python
Natural Language Processing (NLP) libraries (e.g., spaCy, NLTK)
[Other libraries or tools you've used]



## How to run
* Jupyter Notebook

You can run the [chatbot.ipynb](https://github.com/jarunkrishna/AI/blob/main/My_Chatbot.ipynb) which also includes step by step instructions.

* Through Terminal
```
python app.py
```

## Contributing

If you want to contribute to this project, please follow these steps:

Fork the repository
Create a new branch for your feature or bug fix
Make your changes and submit a pull request

## License

This project is licensed under the jarunkrishna - see the LICENSE.md file for details.
