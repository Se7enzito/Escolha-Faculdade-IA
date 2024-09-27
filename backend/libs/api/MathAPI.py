from math import sqrt

class Calcs():
    def media(self, notas: list[float]) -> float:
        total = 0
        
        for nota in notas:
            total += nota
            
        return total / len(notas)

    def variancia(self, notas: list[float]) -> float:
        media = self.media(notas)
        
        soma_quadrados = 0
        
        for nota in notas:
            soma_quadrados += (nota - media) ** 2
        
        return soma_quadrados / len(notas)
    
    def desvio_padrao(self, notas: list[float]) -> float:
        variancia = self.variancia(notas)
        
        return sqrt(variancia)
    
if __name__ == '__main__':
    pass