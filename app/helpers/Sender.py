class Sender:
    def __init__(self):
        # `` itálico
        # ** negrito
        # __ sublinhado
        # ~~ tachado
        pass
    
    def text(self, dispatcher, text, channel=None):
        if channel == 'telegram':
            dispatcher.utter_message(json_message={"text": self.telegram(text), 'parse_mode': 'HTML'})
        elif channel == 'twilio':
            dispatcher.utter_message(self.telegram(text))
        else:
            dispatcher.utter_message(text)

    def telegram(self, text):
        condition = [True]
        while True in condition:
            condition = [
                text.find('``') >= 0,
                text.find('**') >= 0,
                text.find('__') >= 0,
                text.find('~~') >= 0
            ]
            text = text.replace('``', '<i>', 1)
            text = text.replace('``', '</i>', 1)
            text = text.replace('**', '<b>', 1)
            text = text.replace('**', '</b>', 1)
            text = text.replace('__', '<u>', 1)
            text = text.replace('__', '</u>', 1)
            text = text.replace('~~', '<s>', 1)
            text = text.replace('~~', '</s>', 1)
        return text
    
    def whatsapp(self, text):
        text = text.replace('``', '_')
        text = text.replace('**', '*')
        text = text.replace('__', '')
        text = text.replace('~~', '_')
        return text