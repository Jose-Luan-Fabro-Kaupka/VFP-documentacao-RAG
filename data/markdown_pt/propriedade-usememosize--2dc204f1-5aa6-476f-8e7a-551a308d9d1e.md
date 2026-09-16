# Propriedade UseMemoSize

Especifica o tamanho mínimo em bytes para retornar colunas de resultado em campos memo. Por exemplo, se a largura de um resultado de coluna exceder o valor de UseMemoSize, o resultado da coluna é armazenado em um campo memo. Leitura/gravação.

> **Observação:** Definir UseMemoSize se aplica somente a objetos CursorAdapter com fontes de dados ODBC ou ADO e substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

Ao trabalhar com esta propriedade para cursors regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ).

```foxpro
CursorAdapter.UseMemoSize [= nValue]
```

# Valor de retorno
 **nValue**
Tipo de dados numérico. O parâmetro nValue tem um valor padrão de 255 bytes e pode variar de 1 byte a 255 bytes.

# Observações

Aplica-se a: classe CursorAdapter

Esta propriedade se aplica principalmente a views remotas e definir isso não afeta views locais. No entanto, você pode predefinir esta propriedade para views locais que serão upsized.
