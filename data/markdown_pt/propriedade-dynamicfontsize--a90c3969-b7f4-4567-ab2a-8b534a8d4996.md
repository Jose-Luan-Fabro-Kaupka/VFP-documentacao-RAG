# Propriedade DynamicFontSize

Especifica o tamanho da fonte para texto exibido em um Column object. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Column.FontSize [= "nSize"]
```

# Valor de retorno
 **" nSize "**
Especifica uma expressão numérica que resulta em um tamanho de fonte. O tamanho de fonte padrão é 10 pontos. O valor máximo para nSize é 2.048 pontos. O tamanho da fonte é reavaliado em tempo de execução cada vez que o controle Grid é atualizado. Observação Há 72 pontos em 1 polegada.

# Observações

Aplica-se a: Column Object

Você pode usar esta propriedade para alterar o tamanho da fonte de uma linha.

> **Observação:** O método AutoFit do Grid pode não redimensionar adequadamente para exibir todo o conteúdo de uma coluna se você usar esta propriedade.
