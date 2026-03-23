import sqlite3 
 #Cria/connecta no banco 
conn = sqlite3.connect(´pizzas.db´)
cursor = conn.cursor ()
#Cria tabela de pizzas
cursor.execute( ´´´
CREATE TABLE IF NOT EXIST pizzas( id INTEGER PRIMARY KEY, 
                                 nome TEXT, 
                                 preco REAL ) 
´´´) 
# Adiciona pizzas exemplo
pizzas = [ 
( ´Margherita`, 35.0`)
( `Calabresa`, 40.0)
( `Quatro Queijo`, 45.0) 
  ]
cursor.executamy (`INSERT OR IGNORE INTO pizzas (nome, preco) VALUE conn.commit()
# Mostra as pizzas
cursor.execute(`SELECT * FROM pizzas`) 
print(cursor.fetchall() ) 

conn.close()
  
