# Consulta MySQL com Python

Este projeto demonstra como conectar-se a um banco de dados MySQL usando Python e realizar consultas SQL.

## 🚀 Tecnologias

- Python 3
- MySQL Connector/Python

## 📌 Pré-requisitos

- Python instalado
- Banco de dados MySQL
- Biblioteca `mysql-connector-python` instalada:
  ```bash
  pip install mysql-connector-python
  ```

## 📜 Configuração

1. Configure as credenciais do banco no código:
   ```python
   con = mysql.connector.connect(
       host='seu ip ou dominio',
       database='nome do banco',
       user='usuario',
       password='senha'
   )
   ```

## 🛠 Solução de Erros

- **Erro de conexão:** Verifique as credenciais.
- **Tabela não encontrada:** Confirme se `marca` existe no banco.
- **Biblioteca não instalada:** Execute `pip install mysql-connector-python`.

## 📄 Licença

Este projeto está sob a licença MIT.

