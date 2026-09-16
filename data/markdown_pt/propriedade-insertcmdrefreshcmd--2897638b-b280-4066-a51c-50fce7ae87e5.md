# Propriedade InsertCmdRefreshCmd

Especifica o comando para atualizar automaticamente o registro após a execução de um comando Insert. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.InsertCmdRefreshCmd[ = cCommand]
```

# Valor de retorno

| Termo | Definição |
| --- | --- |
| cCommand | Tipo de dados Character. A tabela a seguir lista os valores possíveis para cCommand . cCommand Descrição Cadeia de caracteres ou expressão Especifica um comando de atualização válido para a fonte de dados. Cadeia vazia ("") O objeto CursorAdapter gera o comando de atualização automaticamente. |

# Observações

Aplica-se a: Classe CursorAdapter
