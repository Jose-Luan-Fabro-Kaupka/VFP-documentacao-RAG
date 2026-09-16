# Função PROW( )

Retorna o número da linha atual do cabeçote de impressão da impressora.

```foxpro
PROW()
```

# Valor de retorno

Numérico

# Observações

Se você emitir EJECT, o Visual FoxPro redefine PROW( ) para 0.

PROW( ) é especialmente útil para endereçamento relativo de texto impresso.

# Exemplo

No exemplo a seguir, os dois comandos retornam o mesmo resultado. Você pode usar o operador $ no lugar de PCOL( ). Tanto $ quanto PCOL( ) retornam a posição atual da coluna da impressora.

```foxpro
@ PROW(), PCOL() + 12 SAY 'Contact person'
@ PROW(), $+12 SAY 'Contact person'
```
