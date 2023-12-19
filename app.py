from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import warnings

app = Flask(__name__)
warnings.filterwarnings('ignore')

# Load the sentiment analysis model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("kevinscaria/joint_tk-instruct-base-def-pos-neg-neut-combined")
model = AutoModelForSeq2SeqLM.from_pretrained("kevinscaria/joint_tk-instruct-base-def-pos-neg-neut-combined")

# ... (other Flask code)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        # Perform sentiment analysis using the provided model
        result = perform_sentiment_analysis(input_text)
        return render_template('result.html', input_text=input_text, result=result)

    return render_template('index.html')

@app.route('/perform_sentiment_analysis', methods=['POST'])
def perform_sentiment_analysis(input_text):
    # Given sentiment analysis code
    bos_instruction = """Definition: The output will be the aspects (both implicit and explicit) and the aspects sentiment polarity. In cases where there are no aspects the output should be noaspectterm:none.
    Positive example 1-
    input: I charge it at night and skip taking the cord with me because of the good battery life.
    output: battery life:positive,
    Positive example 2-
    input: I even got my teenage son one, because of the features that it offers, like, iChat, Photobooth, garage band and more!.
    output: features:positive, iChat:positive, Photobooth:positive, garage band:positive
    Negative example 1-
    input: Speaking of the browser, it too has problems.
    output: browser:negative
    Negative example 2-
    input: The keyboard is too slick.
    output: keyboard:negative
    Neutral example 1-
    input: I took it back for an Asus and same thing- blue screen which required me to remove the battery to reset.
    output: battery:neutral
    Neutral example 2-
    input: Nightly my computer defrags itself and runs a virus scan.
    output: virus scan:neutral
    Now complete the following example-
    input: """  # Your definition, positive examples, negative examples, and neutral examples
    delim_instruct = ''
    eos_instruct = ' \noutput:'
    text = input_text

    tokenized_text = tokenizer(bos_instruction + text + delim_instruct + eos_instruct, return_tensors="pt")
    output = model.generate(tokenized_text.input_ids)
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    print(result)
    return result
    

if __name__ == '__main__':
    app.run(debug=True)
'''
# Flask app code

# Flask imports
from flask import Flask, render_template, request  

# Model and evaluation imports
from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM  
from flask_wtf import CSRFProtect

import xml.etree.ElementTree as ET
from seqeval.metrics import accuracy_score, f1_score


app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("kevinscaria/joint_tk-instruct-base-def-pos-neg-neut-combined")
model = AutoModelForSeq2SeqLM.from_pretrained("kevinscaria/joint_tk-instruct-base-def-pos-neg-neut-combined")

# Parse XML dataset
tree = ET.parse('train.xml')
root = tree.getroot()

texts = []
aspects = []
sentiments = []

for review in root.findall('Review'):
    text = ''
    aspects_review = []
    sentiments_review = []

    for sentence in review.findall('sentences/sentence'):
        if sentence.find('text') is not None:
            text += sentence.find('text').text + ' '

        for opinion in sentence.findall('Opinions/Opinion'):
            aspect = opinion.get('category')
            sentiment = opinion.get('polarity')

            aspects_review.append(aspect)
            sentiments_review.append(sentiment)

    texts.append(text)
    aspects.append(aspects_review)
    sentiments.append(sentiments_review)

# Model prediction function
def run_model(input_text):
    # Run model using input_text
    # ...

    predicted_aspects = ['price', 'food']
    predicted_sentiment = ['positive', 'negative']

    return predicted_aspects, predicted_sentiment


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        predicted_aspects, predicted_sentiment = run_model(input_text)
        print(predicted_aspects)
        print(predicted_sentiment)

        # Process the results and return appropriate response or redirect
        # For example, you can render a results template with the predictions
        result = {
            'input_text': input_text,
            'predicted_aspects': predicted_aspects,
            'predicted_sentiment': predicted_sentiment,
        }
        return render_template('result.html', result=result)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)'''