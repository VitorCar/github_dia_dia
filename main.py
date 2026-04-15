class Messages:

    sad_messages = [
        "Por trás do meu sorriso, há um coração pesado de dor",
        "Às vezes, as lágrimas são a única voz do coração machucado",
        "Não deixei de te amar, mas tive que desistir de você"
    ]

    happy_messages = [
        "Sorria, a vida é um presente",
        "A felicidade é um estado de espírito",
        "Hoje meu coração vibra de alegria!"
    ]

    def instructions(self):
        txt = 'Para receber as mesagens em MessageScreen(), digite sad ou happy.'
        line = '-' * len(txt)
        return f'{line}\n{txt}\n{line}'


class MessageScreen(Messages):


    def __init__(self, emotion):
        self.emotion = emotion
    

    def display(self):

        if self.emotion == 'sad':
            for i,msn in enumerate(self.sad_messages):
                print(f'Mensagem Triste [{i}] -> \033[4m{msn}\033[0m')
        
        elif self.emotion == 'happy':
            for i, msn in enumerate(self.happy_messages):
                print(f'Mensagem Alegre [{i}] -> \033[4m{msn}\033[0m')
        
        else:
            print('Somente sad ou happy!')


joao = Messages()
instruction = joao.instructions()
print(instruction)

joao = MessageScreen('sad')
joao.display()
