import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host='seu ip ou dominio',
        database='nome do banco de dados',
        user='usuario',
        password='senha '
    )

    consulta_sql = "SELECT * FROM marca"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    registros = cursor.fetchall()

    print("Número total de registros retornados:", cursor.rowcount)
    print("\nMostrando os autores cadastrados:")

    for linha in registros:
        print("Codigo:", linha[0])
        print("Nome:", linha[1])
        print("Endereco:", linha[2], "\n")

except Error as e:
    print("Erro ao acessar tabela MySQL:", e)

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão bem sucedida")