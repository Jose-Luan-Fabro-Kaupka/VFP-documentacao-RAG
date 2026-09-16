# Propriedade PreviewContainer

Fornece uma referência à superfície de exibição na qual o relatório será renderizado quando o ReportListener fornecer saída do tipo Preview.

```foxpro
ReportListener.PreviewContainer [=oReference]
```

# Valor de retorno

Um objeto que implementa a API PreviewContainer. .

O valor padrão quando você cria uma instância do objeto ReportListener pela primeira vez é nulo (`.NULL.`).

# Observações

Aplica-se a: ReportListener Object.

O ReportListener armazena uma referência a um Preview Container ao renderizar um relatório no modo de visualização (ReportListener.ListenerType = `1`). Você pode fornecer a referência explicitamente ou confiar no comportamento base do ReportListener, que obtém a referência a um PreviewContainer do Report Preview Application. Para obter mais informações, consulte _REPORTPREVIEW System Variable.
