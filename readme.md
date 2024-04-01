## Run

Coloque sua API_KEY no .env:
- `API_KEY="3x3mpl0d3um44p1k31"`


Rodar o banco mongoDB com docker:
- `docker run --name mongodb -d -p 27017:27017 mongo`

Ou com sua conta official seguindo a [documentação do mongoDB](https://www.mongodb.com/docs/atlas/tutorial/connect-to-your-cluster/):
- `from pymongo import MongoClient`
- `client = MongoClient('<connection-string>')` ou `client = AsyncIOMotorClient('<connection-string>')`


Gerar a pasta venv, caso ela não exista:
- `python3 -m venv venv`


Ativar o venv:
- `source venv/bin/activate`


Instalar requerimentos:
- `pip install -r requirements.txt`


Rodar:
- `python main.py`


## API routes

### Versão gratuita
POST -> http://0.0.0.0:8080/save_info
  Body:
  ```json
    {
      "url": "youtube.com"
    }
  ```

POST -> http://0.0.0.0:8080/save_rank
  Body: none

GET -> http://0.0.0.0:8080/get_info
  Body:
  ```json
    {
      "url": "youtube.com"
    }
  ```

GET -> http://0.0.0.0:8080/get_info_rank

### Versão paga
POST -> http://0.0.0.0:8080/save_info_pro
  Body:
  ```json
    {
      "url": "youtube.com"
    }
  ```
GET -> http://0.0.0.0:8080/get_info_pro
  Body:
  ```json
    {
      "url": "youtube.com"
    }
  ```


# Introdução ao Teste

Este teste tem como objetivo uma API para scraping de dados do SimilarWeb e armazená-los em um banco de dados MongoDB. 

Utilizei a linguagem Python para desenvolver a solução.

O similarweb, contem diversas informações sobre acessos de website, principais paises, visitas por paginas e muito mais. 

Essa API captura todas essas informações 🙂.

Porem é paga. Para fazer o teste gratuito tem que colocar um cartão.

Optei por usar a [ferramenta gratuita](https://developers.similarweb.com/docs/digital-rank-api#get-started-with-website-digitalrank-api) para finalizar o teste.

Porem deixei pre configurado caso queiram testar com uma api key paga.

**Tasks:**

1. [x] **Desenvolvimento da API:**
    - [x] Implementar uma API que realize scraping de dados de websites listados e armazene as informações no MongoDB.
2. [x] **Endpoints da API:**
    - [x] **`POST /salve_info`**: Este endpoint deve receber uma URL de um site, realizar o scraping dos dados no SimilarWeb e salvar as informações no MongoDB.
    - [x] **`POST /get_info`**: Este endpoint deve receber uma URL, buscar as informações do site no banco de dados e retorná-las. 
    - [x] Se as informações ainda não estiverem disponíveis, deve retornar um código de erro.
    

[x] **Requisitos Técnicos:**

## Versão gratuita
- [x] As informações a serem salvas incluem: 
  - [x] Classificação;
  - [x] Site;
  - [x] Ranking dos sites mais visitados.

## Versão paga
**Não está testado essa parte, porem de acordo com a [documentação](https://developers.similarweb.com/reference/api-lite), acredito que deva funcionar com uma api key paga:**
- [x] As informações a serem salvas incluem: 
  - [x] Classificação;
  - [x] Site;
  - [x] Categoria;
  - [x] Mudança de Ranking;
  - [x] Duração Média da Visita;
  - [x] Páginas por Visita;
  - [x] Taxa de Rejeição;
  - [x] Principais Países;
  - [x] Distribuição por Gênero;
  - [x] Distribuição por Idade;
  - [x] entre outros dados disponíveis.

- [x] [Ponto Extra] A API deve ser assíncrona, retornando um código 201 com um ID para verificação posterior do status da operação.
- [x] [Ponto Extra] Não utilizar Selenium, Playwright, Cypress ou qualquer outro automatizador de navegador para o scraping.

**Critérios:**

- [x] **Funcionalidade:** Capacidade de salvar informações conforme especificado.
- [x] **Eficiência:** Implementação de uma API assíncrona com retorno de status adequado.
- [x] **Qualidade do Código:** O código deve ser escrito em Python, priorizando clareza e manutenibilidade.
- [x] **Conformidade com Requisitos:** Adesão aos requisitos técnicos, incluindo a proibição do uso de automatizadores de navegador.
