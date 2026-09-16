# O comando não pode ser emitido dentro de uma transação (Erro 1593)

Você deve encerrar todas as transações abertas com o comando END TRANSACTION ou o comando ROLLBACK antes de emitir este comando. O Visual FoxPro não permite que nada que modifique um banco de dados (.dbc) faça parte de uma transação. Os seguintes comandos são ilegais dentro de uma transação:
 - CLEAR ALL
- CLOSE ALL
- CLOSE DATABASE
- CLOSE TABLES
- COPY INDEXES
- CREATE / DELETE / MODIFY DATABASE
- CREATE / DELETE / MODIFY VIEW
- CREATE / DELETE TRIGGER
- CREATE / DELETE / MODIFY CONNECTION
- APPEND / MODIFY / COPY PROCEDURES

Os seguintes comandos não são legais para tabelas que participam de transações:
 - ALTER TABLE
- CREATE TABLE (de uma tabela em um contêiner de banco de dados)
- DELETE TAG
- INDEX ON
- INSERT (non-SQL)
- MODIFY STRUCTURE
- PACK
- TABLEREVERT( )
- Desativar o buffer de tabela (alterando a propriedade Buffering de 3 ou 5 para 1, 2 ou 4 com a função CURSORETPROP( )).
- Fechar uma tabela (emitindo o comando USE na área de trabalho de uma tabela que participa de transação)
- ZAP
