# Atualizando dados usando transações

Depois de terminar offline, você pode atualizar os dados no servidor usando as mesmas transações de atualização de tabela que normalmente usa com dados online. Ao trabalhar com dados remotos, lembre-se das seguintes dicas:
 - Para atualizações de registro único, use transações automáticas.
- Para atualizações em lote, use transações manuais.
- Conforme necessário, inclua código para detectar conflitos de atualização, criar um log de conflitos e resolver conflitos.

Antes de processar suas atualizações, você precisa usar o comando USE Command e a palavra-chave ONLINE para reconectar ao banco de dados host. Depois de emitir o comando, o Visual FoxPro tenta localizar o banco de dados host usando as informações da fonte de dados armazenadas na exibição. Depois que a conexão é estabelecida, você pode usar a Função TABLEUPDATE( ) para processar as atualizações armazenadas nos dados offline.

Para garantir que as informações de conexão estejam corretas independentemente da localização das tabelas host ou de exibição, você precisa usar a sintaxe de cadeia de conexão em vez de uma conexão nomeada.

# Atualizando lotes de registros em tabelas locais

Para processar um lote de alterações em tabelas locais, você pode usar transações manuais que permitem processar todo o lote de alterações em uma única transação em vez de uma série de transações separadas.
 Atualizando tabelas locais com exibições offline
| Código | Comentários |
| --- | --- |
| USE myofflineview ONLINE EXCLUSIVE | Reconecta ao host e abre a exibição. |
| BEGIN TRANSACTION IF TABLEUPDATE (2, .F., "myofflineview") END TRANSACTION ELSE MESSAGEBOX("Error Occurred: Update unsuccessful.") ROLLBACK ENDIF | Verifica conflitos de atualização e atualiza conforme apropriado. |

# Atualizando lotes de registros em tabelas remotas

Para processar um lote de alterações em tabelas remotas, use transações manuais: comece com a Função TABLEUPDATE( ) e termine o processamento com a Função SQLCOMMIT( ) ou a Função SQLROLLBACK( ).

Para definir a conexão para gerenciar suas transações manualmente, você precisa usar a Função CURSORGETPROP( ) no cursor da exibição para obter o identificador de conexão e depois definir a propriedade Transactions para o modo manual.

No código a seguir, a identificação da conexão atual para a exibição, `myview`, é armazenada em `hConn1`. `hConn1` é usado para definir a propriedade Transactions como "2" para transações manuais.

```foxpro
hConn1 = CURSORGETPROP("CONNECTHANDLE","myview") ;
SQLSETPROP(hConn1,"TRANSACTIONS",2)
```

Depois de definir a conexão para manipular as atualizações, você pode usar a Função TABLEUPDATE( ) para manipular suas transações.

Se as tabelas host residem em um servidor remoto, como o SQL Server, você pode usar o código a seguir como diretriz.
 Atualizando tabelas remotas com exibições offline
| Código | Comentário |
| --- | --- |
| USE myofflineview ONLINE EXCLUSIVE | Reconecta ao host e abre a exibição. |
| SQLSetProp(liviewhandle,"transactions",2) SQLSetProp(custviewhandle,"transactions",2) SQLSetProp(ordviewhandle,"transactions",2) | Definindo as conexões nas exibições para manipular transações manualmente. |
| IF NOT TABLEUPDATE(.T.,.F.,"lineitemsview") =SQLROLLBACK(ordviewhandle) =MESSAGEBOX("Can't update line items table") IF NOT TableUpdate(.T.,.F.,"ordersview") =SQLROLLBACK(liviewhandle) =MESSAGEBOX("unable to update the orders table") IF NOT TABLEUPDATE(.T.,.F.,"customerview") =SQLROLLBACK(custviewhandle) =MESSAGEBOX("Can't update customer table") Else *# check out failure scenarios IF NOT SQLCOMMIT(liviewhandle) =SQLROLLBACK(liviewhandle) IF NOT SQLCOMMIT(ordviewhandle) =SQLROLLBACK(ordviewhandle) IF NOT SQLCOMMIT(custviewhandle) =SQLROLLBACK(custviewhandle) ENDIF ENDIF ENDIF ENDIF ENDIF ENDIF | Manipulando atualizações e conflitos de atualização. |

# Atualizando um registro

Se você está atualizando uma única linha, pode usar transações automáticas. Como cada instrução para processar uma atualização, exclusão ou inserção é tratada como uma transação separada, rollbacks contra instruções de transação anteriores não são possíveis.

```foxpro
USE customerview ONLINE EXCLUSIVE
GO TO 3
   IF TABLEUPDATE (0, .F. workarea)
      * conflict handling code
   ENDIF
```

> **Dica:** Para atualizar um único registro em uma tabela local, use a função GETNEXTMODIFIED( ).

# Cancelando atualizações offline

Se você decidir que deseja excluir os dados offline e converter a exibição de volta para uma exibição online, pode usar a Função DROPOFFLINE( ).

Para cancelar atualizações offline, use DROPOFFLINE( ) com o nome da exibição.

Certifique-se de verificar os valores de retorno. True (.T.) indica sucesso e false (.F.) indica que a exibição não foi fechada antes do comando ser emitido.

O código a seguir descarta todas as alterações feitas no subconjunto de dados em `myview`. A exibição permanece parte do banco de dados, mas seu conjunto atual de dados é descartado:

```foxpro
DROPOFFLINE("myview")
```

Você pode excluir registros offline, mas não pode usar os comandos PACK Command, ZAP Command ou INSERT Command com uma exibição offline.
