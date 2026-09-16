# Importação de dados

Se você deseja importar do arquivo de origem, pode deixar o Visual FoxPro definir a estrutura da nova tabela ou usar o Assistente de Importação para especificar sua estrutura. O Visual FoxPro usa a ordem dos campos no arquivo de origem para definir a estrutura da tabela de destino. Se você deseja definir a estrutura, pode modificar o arquivo no aplicativo de origem ou usar o Assistente de Importação.

Se você não tem mais acesso ao aplicativo que suporta o arquivo de origem e deseja alterar a ordem ou o tipo de dados dos campos, pode importar o arquivo de origem e depois criar uma consulta que envie os campos na ordem desejada para outra nova tabela.

Ao importar um arquivo, você deve escolher o tipo de arquivo a importar e especificar os nomes do arquivo de origem e da tabela de destino.

# Escolhendo um tipo de arquivo para importar

A tabela a seguir lista os tipos de arquivo que você pode importar para o Visual FoxPro:

| Tipo de arquivo | Extensão de arquivo | Descrição |
| --- | --- | --- |
| Microsoft Excel | xls | Formato de planilha do Microsoft Excel (versões 2.0, 3.0, 4.0, 5.0 e 97). As células da coluna tornam-se campos e as linhas tornam-se registros. |
| Lotus 1-2-3 | wks wk1 wk3 | Planilha Lotus 1-2-3 para as versões 1-A, 2.x e 3.x. As células da coluna tornam-se campos e as linhas tornam-se registros. |
| Borland Paradox | db | Tabela Paradox para as versões 3.5 e 4.0. |

Se você deseja usar tabelas de uma versão anterior do FoxPro ou arquivos dBASE, pode abri-los e usá-los sem importar. O Visual FoxPro perguntará se você deseja converter a tabela para a versão mais recente do Visual FoxPro. Depois de converter uma tabela de uma versão anterior, essa tabela não poderá ser aberta na versão anterior.

Para obter mais informações sobre a importação de arquivos, consulte o comando IMPORT Command.
