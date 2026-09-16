# Propriedade MinHeight

Especifica a altura mínima para a qual um formulário pode ser redimensionado. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.MinHeight[ = nHeight]
```

# Valor de retorno
 **nHeight**
A altura mínima para a qual o formulário pode ser redimensionado, na unidade de medida especificada pela propriedade ScaleMode do formulário.

# Observações

Aplica-se a: Form Object | Variável de sistema _SCREEN

Quando o usuário dimensiona um formulário escolhendo o comando Size no menu Control ou arrastando as bordas do formulário, o formulário não se torna mais baixo que a altura especificada na configuração da propriedade MinHeight.

A configuração padrão da propriedade MinHeight é –1; nenhuma altura mínima é especificada.
