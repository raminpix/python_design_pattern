class Greeting:

    def say_greeting(self, lang):
        greeting = None
        try:
            greeting = self.say_greeting_factory(lang)
        except ValueError as e:
            print('error !!!!')
            print(e)
        return greeting    

    def say_greeting_factory(self, lang):
        greeting = None
        if (lang == 'English'):            
            greeting = self.say_greeting_English()
        if (lang == 'Spanish'):
            greeting = self.say_greeting_Spanish()
        return greeting

    def say_greeting_English(self):
        return 'Hello'

    def say_greeting_Spanish(self):
        return 'Hola'


    @classmethod
    def say_something(self):
        return 'Hey!'


if __name__ == '__main__':
    print(Greeting().say_something())
    m = Greeting()
    print(m.say_greeting('Spanish'))
