from flask import Flask,jsonify,request
from flask_cors import CORS
from sklearn.linear_model import LinearRegression
import pandas as pd
#Criar o modelo de ML
df= pd.read_csv("dataset_carros_usados.csv")

modelo = LinearRegression()

X = df[["ano", "quilometragem", "motor", "num_revisoes"]]
y = df["preco"]
modelo.fit(X,y)

app = Flask(__name__)
CORS(app)

#Criando a primeira rota e método
@app.route("/",methods=["GET"])
def inicio():
    return jsonify({
        "status":"API online e funcionando corretamente!", 
        "Autor":"Breno"
    })
    
    
@app.route("/prever",methods=["POST"])
def retorno():
    try:
        dados = request.get_json()
        carro = pd.DataFrame({
            "ano":[dados["ano"]],
            "quilometragem":[dados["quilometragem"]],
            "motor":[dados["motor"]],
            "num_revisoes":[dados["num_revisoes"]]
        })
        preco = modelo.predict(carro)[0]
        return jsonify({
            
            "preço":round(float(preco),2)
        })
        
    except Exception as erro:
        return jsonify({
            "erro":str(erro)
        })
        
       
if __name__ == "__main__":
    app.run(port=8000,host="0.0.0.0",debug=True)
 