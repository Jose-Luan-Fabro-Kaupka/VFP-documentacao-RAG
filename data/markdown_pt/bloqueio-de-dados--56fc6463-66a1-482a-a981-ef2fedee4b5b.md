# Bloqueio de dados

Se você compartilha o acesso a arquivos, também deve gerenciar o acesso aos dados bloqueando tabelas e registros. Bloqueios, diferentemente de permissões de acesso, podem fornecer controle de dados de longo e curto prazo. O Visual FoxPro fornece bloqueio automático e manual.

# Escolhendo bloqueios de registro ou de tabela

O bloqueio de registro, seja automático ou manual, impede que um usuário grave em um registro que está sendo gravado por outro usuário. O bloqueio de tabela impede que outros usuários gravem, mas não leiam, em uma tabela inteira. Como o bloqueio de tabela proíbe que outros usuários atualizem registros em uma tabela, deve ser usado com moderação.

# Escolhendo bloqueios automáticos ou manuais

Além do bloqueio de registro ou de tabela, você também pode escolher bloqueio automático ou manual. Muitos comandos do Visual FoxPro tentam automaticamente bloquear um registro ou uma tabela antes que o comando seja executado. Se o registro ou a tabela é bloqueado com sucesso, o comando é executado e o bloqueio é liberado.
 Comandos que bloqueiam registros e tabelas automaticamente
| Comando | Escopo do bloqueio |
| --- | --- |
| ALTER TABLE | Tabela inteira |
| APPEND | Cabeçalho da tabela |
| APPEND BLANK | Cabeçalho da tabela |
| APPEND FROM | Cabeçalho da tabela |
| APPEND FROM ARRAY | Cabeçalho da tabela |
| APPEND MEMO | Registro atual |
| BLANK | Registro atual |
| BROWSE , CHANGE and EDIT | Registro atual e todos os registros de campos com alias em tabelas relacionadas assim que a edição de um campo começa |
| CURSORSETPROP( ) | Depende dos parâmetros |
| DELETE | Registro atual |
| DELETE NEXT 1 | Registro atual |
| DELETE RECORD n | Registro n |
| DELETE de mais de um registro | Tabela inteira |
| DELETE – SQL | Registro atual |
| GATHER | Registro atual |
| INSERT | Tabela inteira |
| INSERT - SQL | Cabeçalho da tabela |
| MODIFY MEMO | Registro atual quando a edição começa |
| READ | Registro atual e todos os registros de campos com alias |
| RECALL | Registro atual |
| RECALL NEXT 1 | Registro atual |
| RECALL RECORD n | Registro n |
| RECALL de mais de um registro | Tabela inteira |
| REPLACE | Registro atual e todos os registros de campos com alias |
| REPLACE NEXT 1 | Registro atual e todos os registros de campos com alias |
| REPLACE RECORD n | Registro n e todos os registros de campos com alias |
| REPLACE de mais de um registro | Tabela inteira e todos os arquivos de campos com alias |
| SHOW GETS | Registro atual e todos os registros referenciados por campos com alias |
| TABLEUPDATE( ) | Depende do buffering |
| UPDATE | Tabela inteira |
| UPDATE – SQL | Tabela inteira |

# Características do bloqueio de registro

Comandos que tentam bloqueios de registro são menos restritivos que comandos que bloqueiam tabelas. Quando você bloqueia um registro, outros usuários ainda podem adicionar ou excluir outros registros. Se um registro ou tabela já está bloqueado por outro usuário, uma tentativa de bloqueio de registro ou tabela falha. Comandos que tentam bloquear o registro atual retornam o erro, "Record is in use by another," se o registro não puder ser bloqueado.

Os comandos BROWSE Command, CHANGE Command, EDIT Command e MODIFY MEMO Command não bloqueiam um registro até que você edite o registro. Se você está editando campos de registros em tabelas relacionadas, os registros relacionados são bloqueados se possível. A tentativa de bloqueio falha se o registro atual ou qualquer um dos registros relacionados também estiver bloqueado por outro usuário. Se a tentativa de bloqueio for bem-sucedida, você pode editar o registro; o bloqueio é liberado quando você move para outro registro ou ativa outra janela.

# Características do bloqueio de cabeçalho e de tabela

Alguns comandos do Visual FoxPro bloqueiam uma tabela inteira, enquanto outros bloqueiam apenas o cabeçalho da tabela. Comandos que bloqueiam a tabela inteira são mais intrusivos que comandos que bloqueiam apenas o cabeçalho da tabela. Quando você bloqueia o cabeçalho da tabela, outros usuários não podem adicionar registros, mas ainda podem alterar dados em campos.

Os usuários podem compartilhar a tabela sem causar conflito quando você emite o comando APPEND Command, mas um erro pode ocorrer enquanto outro usuário também está adicionando um registro BLANK à tabela. Você pode capturar o erro, "File is in use by another," que é retornado quando dois ou mais usuários executam APPEND BLANK simultaneamente. Comandos que bloqueiam uma tabela inteira retornam o erro, "File is in use by another," se a tabela não puder ser bloqueada. Para cancelar a tentativa de bloqueio, pressione ESC.

