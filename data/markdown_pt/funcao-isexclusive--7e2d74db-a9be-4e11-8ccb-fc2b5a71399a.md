# Função ISEXCLUSIVE( )

Retorna verdadeiro (.T.) se uma tabela ou banco de dados estiver aberto para uso exclusivo; caso contrário, retorna falso (.F.).

```foxpro
ISEXCLUSIVE([cTableAlias | nWorkArea | cDatabaseName [, nType]])
```

#### Parâmetros
 **cTableAlias**
Especifica o alias da tabela para a qual o status de uso exclusivo é retornado. O Visual FoxPro gera uma mensagem de erro se você especificar um alias de tabela que não existe.
**nWorkArea**
Especifica a área de trabalho da tabela para a qual o status de uso exclusivo é retornado. ISEXCLUSIVE( ) retorna falso (.F.) se uma tabela não estiver aberta na área de trabalho que você especificar.
**cDatabaseName**
Especifica o nome do banco de dados para o qual o status de uso exclusivo é retornado.
**nType**
Especifica se o status exclusivo é retornado para uma tabela ou um banco de dados. A tabela a seguir lista os valores de nType e o status correspondente retornado. nType Exclusive Status Returned 1 Table 2 Database Para determinar o status exclusivo de um banco de dados, você deve incluir nType com um valor de 2.

# Valor de retorno

Logical

# Observações

ISEXCLUSIVE( ) retorna um valor para a tabela aberta na área de trabalho atualmente selecionada se você omitir os argumentos opcionais cTableAlias, nWorkArea ou cDatabaseName.

Uma tabela é aberta para uso exclusivo incluindo a palavra-chave EXCLUSIVE em USE, ou definindo SET EXCLUSIVE como ON antes de a tabela ser aberta.

Um banco de dados é aberto para uso exclusivo incluindo a palavra-chave EXCLUSIVE em OPEN DATABASE.

# Exemplo

No exemplo a seguir, a função ISEXCLUSIVE( ) verifica se a tabela foi aberta para uso exclusivo. A tabela não é reindexada, pois a da área de trabalho atual não foi aberta para uso exclusivo.

```foxpro
cExclusive = SET('EXCLUSIVE')
SET EXCLUSIVE OFF
SET PATH TO (HOME(2) + 'data\')
OPEN DATA testdata  && Opens the test databsase
USE customer     && Not opened exclusively
USE employee IN 0 EXCLUSIVE    && Opened exclusively in another work area
IF ISEXCLUSIVE()
 REINDEX  && Can only be done if table opened exclusively
ELSE
  WAIT WINDOW 'The table has to be exclusively opened'
ENDIF
SET EXCLUSIVE &cExclusive
```
