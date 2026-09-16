# Gerenciar atualizações usando transações

Mesmo com buffering, as coisas podem dar errado. Se você deseja proteger operações de atualização e recuperar de uma seção inteira de código como uma unidade, use transações.

Adicionar transações à sua aplicação fornece proteção além do buffering de registros e tabelas do Visual FoxPro, colocando uma seção inteira de código em uma unidade protegida e recuperável. Você pode aninhar transações e usá-las para proteger atualizações em buffer. As transações do Visual FoxPro estão disponíveis apenas com tabelas e views contidas em um banco de dados.

# Envolver segmentos de código

Uma transação atua como um wrapper que armazena em cache operações de atualização de dados na memória ou no disco, em vez de aplicar essas atualizações diretamente ao banco de dados. A atualização real do banco de dados é executada no final da transação. Se por qualquer motivo o sistema não conseguir executar as operações de atualização no banco de dados, você pode reverter toda a transação e nenhuma operação de atualização é executada.

> **Observação:** Operações de atualização em buffer feitas fora de uma transação são ignoradas dentro de uma transação na mesma sessão de dados.

# Comandos que controlam transações

O Visual FoxPro fornece três comandos e uma função para gerenciar uma transação.

| Para | Use |
| --- | --- |
| Iniciar uma transação. | BEGIN TRANSACTION |
| Determinar o nível de transação atual. | TXNLEVEL( ) |
| Reverter todas as alterações feitas desde a instrução BEGIN TRANSACTION mais recente. | ROLLBACK |
| Bloquear registros, confirmar no disco todas as alterações feitas nas tabelas no banco de dados desde o BEGIN TRANSACTION mais recente e então desbloquear os registros. | END TRANSACTION |

Você pode usar transações para envolver modificações em tabelas, arquivos estruturais .cdx e arquivos memo associados a tabelas dentro de um banco de dados. Operações envolvendo variáveis e outros objetos não respeitam transações; portanto, você não pode reverter ou confirmar essas operações.

> **Observação:** Ao usar dados armazenados em tabelas remotas, os comandos de transação controlam apenas atualizações nos dados na cópia local do cursor da view; atualizações nas tabelas base remotas não são afetadas. Para habilitar transações manuais em tabelas remotas, use SQLSETPROP( ) e então controle a transação com SQLCOMMIT( ) e SQLROLLBACK( ).

Em geral, você deve usar transações com buffers de registros em vez de com buffering de tabela, exceto para envolver chamadas TABLEUPDATE( ). Se você colocar um comando Função TABLEUPDATE( ) em uma transação, pode reverter uma atualização com falha, tratar o motivo da falha e então tentar novamente o TABLEUPDATE( ) sem perder dados. Isso garante que a atualização ocorra como uma operação "tudo ou nada".

Embora o processamento simples de transações forneça operações seguras de atualização de dados em situações normais, não fornece proteção total contra falhas do sistema. Se a energia falhar ou alguma outra interrupção do sistema ocorrer durante o processamento do Comando END TRANSACTION, a atualização de dados ainda pode falhar.

Use o seguinte modelo de código para transações:

```foxpro
BEGIN TRANSACTION
* Update records
IF lSuccess = .F. && an error occurs
   ROLLBACK
ELSE && commit the changes
   * Validate the data
   IF && error occurs
      ROLLBACK
   ELSE
      END TRANSACTION
   ENDIF
ENDIF
```

As seguintes regras se aplicam a transações:
 - Uma transação começa com o comando BEGIN TRANSACTION e termina com o comando END TRANSACTION ou ROLLBACK. Uma instrução END TRANSACTION sem uma instrução BEGIN TRANSACTION precedente gera um erro.
- Uma instrução ROLLBACK sem uma instrução BEGIN TRANSACTION precedente gera um erro.
- Uma transação, uma vez iniciada, permanece em vigor até que o END TRANSACTION correspondente comece (ou até que um comando ROLLBACK seja emitido), mesmo entre programas e funções, a menos que a aplicação termine, o que causa um rollback.
- O Visual FoxPro usa dados armazenados em cache no buffer de transação antes de usar dados do disco para consultas nos dados envolvidos em transações. Isso garante que os dados mais atuais sejam usados.
- Se a aplicação terminar durante uma transação, todas as operações são revertidas.
- Uma transação funciona apenas em um contêiner de banco de dados.
- Você não pode usar o comando INDEX se ele substituir um arquivo de índice existente, ou se qualquer arquivo de índice .cdx estiver aberto.
- As transações têm escopo de sessões de dados.

