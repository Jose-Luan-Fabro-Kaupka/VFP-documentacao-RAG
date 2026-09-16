# Propriedade MaxWidth

Especifica a largura máxima até a qual um formulário pode ser redimensionado. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.MaxWidth[ = nMaxWidth]
```

# Valor de retorno
 **nMaxWidth**
Especifica a largura máxima até a qual um formulário pode ser redimensionado, na unidade de medida especificada pela propriedade ScaleMode do formulário.

# Observações

Aplica-se a: objeto Form | variável de sistema _SCREEN

Quando o usuário dimensiona um formulário escolhendo o comando Size no menu Control ou arrastando as bordas do formulário, ele não ultrapassa a largura especificada na configuração da propriedade MaxWidth.

O padrão da configuração da propriedade MaxWidth é –1; nenhuma largura máxima é especificada.
