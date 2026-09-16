# Como: importar do Microsoft Excel

Ao importar dados de planilha, o Visual FoxPro usa a primeira linha da planilha do Microsoft Excel para determinar os tipos de dados dos campos na nova tabela. Se a primeira linha tiver cabeçalhos de texto literal para cada coluna, todos os campos na tabela serão campos de caractere, mesmo que as demais linhas contenham dados numéricos.

### Para garantir que os campos tenham o tipo de dados apropriado
- No Microsoft Excel, modifique a planilha para que a primeira linha contenha o primeiro registro de dados que você deseja na tabela. Cuidado Se um campo na planilha do Microsoft Excel tiver comprimento de 255, esse campo é truncado para 254 quando importado para uma tabela do Visual FoxPro.
