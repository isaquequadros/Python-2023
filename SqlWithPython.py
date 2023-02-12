import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-D010101;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

id = 4
cliente = "Kadima"
produto = "PC"
data = "24/05/2020"
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas(Id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()