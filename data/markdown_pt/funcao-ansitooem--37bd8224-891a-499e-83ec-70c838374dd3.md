# Função ANSITOOEM( )

Incluída para compatibilidade com versões anteriores. Use a função CPCONVERT( ) em vez disso.

Converte cada caractere de uma expressão de caractere para o caractere correspondente no conjunto de caracteres MS-DOS (OEM).

```foxpro
ANSITOOEM(expC)
```

# Valor de retorno

Return value - Character

# Observações

ANSITOOEM() é suportada no FoxPro for Windows e no FoxPro for Macintosh.

Use ANSITOOEM() para mover dados do FoxPro for Windows e do FoxPro for Macintosh para o FoxPro for MS-DOS. ANSITOOEM() converte cada caractere em expC para o caractere correspondente no conjunto de caracteres MS-DOS (OEM). A expressão de caractere expC deve conter caracteres do conjunto de caracteres ANSI.

Se um caractere em expC não tiver um equivalente MS-DOS, o caractere é convertido para um caractere MS-DOS similar.
