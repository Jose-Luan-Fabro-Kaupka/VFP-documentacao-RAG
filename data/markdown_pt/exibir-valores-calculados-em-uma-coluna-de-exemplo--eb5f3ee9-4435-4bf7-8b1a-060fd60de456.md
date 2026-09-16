# Exibir valores calculados em uma coluna de exemplo

Arquivo: ...\Samples\Solution\Controls\Grid\Calc.scx

Este exemplo ilustra como exibir um valor calculado em uma coluna.

Defina a propriedade ControlSource da coluna para uma expressão com um cálculo. Por exemplo, a seguinte expressão para o ControlSource da coluna Profit exibe a diferença entre o preço e o custo.

```foxpro
Products.Unit_Price - Products.Unit_Cost
```

Quando você altera um ou mais valores na expressão, o valor na coluna é atualizado automaticamente.

> **Observação:** Colunas que exibem uma expressão contendo um cálculo são somente leitura.
