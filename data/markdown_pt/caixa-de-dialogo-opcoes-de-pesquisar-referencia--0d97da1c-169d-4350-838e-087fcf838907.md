# Caixa de diálogo Opções de Pesquisar Referência

Define opções adicionais para uma pesquisa de referências de código.

A caixa de diálogo Opções aparece quando você clica no botão Opções da caixa de diálogo Pesquisar Referência ou da janela Referências de Código. É possível obter descrições de cada opção clicando no texto da opção.
 **Criar tabela de definições de símbolos durante a pesquisa**
Especifica a coleta de definições de símbolos de código dos arquivos processados durante uma pesquisa de referências. Caso contrário, as definições são coletadas sob demanda ao exibir definições de código. Essa opção executa uma verificação completa de definições durante uma pesquisa de referências e economiza tempo ao exibir definições de código. Para obter mais informações, consulte Como: exibir definições de código.
**Limitar a coleta de definições ao diretório base do projeto e seus subdiretórios**
Especifica que uma coleção de definições de símbolos de código de um projeto inclua somente os arquivos que estejam na árvore do diretório base do projeto. Isso impede a inclusão de definições de estruturas e outros arquivos que não sejam imediatamente relevantes para o projeto atual.
**Pesquisar somente código-fonte e expressões**
Especifica que a pesquisa seja realizada somente em código-fonte e expressões. Caso contrário, valores como nomes de campos em tabelas, valores de etiquetas em relatórios, legendas e outros textos são incluídos na pesquisa.
**Pesquisar nomes e valores de propriedades de formulários/classes**
Especifica que nomes e valores de propriedades de formulários visuais (.scx) e classes visuais (.vcx) sejam incluídos em uma pesquisa de referências.
**Exibir o número de referências encontradas por linha nos resultados da pesquisa**
Especifica que um indicador seja exibido na janela de referências ao lado dos resultados que tenham mais de uma correspondência por linha.
**Mostrar histórico dos tipos de arquivo pesquisados**
Especifica que um histórico dos tipos de arquivo selecionados recentemente seja exibido na janela Pesquisar Referência. Caso contrário, somente os tipos de arquivo comuns e o tipo selecionado mais recentemente são exibidos.
**Mostrar colunas separadas para classe, método e linha**
Especifica que classe, método e linha sejam exibidos em colunas separadas, em vez de serem concatenados em uma única coluna na grade de resultados. Se forem exibidos em colunas separadas, você poderá classificar os métodos clicando com o botão direito do mouse na coluna Métodos e escolhendo Classificar por Método.
**Estilo de backup**
Especifica como os arquivos são nomeados ao fazer backup durante a substituição global de referências de código.
**Fonte**
Exibe a caixa de diálogo Fonte, que pode ser usada para alterar a fonte da janela Referências de Código.
**Pasta para tabelas de referências de código**
Especifica e contém o local das tabelas principais de referências de código. Para selecionar outra pasta, clique no botão de reticências (...) para exibir a caixa de diálogo Selecionar Diretório.
**Limpar tabelas de origem**
Limpa as tabelas de referências do Visual FoxPro procurando registros antigos e desatualizados. Especificamente, essa opção executa as seguintes ações: remove todos os registros Inactive e Error do arquivo RefFile.dbf, exceto quando UniqueID="WINDOW", que sempre permanece; remove do arquivo RefFile.dbf todos os registros que fazem referência a arquivos inexistentes no disco e quaisquer registros correspondentes no arquivo RefDef.dbf; remove todos os registros Inactive do arquivo RefDef.dbf; executa uma operação PACK nos arquivos RefFile.dbf e RefDef.dbf.
