# Propriedade FetchSize

Especifica o número de linhas buscadas progressivamente do conjunto de resultados da tabela remota. Ao manipular esta propriedade para cursors regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ).

> **Observação:** Definir FetchSize se aplica apenas a objetos CursorAdapter com fontes de dados ODBC ou ADO e substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.FetchSize [= nValue]
```

#### Parâmetros
 **nValue**
Tipo de dados numérico. O parâmetro nValue tem um valor padrão de 100 linhas. Se nValue for -1, o Visual FoxPro recupera o conjunto de resultados completo, que é limitado pelo valor da propriedade MaxRecords.

# Observações

Aplica-se a: CursorAdapter Class

FetchSize se aplica principalmente para remote views e definir isso não afeta local views. No entanto, você pode predefinir esta propriedade para local views que serão upsized.
