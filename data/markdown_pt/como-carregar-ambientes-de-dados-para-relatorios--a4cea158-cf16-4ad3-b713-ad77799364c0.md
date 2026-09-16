# Como: carregar ambientes de dados para relatórios

Você pode carregar um ambiente de dados para seu relatório ou etiqueta a partir de outro arquivo de relatório (.frx) ou etiqueta (.lbx), ou a partir de uma definição de classe visual DataEnvironment.

Você carrega o ambiente de dados na guia Data Environment da caixa de diálogo Report Properties.

> **Importante:** A capacidade de carregar um Data Environment é um recurso fornecido pelo aplicativo ReportBuilder. Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Report Properties é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Report Page Setup Dialog Box .

### Para carregar um ambiente de dados de outro relatório
- Abra o relatório ou etiqueta ao qual deseja adicionar o ambiente de dados no Report ou Label Designer.
- No menu Report, clique em Load Data Environment . Como alternativa, escolha Properties no menu e clique na guia Data Environment da caixa de diálogo Report Properties.
- Selecione o botão de opção Copy from another report file .
- Clique no botão Select. A caixa de diálogo Open Dialog Box (Visual FoxPro) aparece. Escolha o arquivo de relatório (.frx) ou etiqueta (.lbx) do qual deseja copiar o Data Environment e clique em OK .
- Uma mensagem aparece em uma caixa de diálogo informando que você está prestes a substituir o conteúdo atual do seu Data Environment para este relatório. Se estiver pronto para fazer isso, confirme clicando em Yes ; caso contrário, clique em No para cancelar.
- O ReportBuilder confirma que atualizou o Data Environment do relatório ou etiqueta, com uma segunda caixa de diálogo.
- Abra o Data Environment do relatório e verifique se as tabelas e views do Data Environment do relatório ou etiqueta original agora estão carregadas neste. Qualquer código do Data Environment original deve ser repetido nos métodos apropriados do Data Environment.

### Para carregar um ambiente de dados de uma definição de classe baseada em DataEnvironment
- Abra o relatório ou etiqueta e navegue até a guia Load Data Environment da caixa de diálogo Report Properties, conforme acima.
- Selecione o botão de opção Link to a DataEnvironment class .
- Clique no botão Select e escolha uma biblioteca de classes (vcx) ou arquivo de programa (prg) apropriado e uma classe baseada em DataEnvironment na lista.
- Como acima, confirme que deseja substituir suas informações existentes do Data Environment. O ReportBuilder fornecerá uma mensagem de erro se a classe escolhida não descender de DataEnvironment , ou confirmará que atualizou com sucesso o Data Environment no relatório ou etiqueta atual.
- Abra o Data Environment do relatório e verifique se as tabelas e views da classe visual agora estão carregadas no Data Environment deste relatório ou etiqueta. Você encontrará código, escrito pelo ReportBuilder, vinculando os eventos e métodos da classe visual incluídos nos snippets de código do Data Environment do relatório ou etiqueta. Você pode editar este código, se necessário.
