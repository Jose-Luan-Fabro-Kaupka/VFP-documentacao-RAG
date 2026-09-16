# Como: especificar um tipo de formulário

Você cria todos os tipos de formulários de maneira muito semelhante, mas define propriedades específicas para indicar como o formulário deve se comportar.

Se você está criando um formulário filho, especifica não apenas que ele deve aparecer dentro de outro formulário, mas também se é um formulário filho compatível com MDI, o que indica como o formulário se comporta quando maximizado. Se o formulário filho é compatível com MDI, ele se combina com o formulário pai, compartilhando a barra de título e a legenda, menus e barras de ferramentas do formulário pai. Um formulário filho que não é compatível com MDI maximiza na área de cliente completa do pai, mas mantém sua própria legenda e barra de título.

### Para especificar um formulário filho
- Crie ou edite o formulário usando o Form Designer.
- Defina a propriedade ShowWindow do formulário para um dos seguintes valores: 0 — In Screen. O pai do formulário filho será a janela principal do Visual FoxPro. 1 — In Top-Level Form. O pai do formulário filho será o formulário de nível superior ativo quando a janela filha for exibida. Use esta configuração se desejar que a janela filha apareça dentro de qualquer janela de nível superior diferente da janela principal do Visual FoxPro.
- Defina a propriedade MDIForm do formulário como .T. (true) se desejar que o formulário filho seja combinado com o pai quando maximizado, ou como .F. (false) se a janela filha deve ser mantida como uma janela separada quando maximizada.

Um formulário flutuante é uma variação de um formulário filho.

### Para especificar um formulário flutuante
- Crie ou edite o formulário usando o Form Designer.
- Defina a propriedade ShowWindow do formulário para um dos seguintes valores: 0 — In Screen. O pai do formulário flutuante será a janela principal do Visual FoxPro. 1 — In Top-Level Form. O pai do formulário flutuante será o formulário de nível superior ativo quando a janela flutuante for exibida.
- Defina a propriedade Desktop do formulário como .T. (true).

### Para especificar um formulário de nível superior
- Crie ou edite o formulário usando o Form Designer.
- Defina a propriedade ShowWindow do formulário como 2 — As Top-Level Form.
