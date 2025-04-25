import os
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, this is your WhatsApp AI Chatbot!"

@app.route("/webhook", methods=["POST"])
def webhook():
    """This endpoint will be called by Twilio when a message is sent to your WhatsApp number."""
    
    # Get the incoming message from Twilio
    incoming_msg = request.form.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Use TextBlob for a simple analysis or response
    if 'hello' in incoming_msg:
        msg.body("Hello! How can I assist you today?")
    elif 'help' in incoming_msg:
        msg.body("Here are some things you can ask me: 'hello', 'help', 'how are you?'")
    else:
        # Analyze the sentiment of the message
        blob = TextBlob(incoming_msg)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            msg.body("I'm glad you're feeling positive!")
        elif sentiment < 0:
            msg.body("I'm sorry to hear you're feeling down. How can I help?")
        else:
            msg.body("I'm here to assist you with anything you need!")

    return str(resp)

if __name__ == "__main__":
    # Get the port from the environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Run the Flask app on all IPs (0.0.0.0) so that it is accessible externally
    app.run(host='0.0.0.0', port=port)

