# Como: visualizar estrutura do banco de dados

Embora o Database Designer exiba uma representação visual e conceitual do banco de dados, você pode querer examinar a estrutura do arquivo de banco de dados (.dbc), que é uma tabela. O arquivo de banco de dados contém um registro para cada tabela, view, índice, tag de índice, relacionamento persistente e conexão associados ao banco de dados, bem como um registro para cada campo de tabela ou campo de view que tenha propriedades estendidas. Também inclui um único registro que contém todos os procedimentos armazenados do banco de dados. Para obter mais informações, consulte Estrutura de arquivo de tabela (.dbc, .dbf, .frx, .lbx, .mnx, .pjx, .scx, .vcx).

Você pode examinar o conteúdo de um arquivo de banco de dados navegando pelo arquivo.

### Para navegar em um arquivo de banco de dados
- Feche o banco de dados.
- Use o comando USE com o nome do arquivo de banco de dados, incluindo a extensão de nome de arquivo .dbc, e a palavra-chave EXCLUSIVE.
- Na linha seguinte, siga o comando USE com o comando BROWSE. Cuidado Não use BROWSE para modificar o conteúdo do arquivo de banco de dados, a menos que você entenda a estrutura do arquivo de banco de dados. Se ocorrer um erro ao tentar alterar o arquivo de banco de dados, o banco de dados pode se tornar inválido e potencialmente perder dados. Em vez disso, use MODIFY STRUCTURE para adicionar campos. Para obter mais informações, consulte Como: estender arquivos de banco de dados .

Por exemplo, o código a seguir abre uma janela de navegação e exibe o conteúdo de um banco de dados chamado MyDatabase como uma tabela:

```foxpro
CLOSE MyDatabase
USE MyDatabase.dbc EXCLUSIVE
BROWSE
```
