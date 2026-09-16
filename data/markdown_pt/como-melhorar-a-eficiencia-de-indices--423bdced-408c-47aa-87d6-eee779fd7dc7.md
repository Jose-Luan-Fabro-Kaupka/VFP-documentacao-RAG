# Como: melhorar a eficiência de índices

Você pode melhorar o desempenho de tabelas indexadas mantendo os índices atualizados e usando expressões que podem ser otimizadas em seus índices. Você pode reconstruir arquivos de índice ativos ou reindexar tabelas em tempo de execução.

# Reconstruindo arquivos de índice ativos

Quando você abre uma tabela sem abrir seus arquivos de índice correspondentes e faz alterações nos campos-chave da tabela, os arquivos de índice ficam desatualizados. Os arquivos de índice também podem se tornar inválidos quando ocorre uma falha do sistema ou potencialmente ao acessar e atualizar uma tabela de um programa diferente do Visual FoxPro. Quando os arquivos de índice ficam desatualizados, você pode atualizá-los reindexando com o comando REINDEX.

### Para reconstruir um arquivo de índice ativo
- Abra a tabela que deseja reindexar.
- No menu Table, escolha Rebuild Indexes.

### Para reconstruir arquivos de índice ativos programaticamente
- Use o comando REINDEX para reconstruir um índice. REINDEX atualiza todos os arquivos de índice abertos na área de trabalho selecionada. O Visual FoxPro reconhece e reindexa cada tipo de arquivo de índice adequadamente. Por exemplo, o código a seguir atualiza o arquivo de índice da tabela Customer no banco de dados de exemplo do Visual FoxPro, TestData: OPEN DATABASE (HOME(2) + 'Data\TestData') USE Customer REINDEX

Para obter mais informações, consulte REINDEX Command.

> **Observação:** Reindexar tabelas em tempo de execução pode levar tempo, particularmente quando você está reindexando tabelas grandes. Você deve reindexar tabelas apenas quando necessário. Você pode melhorar o desempenho reindexando durante a porção de inicialização ou encerramento do seu programa, em vez de realizar manutenção de indexação durante a porção principal de um aplicativo.
