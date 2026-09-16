# Propriedade InsertCmd

Especifica o comando a usar para inserir novas linhas. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.InsertCmd [ = cCommand ]
```

# Valor de retorno
 **cCommand**
Tipo de dados caractere. A tabela a seguir lista os valores possíveis para cCommand. cCommand Descrição Cadeia de caracteres ou expressão Especifica uma cadeia de comando válida para a fonte de dados na propriedade InsertCmdDataSource. Cadeia de caracteres vazia ("") O objeto CursorAdapter gera um comando SQL INSERT automaticamente se a propriedade AllowInsert estiver definida como True (.T.). Para obter mais informações sobre a geração automática de comandos SQL, consulte Gerenciamento de acesso a dados usando CursorAdapters.

# Observações

Aplica-se a: Classe CursorAdapter
