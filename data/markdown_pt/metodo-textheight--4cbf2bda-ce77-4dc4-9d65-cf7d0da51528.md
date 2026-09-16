# Método TextHeight

Retorna a altura de uma cadeia de caracteres de texto conforme seria exibida na fonte atual.

```foxpro
 [nHeight =] [Form.]TextHeight(cText)
```

#### Parâmetros
 **nHeight**
Retorna um valor em pixels que especifica a altura da cadeia de caracteres de texto.
**cText**
Especifica a cadeia de caracteres para a qual a altura do texto é determinada.

# Observações

Aplica-se a: Objeto Form | Variável de sistema _SCREEN

O método TextHeight determina a quantidade de espaço vertical necessária para exibir cText. A altura retornada inclui o espaço de entrelinha acima e abaixo da cadeia de caracteres, para que você possa usar a altura retornada para calcular e posicionar várias linhas de texto dentro do formulário. Se cText contém retornos de carro incorporados, o método TextHeight retorna a altura cumulativa das linhas, incluindo o espaço de entrelinha acima e abaixo de cada linha.
