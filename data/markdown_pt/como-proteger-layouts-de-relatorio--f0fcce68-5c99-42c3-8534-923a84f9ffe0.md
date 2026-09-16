# Como: proteger layouts de relatório

Você pode proteger um layout de relatório ou etiqueta contra modificações indesejadas por usuários finais definindo restrições de edição com sinalizadores de proteção de relatório e permitindo que seus usuários editem layouts de relatório por meio do comando MODIFY REPORT … PROTECTED.

### Para definir proteção para relatórios
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Properties, ou clique com o botão direito no layout e selecione Properties no menu de contexto. A caixa de diálogo Report Properties é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão, a caixa de diálogo Report Page Setup é aberta em vez disso. Se _REPORTBUILDER estiver definida para um builder de terceiros, uma caixa de diálogo diferente pode ser exibida. Não há como definir sinalizadores de proteção usando as caixas de diálogo nativas de relatório. Para obter mais informações, consulte _REPORTBUILDER System Variable e Report Page Setup Dialog Box.
- Na caixa de diálogo Report Properties, clique na guia Protection.
- Na guia Protection, selecione uma combinação das seguintes opções de proteção: O usuário não poderá executar o relatório a partir do designer nem usar a opção Print… no menu File. O usuário não poderá visualizar o relatório a partir do designer. O usuário não poderá modificar o Data Environment do relatório. O usuário não poderá acessar a caixa de diálogo de layout de página. O usuário não poderá configurar as bandas opcionais do layout (em outras palavras, elas não serão opcionais para o usuário). O usuário não poderá acessar a caixa de diálogo de agrupamento de dados. O usuário não poderá alterar as configurações das variáveis de relatório.
- Quando terminar, clique em OK.

Para obter mais informações, consulte Protection Tab, Report Properties Dialog Box (Report Builder) e Report Properties Dialog Box (Report Builder).
