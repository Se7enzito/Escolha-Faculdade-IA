import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

def prevNota(notas: dict) -> dict:
    previsoes = {}
    
    proxAno = max(notas.keys()) + 1

    # Treinamento do modelo de regressão linear
    anos = np.array(list(notas.keys())).reshape(-1, 1)  # Correção aqui
    notas = np.array(list(notas.values()))  # Correção aqui

    modelo = LinearRegression()
    modelo.fit(anos, notas)

    ano_futuro = np.array([[proxAno]])
    nota_prevista = modelo.predict(ano_futuro)

    previsoes['Regressão Linear'] = nota_prevista[0]
    
    # Treinamento do modelo SVR
    svr_model = SVR(kernel='rbf', C=100, gamma=0.1)
    svr_model.fit(anos, notas)

    nota_prevista_svr = svr_model.predict([[proxAno]])

    previsoes['SVR'] = nota_prevista_svr[0]
    
    # Treinamento do modelo Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(anos, notas)

    nota_prevista_rf = rf_model.predict([[proxAno]])

    previsoes['Random Forest'] = nota_prevista_rf[0]
    
    return previsoes