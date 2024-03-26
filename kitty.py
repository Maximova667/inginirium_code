class  Kitty:
    def __init__(self, name):
        self.name = name

    def meo(self):
        print(self.name, 'meoooooo')


Kit = Kitty('Rasputin:')
Kit.meo()