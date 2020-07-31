class Pessoa(object):
    'Classe para calcular o IMC de uma pessoa'
    def __init__(self,nome,peso,altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.imc = 0

    def calcula(self):
        self.imc = self.peso/(self.altura*self.altura)
        #print "O IMC do %s eh %f" % (self.nome,imc)    

    def imprime(self):
        print ("O IMC do %s eh %f" % (self.nome,self.imc))
        
    
        
nome = str(input('Entre com seu nome:')) 
altura
