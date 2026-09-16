# Tipo de dados Currency

Para armazenar valores monetários ou cálculos financeiros precisos, use o tipo de dados Currency em vez de Numeric.

> **Dica:** Você pode converter valores de Numeric para Currency e vice-versa usando as funções NTOM( ) e MTON( ). Para mais informações, consulte Tipo de dados Numeric , Função NTOM( ) e Função MTON( ) .

Para atribuir o tipo de dados Currency, use o cifrão:

```foxpro
money = $50.33
moremoney = $675.43886
```

Se você especificar mais de quatro casas decimais em uma expressão currency, o Visual FoxPro arredonda a expressão para quatro casas antes de avaliar a expressão. No exemplo, a variável `moremoney` é arredondada internamente para 675.4389.

Campos Currency respeitam configurações do sistema, como SET CURRENCY, quando exibidos em janelas Browse, campos ou quando listados na tela.

Para mais especificações sobre o tipo de dados Currency, consulte Tipos de dados e campos do Visual FoxPro.
