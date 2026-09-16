# Propriedade FetchAsNeeded

Especifica como os registros são buscados. Ao trabalhar com esta propriedade para cursores regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** Definir FetchAsNeeded se aplica apenas a objetos CursorAdapter com fontes de dados ODBC ou ADO, afeta apenas o próximo cursor aberto e substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.FetchAsNeeded [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. A tabela a seguir lista os valores para lValue . lValue Descrição True (.T.) Busca registros conforme necessário. False (.F.) Para objetos CursorAdapter com fontes de dados ODBC e ADO, a propriedade MaxRecords determina o número de registros buscados. Para fontes de dados nativas e XML, todos os registros são buscados.

# Observações

Aplica-se a: classe CursorAdapter
