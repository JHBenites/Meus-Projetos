class Endereço:
    def __init__(self, logradouro, número, complemento, bairro, cidade, cep):
        self.logradouro = logradouro
        self.número = número
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def __str__(self):
        endereço_str = self.logradouro + ' - ' + str(self.complemento)
        if self.complemento != None: endereço_str += ' - ' + self.complemento
        endereço_str += ' - bairro: ' + self.bairro + ' - ' + self.cidade + ' - CEP: ' + self.cep
        return endereço_str
