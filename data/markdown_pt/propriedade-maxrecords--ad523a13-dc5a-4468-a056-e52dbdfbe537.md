# Propriedade MaxRecords

Especifica o número máximo de linhas a buscar quando conjuntos de resultados são retornados. Ao trabalhar com esta propriedade para cursors regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** Definir MaxRecords se aplica apenas a objetos CursorAdapter com fontes de dados ODBC ou ADO e substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.MaxRecords [= nValue]
```

# Valor de retorno
 **nValue**
Tipo de dados numérico. O parâmetro nValue tem um valor padrão de -1, que especifica que todas as linhas sejam retornadas. Definir nValue como 0 especifica que a view é executada, mas nenhum resultado é buscado.

# Observações

Aplica-se a: Classe CursorAdapter

MaxRecords se aplica principalmente a views remotas e definir isso não afeta views locais. No entanto, você pode predefinir esta propriedade para views locais que serão convertidas para tamanho maior.
