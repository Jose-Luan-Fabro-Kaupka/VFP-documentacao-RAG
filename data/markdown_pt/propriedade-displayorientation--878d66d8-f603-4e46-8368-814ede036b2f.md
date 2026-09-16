# Propriedade DisplayOrientation

Especifica a orientação de exibição para um aplicativo em execução em um Tablet PC.

```foxpro
_SCREEN.DisplayOrientation [= nValue]
```

# Valor de retorno
 **nValue**
As configurações da propriedade DisplayOrientation são: Configuração Descrição 0 A exibição está no modo Upright Landscape. 1 A exibição está no modo Upright Portrait. 2 A exibição está no modo Inverted Landscape. 3 A exibição está no modo Inverted Portrait. Se você omitir o parâmetro nValue, DisplayOrientation retorna um valor que indica a orientação de exibição atual.

# Observações

A propriedade DisplayOrientation é de leitura/gravação. Se você alterar o valor da propriedade DisplayOrientation, a orientação de exibição do Tablet PC é girada como seria no painel de controle do Tablet PC.

Você pode detectar um evento de rotação de tela do Tablet PC usando a Função BINDEVENT( ) com a propriedade DisplayOrientation.
