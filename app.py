from flask import Flask, request
import random
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAHE1O27NxoBADmFJUZCSP5EWdVdu633XBmkpXa6Am4XBv9JSTDXZAbta5OXvDbZCAAh0ysez6jthcKnQM2a4x2ITcWbpvQOXhohnaOdvZBd4KQOX8O5qenQHNhz8eQrbhMml3jcnhpYPuwJu7ItCMvFl0xcCqMZCxSKOldHX7QZDZD'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)


@app.route('/', methods=['GET', 'POST'])
def receive_message():
            if request.method == 'GET':
                        token_sent = request.args.get("hub.verify _token")
                        return verify_fb_token(token_sent)
            else:
                  output = request.get_json()
                  for event in output['entry']:
                        massaging = event['messaging']
                        for message in massaging:
                              if message.get('message'):
                                    recipient_id = message['sender']['id']
                                    if message['message'].get('text'):
                                          response_sent_text = get_message()
                                          send_message(recipient_id, response_sent_text)
            return "Message Processed"

def verify_fb_token(token_sent):
              if token_sent == VERIFY_TOKEN:
                    return request.args.get("hub.challenge")
              return 'Invalid verifycation token'
            
def get_message():
            sample_responses = ["You are stunning!", "We'ra proud of you.",  "Keep on being you!", "We're greatful to know you :)"]
            return random.choice(sample_responses)

def send_message(recipient_id, response):
      bot.send_text_message(recipient_id, response)
      return "success"

if __name__ == '__main__':
      app.run()
