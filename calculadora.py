class Livro:
    def __init__(self,nome,editora,ano,paginas,autor):
        self.nome=nome
        self.editora= editora
        self.ano =ano
        self.paginas=paginas
        self.autor=autor


livro1 = Livro('Problemas Classicos de Ciecncia da Computacao','manning',2019,272,'David Kopec')
livro2=Livro('Machine learning','O`reilly',2019,300,'Matt Harrison')

print(livro1.nome)
print(livro2.nome)


