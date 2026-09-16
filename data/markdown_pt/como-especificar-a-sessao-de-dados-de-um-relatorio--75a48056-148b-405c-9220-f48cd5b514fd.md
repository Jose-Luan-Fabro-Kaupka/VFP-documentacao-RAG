# Como: especificar a sessão de dados de um relatório

Você pode especificar que a sessão de dados do relatório seja privada para evitar que alterações na sessão de dados global afetem a sessão de dados do seu relatório. Outros designers ou código de aplicação podem afetar a sessão de dados global, e essas alterações afetariam os dados disponíveis para o seu relatório. Por exemplo, código externo poderia `SET DELETED ON` quando seu relatório esperava que a configuração fosse `OFF`, ou poderia fechar tabelas que seu relatório esperava que estivessem abertas.

### Para definir uma sessão de dados privada
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Private Data Session.

Você também pode definir a sessão de dados como privada para o relatório ou etiqueta clicando em Properties no menu Report. Quando a caixa de diálogo Report Properties abrir, clique na guia Data Environment se ela não estiver selecionada.

> **Observação:** Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Report Page Setup é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Report Page Setup Dialog Box.

Para obter mais informações, consulte Data Environment Tab, Report Properties Dialog Box (Report Builder).
