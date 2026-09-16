# Comando INSERT

Incluído para compatibilidade com versões anteriores. Use o Comando APPEND ou o Comando INSERT - SQL.

Insere um novo registro na tabela atual imediatamente após o registro atual e exibe o novo registro para edição.

```foxpro
INSERT [BEFORE] [BLANK]
```

# Observações

INSERT está incluído para compatibilidade com versões anteriores. Use APPEND ou INSERT - SQL.

Se SET CARRY estiver ON e BLANK não estiver incluído, os dados do registro anterior são automaticamente copiados para o novo registro.

Se o arquivo estiver indexado, INSERT funciona como APPEND.
