# Função TABLEREVERT( )

Descarta alterações feitas em uma linha, tabela ou cursor com buffer e restaura os dados OLDVAL( ) para cursores remotos e os valores atuais do disco para tabelas e cursores locais.

> **Observação:** Em uma rede, os dados atualmente no disco podem diferir dos dados existentes quando a tabela foi aberta ou o cursor foi criado. Outros usuários da rede podem ter alterado os dados depois disso.

```foxpro
TABLEREVERT( [lAllRows [, cTableAlias | nWorkArea] ] )
```

#### Parâmetros
 **lAllRows**
Determina se todas as alterações feitas na tabela ou no cursor são descartadas. A tabela a seguir descreve os valores de lAllRows. lAllRows Descrição False (.F.) Se o buffer de tabela estiver habilitado, somente as alterações feitas no registro atual da tabela ou do cursor serão descartadas. (Padrão) True (.T.) Se o buffer de tabela estiver habilitado, as alterações em todos os registros serão descartadas. Se o buffer de linha estiver habilitado, o Visual FoxPro ignorará lAllRows e descartará as alterações do registro atual.
**cTableAlias**
Especifica o alias da tabela ou cursor em que as alterações são descartadas.
**nWorkArea**
Especifica a área de trabalho da tabela ou cursor em que as alterações são descartadas.

# Valor de retorno

Tipo de dados Numeric. TABLEREVERT( ) retorna o número de registros cujas alterações foram descartadas.

# Observações

TABLEREVERT( ) não pode descartar alterações em uma tabela ou cursor sem buffer de linha ou de tabela habilitado. Se você emitir TABLEREVERT( ) sem que o buffer esteja habilitado, o Visual FoxPro gerará uma mensagem de erro. Use CURSORSETPROP( ) para habilitar ou desabilitar o buffer de linha e de tabela.

As alterações são descartadas na tabela ou cursor aberto na área de trabalho selecionada no momento se TABLEREVERT( ) for emitida sem os argumentos opcionais cTableAlias ou nWorkArea.

TABLEREVERT( ) não retorna o ponteiro de registro à sua posição original.

TABLEREVERT( ) opera em objetos CursorAdapter da mesma forma que em outros cursores com buffer.

No Visual FoxPro 9.0, não é possível emitir TABLEREVERT( ) durante uma operação TABLEUPDATE( ).

# Exemplo

O exemplo a seguir demonstra como usar TABLEREVERT( ) para descartar alterações em uma tabela com buffer. MULTILOCKS é definido como ON, requisito para o buffer de tabela. A tabela `customer` do banco de dados `testdata` é aberta e CURSORSETPROP( ) define o modo de buffer como buffer de tabela otimista (5).

O valor do campo `cust_id` é exibido e depois modificado com REPLACE. O novo valor é exibido. TABLEREVERT( ) retorna a tabela ao estado original (TABLEUPDATE( ) poderia ser emitida para confirmar as alterações). O valor revertido do campo `cust_id` é então exibido.

```foxpro
CLOSE DATABASES
SET MULTILOCKS ON  && Must be on for table buffering
SET PATH TO (HOME(2) + 'data\')     && Sets path to database
OPEN DATABASE testdata  && Open testdata database
USE Customer     && Open customer table
= CURSORSETPROP('Buffering', 5, 'customer')  && Enable table buffering
CLEAR
? 'Original cust_id value: '
?? cust_id  && Displays current cust_id value
REPLACE cust_id    WITH '***'  && Changes field contents
? 'New cust_id value: '
?? cust_id  && Displays new cust_id value
= TABLEREVERT(.T.)  && Discard all table changes
? 'Reverted cust_id value: '
?? cust_id  && Displays reverted cust_id value
```
