# Propriedade DynamicFontName

Especifica o nome da fonte usada para exibir texto em um objeto Column. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Column.DynamicFontName [= cName]
```

# Valor de retorno
 **cName**
Especifica uma expressão de caracteres que avalia para o nome de uma fonte. A expressão é reavaliada em tempo de execução cada vez que o controle Grid é atualizado. Observação Em tempo de design, você pode visualizar uma lista de fontes disponíveis selecionando a propriedade FontName na janela Properties e clicando na seta à direita da caixa de configurações da propriedade.

# Observações

Aplica-se a: Column Object

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar esta propriedade.