As transações exibem os seguintes comportamentos de bloqueio:
 - Dentro de uma transação, o Visual FoxPro impõe um bloqueio no momento em que um comando chama direta ou indiretamente por ele. Quaisquer comandos de desbloqueio diretos ou indiretos do sistema ou do usuário são armazenados em cache até a conclusão da transação pelos comandos ROLLBACK ou END TRANSACTION.
- Se você usar um comando de bloqueio como FLOCK( ) ou RLOCK( ) dentro de uma transação, a instrução END TRANSACTION não liberará o bloqueio. Nesse caso, você deve desbloquear explicitamente quaisquer bloqueios tomados explicitamente dentro de uma transação. Você também deve manter transações contendo os comandos FLOCK( ) ou RLOCK( ) o mais breves possível; caso contrário, os usuários podem ficar bloqueados fora dos registros por muito tempo.

# Aninhar transações

Transações aninhadas fornecem grupos lógicos de operações de atualização de tabela que são isolados de processos concorrentes. Pares BEGIN TRANSACTION...END TRANSACTION não precisam estar na mesma função ou procedimento. As seguintes regras se aplicam a transações aninhadas:
 - Você pode aninhar até cinco pares BEGIN TRANSACTION ... END TRANSACTION.
- Atualizações feitas em uma transação aninhada não são confirmadas até que o END TRANSACTION mais externo seja chamado.
- Em transações aninhadas, um END TRANSACTION opera apenas na transação iniciada pelo último BEGIN TRANSACTION emitido.
- Em transações aninhadas, uma instrução ROLLBACK opera apenas na transação iniciada pelo último BEGIN TRANSACTION emitido.
- A atualização mais interna em um conjunto de transações aninhadas nos mesmos dados tem precedência sobre todas as outras no mesmo bloco de transações aninhadas.

Observe no exemplo a seguir que, porque as alterações em uma transação aninhada não são gravadas no disco, mas no buffer de transação, a transação interna substituirá as alterações feitas nos mesmos campos STATUS na transação anterior:

```foxpro
BEGIN TRANSACTION &&  transaction 1
   UPDATE EMPLOYEE ; &&  first change
      SET STATUS = "Contract" ;
      WHERE EMPID BETWEEN 9001 AND 10000
   BEGIN TRANSACTION &&  transaction 2
      UPDATE EMPLOYEE ;
         SET STATUS = "Exempt" ;
         WHERE HIREDATE > {^1998-01-01}  &&  overwrites
   END TRANSACTION &&  transaction 2
END TRANSACTION    &&  transaction 1
```

O exemplo de transação aninhada a seguir exclui um registro de cliente e todas as suas faturas relacionadas. A transação será revertida se ocorrerem erros durante um Comando DELETE. Este exemplo demonstra agrupar operações de atualização de tabela para proteger atualizações de conclusão parcial e evitar conflitos de concorrência.
 Exemplo de modificação de registros em transações aninhadas
| Código | Comentários |
| --- | --- |
| DO WHILE TXNLEVEL( ) > 0 ROLLBACK ENDDO | Limpeza de outras transações. |
| CLOSE ALL SET MULTILOCKS ON SET EXCLUSIVE OFF | Estabelece ambiente para buffering. |
| OPEN DATABASE test USE mrgtest1 CURSORSETPROP('buffering',5) GO TOP | Habilita buffering otimista de tabela. |
| REPLACE fld1 WITH "changed" SKIP REPLACE fld1 WITH "another change" MESSAGEBOX("modify first field of both" + ; "records on another machine") | Altera um registro. Altera outro registro. |
| BEGIN TRANSACTION lSuccess = TABLEUPDATE(.T.,.F.) | Inicia transação 1 e tenta atualizar todos os registros modificados sem forçar. |
| IF lSuccess = .F. ROLLBACK AERROR(aErrors) DO CASE CASE aErrors[1,1] = 1539 ... CASE aErrors[1,1] = 1581 ... CASE aErrors[1,1] = 1582 | Se a atualização falhou, reverte a transação. Obtém o erro de AERROR( ). Determina a causa da falha. Se um trigger falhou, trata. Se um campo não aceita valores nulos, trata. Se uma regra de campo foi violada, trata. |
| CASE aErrors[1,1] = 1585 nNextModified = getnextmodified(0) DO WHILE nNextModified <> 0 GO nNextModified RLOCK() FOR nField = 1 to FCOUNT() cField = FIELD(nField) if OLDVAL(cField) <> CURVAL(cField) | Se um registro foi alterado por outro usuário, localiza o primeiro registro modificado. Percorre todos os registros modificados, começando pelo primeiro registro. Bloqueia cada registro para garantir que você possa atualizar. Verifica cada campo para alterações. Verifica o valor em buffer contra o valor no disco e então apresenta uma caixa de diálogo ao usuário. |
| nResult = MESSAGEBOX; ("Data was changed " + ; "by another user — keep"+ ; "changes?", 4+48, ; "Modified Record") | |
| IF nResult = 7 TABLEREVERT(.F.) UNLOCK record nNextModified ENDIF | Se o usuário respondeu "Não", reverte o registro e desbloqueia. |
| EXIT ENDIF ENDFOR | Sai do loop "FOR nField...". |
| ENDDO | Obtém o próximo registro modificado. |
| BEGIN TRANSACTION TABLEUPDATE(.T.,.T.) END TRANSACTION UNLOCK | Inicia transação 2 e atualiza todos os registros não revertidos com força. Encerra transação 2. Libera o bloqueio. |
| CASE aErrors[1,1] = 109 ... CASE aErrors[1,1] = 1583 ... CASE aErrors[1,1] = 1884 ... OTHERWISE MESSAGEBOX( "Unknown error "+; "message: " + STR(aErrors[1,1])) ENDCASE | Se o registro está em uso por outro usuário, trata. Se uma regra de linha foi violada, trata. Se houve violação de índice único, trata. Caso contrário, apresenta uma caixa de diálogo ao usuário. |
| ELSE END TRANSACTION ENDIF | Encerra transação 1. |

