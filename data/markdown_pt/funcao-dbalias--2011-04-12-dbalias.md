# Função DBALIAS( )

Retorna o alias do banco de dados definido atualmente.

```foxpro
DBALIAS()
```

# Valor de retorno

Character.

# Observações

DBALIAS( ) retorna a cadeia vazia se não houver um banco de dados atual.

# Exemplo

```foxpro
OPEN DATABASE HOME(2)+"northwind\northwind" SHARED
OPEN DATABASE HOME(2)+"tastrade\data\tastrade" SHARED
SET DATABASE TO NORTHWIND
? DBALIAS()
SET DATABASE TO TASTRADE
? DBALIAS()
? JUSTSTEM(DBC())
```
