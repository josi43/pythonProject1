hexadecimal={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:"E",15:'F'}

class Calc():
    def hexa(self,res):
        self.listhex=[]
        self.res=res
        self.v2= res//16
        self.v3=res%16
        self.listhex.append(self.v3)
        if self.v2>16:
            self.hexa(self.v2)
        elif self.v2>0:
            self.listhex.append(self.v2)
        return self.listhex
    def contrario(self,valor):
        self.valor = self.hexa(valor)
        self.valor.reverse()
        return self.valor
    def dicionario(self,valor):
        self.dicio= self.contrario(valor)
        self.tabela= []
        n=0
        for x in hexadecimal:
            if len(self.dicio)== n:
                break
            elif self.dicio[n] in hexadecimal:
                self.tabela.append(hexadecimal[self.dicio[n]])
                n+=1
        return self.tabela
    def stri(self,lista):
        self.lista=self.dicionario(lista)
        self.str=''.join([str(_) for _ in self.lista])
        return self.str

class Doido():
    def __init__(self):
        self.numeros = []
        self.resultado = []
    def calcular(self,numero):
        self.num=numero
        if self.num>=8:
            self.n_numero= numero/8
            self.nocto= int((self.n_numero-(int(self.n_numero)))*8)
            self.numeros.append(self.nocto)
            self.calcular(int(self.n_numero))
        else:
            self.numeros.append(numero)
        return self.numeros
    def contrario(self,valor):
        self.valor = self.calcular(valor)
        self.valor.reverse()
        return self.valor
    def stri(self,lista):
        self.lista=self.contrario(lista)
        self.str=''.join([str(_) for _ in self.lista])
        self.numeros.clear()
        return self.str

class Bina():
    def __init__(self):
        self.listhex = []
    def calcular(self,numero):
        self.res = numero
        self.v2 = self.res //2
        self.v3 = self.res% 2
        self.listhex.append(self.v3)
        if self.res==1:
            pass
        elif self.v2 >= 2:
            self.calcular(self.v2)
        else:
            self.listhex.append(self.v2)
        return self.listhex
    def contrario(self,valor):
        self.valor = self.calcular(valor)
        self.valor.reverse()
        return self.valor
    def stri(self,lista):
        self.lista=self.contrario(lista)
        self.str=''.join([str(_) for _ in self.lista])
        self.listhex.clear()
        return self.str
def print_formatted(n):
    z=1
    final = Calc()
    bina = Bina()
    doido = Doido()
    print(f'{z} {final} {doido} {bina}')

if __name__ == '__main__':
    n = int(input())
    print(print_formatted(n))
