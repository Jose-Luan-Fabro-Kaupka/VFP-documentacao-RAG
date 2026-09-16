# Guia Format, caixa de diálogo Report Control Properties (Report Builder)

Permite especificar expressões de formato para a saída gerada a partir de controles de relatório Field no Report Designer ou Label Designer. Para obter mais informações, consulte Format Expressions for Field Controls. e Função TRANSFORM( ).

> **Observação:** Esta guia substitui a funcionalidade da caixa de diálogo nativa Format (Field) do Visual FoxPro quando o Report Builder está ativo.
 - Como: especificar tipos de dados para controles de campo
- Como: definir alinhamento do conteúdo de controles de relatório

# Opções gerais de formatação
 **Format expression**
Especifica uma expressão de formato, que pode incluir códigos de formato e caracteres de modelo de formato, em vez de selecionar opções no grupo Format options.
**Character**
Especifica que a saída do controle de relatório Field tem tipo Character e exibe as opções apropriadas no grupo Format options.
**Numeric**
Especifica que a saída do controle de relatório Field tem tipo Numeric e exibe as opções apropriadas no grupo Format options.
**Date**
Especifica que a saída do controle de relatório Field tem tipo Date e exibe as opções apropriadas no grupo Format options.

# Opções de formatação específicas por tipo de dados

Exibe opções de formato disponíveis dependendo do tipo de dados selecionado.
 **Template characters**
Determina como modelos de formato adicionais são exibidos com saída do tipo Character: Overlay Especifica que caracteres adicionais no modelo de formato substituem a saída do controle de relatório Field. Interleave Especifica que caracteres adicionais nos caracteres do modelo de formato são exibidos com a saída do controle de relatório Field. Por exemplo, suponha que um registro na tabela subjacente contém os caracteres ABC1234, e você especifica o modelo de formato NNN-NNNN. Escolher Overlay exibe ABC1234 como ABC-234; enquanto escolher Interleave exibe ABC1234 como ABC-1234.
**To upper case**
Exibe saída com tipo Character em caracteres maiúsculos.
**SET DATE format**
Especifica que a saída apareça como uma data usando a configuração de formato atual do comando SET DATE. Para obter mais informações, consulte Comando SET DATE .
**British date**
Exibe a saída como uma data no formato de data britânico. Para obter mais informações, consulte Comando SET DATE .
**Blank if empty**
Não exibe saída com tipos Date que estão vazios.
**Justification**
Especifica que a saída com tipo Character use uma das seguintes configurações de alinhamento de texto: Left Alinha a saída com a posição mais à esquerda no controle Field. Right Alinha a saída com a posição mais à direita no controle Field. Center Alinha a saída com o centro do controle Field.
**Left justify**
Alinha a saída com tipo Numeric com a posição mais à esquerda no controle Field.
**Blank if zero**
Não exibe saída com tipo Numeric que consiste apenas em zeros.
**(Negative)**
Exibe e envolve valores negativos na saída com tipo Numeric com parênteses (()).
**CR if positive**
Exibe e segue valores positivos na saída com tipo Numeric com o texto, "CR (credit)".
**DB if negative**
Exibe e segue valores negativos na saída com tipo Numeric com o texto, "DB (debit)".
**Leading zeros**
Exibe todos os zeros à esquerda na saída com tipo Numeric.
**Currency**
Exibe saída com tipo Numeric usando o formato de moeda especificado na guia Regional na caixa de diálogo Options. Para obter mais informações, consulte Guia Regional, caixa de diálogo Options .
**Scientific**
Exibe saída com tipo Numeric em notação científica, o que pode ser útil para números muito grandes ou muito pequenos.
**Trim mode for character expressions**
Especifica como expressões de caracteres que têm espaço de renderização insuficiente no controle de expressão de campo são aparadas. Os valores possíveis são: Default (como em versões anteriores do Visual FoxPro) Trim to nearest character Trim to nearest word Trim to nearest character, append ellipsis Trim to nearest word, append ellipsis Trim "filespec" style with an intermediate ellipsis Consulte o tópico Usando GDI+ em relatórios para obter mais informações sobre opções de aparagem de cadeias de caracteres.
