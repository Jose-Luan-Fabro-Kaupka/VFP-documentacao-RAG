# Amostra Display Different Pages without Tabs

Arquivo: ...\Samples\Solution\Controls\PgFrame\Pfsam2.scx

Esta amostra demonstra a manipulação de páginas sem guias em um formulário. O frame no meio do formulário contém três páginas que são trazidas para a frente conforme o usuário escolhe botões de comando. Cada página pode ter seus próprios controles e aparência.

O método que traz uma página específica para a frente é ZOrder. Por exemplo, a linha de código a seguir no evento click de um dos botões de comando traz pagCustomers para a frente:

```foxpro
THISFORM.pgfPeople.pagCustomers.ZOrder
```

Você também pode usar a propriedade ActivePage do page frame para determinar quais páginas são exibidas.

```foxpro
THISFORM.pgfPeople.ActivePage = 1
```
