# Usando modelos de formulário

Os modelos de formulário permitem definir propriedades padrão para seus formulários, de modo que você possa facilmente dar a todos os formulários de sua aplicação uma aparência consistente. Você poderia incluir um logotipo da empresa, por exemplo, e usar um esquema de cores consistente em todos os seus formulários, projetando uma classe de formulário modelo com esses atributos. Se o logotipo da empresa mudar, você poderia alterar a imagem na classe de formulário modelo e todos os formulários criados com base no modelo herdariam automaticamente o novo logotipo.

Você pode adicionar propriedades e métodos personalizados à classe Form do Visual FoxPro para que essas propriedades e métodos estejam disponíveis para cada formulário em sua aplicação. Se você está acostumado a criar variáveis e procedimentos definidos pelo usuário com escopo de formulário, usar propriedades e métodos personalizados fornece essa funcionalidade e também permite um modelo de encapsulamento mais limpo.

Você pode especificar modelos de form set da mesma forma que define modelos de formulário. As seguintes combinações são possíveis:
 - Tanto o modelo de form set quanto o modelo de formulário são especificados. Escolher Form na caixa de diálogo New (e todas as outras maneiras de criar um novo formulário) criará automaticamente um form set baseado na classe de form set modelo. Quando você escolhe Add New Form no menu Form no Form Designer, um formulário baseado em seu modelo de formulário é adicionado ao form set.
- Somente o modelo de form set é especificado. Escolher Form na caixa de diálogo New (e todas as outras maneiras de criar um novo formulário) criará automaticamente um form set baseado na classe FormSet modelo. Quando você escolhe Add New Form no menu Form no Form Designer, um formulário baseado na classe base Form do Visual FoxPro é adicionado ao form set.
- Somente o modelo de formulário é especificado. Escolher Form na caixa de diálogo New (e todas as outras maneiras de criar um novo formulário) criará automaticamente um formulário baseado na classe Form modelo.
- Nenhum modelo é especificado. Escolher Form na caixa de diálogo New (e todas as outras maneiras de criar um novo formulário) criará automaticamente um formulário baseado na classe base Form do Visual FoxPro.

Para obter mais informações, consulte How to: Set Form Templates.
