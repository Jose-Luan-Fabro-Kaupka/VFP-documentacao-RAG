# Propriedade UpdateCmdRefreshCmd

Especifica o comando para atualizar automaticamente o registro após a execução de um comando Update. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UpdateCmdRefreshCmd[ = cCommand]
```

# Valor de retorno

| Term | Definition |
| --- | --- |
| cCommand | Tipo de dados Character. A tabela a seguir lista os valores possíveis para cCommand. cCommand Descrição Cadeia de caracteres ou expressão Especifica um comando de atualização válido para a fonte de dados. Cadeia de caracteres vazia ("") O objeto CursorAdapter gera um comando de atualização automaticamente. |

# Observações

Aplica-se a: CursorAdapter Class

> **Observação:** A propriedade AllowUpdate Property deve ser definida como True (.T.) para permitir operações de atualização em uma fonte de dados.

Para obter mais informações sobre como o Visual FoxPro atualiza CursorAdapters, consulte Data Access Management Using CursorAdapters.
