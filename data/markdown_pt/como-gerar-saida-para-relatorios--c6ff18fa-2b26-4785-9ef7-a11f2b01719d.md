# Como: gerar saída para relatórios

Você pode gerar relatórios e etiquetas de saída executando o seguinte:
 - Imprimindo relatórios
- Enviando relatórios para a tela
- Enviando relatórios para um arquivo
- Salvando relatórios como HTML

> **Observação:** Algumas das ações discutidas neste tópico têm resultados diferentes, dependendo da configuração de REPORTBEHAVIOR. Quando você usa o comando SET REPORTBEHAVIOR 90, o Visual FoxPro usa um objeto ReportListener para gerar seus resultados por meio de GDI+ em vez de GDI. Para obter mais informações, consulte o comando SET REPORTBEHAVIOR.

# Imprimindo relatórios

Você pode alterar as configurações da impressora antes de imprimir o relatório ou imprimir o relatório programaticamente.

### Para imprimir um relatório ou etiqueta
- Escolha a opção Print… no menu File e selecione Report ou Label como o tipo de saída a imprimir na caixa de diálogo Print. Clique no botão de reticências (...) para escolher o arquivo de relatório ou etiqueta (.frx ou .lbx) a imprimir. Como alternativa, abra o relatório ou etiqueta no designer apropriado e clique em Run Report no menu Report.
- A caixa de diálogo Print abre para que você possa fazer alterações nas configurações da impressora.
- Na caixa de diálogo Print, clique em Print.

### Para imprimir relatórios e etiquetas programaticamente
- Opção 1: Use o comando REPORT FORM ou LABEL com a cláusula TO PRINTER.
- Opção 2: Use o comando REPORT FORM ou LABEL com a cláusula OBJECT TYPE 0.
- Opção 3: Use o comando REPORT FORM ou LABEL com a cláusula OBJECT <oReference>, onde <oReference> é uma instância de uma classe derivada de ReportListener com o valor da propriedade ListenerType definido como 0. Para obter mais informações, consulte a propriedade ListenerType.

Ao usar esses comandos, você também pode exibir ou suprimir a exibição da caixa de diálogo Print e da mensagem de status de impressão. Você pode definir muitas outras opções, como quais registros imprimir.

Para obter mais informações, consulte o comando REPORT FORM ou o comando LABEL.

# Enviando relatórios para a tela

Você pode enviar a saída de relatório ou etiqueta para a tela principal do Visual FoxPro ou para a janela atualmente ativa.

### Para enviar a saída de relatório ou etiqueta para a tela ou janela atualmente ativa
- Ao usar os comandos REPORT FORM e LABEL, omita todas as cláusulas que direcionam a saída para outro destino que não seja a tela ou a janela atualmente ativa.

> **Dica:** O mecanismo de renderização de relatórios GDI+ do Visual FoxPro 9 não ecoa o conteúdo do relatório ou etiqueta diretamente na janela de saída atual; portanto, certifique-se de que SET REPORTBEHAVIOR esteja definido como 80 quando desejar esse resultado. Como alternativa, você pode usar um objeto ReportListener para desenhar o conteúdo do relatório em um shape ou container em _SCREEN ou em qualquer formulário do Visual FoxPro. Creating a Custom Preview Container for an example performing this task with minimal code.

# Enviando relatórios para um arquivo

Enviar relatórios para um arquivo permite criar uma versão eletrônica do relatório e imprimi-los como um arquivo em lote na impressora posteriormente.

### Para enviar um relatório para um arquivo
- Use o comando REPORT FORM ou LABEL e inclua a cláusula TO FILE.

Para obter mais informações, consulte o comando REPORT FORM ou o comando LABEL.

# Salvando relatórios como HTML

Você pode salvar um relatório no formato Hypertext Markup Language (HTML).

> **Dica:** Você deve primeiro salvar o relatório e quaisquer alterações no disco antes de salvá-lo como HTML.

### Para salvar um relatório como HTML
- Abra o relatório ou etiqueta no designer apropriado.
- No menu File, clique em Save As HTML.
- Na caixa de diálogo Save As HTML, selecione as opções desejadas.
- Para salvar o arquivo HTML (.htm) com um nome diferente, clique no botão de reticências (...) para abrir a caixa de diálogo Save As e especificar um nome diferente. Quando terminar na caixa de diálogo Save As, clique em Save.
- Na caixa de diálogo Save As HTML, clique em OK.

Para obter mais informações, consulte a caixa de diálogo Save As HTML.

> **Dica:** Sem abrir o Report ou Label Designer, você também pode gerar HTML a partir do seu formulário de relatório usando o comando REPORT FORM <your filename> OBJECT TYPE 5. Este comando usa uma instância da Foundation Class ReportListener HTML para gerar seu arquivo HTML; a caixa de diálogo Save As HTML invoca o mesmo objeto para executar sua tarefa.