# Proteger atualizações remotas

As transações podem proteger você de erros gerados pelo sistema durante atualizações de dados em tabelas remotas. O exemplo a seguir usa uma transação para envolver operações de gravação de dados em uma tabela remota.
 Exemplo de transação em uma tabela remota
| Código | Comentário |
| --- | --- |
| hConnect = CURSORGETPROP('connecthandle') SQLSETPROP(hConnect, 'transmode', DB_TRANSMANUAL) | Obtém o identificador de conexão e habilita transações manuais. |
| BEGIN TRANSACTION | Inicia a transação manual. |
| lSuccess = TABLEUPDATE(.T.,.F.) IF lSuccess = .F. SQLROLLBACK (hConnect) ROLLBACK | Tenta atualizar todos os registros sem forçar. Se a atualização falhou, reverte a transação na conexão do cursor. |
| AERROR(aErrors) DO CASE | Obtém o erro de AERROR( ). |
| CASE aErrors[1,1] = 1539 ... | Se um trigger falhou, trata. |
| CASE aErrors[1,1] = 1581 ... | Se um campo não aceita valores nulos, trata. |
| CASE aErrors[1,1] = 1582 ... | Se uma regra de campo foi violada, trata. |
| CASE aErrors[1,1] = 1585 nNextModified = GETNEXTMODIFIED(0) DO WHILE nNextModified <> 0 GO nNextModified | Se um registro foi alterado por outro usuário, trata. Percorre todos os registros modificados, começando pelo primeiro registro. |
| FOR nField = 1 to FCOUNT() cField = FIELD(nField) IF OLDVAL(cField) <> CURVAL(cField) nResult = MESSAGEBOX; ("Data has been changed ; by another user. ; Keep changes?",4+48,; "Modified Record") | Verifica cada campo para alterações. Verifica o valor em buffer contra o valor no disco e então apresenta uma caixa de diálogo ao usuário. |
| IF nResult = 7 TABLEREVERT(.F.) ENDIF EXIT ENDIF ENDFOR nNextModified = ; GETNEXTMODIFIED(nNextModified) ENDDO | Se o usuário respondeu "Não", reverte o registro. Sai do loop "FOR nField...". Obtém o próximo registro modificado. |
| TABLEUPDATE(.T.,.T.) SQLCOMMIT(hConnect) | Atualiza todos os registros não revertidos com força e emite um commit. |
| CASE aErrors[1,1] = 109 * Handle the error | O erro 109 indica que o registro está em uso por outro usuário. |
| CASE aErrors[1,1] = 1583 * Handle the error | O erro 1583 indica que uma regra de linha foi violada. |
| CASE aErrors[1,1] = 1884 * Handle the error | O erro 1884 indica que a unicidade do índice foi violada. |
| OTHERWISE * Handle generic errors. | |
| MESSAGEBOX("Unknown error message:" ; + STR(aErrors[1,1])) ENDCASE | Apresenta uma caixa de diálogo ao usuário. Fim do tratamento de erros. |
| ELSE SQLCOMMIT(hConnect) END TRANSACTION ENDIF | Se todos os erros foram tratados e toda a transação foi bem-sucedida, emite um commit e encerra a transação. |
