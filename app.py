from flask import Flask, request, render_template
from model import SentimentRecommenderSystem
import pandas as pd

app = Flask(__name__)

sent_reco_model = SentimentRecommenderSystem()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the username as input
    user_name_input = request.form['username'].lower()
    sent_reco_output = sent_reco_model.top5_recommendations(user_name_input)
    result_df=pd.DataFrame({"S.No":[1,2,3,4,5],"ProductName":sent_reco_output})
    final_result=list(zip(*map(result_df.get, result_df)))
    if not (sent_reco_output is None):
        return render_template("index.html", output=final_result,query="Top 5 Product Recommendations")
    else:
        return render_template("index.html",
                               message_display="User Name doesn't exist. Please provide a valid user!")


if __name__ == '__main__':
    app.run()
