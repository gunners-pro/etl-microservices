# :bulb: ETL Microservices

<p align="justify">
  Um projeto onde uma aplicação atua como um micro serviço(servidor API), devolvendo como resposta um JSON com dados fake.
  Outra aplicação roda em paralelo com o papel de extrair, transformar e carregar os dados; executar uma aplicação web onde é servido esses dados em forma de gráficos.
</p><br />

## :wrench: Infra-estrutura

<img src="infra.png" /><br /><br />

## :computer: Tecnologias utilizadas

<div>
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" /><br />
  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" /><br />
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/plotly-3F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white" />
</div><br />

## :hammer: Instalação

> [!IMPORTANT]
> É preciso ter docker e git instalado na sua máquina
<br />

> [!IMPORTANT]
> Renomear o arquivo '.env.example' dentro da pasta services/consumer-analytics para '.env'
<br />

- Clonar o repositorio:
```bash
  git clone https://github.com/gunners-pro/etl-microservices
```
<br />

- Entrar na pasta do projeto:
```bash
  cd etl-microservices
```
<br />

- Subir os containers docker:
```bash
  docker compose up -d
```
<br />

- Abrir a aplicação no navegador de internet:
```bash
  digite a url http://localhost:5001
```
<br />
<br />
