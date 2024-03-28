## Run

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`docker run --name mongodb -d -p 27017:27017 mongo`

`python main.py`


# Introdução ao Teste

Este teste tem como objetivo uma API para scraping de dados do SimilarWeb e armazená-los em um banco de dados MongoDB. 

Utilizei a linguagem Python para desenvolver a solução.

O similarweb, contem diversas informações sobre acessos de website, principais paises, visitas por paginas e muito mais. 

Essa API captura todas essas informações 🙂.

**Tasks:**

1. [x] **Desenvolvimento da API:**
    - [x] Implementar uma API que realize scraping de dados de websites listados e armazene as informações no MongoDB.
2. [x] **Endpoints da API:**
    - [x]**`POST /salve_info`**: Este endpoint deve receber uma URL de um site, realizar o scraping dos dados no SimilarWeb e salvar as informações no MongoDB.
    - [x]**`POST /get_info`**: Este endpoint deve receber uma URL, buscar as informações do site no banco de dados e retorná-las. 
    - [x] Se as informações ainda não estiverem disponíveis, deve retornar um código de erro.
    

[x] **Requisitos Técnicos:**

- [] As informações a serem salvas incluem: 
  - [] Classificação;
  - [] Site;
  - [] Categoria;
  - [] Mudança de Ranking;
  - [] Duração Média da Visita;
  - [] Páginas por Visita;
  - [] Taxa de Rejeição;
  - [] Principais Países;
  - [] Distribuição por Gênero;
  - [] Distribuição por Idade;
  - [] entre outros dados disponíveis.

- [x] [Ponto Extra] A API deve ser assíncrona, retornando um código 201 com um ID para verificação posterior do status da operação.
- [x] [Ponto Extra] Não utilizar Selenium, Playwright, Cypress ou qualquer outro automatizador de navegador para o scraping.

**Critérios:**

- [x] **Funcionalidade:** Capacidade de salvar informações conforme especificado.
- [x] **Eficiência:** Implementação de uma API assíncrona com retorno de status adequado.
- [x] **Qualidade do Código:** O código deve ser escrito em Python, priorizando clareza e manutenibilidade.
- [x] **Conformidade com Requisitos:** Adesão aos requisitos técnicos, incluindo a proibição do uso de automatizadores de navegador.
