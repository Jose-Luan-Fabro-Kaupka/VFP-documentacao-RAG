# Propriedade ListenerType

Especifica o tipo de saída de relatório que o ReportListener produz.

```foxpro
ReportListener.ListenerType [= iExpr]
```

# Valor de retorno

Tipo de dados inteiro.

A tabela a seguir lista os valores reconhecidos nativamente pelo Visual FoxPro.

| ListenerType nativo | Resultado de saída |
| --- | --- |
| -1 | (Padrão) Este é o estado base da classe nativa abstrata ReportListener. Não produz saída. |
| 0 | O ReportListener renderiza a saída página por página, enviando eventos de renderização a um driver de impressora. |
| 1 | O ReportListener renderiza todas as páginas e depois disponibiliza as páginas de saída a um novo componente Xbase armazenado em _REPORTPREVIEW. Este ListenerType não executa nenhuma ação se não houver um objeto _REPORTPREVIEW disponível. |
| 2 | O ReportListener renderiza a saída página por página, mas não a envia a uma impressora. Você pode usar a saída escrevendo código no método OutputPage, que é invocado conforme cada página é produzida. |
| 3 | O ReportListener renderiza todas as páginas de uma vez e não chama explicitamente _REPORTPREVIEW. Você pode usar a saída escrevendo código após a execução do relatório, chamando OutputPage para instruir o ReportListener a enviar uma página ao dispositivo de destino escolhido. |

O Report Output Application adiciona alguns resultados de renderização definidos pelo usuário ao conjunto nativo acima. No entanto, usar esses valores não impede que você receba simultaneamente resultados de saída nativos do Visual FoxPro do mesmo objeto ReportListener, de acordo com os valores nativos de ListenerType acima. Para obter mais informações, consulte Propriedade OutputType (Visual FoxPro).

| Chamar Report Output Application com | Resultado de saída |
| --- | --- |
| 4 | O ReportListener fornece um arquivo XML como saída. Por padrão, seu ListenerType é -1 (sem saída nativa). Você também pode definir sua propriedade ListenerType para um dos valores suportados nativamente, para dois tipos de saída ao mesmo tempo. |
| 5 | O ReportListener fornece um arquivo HTML e arquivos de imagem subsidiários opcionais como saída. Por padrão, seu ListenerType é -1 (sem saída nativa). Você também pode definir sua propriedade ListenerType para um dos valores suportados nativamente, para dois tipos de saída ao mesmo tempo. |

# Observações

Aplica-se a: Objeto ReportListener.

O Report Engine fornece um valor ListenerType ao Report Output Application quando você usa a cláusula OBJECT TYPE <N> em um comando REPORT FORM, ou quando você define SET REPORTBEHAVIOR 90, indicando que deseja usar relatórios assistidos por objetos para todos os comandos REPORT FORM. O Report Output Application mantém um registro para classes ReportListener padrão que tratam dos valores nativos de ListenerType, bem como dos dois valores adicionais de OutputType adicionados por sua própria biblioteca de classes Visual FoxPro e quaisquer outros que você indique. Para obter mais informações, consulte Report Output Application.

Suas classes ReportListener derivadas podem tratar de vários tipos de resultados de saída suportando vários valores ListenerType. Você pode usar o método SupportsListenerType para avaliar a propriedade ListenerType durante uma execução de relatório e determinar se sua classe derivada deve executar uma ação.

Você pode registrar uma única classe como o manipulador padrão para vários tipos de resultados de saída com o Report Output Application. O Report Output Application atribui o valor que recebe do Report Engine a uma propriedade complementar do seu objeto derivado de ReportListener, OutputType. Sua classe pode determinar dinamicamente o valor ListenerType correto a usar, com base no OutputType que recebe e em suas próprias capacidades de tratar diferentes resultados de saída.

Por exemplo, o Report Output Application fornece UpdateListener, a Classe base ReportListener User Feedback Foundation, como o manipulador padrão para vários valores nativos de ListenerType. Quando inicializado, UpdateListener tem um ListenerType de `-1` (sem saída). Ele verifica OutputType para determinar qual ListenerType deve ter para cada comando REPORT FORM que você executa.

# Exemplo

O código a seguir vem do método OutputType_assign da Classe base ReportListener Base Foundation, a classe da qual UpdateListener deriva. O código verifica se o valor recebido como OutputType é um dos valores ListenerType que a classe suporta e atribui o valor a ListenerType se for.

```foxpro
IF THIS.SupportsListenerType(THIS.OutputType)
   THIS.ListenerType = THIS.OutputType
ENDIF
```
