# Comando ROLLBACK

Cancela quaisquer alterações feitas durante a transação atual.

```foxpro
ROLLBACK
```

# Observações

ROLLBACK restaura as tabelas originais, arquivos memo de tabela e arquivos de índice ao estado em que estavam antes do início da transação.

Quando você modifica registros em um banco de dados que faz parte de uma transação, outros usuários na rede não têm acesso (leitura ou gravação) aos registros até que você encerre a transação.

Quando outros usuários na rede tentam acessar registros que você modificou, eles devem aguardar até que você encerre sua transação. Eles recebem a mensagem "Record not available ... please wait" até que os registros se tornem disponíveis. Por isso, é importante manter a duração da transação no mínimo ou conduzir a transação em horários em que outras pessoas não precisem de acesso.

ROLLBACK desfaz quaisquer alterações feitas durante a transação atual. Se a transação estiver aninhada, somente as modificações feitas desde o BEGIN TRANSACTION anterior são desfeitas. A execução do programa continua com a próxima instrução.

Se algum bloqueio de registro ou arquivo foi colocado, ele é liberado.

# Exemplo

No exemplo a seguir, a tabela customer no banco de dados testdata é aberta. O buffer de tabela otimista é definido para a tabela customer. O conteúdo dos campos `cust_id` e `company` é exibido e, em seguida, o conteúdo do campo `company` é substituído nos dados em buffer.

BEGIN TRANSACTION é emitido para iniciar uma transação. Um TABLEUPDATE é usado para gravar as alterações na tabela. O novo conteúdo é exibido e ROLLBACK é emitido para restaurar o conteúdo original do campo `company`. Os campos `cust_id` e `company` são exibidos novamente com o campo `company` contendo seus valores originais.

```foxpro
CLOSE DATABASES
CLEAR
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
