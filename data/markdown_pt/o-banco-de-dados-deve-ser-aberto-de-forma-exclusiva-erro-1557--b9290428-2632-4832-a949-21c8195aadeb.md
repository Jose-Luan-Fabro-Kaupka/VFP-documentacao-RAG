# O banco de dados deve ser aberto de forma exclusiva (Erro 1557)

Comandos como VALIDATE DATABASE RECOVER, PACK DATABASE e aqueles envolvendo criação ou modificação de objetos de banco de dados requerem acesso exclusivo ao banco de dados.

Feche o banco de dados e reabra-o usando OPEN DATABASE Command FileName EXCLUSIVE.
