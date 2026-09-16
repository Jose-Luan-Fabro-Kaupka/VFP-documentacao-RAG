# Função RGBSCHEME( )

Retorna um par de cores RGB ou uma lista de pares de cores RGB de um esquema de cores especificado.

```foxpro
RGBSCHEME(nColorSchemeNumber [, nColorPairPosition])
```

#### Parâmetros
 **nColorSchemeNumber**
Especifica o número do esquema de cores para o qual você deseja uma listagem completa de cores RGB. RGBSCHEME( ) retorna 10 pares de cores RGB.
**nColorPairPosition**
Retorna um único par de cores RGB de um esquema de cores. nColorPairPosition especifica a posição do par de cores RGB no esquema de cores. Por exemplo, se nColorPairPosition for 4, o quarto par de cores RGB é retornado.

# Valor de retorno

Character

# Observações

Use SCHEME( ) para retornar um par de cores tradicional ou uma lista de pares de cores de um esquema de cores. Pares de cores RGB usam valores numéricos para especificar cores. Pares de cores tradicionais usam letras para especificar cores.

# Exemplo

O seguinte exibe o terceiro par de cores RGB do esquema de cores número 4.

```foxpro
CLEAR
? RGBSCHEME(4,3)
```
