# Função FLOCK( )

Tenta bloquear a tabela atual ou especificada.

```foxpro
FLOCK([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho da tabela que FLOCK( ) tenta bloquear. Omitir nWorkArea ou cTableAlias faz com que FLOCK( ) tente bloquear a tabela aberta na área de trabalho atualmente selecionada.
**cTableAlias**
Especifica o alias da tabela que FLOCK( ) tenta bloquear. Observe que o Visual FoxPro gera uma mensagem de erro se você especificar um alias de tabela que não existe.

# Valor de retorno

Valor lógico. FLOCK( ) retorna True (.T.) se a tabela for bloqueada com sucesso. Caso contrário, retorna False (.F.) nas seguintes condições:
 - A tabela ou um registro na tabela já está bloqueado por outro usuário.
- Não há uma tabela aberta na área de trabalho que você especificar.

> **Observação:** Se FLOCK() falhar ao bloquear uma tabela e retornar False (.F.), FLOCK() não gera um erro. Como resultado, você não pode usar FLOCK() para acionar uma rotina ON ERROR.

# Observações

Quando uma tabela é bloqueada, ela está disponível para acesso de leitura e gravação pelo usuário que colocou o bloqueio. Outros usuários na rede têm acesso somente leitura à tabela. Para obter informações sobre como bloquear uma tabela e impedir o acesso a ela por outros usuários, consulte Comando SET EXCLUSIVE e Comando USE.

Uma tabela permanece bloqueada até ser desbloqueada pelo usuário que colocou o bloqueio. A tabela pode ser desbloqueada emitindo UNLOCK, fechando a tabela ou encerrando o Visual FoxPro. Tabelas podem ser fechadas com USE, CLEAR ALL ou CLOSE DATABASES.

Por padrão, FLOCK( ) tenta bloquear uma tabela uma vez. Use SET REPROCESS para repetir automaticamente uma tentativa de bloqueio de tabela quando a primeira tentativa falhar. SET REPROCESS determina o número de tentativas de bloqueio ou o período durante o qual as tentativas de bloqueio são feitas quando a tentativa inicial de bloqueio não é bem-sucedida. Para obter mais informações, consulte Comando SET REPROCESS.

Você pode estabelecer relações entre duas ou mais tabelas com SET RELATION. Colocar um bloqueio de arquivo em uma tabela que está relacionada a uma ou mais tabelas não coloca um bloqueio de arquivo nas tabelas relacionadas. Você deve colocar e remover bloqueios explicitamente nas tabelas relacionadas.

Para informações adicionais sobre bloqueio de registros e arquivos e compartilhamento de tabelas em uma rede, consulte Programação para acesso compartilhado.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE products  && Opens products table
SET REPROCESS TO 3 SECONDS
SELECT * FROM products INTO TABLE newprods
IF FLOCK()
   *** New product initialization ***
   REPLACE ALL in_stock  WITH 0.00
   REPLACE ALL on_order WITH 0.00
   WAIT 'Initialization Complete' WINDOW NOWAIT
ELSE
   *** File is locked, warn user ***
   WAIT WINDOW 'Unable to open products file; try again later!' NOWAIT
ENDIF
BROWSE FIELDS in_stock, on_order && Displays newprods table
USE
ERASE newprods.dbf
```
