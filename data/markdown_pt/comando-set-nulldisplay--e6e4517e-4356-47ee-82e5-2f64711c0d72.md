# Comando SET NULLDISPLAY

Especifica o texto exibido para valores nulos.

```foxpro
SET NULLDISPLAY TO [cNullText]
```

#### Parâmetros
 **cNullText**
Especifica o texto exibido para valores nulos. Se cNullText for omitido, o texto padrão de valor nulo, .NULL., é restaurado e exibido para valores nulos.

# Observações

Por padrão, o Visual FoxPro exibe .NULL. para valores nulos em objetos, janelas Browse, saída DISPLAY, saída LIST e assim por diante. Use SET NULLDISPLAY para alterar o texto padrão de valor nulo para uma cadeia de caracteres diferente. SET NULLDISPLAY altera o texto padrão de valor nulo para todos os objetos cuja propriedade NullDisplay é a cadeia vazia.

Use a propriedade NullDisplay para alterar o texto padrão de valor nulo para uma cadeia de caracteres diferente para um objeto individual.
