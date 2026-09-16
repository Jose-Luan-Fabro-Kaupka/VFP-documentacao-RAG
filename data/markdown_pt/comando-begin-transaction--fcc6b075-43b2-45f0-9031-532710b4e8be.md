# Comando BEGIN TRANSACTION

Inicia uma transação. Transações são suportadas apenas para tabelas em um banco de dados. Consulte Comando CREATE DATABASE e Comando ADD TABLE para obter informações sobre como criar e adicionar tabelas a um banco de dados.

```foxpro
BEGIN TRANSACTION
```

# Observações

Para salvar quaisquer modificações feitas e encerrar a transação, emita END TRANSACTION. Se a transação falhar (o servidor falha, a estação de trabalho falha ou você sai do Visual FoxPro sem confirmar a transação) ou se você emitir ROLLBACK, o arquivo ou arquivos na transação são restaurados ao estado original.

Transações podem ser aninhadas até cinco níveis de profundidade. Um erro é gerado se você tentar um sexto nível de aninhamento.

Quando você modifica registros em uma tabela que faz parte de uma transação, outros usuários na rede não têm acesso (leitura ou gravação) aos registros até você encerrar a transação.

Quando outros usuários na rede tentam acessar registros que você modificou, eles devem aguardar até você encerrar sua transação. Eles recebem a mensagem "Record not available ... please wait" até que os registros estejam disponíveis. Por isso, é importante manter a duração da transação ao mínimo ou conduzir a transação em horários em que outros não precisam de acesso.

Todos os arquivos de índice IDX (índices não estruturais, ou não baseados em CDX) devem ser fechados durante transações. Apenas índices estruturais são suportados dentro de transações.

Os seguintes comandos e funções não são suportados durante uma transação:

| Comandos e funções | |
| --- | --- |
| ADD TABLE | DELETE CONNECTION |
| APPEND PROCEDURES | DELETE DATABASE |
| CLEAR ALL | DELETE TRIGGER |
| CLOSE ALL1 | DELETE VIEW |
| CLOSE DATABASES1 | MODIFY CONNECTION |
| COPY INDEXES | MODIFY DATABASE |
| COPY PROCEDURES | MODIFY PROCEDURE |
| CREATE CONNECTION | MODIFY VIEW |
| CREATE DATABASE | REMOVE TABLE |
| CREATE TRIGGER | RENAME TABLE |
| CREATE VIEW | REQUERY( ) |
| CREATE SQL VIEW | |

1 Se CLOSE ALL é emitido enquanto uma transação está em andamento, todas as tabelas em todos os bancos de dados abertos são fechadas. No entanto, os bancos de dados permanecem abertos. Emitir CLOSE DATABASES dentro de uma transação fecha todas as tabelas no banco de dados atual, mas o banco de dados permanece aberto.

Além disso, os seguintes comandos e funções não podem ser emitidos para uma tabela específica participando de uma transação:

| Comandos e funções | |
| --- | --- |
| ALTER TABLE | MODIFY STRUCTURE |
| CREATE TABLE | PACK |
| CURSORSETPROP( ) | REINDEX |
| DELETE TAG | TABLEREVERT( ) |
| INDEX | ZAP |
| INSERT | |

# Exemplo

No exemplo a seguir, a tabela customer no banco de dados testdata é aberta. O buffer de tabela otimista é definido para a tabela customer. O conteúdo dos campos `cust_id` e `company` é exibido, e então o conteúdo do campo `company` é substituído nos dados em buffer.

BEGIN TRANSACTION é emitido para iniciar uma transação. A função TABLEUPDATE( ) é usada para gravar as alterações na tabela. O novo conteúdo é exibido, e ROLLBACK é emitido para restaurar o conteúdo original do campo `company`. Os campos `cust_id` e `company` são exibidos novamente com o campo `company` contendo seus valores originais.

```foxpro
CLEAR
CLOSE DATABASES
* Transactions are only supported within a DBC
OPEN DATABASE (HOME(2) + 'Data\testdata')
SET MULTILOCKS ON      && Required for buffering
USE customer
=CURSORSETPROP("Buffering",5)
? 'The original company field'
LIST FIELDS cust_id, company NEXT 5
REPLACE ALL company WITH "***" && Change field contents
BEGIN TRANSACTION
   =TABLEUPDATE(.T.)
   GO TOP
   ? 'The modified company field'
   LIST FIELDS cust_id, company NEXT 5
   ROLLBACK           && Restore original field contents
=TABLEREVERT(.T.)
GO TOP
? 'The restored company field'
LIST FIELDS cust_id, company NEXT 5
```
