#imports
from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__,template_folder='templates',static_folder='static')

csv_file = 'sampled.csv'


#create chatbot
def chatbot(input,csv_file):
    df = pd.read_csv(csv_file,delimiter='\t')
    user =0
    chat = 1
    user_input = input.lower()
    if(user_input==df.columns[user]):
        return df.columns[chat]
    if(user_input == "hi" or user_input=="hello"):
        return "hi,good morning"
    if(user_input=="bye" or user_input == "thanks" or user_input == "thank you"):
        return "Welcome"
    user_response = df[df.iloc[:,user]==input].iloc[:,chat].values
    if(len(user_response)>0):
        return user_response[0]
    else:
        return "No data available"


#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot(userText.strip(),csv_file)

if __name__ == "__main__":
    app.run(debug=True)
