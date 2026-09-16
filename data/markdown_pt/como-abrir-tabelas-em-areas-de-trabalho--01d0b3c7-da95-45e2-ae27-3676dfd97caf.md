# Como: abrir tabelas em áreas de trabalho

Você pode abrir tabelas em áreas de trabalho dentro de sessões de dados. Também pode referenciar ou ir para a próxima área disponível antes de abrir uma tabela. Para obter mais informações, consulte Áreas de trabalho em sessões de dados e Como: usar sessões de dados.

> **Observação:** Mais de uma tabela não pode permanecer aberta na mesma área de trabalho. Ao abrir outra tabela nessa área, a tabela aberta no momento é fechada automaticamente.

### Para abrir uma tabela em uma área de trabalho
- Abra na sessão de dados as tabelas com as quais deseja trabalhar.
- No menu Janela, escolha Sessão de Dados.
- Na lista Alias, clique no alias da tabela e depois em Abrir.

### Para abrir uma tabela em várias áreas de trabalho
- Na lista Alias da janela Sessão de Dados, clique no alias da mesma tabela e depois em Abrir. O Visual FoxPro atribui outro alias à tabela.

### Para abrir uma tabela em uma área de trabalho por meio de programação
- Use o comando USE com o nome da tabela e o número da área de trabalho. Dica: para abrir a mesma tabela em outra área, repita USE com o mesmo nome e inclua a palavra-chave AGAIN.

Para obter mais informações, consulte Comando USE.

Quando você abre uma tabela pelo menu Arquivo, ela também é aberta em uma área de trabalho.

### Para referenciar a próxima área de trabalho
- Use o comando SELECT e inclua o número da área de trabalho ou o alias da tabela.

Para obter mais informações, consulte Comando SELECT.
