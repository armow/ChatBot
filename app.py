import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine
from pygraphviz import *

API_TOKEN = '517911978:AAFmJsGB5rNOW_6_SuxT5WqyVe7IObOz95w'
WEBHOOK_URL = 'https://1bd2eeee.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'help',
        'garbage',
        'search',
        'table',
        'team',
        'result',
        'content',
        'member',
        'intro'
    ],
    transitions=[
        {
            'trigger':'advance',
            'source':'user',
            'dest':'help',
            'conditions':'is_going_to_help'
        }, 
        {
            'trigger':'advance',
            'source':'user',
            'dest':'garbage',
            'conditions':'is_going_to_garbage'
        },        
        {
            'trigger':'advance',
            'source':'user',
            'dest':'search',
            'conditions':'is_going_to_search'
        },
        {
            'trigger':'advance',
            'source':'search',
            'dest':'table',
            'conditions':'is_going_to_table'
        },
        {
            'trigger':'advance',
            'source':'search',
            'dest':'team',
            'conditions':'is_going_to_team'
        },
        {
            'trigger':'advance',
            'source':'search',
            'dest':'result',
            'conditions':'is_going_to_result'
        },
        {
            'trigger':'advance',
            'source':'search',
            'dest':'intro',
            'conditions':'is_going_to_intro'
        },
        {
            'trigger':'advance',
            'source':'team',
            'dest':'content',
            'conditions':'is_going_to_content'
        },
        {
            'trigger':'advance',
            'source':'content',
            'dest':'member',
            'conditions':'is_going_to_member'
        },
        {
            'trigger':'go_back',
            'source':[
                'help',
                'garbage'
            ],
            'dest':'user'
        },
        {
            'trigger':'go_back',
            'source':[
                'member',
                'table',
                'result',
                'intro'
            ],
            'dest':'search'
        }
        ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))

@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'

"""@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')"""
machine.graph.draw('show-fsm.png',prog='dot')

if __name__ == "__main__":
    _set_webhook()
    app.run()
