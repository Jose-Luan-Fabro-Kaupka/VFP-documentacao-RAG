# Método TextWidth

Retorna a largura de uma cadeia de caracteres de texto conforme seria exibida na fonte atual.

```foxpro
 [nWidth =] [Form.]TextWidth(cText)
```

#### Parâmetros
 **nWidth**
Retorna um valor em pixels especificando a largura da cadeia de caracteres de texto.
**cText**
Especifica a cadeia de caracteres para a qual a largura do texto é determinada.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable

O método TextWidth determina a quantidade de espaço horizontal necessária para exibir cText.

Se você deseja obter o comprimento de uma expressão de caractere em relação à largura média de caractere de uma fonte, use a função TXTWIDTH( ).
