# Projeto-final-analise-dados

# 🚗💰 Previsão de Preços de Carros Usados
### API inteligente que estima o valor de um veículo usado com Machine Learning

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API%20REST-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Análise%20de%20Dados-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/Licença-MIT-brightgreen?style=for-the-badge)]()


**[📖 Sobre](#-sobre-o-projeto)** •
**[⚙️ Como funciona](#️-como-o-modelo-funciona)** •
**[🚀 Instalação](#-instalação-e-execução)** •
**[📡 Endpoints](#-documentação-da-api)** •
**[🧪 Exemplos](#-exemplos-práticos-de-uso)** •
**[🗺️ Roadmap](#️-roadmap)**

---

## 📖 Sobre o Projeto

Já imaginou perguntar a uma API *"quanto vale esse carro?"* e receber uma resposta em milissegundos, baseada em dados reais de milhares de veículos? **É exatamente isso que este projeto faz.**

Este é o **projeto final** de um percurso de estudos em Análise de Dados e Inteligência Artificial, e reúne, em uma única aplicação, todo o ciclo de um produto de Data Science:

```
📊 Dados brutos  →  🧹 Análise e preparação  →  🤖 Treinamento do modelo  →  🌐 API em produção
```

O resultado é uma **API REST construída com Flask** que expõe um modelo de **Regressão Linear** (Scikit-Learn), treinado sobre uma base real de carros usados, capaz de prever o **preço estimado de um veículo** a partir de quatro características simples: ano, quilometragem, motor e número de revisões.

> 🎯 **Em resumo:** não é só um notebook de estudo — é um serviço de Machine Learning pronto para ser consumido por qualquer front-end, aplicativo ou sistema externo.

---

### 🧠
**Modelo Preditivo**
Regressão Linear treinada com `scikit-learn` sobre dados reais de carros usados

### ⚡
**API Rápida e Leve**
Backend em Flask com CORS habilitado, pronto para integração com qualquer front-end

### 📦
**Pronto para Deploy**
Inclui `gunicorn` nas dependências — pronto para produção em serviços como Render, Railway ou Heroku

---

## 🗂️ Estrutura do Projeto

```
Projeto-final-analise-dados/
│
├── 🐍 app.py                       # API Flask + treinamento do modelo de ML
├── 📊 dataset_carros_usados.csv    # Base de dados com os carros usados
├── 📋 requirements.txt             # Dependências do projeto
├── 🚫 .gitignore                   # Arquivos ignorados pelo Git
└── 📄 README.md                    # Este documento
```

---

## ⚙️ Como o Modelo Funciona

O coração do projeto está em `app.py`. Ao iniciar a aplicação, o fluxo é o seguinte:

```mermaid
flowchart LR
    A[📄 dataset_carros_usados.csv] --> B[🐼 Pandas carrega os dados]
    B --> C["🧮 Features: ano, quilometragem, motor, num_revisões"]
    C --> D[📈 LinearRegression.fit]
    D --> E[🤖 Modelo treinado em memória]
    E --> F["🌐 Flask expõe o modelo via API REST"]
    F --> G["📲 Cliente envia POST /prever"]
    G --> H["💰 API retorna o preço estimado"]
```

**Variáveis utilizadas pelo modelo (features):**

| Variável | Descrição | Tipo |
|---|---|---|
| `ano` | Ano de fabricação/modelo do veículo | Numérico |
| `quilometragem` | Quilometragem total rodada | Numérico |
| `motor` | Potência/cilindrada do motor | Numérico |
| `num_revisoes` | Quantidade de revisões realizadas | Numérico |

**Variável-alvo (target):** `preco` — o valor de mercado do veículo, que o modelo aprende a estimar.

---

## 🚀 Instalação e Execução

### ✅ Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/)

### 🔧 Passo a passo

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/breno209/Projeto-final-analise-dados.git

# 2️⃣ Acesse a pasta do projeto
cd Projeto-final-analise-dados

# 3️⃣ Crie um ambiente virtual (recomendado)
python -m venv venv

# 4️⃣ Ative o ambiente virtual
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# 5️⃣ Instale as dependências
pip install -r requirements.txt

# 6️⃣ Execute a aplicação
python app.py
```

Se tudo ocorrer bem, você verá a API rodando em:

```
🌐 http://localhost:8000
```

---

## 📡 Documentação da API

### 🔹 `GET /`
Verifica se a API está online.

<details>
<summary><b>📥 Requisição</b></summary>

```bash
curl http://localhost:8000/
```

</details>

<details open>
<summary><b>📤 Resposta</b></summary>

```json
{
  "status": "API online e funcionando corretamente!",
  "Autor": "Breno"
}
```

---

### 🔹 `POST /prever`
Recebe as características de um veículo e retorna o **preço estimado**.

<details open>
<summary><b>📥 Requisição</b></summary>

```bash
curl -X POST http://localhost:8000/prever \
  -H "Content-Type: application/json" \
  -d '{
        "ano": 2019,
        "quilometragem": 45000,
        "motor": 2.0,
        "num_revisoes": 6
      }'
```

**Corpo da requisição (JSON):**

| Campo | Tipo | Exemplo | Obrigatório |
|---|---|---|:---:|
| `ano` | `int` | `2019` | ✅ |
| `quilometragem` | `int` | `45000` | ✅ |
| `motor` | `float` | `2.0` | ✅ |
| `num_revisoes` | `int` | `6` | ✅ |

```json
{
  "preço": 68450.32
}
```

</details>

<details>
<summary><b>⚠️ Resposta em caso de erro</b></summary>

```json
{
  "erro": "descrição do erro retornada pela exceção"
}
```

</details>

---

> 💡 **Dica:** você pode testar a API rapidamente com ferramentas como [Postman](https://www.postman.com/), [Insomnia](https://insomnia.rest/) ou o próprio `curl`.

---

## 🛠️ Stack Tecnológica


| Camada | Tecnologia |
|---|---|
| **Linguagem** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Framework Web** | ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white) |
| **Machine Learning** | ![Scikit-Learn](https://img.shields.io/badge/-Scikit--Learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) |
| **Manipulação de Dados** | ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white) |
| **CORS** | Flask-CORS |
| **Servidor de Produção** | Gunicorn |

---

## 🌍 Deploy em Produção

O projeto já vem com `gunicorn` nas dependências, ou seja, está pronto para ser publicado em plataformas como:

<div align="center">

[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)
[![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app/)
[![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/)

```bash
# Exemplo de execução com gunicorn em produção
gunicorn app:app --bind 0.0.0.0:8000
```

---

## 🗺️ Roadmap

- [x] Análise e tratamento do dataset de carros usados
- [x] Treinamento do modelo de Regressão Linear
- [x] Construção da API REST com Flask
- [x] Endpoint de previsão de preços
- [ ] Validação e tratamento de entradas inválidas
- [ ] Testes automatizados (pytest)
- [ ] Comparação com outros algoritmos (Random Forest, XGBoost)
- [ ] Métricas de avaliação do modelo (MAE, RMSE, R²)
- [ ] Front-end simples para consumo da API
- [ ] Deploy público com link de demonstração

---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Para colaborar:

1. 🍴 Faça um **fork** do projeto
2. 🌱 Crie uma branch (`git checkout -b feature/minha-feature`)
3. 💻 Faça suas alterações e commit (`git commit -m 'feat: minha nova feature'`)
4. 📤 Envie para o seu fork (`git push origin feature/minha-feature`)
5. 🔃 Abra um **Pull Request**

---

## 📜 Licença

Distribuído sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais informações (ou sinta-se livre para estudar e reutilizar este código com os devidos créditos).

---

## 👤 Autor

**Breno209**
Desenvolvedor em formação, apaixonado por dados, IA e por transformar números em decisões inteligentes.

[![GitHub](https://img.shields.io/badge/GitHub-breno209-181717?style=for-the-badge&logo=github)](https://github.com/breno209)

---

link do meu projeto:https://road-price-predict.lovable.app

### ⭐ Gostou do projeto?

Deixe uma estrela no repositório — isso ajuda muito e motiva a continuar evoluindo o projeto!
