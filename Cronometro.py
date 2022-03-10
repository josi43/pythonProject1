#fazer cronometro simples que apareça o tempo para o usuário
import time
import winsound

#calculo
class Cronometro():
    def __init__(self,tempo):
        self.tempo=tempo
        self.segundo = 60
        self.minuto=0
    def calculo(self):
        self.hora=self.tempo-1
        for i in range(59, -1,-1):
            time.sleep(1)
            print(f'{self.hora}:{i}')
            if  i==0 and self.hora<1:
                print('acabou ')
                duration = 1000  # milliseconds
                freq = 440  # Hz
                winsound.Beep(freq, duration)
                break
            elif i == 0:
                self.tempo-=1
                self.calculo()

#perguntar quanto tempo
tempo=int(input('Minutos: '))
crono=Cronometro(tempo)
crono.calculo()