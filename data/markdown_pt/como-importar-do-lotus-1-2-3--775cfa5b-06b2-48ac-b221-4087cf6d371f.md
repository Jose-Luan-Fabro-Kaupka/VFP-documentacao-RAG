# Como: importar do Lotus 1-2-3

Ao importar dados de planilha, o Visual FoxPro usa a primeira linha da planilha Lotus 1-2-3 para determinar os tipos de dados dos campos na nova tabela. Se a primeira linha tiver cabeçalhos de texto literal para cada coluna, todos os campos da tabela serão campos de caractere, mesmo que as demais linhas contenham dados numéricos.

### Para garantir que os campos tenham o tipo de dados apropriado
- No Lotus 1-2-3, modifique a planilha para que a primeira linha contenha o primeiro registro de dados que você deseja na tabela. Cuidado Se sua planilha é da versão 2.x ou 3.x (extensão de arquivo .wk1 ou .wk3) e tem colunas com mais de oito ou nove caracteres, o Visual FoxPro trunca campos de caractere para nove caracteres em planilhas da versão 2.x e oito caracteres na versão 3.x. Para evitar campos truncados na tabela, você pode usar o Assistente de Importação ou criar uma tabela Visual FoxPro e, em seguida, acrescentar registros da planilha.

O Lotus armazena datas como o número não negativo de dias desde 1 de janeiro de 1900. Se a nova tabela não tiver o tipo de dados correto, você pode converter os campos de data do Lotus no Visual FoxPro.
