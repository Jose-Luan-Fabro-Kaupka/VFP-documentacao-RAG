# Função COL( )

Incluída para compatibilidade com versões anteriores. Use as propriedades CurrentX e CurrentY.

Retorna a posição atual da coluna do cursor.

```foxpro
COL()
```

# Valor de retorno

Valor de retorno — Numeric

# Observações

COL() é especialmente útil para direcionar a saída de tela a uma posição de coluna relativa à posição atual do cursor.

O operador especial $ pode ser usado no lugar de COL().

# Exemplo

```foxpro
@ 5,5 SAY ''
@ ROW(), COL()+12 SAY 'Contact person'
@ ROW(), $+12 SAY 'Contact person'
```
