# Guia Avançado, caixa de diálogo Propriedades do controle de relatório (Report Builder)

A guia Avançado permite definir, adicionar ou excluir propriedades personalizadas para um controle de relatório. Você também pode usá-la para alterar a rotação do controle. A caixa de diálogo Propriedades do controle de relatório aparece quando você clica em Propriedades no menu de contexto de um controle de relatório ou quando você clica duas vezes em um controle de relatório.
 **Propriedades**
Lista as propriedades associadas ao controle de relatório. Também lista os valores das propriedades. Clique em um item na lista para selecioná-lo e, em seguida, habilite os botões Editar e Limpar.
**Editar**
Exibe a caixa de diálogo Expression Builder para que você possa editar o valor da propriedade selecionada.
**Adicionar**
Exibe a caixa de diálogo Adicionar propriedade (Report Builder) para que você possa adicionar uma nova propriedade personalizada. Nesta caixa de diálogo, você pode especificar o nome, o tipo e o valor da propriedade.
**Limpar**
Exclui a propriedade selecionada.
**Ângulo**
Permite digitar o ângulo desejado ou selecionar o ângulo no spinner.

# Propriedades padrão

As seguintes propriedades estão associadas a um controle de relatório quando você o adiciona a um relatório. Você pode editar os valores, excluir as propriedades ou adicionar novas propriedades.

| Propriedade | Descrição |
| --- | --- |
| HTML.Link | Quando você executa o relatório com saída HTML, a expressão avaliada é incluída como um atributo HREF em uma tag de âncora para o controle. |
| HTML.Anchor | Quando você executa o relatório com saída HTML, a expressão avaliada é incluída como um atributo name em uma tag de âncora para o controle. |
| HTML.Alt-Title | Quando você executa o relatório com saída HTML, a expressão avaliada é incluída como um atributo title em um elemento para o controle. |
| HTML.CSSClass.OverrideFRX | Quando você executa o relatório com saída HTML, o aplicativo ReportOutput cria classes CSS com definições de estilo para cada elemento do relatório. Se você definir a propriedade HTML.CSSFile do relatório na guia Propriedades do documento, caixa de diálogo Propriedades do relatório (Report Builder) da caixa de diálogo Propriedades do Report Builder para um arquivo CSS, você pode usar a propriedade HTML.CSSClass.OverrideFRX para especificar uma classe CSS nesse arquivo. Isso substitui o estilo criado pelo Report Builder. |
| HTML.CSSClass.ExtendFRX | Se você definir a propriedade HTML.CSSFile do relatório para um arquivo CSS, pode usar esta propriedade para especificar uma classe que adiciona características de estilo ao estilo criado pelo Report Builder. |
| HTML.PrintablePageLink | Nos relatórios HTML, o sistema cria um arquivo bitmap para cada página. Isso ocorre quando os bitmaps impressos são uma representação muito mais próxima da página original do que o HTML. Definir isso como true em um controle transformará o controle em um hiperlink para a imagem. |
| ListenerRef.NoRenderWhen | Quando esta expressão é avaliada como true (.T.), a página impressa não incluirá o objeto especificado. |
| ListenerRef.Preprocess.NoRenderWhen | Quando esta expressão é avaliada como true (.T.), a página impressa não incluirá o objeto especificado durante a primeira passagem de uma execução de relatório de múltiplas passagens. |

# Rotação de objeto

A área Rotação de objeto permite rotacionar o controle de relatório de 0 a 360 graus. O ponto de pivô da rotação é o canto superior esquerdo do controle. Você pode clicar na área de visualização de rotação de objeto para alterar o ângulo ou usar o spinner Ângulo para definir o ângulo de forma mais explícita.
