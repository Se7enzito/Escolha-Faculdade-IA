from flask import Flask, render_template, redirect, url_for, session, request
from flask_session import Session
from libs.api.DataAPI import DataGeren
from libs.api.MathAPI import Calcs
from libs.api.ExelAPI import Exel
from libs.api.MachineAPI import prevNota

ARCHIVES_DIR = "libs/archives"
DATABSE_DIR = "libs/data"

app = Flask(__name__, template_folder="../frontend/templates")

app.static_folder = '../frontend/src'
app.static_url_path = '/static'

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

dataGeren = DataGeren()
calcs = Calcs()
exel = Exel()

dadosTeste = {
    'Universidade Federal do Ceara': {
        'Sigla': 'UFC',
        'Cursos': ['Ciências da Computação', 'Direito'],
        'Notas': {
            'Ciências da Computação': {
                'Ampla Concorrência': {
                    2000: 675.32,
                    2001: 689.47,
                    2002: 710.21,
                    2003: 652.33,
                    2004: 732.68,
                    2005: 695.44,
                    2006: 768.01,
                    2007: 720.37,
                    2008: 812.29,
                    2009: 680.15,
                    2010: 745.72,
                    2011: 812.88,
                    2012: 676.54,
                    2013: 724.99,
                    2014: 690.11,
                    2015: 810.66,
                    2016: 720.48,
                    2017: 678.92,
                    2018: 732.25,
                    2019: 710.87,
                    2020: 689.91,
                    2021: 500.87,
                    2022: 885.65,
                    2023: 745.99
                }
            },
            'Direito': {
                'Ampla Concorrência': {
                    2000: 625.45,
                    2001: 689.12,
                    2002: 698.78,
                    2003: 743.19,
                    2004: 720.56,
                    2005: 652.89,
                    2006: 788.34,
                    2007: 710.04,
                    2008: 825.67,
                    2009: 675.91,
                    2010: 710.63,
                    2011: 798.24,
                    2012: 683.77,
                    2013: 739.28,
                    2014: 662.41,
                    2015: 789.09,
                    2016: 730.59,
                    2017: 688.71,
                    2018: 712.54,
                    2019: 698.15,
                    2020: 676.38,
                    2021: 520.46,
                    2022: 865.72,
                    2023: 728.83
                }
            }
        }        
    }
}

def getMediaNotasCurso(faculdade: str, curso: str, concorrencia: str) -> float:
    notas = dadosTeste[faculdade]['Notas'][curso][concorrencia]
    newNotas = []
    
    if notas is None:
        return None
    
    for ano, nota in notas.items():
        newNotas.append(nota)
    
    return calcs.media(newNotas)

def getVariancia(faculdade: str, curso: str, concorrencia: str) -> float:
    notas = dadosTeste[faculdade]['Notas'][curso][concorrencia]
    newNotas = []
    
    if notas is None:
        return None
    
    for ano, nota in notas.items():
        newNotas.append(nota)
        
    return calcs.variancia(newNotas)

def getDesvioPadrao(faculdade: str, curso: str, concorrencia: str) -> float:
    notas = dadosTeste[faculdade]['Notas'][curso][concorrencia]
    newNotas = []
    
    if notas is None:
        return None
    
    for ano, nota in notas.items():
        newNotas.append(nota)
    
    return calcs.desvio_padrao(newNotas)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    pass

if __name__ == "__main__":
    # Padrão de dados utilizados: 'Universidade Federal do Ceara', 'Ciências da Computação', 'Ampla Concorrência'
    
    # Testes
    media  = getMediaNotasCurso('Universidade Federal do Ceara', 'Ciências da Computação', 'Ampla Concorrência')
    variancia = getVariancia('Universidade Federal do Ceara', 'Ciências da Computação', 'Ampla Concorrência')
    desvio_padrao = getDesvioPadrao('Universidade Federal do Ceara', 'Ciências da Computação', 'Ampla Concorrência')
    
    notas = dadosTeste['Universidade Federal do Ceara']['Notas']['Ciências da Computação']['Ampla Concorrência']
    notasMl = prevNota(notas)
    
    print(f'Média: {media} / Variância: {variancia} / Desvio Padrão: {desvio_padrao}')
    print(notasMl)
    
    todasNotas = [media, media + desvio_padrao, media - desvio_padrao]
    todasNotas.extend(list(notasMl.values()))
    
    print(todasNotas)
    
    userNota = float(input("Digite sua nota: "))

    intervalo = 0
    
    if (userNota in todasNotas):
        intervalo = 1
        print("Você está dentro do intervalo de confiança. " + str(intervalo) + " cenário.")
    else:
        for nota in todasNotas:
            if (userNota >= nota):
                print("Você está dentro do intervalo de confiança. " + str(intervalo) + " cenário.")
                
                intervalo += 1
        
        if (intervalo == 0):
            print("Você não está em qualquer intervalo de segunraça.")