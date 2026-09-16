# Propriedade AllowModalMessages

Especifica se um ReportListener pode fornecer mensagens modais como parte de sua interface do usuário.

```foxpro
ReportListener.AllowModalMessages [= lExpr]
```

# Valor de retorno

Tipo de dados lógico.
 **True, (.T.)**
Mensagens modais são permitidas.
**False, (.F.)**
(Padrão) Mensagens modais não são permitidas.

# Observações

Aplica-se a: Objeto ReportListener.

A classe ReportListener possui dois métodos, DoMessage e DoStatus, que você pode usar para exibir feedback do usuário de diferentes tipos. A distinção permite código diferente para exibição de mensagem modal (como um MESSAGEBOX ao concluir a execução de um relatório) e para exibição de status não modal (como uma mensagem WAIT NOWAIT para indicar progresso durante a execução do relatório).

Ao escrever código que normalmente fornece uma mensagem modal em uma classe derivada de ReportListener, use o valor de AllowModalMessages para determinar se essa mensagem é apropriada no ambiente atual. Se o valor de AllowModalMessages for `.F.`, seu código DoMessage pode decidir delegar a DoStatus para exibir uma mensagem não modal. Alternativamente, seu código DoMessage pode optar por suprimir a mensagem de feedback.

O valor da propriedade QuietMode tem precedência sobre AllowModalMessages. Se o valor de QuietMode for `.T.`, o usuário da classe opta por suprimir todo o feedback do usuário.
