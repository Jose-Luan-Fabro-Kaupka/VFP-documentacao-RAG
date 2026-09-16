# Método SupportsListenerType

Especifica se o ReportListener suporta um tipo particular de renderização de relatório.

```foxpro
? oReportListener.SupportsListenerType(iListenerType)
```

#### Parâmetros
 **iListenerType**
Especifica o tipo de mecanismo de renderização para o qual o ReportListener indica suporte.

# Valor de retorno

Tipo de dados Lógico.

Retorna True (`.T.`) se o parâmetro que você passa identifica um tipo suportado.

# Observações

Aplica-se a: objeto ReportListener.

A classe ReportListener não gerará erro se ListenerType for definido com um valor que não reconhece; simplesmente não fornece saída. Suas classes derivadas devem seguir a mesma estratégia. Implementar SupportsListenerType fornece uma maneira de informar ao usuário de sua classe o que sua classe pode tratar, sem disparar um erro.

Classes derivadas de ReportListener podem usar este método para eliminar certas formas de saída suportada nativamente de seus tipos suportados. Por exemplo, você pode criar uma classe que requer que todas as imagens de página estejam disponíveis no final da execução do relatório, assim como o Preview faz. Esta classe suporta apenas valores ListenerType 1 e 3, os dois valores que permitem usar OutputPage para solicitar imagens de página no final da execução do relatório. A classe retorna False (`.F.`) para os valores ListenerType nativos -1, 0 e 2. Esses valores ListenerType não armazenam em cache imagens de página e, portanto, não fornecem a funcionalidade que sua classe precisa.

> **Observação:** Consulte a propriedade ListenerType para obter mais informações sobre valores ListenerType suportados e reconhecidos. Este tópico também tem outro exemplo de código usando o método SupportsListenerType.

Classes derivadas de ReportListener não são obrigadas a retornar True (`.T.`) para valores adicionais, mesmo se estiverem registradas com valores inteiros adicionais na Report Output Application. Uma classe pode optar por respeitar todos os valores ListenerType nativos (0 a 3), para fornecer todos os resultados de saída suportados internamente, enquanto usa seu valor OutputType, recebido da Report Output Application, para determinar um resultado de saída alternativo.

Por exemplo, a classe foundation ReportListener HTML suporta todos os valores ListenerType nativos e não os adiciona. Ela fornece um resultado de saída alternativo, mas não ajusta nem seu valor ListenerType nem o método SupportsListenerType. Por este motivo, você pode optar por instruir o HtmlListener a visualizar ou imprimir, usando os valores ListenerType apropriados, ao mesmo tempo em que gera HTML. Para obter mais informações, consulte Propriedade OutputType (Visual FoxPro).

# Exemplo

No exemplo a seguir, você passa o valor inteiro `99` para uma instância da classe base ReportListener. Você recebe um valor de retorno False (`.F.`) porque ReportListener não suporta este tipo. Em seguida, você passa o valor inteiro `2` e recebe um valor de retorno True (`.T.`), porque este é um Listenertype suportado.

```foxpro
LOCAL loReportListener
loReportListener = CREATEOBJECT("ReportListener")
? loReportListener.SupportsListenerType(99)
* displays: .F.
? loReportListener.SupportsListenerType(2)
* displays: .T.
```
