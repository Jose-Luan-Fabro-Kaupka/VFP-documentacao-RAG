# Função PCOL( )

Retorna a posição de coluna atual do cabeçote de impressão da impressora.

```foxpro
PCOL()
```

# Valor de retorno

Numérico

# Observações

O valor que PCOL( ) retorna é relativo à configuração atual da margem esquerda da impressora. Você pode definir a margem esquerda com SET MARGIN ou armazenando um valor na variável de memória do sistema _PLOFFSET.

PCOL( ) é especialmente útil para endereçamento relativo de texto impresso.

Você pode usar o operador $ no lugar de PCOL( ).

# Exemplo

```foxpro
CLEAR
@ PROW(), PCOL()+12 SAY 'Contact person'
@ PROW(), $+12 SAY 'Contact person'
```
