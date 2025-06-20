# Consulta Espacial com SQL Server e Python

Este projeto demonstra como utilizar Python para automatizar consultas espaciais em um banco de dados SQL Server com geodados do tipo `geometry`.

## 🔧 Tecnologias utilizadas

- Python 3
- SQL Server Express
- pyodbc
- Dados espaciais (`geometry`, `STContains`)

## 🗺️ O que o script faz

- Conecta ao banco SQL Server
- Cria um ponto (`POINT(0.5 0.5)`)
- Verifica quais bairros (polígonos) contêm esse ponto
- Exibe os resultados no terminal

## ▶️ Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
