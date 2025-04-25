from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from textblob import TextBlob

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    """Respond to incoming messages with a simple AI reply."""
    msg = request.form.get("Body")
    resp = MessagingResponse()

    # Analyze the incoming message with TextBlob
    blob = TextBlob(msg)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        resp.message("Thanks for your positive message! 😊")
    elif sentiment < 0:
        resp.message("Sorry you're feeling down. Let us know how we can help. 😔")
    else:
        resp.message("Thanks for reaching out! How can we assist you? 🤖")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
