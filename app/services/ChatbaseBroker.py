import requests
import json
import pika

class ChatbaseBroker:
    def __init__(self):
        self.URL = 'https://chatbase.com/api/message'
        self.API_KEY = "2157e864-e94c-405e-b4db-03a58201e6b9"
        credentials = pika.PlainCredentials('admin', 'admin')
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
        channel = connection.channel()
        channel.basic_consume('chatbase', self._callback, auto_ack=True)
        print('Serviço rodando...')
        channel.start_consuming()

    def _callback(self, channel, method, properties, body):
        body = json.loads(body)
        self._sendMessage(body)

    def _getPlataform(self, body):
        platform = body.get('input_channel')
        if platform == 'cmdline' or not platform:
            return 'CMD'
        elif platform == 'telegram':
            return 'Telegram'
        elif platform == 'twilio':
            return 'WhatsApp'
        else:
            return platform

    def _getIntent(self, body):
        return body['parse_data']['intent']['name']

    def _ifFallback(self, body):
        return body['parse_data']['intent']['name'] in ['nlu_fallback', 'out_of_scope']

    def _formatBody(self, body):
        type_ = body.get('event')
        if type_ == 'user':
            return {
                "api_key": self.API_KEY,                        #string, <required> the Chatbase ID of the bot
                "type": 'user',                                 #string, <required> valid values "user" or "agent" (akayour bot) message
                "user_id": body.get("sender_id"),               #string, <required> the ID of the end-user
                "time_stamp": int(body.get("timestamp")),       #int,    <required> milliseconds since the UNIX epoch, used to sequence messages. (must be within previous 30 days)
                "platform": self._getPlataform(body),           #string, <required> valid values "Facebook", "SMS", "Web", "Android", "iOS", "Actions", "Alexa", "Cortana", "Kik", "Skype", "Twitter", "Viber", "Telegram", "Slack", "WhatsApp", "WeChat", "Line", "Kakao" or a custom name like "Workplace" or "OurPlatform"
                "message": body.get('text'),                    #string, <optional> the raw message body regardless of type for example a typed-in or a tapped button or tapped image; 1,200 characters max
                "intent": self._getIntent(body),                #string, <optional> set for user messages only; if not set usage metrics will not be shown per intent; do not set if it is a generic catch all intent, like default fallback, so that clusters of similar messages can be reported
                "not_handled": self._ifFallback(body),          #bool,   <optional> set for user messages only; indicates that the bot was not able to handle the message because it was not understood (e.g. no intent for "Start over"), or it was understood (e.g. has intent for "Order drink") but not supported; if not set then these high churn issues are not shown across reports; set for generic catch all intents, like default fallback
                "version": None,                                #string, <optional> set for user and bot messages; used to track versions of your code or to track A/B tests
                "session_id": None                              #string, <optional> set for user and bot messages; used to define your own custom sessions for Session Flow report and daily session metrics
            }
        elif type_ == 'bot':
            return {
                "api_key": self.API_KEY,                        #string, <required> the Chatbase ID of the bot
                "type": 'agent',                                #string, <required> valid values "user" or "agent" (akayour bot) message
                "user_id": body.get("sender_id"),               #string, <required> the ID of the end-user
                "time_stamp": int(body.get("timestamp")),       #int,    <required> milliseconds since the UNIX epoch, used to sequence messages. (must be within previous 30 days)
                "platform": self._getPlataform(body),           #string, <required> valid values "Facebook", "SMS", "Web", "Android", "iOS", "Actions", "Alexa", "Cortana", "Kik", "Skype", "Twitter", "Viber", "Telegram", "Slack", "WhatsApp", "WeChat", "Line", "Kakao" or a custom name like "Workplace" or "OurPlatform"
                "message": body.get('text'),                    #string, <optional> the raw message body regardless of type for example a typed-in or a tapped button or tapped image; 1,200 characters max
                "version": None,                                #string, <optional> set for user and bot messages; used to track versions of your code or to track A/B tests
                "session_id": None
            }
        else:
            return None

    def _sendMessage(self, body):
        body = self._formatBody(body)
        if body:
            response = requests.post(self.URL, json.dumps(body))
            if response.status_code == 200:
                print('Mensagem enviada para o Chatbase')
            else:
                print(f'Houve algum problema [Código: {response.status_code}: {response.text}]')   


if __name__ == "__main__":
    ChatbaseBroker()