# Bloqueio automático

No exemplo a seguir, o usuário bloqueia automaticamente o cabeçalho da tabela ao adicionar registros de outra tabela, mesmo que `customer` tenha sido aberto como arquivo compartilhado:

```foxpro
SET EXCLUSIVE OFF
USE customer
APPEND FROM oldcust FOR status = "OPEN"
```

# Bloqueio manual

Você pode bloquear manualmente um registro ou uma tabela usando uma das seguintes funções de bloqueio:
 - RLOCK( ) Function
- LOCK( ) Function
- FLOCK( ) Function

As funções LOCK( ) e RLOCK( ) podem ser aplicadas a um cabeçalho de tabela. Se você fornecer 0 como o registro para LOCK( ) ou RLOCK( ) e o teste indicar que o cabeçalho está desbloqueado, a função bloqueia o cabeçalho e retorna true (.T.).

Depois de bloquear um registro ou tabela, certifique-se de liberar o bloqueio usando o comando UNLOCK Command o mais rápido possível para fornecer acesso a outros usuários.

Essas funções de bloqueio manual executam as seguintes ações:
 - Testam o status de bloqueio do registro ou tabela.
- Se o teste indicar que o registro está desbloqueado, bloqueiam o registro ou tabela e retornam true (.T.).
- Se o registro ou tabela não puder ser bloqueado, tentam bloquear o registro ou tabela novamente, dependendo da configuração atual de SET REPROCESS .
- Retornam true (.T.) ou false (.F.), indicando se a tentativa de bloqueio foi bem-sucedida. Dica Se você deseja testar o status de bloqueio de um registro em sua sessão sem bloquear o registro, use a função ISRLOCKED( ) ou ISFLOCKED( ).

Se uma tentativa de bloquear um registro ou tabela falhar, o comando SET REPROCESS e sua rotina de erro atual determinam se o bloqueio é tentado novamente. SET REPROCESS afeta o resultado de uma tentativa de bloqueio malsucedida. Você pode controlar o número de tentativas de bloqueio ou a duração de uma tentativa de bloqueio com SET REPROCESS.

O exemplo a seguir abre a tabela `customer` para acesso compartilhado e usa FLOCK( ) para tentar bloquear a tabela. Se a tabela é bloqueada com sucesso, REPLACE ALL atualiza cada registro na tabela. UNLOCK libera o bloqueio do arquivo. Se o arquivo não puder ser bloqueado porque outro usuário bloqueou o arquivo ou um registro no arquivo, uma mensagem é exibida.

```foxpro
SET EXCLUSIVE OFF
SET REPROCESS TO 0
USE customer    && Open table shared
IF FLOCK()
 REPLACE ALL contact ;    && Replace and unlock
  WITH UPPER(contact)
 UNLOCK
ELSE  && Output message
 WAIT "File in use by another." WINDOW NOWAIT
ENDIF
```

# Desbloqueio de dados

Depois de estabelecer um bloqueio de registro ou arquivo e completar uma operação de dados em um ambiente compartilhado, você deve liberar o bloqueio o mais rápido possível. Existem várias formas de liberar bloqueios. Em alguns casos, simplesmente mover para o próximo registro é suficiente para desbloquear os dados. Outras situações exigem comandos explícitos.

Para desbloquear um registro que foi bloqueado automaticamente, você precisa apenas mover o ponteiro de registro, mesmo se você definiu MULTILOCKS ON. Você deve remover explicitamente um bloqueio de um registro que bloqueou manualmente; simplesmente mover o ponteiro de registro não é suficiente.

A tabela a seguir descreve os efeitos dos comandos em bloqueios manuais e automáticos de registro e tabela.

| Comando | Efeito |
| --- | --- |
| UNLOCK | Libera bloqueios de registro e arquivo na área de trabalho atual. |
| UNLOCK ALL | Libera todos os bloqueios em todas as áreas de trabalho na sessão atual. |
| SET MULTILOCKS OFF | Habilita a liberação automática do bloqueio atual quando um novo bloqueio é obtido. |
| FLOCK( ) | Libera todos os bloqueios de registro no arquivo afetado antes de bloquear o arquivo. |
| CLEAR ALL , CLOSE ALL , USE , QUIT | Libera todos os bloqueios de registro e arquivo. |
| END TRANSACTION | Libera bloqueios automáticos. |
| TABLEUPDATE( ) | Libera todos os bloqueios após atualizar a tabela. |

> **Cuidado:** Se um registro foi bloqueado automaticamente em uma função definida pelo usuário e você move o ponteiro de registro para fora e depois de volta ao registro, o bloqueio será liberado. Use table buffering para evitar este problema.
