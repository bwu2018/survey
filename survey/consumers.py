import json
from channels.generic.websocket import WebsocketConsumer

class AnswerConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, answer_data):
        answer_data_json = json.loads(answer_data)
        answer = answer_data_json['answer']

        self.send(answer_data=json.dumps({
            'answer': answer
        }))