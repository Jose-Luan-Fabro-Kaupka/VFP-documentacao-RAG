# Propriedade UpdateCmd

Especifica o comando a usar ao atualizar tabelas. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UpdateCmd [ = cCommand ]
```

# Valor de retorno
 **cCommand**
Tipo de dados Character. A tabela a seguir lista os valores possíveis para cCommand . cCommand Descrição Cadeia de caracteres ou expressão Especifica uma cadeia de comando válida para a fonte de dados na propriedade UpdateCmdDataSource. Cadeia vazia ("") O objeto CursorAdapter gera um comando SQL UPDATE automaticamente se a propriedade AllowUpdate do CursorAdapter estiver definida como True (.T.).

# Observações

Aplica-se a: CursorAdapter Class
