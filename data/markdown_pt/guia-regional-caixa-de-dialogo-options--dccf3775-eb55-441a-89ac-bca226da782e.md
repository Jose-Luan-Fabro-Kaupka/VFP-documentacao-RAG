# Guia Regional, caixa de diálogo Options

Contém opções para formatação de data, hora e números. Você pode substituir temporária ou persistentemente as configurações do sistema no Visual FoxPro. As configurações de opção nesta guia são refletidas na saída de hora, data e moeda.

Quando você escolhe Set As Default — que aparece em cada guia da caixa de diálogo — o Visual FoxPro salva as configurações de opção no registro (banco de dados de registro do sistema Windows).
 **Use System Settings**
Especifica que todas as configurações nesta guia são lidas do sistema (conforme estabelecido no Painel de Controle). Neste modo, a maioria das opções é somente leitura. Se você desmarcar esta opção, pode especificar configurações que substituem as configurações do sistema.

# Data e hora

Especifica como os dados de data e hora são exibidos por padrão. Um exemplo das configurações atuais aparece na caixa superior direita do grupo de opções.
 **Date format**
Especifica a ordem do dia, mês e ano em uma data. Escolha Short para remover zeros à esquerda da data. Escolha Long para exibir a data por extenso. Corresponde ao SET DATE Command .
**Date Separator**
Especifica o caractere que aparece entre partes de uma data. Desmarque esta opção para usar o separador padrão. Corresponde ao SET MARK TO Command .
**Century**
Especifica que o ano é exibido com informação de século (por exemplo, 1997). Desmarque esta opção para exibir o ano com 2 dígitos (por exemplo, 97). Corresponde ao SET CENTURY Command .
**12-Hour**
Especifica que as horas são exibidas no formato de 12 horas com "AM" ou "PM."
**24-Hour**
Especifica que as horas são exibidas no formato de 24 horas.
**Seconds**
Especifica que os segundos são incluídos na exibição de hora.

# Moeda e números

Especifica como os dados de moeda são exibidos por padrão. Um exemplo das configurações atuais aparece na caixa superior direita do grupo de opções.
 **Currency Format**
Especifica a localização do símbolo de moeda. Corresponde ao SET CURRENCY Command .
**Currency Symbol**
Especifica o caractere ou caracteres usados para moeda. Corresponde ao SET CURRENCY Command .
**1000 Separator**
Especifica o caractere inserido a cada terceiro dígito à esquerda do separador decimal. Corresponde ao SET SEPARATOR Command .
**Decimal Separator**
Especifica um caractere usado para indicar o decimal. Corresponde ao SET POINT Command .
**Decimal Digits**
Especifica o número de dígitos após o separador decimal. Corresponde ao SET DECIMALS Command .
**Week Starts on**
Especifica em qual dia a semana começa. Corresponde ao SET FDOW Command .
**First Week of Year**
Especifica onde um calendário anual começa. Corresponde ao SET FWEEK Command .
