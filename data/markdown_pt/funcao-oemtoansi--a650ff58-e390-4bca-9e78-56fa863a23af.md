# Função OEMTOANSI( )

Incluída para compatibilidade retroativa. Use a função CPCONVERT( ) em vez disso.

Converte cada caractere em uma expressão de caracteres para o caractere correspondente no conjunto de caracteres ANSI.

```foxpro
OEMTOANSI(expC)
```

#### Parâmetros
 expC

 OEMTOANSI() converte cada caractere em expC para o caractere correspondente no conjunto de caracteres ANSI. A expressão de caracteres expC deve conter caracteres do conjunto de caracteres MS-DOS (OEM).

 Se um caractere em expC não tiver equivalente ANSI, o caractere é convertido para um caractere ANSI semelhante. Por exemplo, caracteres de desenho de linha do MS-DOS podem não ser encontrados no conjunto de caracteres ANSI.

# Valor de retorno

Valor de retorno - Caractere

# Observações

OEMTOANSI() é suportada no FoxPro for Windows e no FoxPro for Macintosh.

Use OEMTOANSI() para mover dados do FoxPro for MS-DOS para o FoxPro for Windows e o FoxPro for Macintosh.
