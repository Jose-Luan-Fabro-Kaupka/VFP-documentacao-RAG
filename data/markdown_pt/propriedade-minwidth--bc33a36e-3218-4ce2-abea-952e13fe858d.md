# Propriedade MinWidth

Especifica a largura mínima para a qual um formulário pode ser redimensionado. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.MinWidth[ = nWidth]
```

# Valor de retorno
 **nWidth**
A largura mínima para a qual o formulário pode ser redimensionado, na unidade de medida especificada pela propriedade ScaleMode do Form.

# Observações

Aplica-se a: Form Object | _SCREEN System Variable

Quando o usuário redimensiona um Form escolhendo o comando Size no menu Control ou arrastando as bordas do formulário, o Form não pode ser tornado mais estreito que a largura especificada na configuração da propriedade MinWidth.

A configuração padrão da propriedade MinWidth é – 1; nenhuma largura mínima é especificada.
