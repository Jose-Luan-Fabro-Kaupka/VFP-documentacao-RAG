# Guia de estilo, construtor de caixa de texto

Esta guia no construtor Text Box especifica o efeito visual, a borda e o alinhamento de caracteres da caixa de texto.

# Efeito Visual
 **3D**
Especifica uma borda esquerda e superior em negrito para a caixa de texto. Esta opção corresponde à configuração 3D da propriedade SpecialEffect.
**Simples**
Especifica que a caixa de texto é uma caixa sem sombra no formulário. Esta opção corresponde à configuração Simples da propriedade SpecialEffect.

# Fronteira
 **Solteiro**
Especifica uma única linha ao redor da caixa de texto. Esta opção corresponde à configuração Fixed-Single da propriedade BorderStyle.
**Nenhum**
Não especifica nenhuma linha ao redor da caixa de texto. Esta opção corresponde à configuração Nenhum da propriedade BorderStyle.

# Alinhamento de caracteres
 **Esquerda**
Especifica que o texto na caixa de texto será alinhado à esquerda. Esta opção corresponde à configuração Esquerda da propriedade Alignment.
**Certo**
Especifica que o texto na caixa de texto será alinhado à direita. Esta opção corresponde à configuração Right da propriedade Alignment.
**Centro**
Especifica que o texto na caixa de texto será centralizado. Esta opção corresponde à configuração Center da propriedade Alignment.
**Automático**
Especifica que o texto na caixa de texto será alinhado de acordo com o tipo de dados da fonte de controle the. Esta opção corresponde à configuração Automático (Padrão) da propriedade Alignment.
**Dimensione a caixa de texto para caber**
Dimensiona automaticamente a caixa de texto. Se uma máscara de entrada for especificada, as configurações da máscara de entrada serão usadas para ajustar a caixa de texto. Caso contrário, o comprimento do campo de propriedade ControlSource será usado para ajustar a caixa de texto. Nota Se você especificou uma máscara de entrada na guia Formato do construtor Text Box, a caixa de texto será ampliada para caber no comprimento da máscara de entrada. Se você não especificou uma máscara de entrada, a caixa de texto será ampliada para caber no comprimento do campo.
