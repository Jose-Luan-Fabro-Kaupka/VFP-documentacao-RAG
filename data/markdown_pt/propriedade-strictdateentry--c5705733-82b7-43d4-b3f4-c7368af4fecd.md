# Propriedade StrictDateEntry

Especifica se valores Date e DateTime devem ser digitados em um formato específico e estrito em uma caixa de texto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.StrictDateEntry[ = nValue]
```

# Valor de retorno
 **nValue**
Uma das seguintes configurações: Configuração Descrição 0 Flexível. Datas e valores DateTime podem ser digitados de forma flexível. A ordem em que os dias, meses e anos são digitados é determinada pela propriedade DateFormat ou SET DATE. Espaços, barras invertidas, pontos, hifens e o delimitador de data atual (especificado com a propriedade DateMark ou SET MARK ) podem ser usados para delimitar valores de data. Se o ano for omitido de uma data, o ano atual é usado para a data. Um acento circunflexo (^) pode ser incluído como o primeiro caractere em uma data para especificar a ordenação ano-mês-dia, substituindo a ordem especificada pela propriedade DateFormat ou SET DATE. Uma vírgula ou um espaço pode ser usado para delimitar a data da hora em um valor DateTime. Ao digitar apenas uma hora em um valor DateTime, o dois-pontos pode ser omitido se o ano estiver incluído na data ou se uma vírgula for usada para separar a data da hora. Se uma data ou valor DateTime inválido for digitado, uma mensagem de erro não é exibida e o valor da caixa de texto é definido como uma data ou valor DateTime vazio. Você pode testar uma data inválida no evento Valid. 1 (Padrão) Estrito. Fornece compatibilidade com versões anteriores do Visual FoxPro. As datas em valores Date e DateTime devem ser digitadas em um formato estrito 99/99/99 quando CENTURY estiver definido como OFF, ou em um formato 99/99/9999 quando CENTURY estiver definido como ON. 99 representa dias, meses e anos, e 9999 representa anos incluindo o século. A ordem em que os dias, meses e anos são digitados é determinada pela propriedade DateFormat ou SET DATE.

# Observações

Aplica-se a: Controle TextBox (Visual FoxPro)

A tabela a seguir lista valores Date e DateTime válidos que você pode digitar em uma caixa de texto quando StrictDateEntry está definido como 0 (Flexível).

| Valor Date ou DateTime | Descrição |
| --- | --- |
| 12 31 | 31 de dezembro do ano atual. |
| 12 31 98 14 | 31 de dezembro de 1998, 14h. |
| 12 31, 14 | 31 de dezembro do ano atual, 14h. |
| 12 - 31 - 98, 2p | 31 de dezembro de 1998, 14h. Observe os espaços extras entre os delimitadores de hífen. |
| ^98-12-31, 2p | 31 de dezembro de 1998, 14h. O acento circunflexo (^) especifica a ordenação ano-mês-dia, substituindo a ordem especificada pela propriedade DateFormat ou SET DATE. |
| ^/12/31 | 31 de dezembro do ano atual. O acento circunflexo (^) especifica a ordenação ano-mês-dia, substituindo a ordem especificada pela propriedade DateFormat ou SET DATE. |
