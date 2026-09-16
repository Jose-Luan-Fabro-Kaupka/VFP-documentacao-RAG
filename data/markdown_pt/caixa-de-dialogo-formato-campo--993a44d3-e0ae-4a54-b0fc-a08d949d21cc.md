# Caixa de diálogo Formato (campo)

Permite especificar expressões de formato para saída gerada a partir de controles de relatório Field no Report Designer ou Label Designer. Para obter mais informações, consulte Expressões de formato para controles Field.

> **Observação:** Dependendo da configuração da variável de sistema _REPORTBUILDER, esta caixa de diálogo pode ser substituída por uma interface alternativa. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER.

# Opções gerais de formatação
 **Formato**
Especifica uma expressão de formato, que pode incluir códigos de formato e caracteres de modelo de formato, em vez de selecionar opções no grupo Opções de edição.
**Character**
Especifica que a saída do controle de relatório Field tem tipo Character e exibe as opções apropriadas no grupo Opções de edição.
**Numeric**
Especifica que a saída do controle de relatório Field tem tipo Numeric e exibe as opções apropriadas no grupo Opções de edição.
**Date**
Especifica que a saída do controle de relatório Field tem tipo Date e exibe as opções apropriadas no grupo Opções de edição.

# Opções de edição

Exibe opções de formato dependendo do tipo de dados selecionado. Selecionar essas opções insere um código de formatação na caixa Formato na caixa de diálogo Expressão do relatório. Para obter mais informações, consulte Caixa de diálogo Expressão do relatório.
 **Para maiúsculas**
Exibe saída com tipo Character em caracteres maiúsculos.
**Ignorar máscara de entrada**
Determina como modelos de formato adicionais são exibidos com saída do tipo Character. Se Ignorar máscara de entrada estiver marcado, caracteres adicionais nos caracteres do modelo de formato são exibidos entrelaçados entre os caracteres da expressão de campo avaliada. Se Ignorar máscara de entrada estiver desmarcado, caracteres adicionais na função de modelo de formato substituem (ou sobrepõem) caracteres da expressão de campo avaliada. Por exemplo, suponha que um registro na tabela subjacente contenha os caracteres ABC1234 e você especifique o modelo de formato NNN-NNNN. Selecionar a caixa de seleção Ignorar máscara de entrada exibe ABC1234 como ABC-1234; enquanto desmarcar a caixa de seleção Ignorar máscara de entrada exibe ABC1234 como ABC-234.
**Alinhar à esquerda**
Alinha saída com tipo Character ou Numeric com a posição mais à esquerda no controle Field.
**Alinhar à direita**
Alinha saída com tipo Character com a posição mais à direita no controle Field.
**Alinhar à direita**
Alinha saída com tipo Character com o centro do controle Field.
**Em branco se zero**
Não exibe saída com tipo Numeric que consiste apenas em zeros.
**(Negativo)**
Exibe e coloca valores negativos em saída com tipo Numeric entre parênteses (()).
**Formato SET DATE**
Especifica que a saída apareça como uma data usando a configuração de formato atual do comando SET DATE. Para obter mais informações, consulte Comando SET DATE.
**Data britânica**
Exibe saída como uma data no formato de data britânico. Para obter mais informações, consulte Comando SET DATE.
**CR se positivo**
Exibe e segue valores positivos em saída com tipo Numeric com o texto "CR (crédito)".
**DB se negativo**
Exibe e segue valores negativos em saída com tipo Numeric com o texto "DB (débito)".
**Zeros à esquerda**
Exibe todos os zeros à esquerda em saída com tipo Numeric.
**Moeda**
Exibe saída com tipo Numeric usando o formato de moeda especificado na guia Regional na caixa de diálogo Opções. Para obter mais informações, consulte Guia Regional, caixa de diálogo Opções.
**Científico**
Exibe saída com tipo Numeric em notação científica, que pode ser útil para números muito grandes ou muito pequenos.
