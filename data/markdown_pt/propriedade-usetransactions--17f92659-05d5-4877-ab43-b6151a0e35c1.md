# Propriedade UseTransactions

Especifica se o CursorAdapter usa transações ao enviar comandos Insert, Update ou Delete por meio de ADO ou ODBC. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UseTransactions[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações para a propriedade UseTransactions são: Configuração Descrição True (.T.) (Padrão) O CursorAdapter usa transações ao enviar comandos Insert, Update ou Delete por meio de ADO ou ODBC. False (.F.) O CursorAdapter não usa transações ao enviar comandos Insert, Update ou Delete por meio de ADO ou ODBC.

# Observações

Aplica-se a: Classe CursorAdapter.

O objeto CursorAdapter depende das APIs ADO e ODBC para gerenciar transações. Se você ignorar as recomendações da API e enviar comandos de transação específicos diretamente para um backend ADO ou ODBC, você pode querer definir a propriedade UseTransactions como False (.F.) para evitar interação indesejável de transações.
