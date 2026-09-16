# Como: configurar saída para grupos de dados

Você pode controlar a forma como a saída de grupos de dados aparece em seu relatório ou etiqueta. As seções a seguir descrevem maneiras de configurar a saída para grupos de dados:
 - Specifying Page or Column Breaks for Data Groups
- Preventing Orphaned Group Headers
- Repeating Group Headers

# Especificar quebras de página ou coluna para grupos de dados

Você pode usar quebras de página ou coluna para especificar que os registros de cada grupo comecem em uma nova página ou coluna.

### Para especificar quebras de página ou coluna para um grupo de dados
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Data Grouping. A caixa de diálogo Report Properties abre. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Data Grouping é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Data Grouping Dialog Box.
- Na caixa de diálogo Report Properties, clique na guia Data Grouping se ela não estiver selecionada.
- Na lista Group nesting order, selecione a expressão de grupo de dados desejada.
- Na área Group starts on, selecione New page ou New column. Dica Para iniciar o grupo de dados em uma nova página e redefinir a numeração de página para 1, clique em New page number 1.

Para obter mais informações, consulte Data Grouping Tab, Report Properties Dialog Box (Report Builder).

# Evitar cabeçalhos de grupo órfãos

Às vezes, a saída de um grupo de dados pode aparecer parcialmente em uma página e depois terminar na próxima. Neste cenário, o cabeçalho do grupo pode aparecer perto da parte inferior da página com a maioria dos registros aparecendo na próxima.

Para evitar este cenário, defina a distância mínima que um cabeçalho de grupo será exibido da parte inferior da página. Se o cabeçalho do grupo aparecer mais próximo da parte inferior do que a distância que você especificar, o cabeçalho aparece em uma nova página.

### Para evitar cabeçalhos de grupo órfãos
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Data Grouping. A caixa de diálogo Report Properties abre. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Data Grouping é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Data Grouping Dialog Box.
- Na caixa de diálogo Report Properties, clique na guia Data Grouping se ela não estiver selecionada.
- Na lista Group nesting order, selecione a expressão de grupo de dados desejada.
- Na caixa Start group on a new page when less than, selecione ou digite a distância mínima desejada. Dica Um valor recomendado é de uma a três vezes a altura da banda Detail mais a altura do Group Header.

Para obter mais informações, consulte Data Grouping Tab, Report Properties Dialog Box (Report Builder).

# Repetir cabeçalhos de grupo

Quando registros de um grupo continuam na próxima página, você pode repetir o cabeçalho do grupo para esses registros.

> **Dica:** Você pode marcar várias bandas de grupo para repetir seu conteúdo quando um grupo continua em uma nova página. Se você deseja que controles em uma banda de cabeçalho de grupo repitam quando o grupo continua na próxima página, certifique-se de marcar a banda de cabeçalho de grupo que contém esses controles para repetir seu conteúdo. Marcar apenas uma banda de cabeçalho de grupo repete apenas os controles dessa banda.

### Para repetir o cabeçalho do grupo na próxima página
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Report, clique em Data Grouping. A caixa de diálogo Report Properties abre. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um builder de terceiros, a caixa de diálogo Data Grouping é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte _REPORTBUILDER System Variable e Data Grouping Dialog Box.
- Na caixa de diálogo Report Properties, clique na guia Data Grouping se ela não estiver selecionada.
- Na lista Group nesting order, selecione a expressão de grupo de dados desejada.
- Clique em Reprint group header on each page. Dica Desmarcar a caixa Reprint group header on each page impede que o cabeçalho do grupo se repita.

Para obter mais informações, consulte Data Grouping Tab, Report Properties Dialog Box (Report Builder).
