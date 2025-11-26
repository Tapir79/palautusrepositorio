class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.operaatiot = []

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self.operaatiot.append(("miinus", operandi))

    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self.operaatiot.append(("plus", operandi))

    def nollaa(self):
        self._arvo = 0
        self.operaatiot = []

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def kumoa(self):
        if not self.operaatiot:
            return
        
        viimeisin_toiminto = self.operaatiot.pop()
        toiminto, operandi = viimeisin_toiminto
        
        if toiminto == "plus":
            self._arvo -= operandi
        elif toiminto == "miinus":
            self._arvo += operandi
