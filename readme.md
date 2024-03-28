


## Run

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`docker run --name mongodb -d -p 27017:27017 mongo`

`python main.py`


### Start venv

´´shell
  # activate
  source .venv/bin/activate

  # deactivate
  deactivate
´´



### Start MongoDB

´´´shell
  docker run --name speedio-mongo -d -p 27017:27017 mongo:4.4
  # or
  docker run --name mongodb -d -p 27017:27017 mongo
´´´



# Introdução ao Teste

Este teste tem como objetivo uma API para scraping de dados do SimilarWeb e armazená-los em um banco de dados MongoDB. 

Utilizei a linguagem Python para desenvolver a solução.

O similarweb, contem diversas informações sobre acessos de website, principais paises, visitas por paginas e muito mais. 

Essa API captura todas essas informações 🙂.

**Tasks:**

1. [] **Desenvolvimento da API:**
    - [] Implementar uma API que realize scraping de dados de websites listados e armazene as informações no MongoDB.
2. [] **Endpoints da API:**
    - []**`POST /salve_info`**: Este endpoint deve receber uma URL de um site, realizar o scraping dos dados no SimilarWeb e salvar as informações no MongoDB.
    - []**`POST /get_info`**: Este endpoint deve receber uma URL, buscar as informações do site no banco de dados e retorná-las. 
    - [] Se as informações ainda não estiverem disponíveis, deve retornar um código de erro.
    

[] **Requisitos Técnicos:**

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

- [] **Funcionalidade:** Capacidade de salvar informações conforme especificado.
- [] **Eficiência:** Implementação de uma API assíncrona com retorno de status adequado.
- [] **Qualidade do Código:** O código deve ser escrito em Ruby, priorizando clareza e manutenibilidade.
- [] **Conformidade com Requisitos:** Adesão aos requisitos técnicos, incluindo a proibição do uso de automatizadores de navegador.

🚨**Prazos e Informações adicionais:**

- Você terá 5 dias a partir do recebimento desse teste.
- Depois de feito, enviei no github em um repositorio publico e compartilhar o link conosco.


## Infos
https://rapid-fortnight-294.notion.site/Teste-para-o-backend-5c20a5399b9c481d8b51744cf6473bb9