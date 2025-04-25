from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Get the incoming message text from the user
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    # Greeting message and categories
    if "hi" in incoming_msg or "hello" in incoming_msg:
        msg.body("Hi! Welcome to the Abacus Claiming Portal. How may I assist you today?\n\n"
                 "1. Submit a claim\n"
                 "2. Check claim status\n"
                 "3. Speak to an agent\n"
                 "4. Exit")
    
    elif "1" in incoming_msg:
        msg.body("You chose to submit a claim. Please provide your claim details and any supporting documents.")
        # You can ask for further details here or integrate file upload functionality if needed.
    
    elif "2" in incoming_msg:
        msg.body("You chose to check claim status. Please provide your claim number, and I'll check the status for you.")
    
    elif "3" in incoming_msg:
        msg.body("You chose to speak to an agent. One of our agents will reach out to you shortly.")
        # Optionally, you can integrate an actual agent feature here or notify a human agent.
    
    elif "4" in incoming_msg:
        msg.body("You chose to exit. Thank you for using the Abacus Claiming Portal. Have a great day!")
    
    else:
        msg.body("Sorry, I didn't understand that. Please choose from the following options:\n\n"
                 "1. Submit a claim\n"
                 "2. Check claim status\n"
                 "3. Speak to an agent\n"
                 "4. Exit")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)


