# Função GETNEXTMODIFIED( )

Retorna o número do registro do próximo registro modificado em uma tabela ou cursor em buffer.

```foxpro
GETNEXTMODIFIED(nRecordNumber [, cTableAlias | nWorkArea] [, lNoFire])
```

#### Parâmetros
 **nRecordNumber**
Especifica o número do registro após o qual GETNEXTMODIFIED( ) pesquisa o próximo registro modificado. Especifique 0 para nRecordNumber para determinar o primeiro registro na tabela ou cursor que foi modificado.
**cTableAlias**
Especifica o alias da tabela ou cursor para o qual GETNEXTMODIFIED( ) retorna o número do próximo registro modificado.
**nWorkArea**
Especifica a área de trabalho da tabela ou cursor para o qual GETNEXTMODIFIED( ) retorna o número do próximo registro modificado. Se você não especificar um alias ou área de trabalho, GETNEXTMODIFIED( ) retorna o número do registro do próximo registro modificado na tabela ou cursor atualmente selecionada.
**lNoFire**
Especifica que toda a execução de regras é suprimida.

# Valor de retorno

Numeric

# Observações

GETNEXTMODIFIED( ) retorna 0 se não houver registros modificados após o registro que você especificar. Por isso, se você modificar apenas um registro, para verificar sua modificação deve primeiro usar o comando GO TOP para posicionar o cursor antes do registro alterado. Um registro é considerado modificado se o conteúdo de qualquer um de seus campos for alterado de qualquer forma (mesmo se o conteúdo original do campo for restaurado) ou se o status de exclusão do registro for alterado.

GETNEXTMODIFIED( ) pode operar apenas em tabelas e cursores para os quais o buffer de tabela está habilitado. O buffer de tabela é habilitado com CURSORSETPROP( ).

Como os triggers não são afetados por GETNEXTMODIFIED( ), lNoFire suprime apenas regras de campo e registro e o erro "Uniqueness of index ID is violated". lNoFire impede o flush de dados temporários, como dados armazenados em controles ou atualizações feitas no registro atual, para o cursor subjacente.

# Exemplo

O exemplo de código a seguir usa a função GETNEXTMODIFIED( ) para examinar alterações em registros de uma tabela em buffer. Normalmente, as alterações são feitas por interação do usuário com um formulário. Para os fins deste exemplo, os dados são atualizados usando o comando SQL UPDATE. Como preparação para demonstrar o método GetNextModified, o código de exemplo abre uma tabela no banco de dados de exemplo, define buffer de linha otimista e atualiza a tabela.

A função GetNextModified( ) é chamada com 0 como parâmetro para obter o número do registro do primeiro registro atualizado no buffer. Um loop processa os registros atualizados com base no valor de MaxOrdAmt. As alterações são descartadas se o valor de MaxOrdAmt for maior que 8500. GetNextModified( ) é chamada novamente, desta vez com o número do registro atual, para obter o próximo registro modificado no buffer. Se GetNextModified( ) retornar 0, não há mais registros modificados para processar e o loop termina. TableRevert(.t.) é chamado para descartar todas as alterações e restaurar os dados de exemplo ao estado original.

```foxpro
LOCAL lnCurRec
CLEAR
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE Customer
* Enable table buffering.
SET MULTILOCKS ON
=CURSORSETPROP("Buffering", 5, "customer")
* Increase MAXORDAMT by 10% for customers in Mexico.
UPDATE Customer SET MaxOrdAmt=MaxOrdAmt * 1.1 WHERE Country = "Mexico"
* Start with the first modified record.
lnCurRec = GETNEXTMODIFIED(0)
* DO until all modified records are processed.
DO WHILE .T.
   * Move to the current modified record.
   GOTO (m.lnCurRec)
   * Process modified row here.
   ? Customer.Company, Customer.MaxOrdAmt
   IF Customer.MaxOrdAmt > 8500
      =TABLEREVERT(.F.)
   ENDIF
   ?? Customer.MaxOrdAmt
   * Get the next modified record from here.
   lnCurRec = GETNEXTMODIFIED(m.lnCurRec)
   IF m.lnCurRec = 0 && No more modified records.
      EXIT
   ENDIF
ENDDO
=TABLEREVERT(.T.)  && Restore sample data and discard all changes.
```
