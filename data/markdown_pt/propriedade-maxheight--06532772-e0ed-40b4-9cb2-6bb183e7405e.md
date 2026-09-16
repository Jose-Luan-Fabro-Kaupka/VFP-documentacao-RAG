# Propriedade MaxHeight

Determina a altura máxima até a qual um formulário pode ser dimensionado. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.MaxHeight[ = nHeight]
```

# Valor de retorno
 **nHeight**
A altura máxima, na unidade de medida especificada pela propriedade ScaleMode do formulário.

# Observações

Aplica-se a: Objeto Form | Variável de sistema _SCREEN

Quando o usuário dimensiona um formulário escolhendo o comando Size no menu Control ou arrastando as bordas do formulário, o formulário não excede a altura especificada na configuração da propriedade MaxHeight.

A configuração padrão da propriedade MaxHeight é –1; nenhuma altura máxima é especificada.
