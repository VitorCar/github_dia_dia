class Messages:

    sad_messages = [
        "Por trás do meu sorriso, há um coração pesado de dor",
        "Às vezes, as lágrimas são a única voz do coração machucado"
    ]

    happy_messages = [
        "Sorria, a vida é um presente",
        "A felicidade é um estado de espírito"
    ]

    def instructions(self):
        txt = 'Para receber as mesagens em MessageScreen(), digite sad ou happy.'
        line = '-' * len(txt)
        return f'{txt}\n{line}'


class MessageScreen(Messages):


    def __init__(self, emotion):
        self.emotion = emotion
    

    def display(self):

        if self.emotion == 'sad':
            for msn in self.sad_messages:
                print(msn)
        
        elif self.emotion == 'happy':
            for msn in self.happy_messages:
                print(msn)
        
        else:
            print('Somente sad ou happy!')


joao = Messages()
instruction = joao.instructions()
print(instruction)

joao = MessageScreen('sad')
joao.display()
