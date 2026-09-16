# Caixa de diálogo Adicionar propriedade (Report Builder)

Permite criar uma propriedade para um relatório ou um controle de relatório e depois especificar o tipo e o valor da propriedade.

Esta caixa de diálogo aparece quando você clica no botão Add na guia Advanced da caixa de diálogo Propriedades do controle de relatório ou clica no botão Add na guia Document Properties da caixa de diálogo Propriedades do relatório.
 - Como: adicionar propriedades de documento a um relatório
 **Tipo**
Especifica se a propriedade é uma expressão, text/xml, uma cadeia de caracteres, um arquivo ou um valor Booleano sim ou não.
**Nome da propriedade**
Especifica o nome da propriedade que é incluída na sua saída XML ou HTML.
**Valor**
Especifica o valor associado à propriedade. O comportamento da caixa Valor varia dependendo do Tipo da propriedade. Tipo Comportamento do Valor Expression O botão ao lado da caixa Valor abre o Expression Builder. Text/XML A caixa Valor é desabilitada, mas o botão ao lado da caixa Valor abre uma janela de edição de texto. String O botão ao lado da caixa Valor abre uma janela para você inserir um valor de cadeia de caracteres. File O botão ao lado da caixa Valor abre a caixa de diálogo Abrir para você selecionar um arquivo. Quando você seleciona um arquivo, o caminho é exibido na caixa Valor. Yes or No Valor exibe um controle de botão de opção para você escolher Yes ou No .

# Tipos de propriedade

| Propriedade | Descrição |
| --- | --- |
| Expression | Uma expressão do Visual FoxPro ou função definida pelo usuário que é avaliada em tempo de execução. |
| Text/XML | Texto que pode incluir conteúdo XML bem formado. |
| String | Uma cadeia de caracteres. Não é necessário colocar aspas ao redor do valor. |
| File | O caminho para um arquivo. |
| Yes or No | Um valor Booleano: yes ou no. |
