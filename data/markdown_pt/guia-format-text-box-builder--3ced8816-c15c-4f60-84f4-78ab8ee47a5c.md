# Guia Format, Text Box Builder

Esta guia no Text Box builder especifica opções diversas de formato para a caixa de texto e o tipo de máscara de entrada.
 **Data Type**
Especifica um tipo de dados Character, Date, Logical ou Numeric para sua caixa de texto. Se você escolher um valor na guia Value, certifique-se de que seja do mesmo tipo de dados do valor especificado aqui.
**Enable at Run Time**
Especifica que a caixa de texto seja habilitada quando o formulário é executado. Esta opção está disponível para todos os tipos de dados e é marcada por padrão. Esta opção corresponde à propriedade Enabled.
**Alphabetic Characters Only**
Especifica que apenas caracteres alfabéticos sejam permitidos na caixa de texto (sem números ou símbolos). Esta opção está disponível somente para o tipo de dados Character. Esta opção corresponde à configuração "A" da propriedade Format.
**Make Read-Only**
Impede que o usuário altere o texto na caixa de texto. Esta opção corresponde à propriedade ReadOnly e está disponível para todos os tipos de dados.
**Select on Entry**
Especifica que o texto na caixa de texto seja selecionado quando a caixa de texto tem o foco. Esta opção está disponível somente para o tipo de dados Character. Esta opção corresponde à configuração "K" da propriedade Format.
**HideSelection**
Especifica se o texto selecionado na caixa de texto permanece visivelmente selecionado quando a caixa de texto não tem o foco. Esta opção corresponde à propriedade HideSelection e está disponível para todos os tipos de dados.
**Display Leading Zeros**
Especifica que zeros à esquerda do ponto decimal sejam exibidos. Isso está disponível somente para o tipo de dados Numeric. Esta opção corresponde à configuração "L" da propriedade Format.
**Use Current SET DATE**
Adiciona a configuração "D" à propriedade Format para que as entradas de data sigam o SET DATE atual ou o Date Format da guia Regional da caixa de diálogo Options. Esta opção aparece quando você seleciona Date na caixa suspensa Data Type.
**British Date**
Adiciona a configuração "E" à propriedade Format para que as entradas de data sigam a formatação britânica do SET DATE ou do Date Format da guia Regional da caixa de diálogo Options. Esta opção aparece quando você seleciona Date na caixa suspensa Data Type.
**InputMask**
Especifica o formato da entrada do usuário para campos Numeric , Character e Logical. Várias opções estão disponíveis na lista suspensa; um exemplo da máscara de entrada selecionada aparece à direita da lista suspensa. Por exemplo, uma máscara de entrada para o tipo de dados Numeric é o formato de número de telefone norte-americano: (###) ###-####.
