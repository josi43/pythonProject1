class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ''
    def choose(self):
        self.choice= input('{name},escolha entre pedra papel e tesoura: '.format(name=self.name))

    def toNumericalChoice(self):
        switcher = {
            'pedra':0,
            'papel':1,
            'tesoura':2
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points+=1
class GameRound:
    def __init__(self,p1,p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        print('O round acabou em {result}'.format(result = self.getResultAsString(result)))
        if result>0:
            p1.incrementPoint()
        elif result<0:
            p2.incrementPoint()
    def compareChoices(self,p1,p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def awardPOints(self):
        print('implement')
    def getResultAsString(self,result):
        res={
            0:'empate',
            1:'vitoria',
            -1:'derrota'
        }
        return res[result]
class Game:
    def __init__(self):
        self.endgame = False
        self.n1=input('Nome jogador1? ')
        self.n2=input('Nome jogador2? ')
        self.participant = Participant(self.n1)
        self.secondParticipant = Participant(self.n2)
    def start(self):
        while not self.endgame:
            GameRound(self.participant,self.secondParticipant)
            self.checkEndCondition()
    def determineWinner(self):
        resultString='e um empate'
        if self.participant.points>self.secondParticipant.points:
            resultString=f'o vencedor e {self.participant.name}!'
            pontuacao= self.participant.points
        elif self.participant.points<self.secondParticipant.points:
            resultString=f'o vencedor e {self.secondParticipant.name}'
            pontuacao =self.secondParticipant.points
        print(resultString)
        print(pontuacao)
    def checkEndCondition(self):
        answer = input('continue game s/n? ')
        if answer== 's':
            GameRound(self.participant,self.secondParticipant)
            self.checkEndCondition()
        else:
            print('jogo acabou')
            self.determineWinner()
            self.endgame = True
game = Game()
game.start()
