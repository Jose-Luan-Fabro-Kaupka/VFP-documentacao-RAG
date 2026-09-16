# Substituir configurações de propriedade padrão

Para uma classe definida pelo usuário, você pode alterar os valores padrão de propriedades que não estão marcadas como Protected quando adiciona objetos baseados nessa classe a um formulário. Esta ação substitui os valores padrão dessas propriedades conforme definidos pela classe. Se você alterar posteriormente os valores padrão de propriedades na classe, por exemplo, usando o Class Designer, os valores dessas propriedades para o objeto no formulário não são afetados.

No entanto, se você não alterar o valor padrão da propriedade ao adicionar o objeto ao formulário e alterar o valor padrão da propriedade na classe, o valor da propriedade do objeto é alterado para corresponder ao novo valor padrão.

Por exemplo, suponha que você adicione um botão de comando baseado em uma classe definida pelo usuário a um formulário e altere a propriedade BackColor de branco para vermelho. Se você alterar o valor padrão da propriedade BackColor na classe definida pelo usuário para verde, a cor de fundo do botão de comando no formulário permanece vermelha. No entanto, se você não alterar a cor de fundo do botão de comando e alterar a cor padrão da propriedade BackColor na classe para verde, a cor de fundo do botão de comando no formulário herda a alteração e é definida como verde.
