# Função LOCK( )

Tenta bloquear um ou mais registros em uma tabela.

```foxpro
LOCK([nWorkArea | cTableAlias]|
 [cRecordNumberList, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea | cTableAlias**
Tenta um bloqueio no registro atual em uma tabela aberta em uma área de trabalho específica. nWorkArea especifica o número da área de trabalho e cTableAlias especifica o alias da tabela. Se você não especificar uma área de trabalho ou alias de tabela, LOCK( ) tenta bloquear o registro atual na tabela na área de trabalho atual.
**cRecordNumberList**
Especifica uma lista de um ou mais números de registro que você deve incluir para tentar bloquear múltiplos registros. SET MULTILOCKS deve estar ON e você deve incluir a área de trabalho ou alias da tabela para a qual está tentando colocar bloqueios de múltiplos registros. LOCK( ) tenta bloquear todos os registros que você especificar. Os números de registro especificados com cRecordNumberList são separados por vírgulas. Por exemplo, para tentar bloqueios de registro nos primeiros quatro registros em uma tabela, cRecordNumberList deve conter 1,2,3,4. Você também pode bloquear múltiplos registros movendo o ponteiro de registro para o registro que deseja bloquear, emitindo LOCK( ) ou RLOCK( ) e repetindo essas etapas para cada registro adicional. No Visual FoxPro, você pode especificar 0 como número de registro. Especificar 0 permite tentar bloquear o cabeçalho da tabela. Observação Mantenha o cabeçalho da tabela bloqueado pelo menor tempo possível porque outros usuários não podem adicionar registros à tabela quando o cabeçalho da tabela está bloqueado. Libere o bloqueio do cabeçalho da tabela com UNLOCK RECORD 0, UNLOCK ou UNLOCK ALL. Se todos os registros especificados em cRecordNumbers são bloqueados com sucesso, LOCK( ) retorna true (.T.). Se mesmo um dos registros especificados com cRecordNumbers não puder ser bloqueado, LOCK( ) retorna false (.F.) e nenhum dos registros é bloqueado. No entanto, quaisquer bloqueios de registro existentes permanecem em vigor. O bloqueio de múltiplos registros é um processo aditivo. Colocar bloqueios de registro adicionais não libera bloqueios em outros registros. O número máximo de registros que podem ser bloqueados em cada área de trabalho é de aproximadamente 8.000. É sempre mais rápido bloquear a tabela inteira do que mesmo um pequeno número de registros.

# Valor de retorno

Logical

# Observações

LOCK( ) é idêntico a RLOCK( ).

Alterações em registros bloqueados explicitamente não são salvas até que o registro seja desbloqueado ou o ponteiro de registro seja movido.

Se o bloqueio ou bloqueios são colocados com sucesso, LOCK( ) retorna true (.T.). Registros bloqueados estão disponíveis para acesso de leitura e gravação para o usuário que colocou os bloqueios; estão disponíveis para acesso somente leitura para todos os outros usuários na rede.

Executar LOCK( ) não garante que o bloqueio de registro ou bloqueios serão colocados com sucesso. Um bloqueio de registro não pode ser colocado em um registro já bloqueado por outro usuário ou em uma tabela bloqueada por outro usuário. Se o bloqueio de registro ou bloqueios não puderem ser colocados por qualquer motivo, LOCK( ) retorna false (.F.).

Por padrão, LOCK( ) faz uma tentativa de bloquear um registro. Use SET REPROCESS para tentar novamente automaticamente um bloqueio de registro quando a primeira tentativa falhar. SET REPROCESS determina o número de tentativas de bloqueio ou o período de tempo durante o qual as tentativas de bloqueio são feitas quando a tentativa inicial de bloqueio é malsucedida. Para obter mais informações, consulte SET REPROCESS Command.

SET MULTILOCKS determina se você pode bloquear múltiplos registros em uma tabela. Se SET MULTILOCKS estiver OFF (o padrão), você pode bloquear apenas um único registro em uma tabela. Quando SET MULTILOCKS está ON, você pode bloquear múltiplos registros em uma tabela. Para obter mais informações, consulte SET MULTILOCKS Command.

Desbloqueando registros Um registro de tabela pode ser desbloqueado apenas pelo usuário que colocou o bloqueio. Você pode liberar bloqueios de registro emitindo UNLOCK, fechando a tabela ou saindo do Visual FoxPro.

UNLOCK pode ser usado para liberar bloqueios de registro na área de trabalho atual, em uma área de trabalho específica ou em todas as áreas de trabalho. Para obter mais informações, consulte UNLOCK Command.

Alternar SET MULTILOCKS de ON para OFF ou de OFF para ON executa implicitamente UNLOCK ALL — todos os bloqueios de registro em todas as áreas de trabalho são liberados.

Tabelas podem ser fechadas com USE, CLEAR ALL ou CLOSE DATABASES.

Para obter mais informações sobre bloqueio de registros e arquivos e compartilhamento de tabelas em uma rede, consulte Programming for Shared Access.

# Exemplo

O exemplo a seguir bloqueia e desbloqueia os primeiros quatro registros nas tabelas `customer` e `employee`.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
SET REPROCESS TO 3 AUTOMATIC
STORE '1,2,3,4' TO gcRecList
gcOldExc = SET('EXCLUSIVE')
SET EXCLUSIVE OFF
SELECT 0
USE employee  && Open Employee table
SELECT 0
USE customer  && Open Customer table
? LOCK('1,2,3,4', 'customer')  && Lock 1st 4 records in customer
? RLOCK(gcRecList, 'employee')  && Lock 1st 4 records in employee
UNLOCK IN customer
UNLOCK IN employee
SET EXCLUSIVE &gcOldExc
```
