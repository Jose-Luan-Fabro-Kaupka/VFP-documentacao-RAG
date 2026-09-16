# Propriedade OutputType (Visual FoxPro)

Fornece o valor que o Report Engine passa para _REPORTOUTPUT para representar a cláusula OBJECT TYPE do comando LABEL ou REPORT FORM.

```foxpro
ReportListener.OutputType [= iExpr]
```

# Valor de retorno

Tipo de dados Integer.

Valor padrão: -1.

# Observações

Aplica-se a: Objeto ReportListener.

Esta propriedade é uma propriedade complementar de ListenerType. Não é usada pela ReportListener da classe base.

Os valores das duas propriedades não necessariamente correspondem, embora estejam relacionados. Se correspondem, o ReportListener fornece uma única forma de saída, especificada por ListenerType; o objeto pode substituir ou aumentar o comportamento nativo para este ListenerType. Se não correspondem, o objeto pode usar OutputType para fornecer um segundo resultado de saída, enquanto aproveita o comportamento herdado para o resultado de saída especificado por ListenerType.

Para obter mais informações e um exemplo de uso, consulte Propriedade ListenerType.

> **Dica:** Como o Visual FoxPro não usa OutputType internamente e não precisa avaliar seu valor, não há método complementar a SupportsListenerType. No entanto, se você deseja avaliar e responder somente a valores OutputType especificados, pode criar um método SupportsOutputType correspondente em sua classe derivada. Para obter mais informações, consulte Método SupportsListenerType.
