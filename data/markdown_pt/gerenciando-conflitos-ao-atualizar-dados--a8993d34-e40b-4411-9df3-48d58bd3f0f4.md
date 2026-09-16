# Gerenciando conflitos ao atualizar dados

Seja qual for sua escolha entre buffering, transactions ou views, você deve gerenciar conflitos durante o processo de atualização. Gerenciar conflitos encontrados em ambientes multiusuário pode exigir código extenso e repetitivo. Uma rotina completa de gerenciamento de conflitos executa o seguinte:
 - Detecta um conflito.
- Identifica a natureza e a localização do conflito.
- Fornece informações suficientes para que o usuário possa resolver o conflito de forma inteligente.

Para um exemplo de rotina de gerenciamento de conflitos, consulte a classe data checker em Samples.vcx, localizada no diretório Visual FoxPro ...\Samples\Classes. Basta adicionar a classe a um formulário e chamar o método CheckConflicts antes de qualquer operação que grave dados em buffer na tabela, por exemplo mover o ponteiro de registro se você estiver usando row buffering, fechar uma tabela ou emitir TABLEUPDATE( ).

# Gerenciando conflitos de buffering

Você pode tornar as operações de atualização de dados mais eficientes escolhendo cuidadosamente como e quando abrir, fazer buffering e bloquear dados em um ambiente multiusuário. Você deve limitar o tempo em que um registro ou tabela está sujeito a conflitos de acesso. Ainda assim, você deve antecipar e gerenciar os conflitos inevitáveis que resultam. Um conflito ocorre quando um usuário tenta bloquear um registro ou tabela que está atualmente bloqueado por outro usuário. Dois usuários não podem bloquear o mesmo registro ou tabela ao mesmo tempo.

Seu aplicativo deve conter uma rotina para gerenciar esses conflitos. Se seu aplicativo não tiver uma rotina de conflito, o sistema pode travar. Um deadlock ocorre quando um usuário bloqueou um registro ou uma tabela e tenta bloquear outro registro que está bloqueado por um segundo usuário que, por sua vez, está tentando bloquear o registro bloqueado pelo primeiro usuário. Embora tais ocorrências sejam raras, quanto mais tempo um registro ou tabela permanecer bloqueado, maior a chance de deadlock.

### Capturando erros

Projetar um aplicativo multiusuário ou adicionar suporte de rede a um sistema de usuário único exige que você lide com colisões e capture erros. Usar buffers de registro e tabela do Visual FoxPro simplifica parte desse trabalho.

Se você tentar bloquear um registro ou tabela já bloqueado por outro usuário, o Visual FoxPro retorna uma mensagem de erro. Você pode usar o comando SET REPROCESS para lidar automaticamente com tentativas de bloqueio malsucedidas. Este comando, em combinação com uma rotina ON ERROR Command e o comando RETRY Command, permite que você continue ou cancele as tentativas de bloqueio.

O exemplo a seguir demonstra o reprocessamento automático de uma operação malsucedida, usando SET REPROCESS.
 Usando SET REPROCESS e ON ERROR para gerenciar colisões de usuário
| Código | Comentário |
| --- | --- |
| ON ERROR DO err_fix WITH ERROR(),MESSAGE() SET EXCLUSIVE OFF SET REPROCESS TO AUTOMATIC USE customer IF !FILE('cus_copy.dbf') COPY TO cus_copy ENDIF | Esta rotina é executada se ocorrer um erro. Abre os arquivos de forma não exclusiva. O reprocessamento de bloqueios malsucedidos é automático. Abre a tabela. Cria a tabela APPEND FROM se necessário. |
| DO app_blank DO rep_next DO rep_all DO rep_curr DO add_recs | A rotina principal começa aqui. Estes comandos são exemplos de códigos que poderiam ser executados no curso do seu programa. |
| ON ERROR | A rotina principal termina aqui. |
| PROCEDURE app_blank APPEND BLANK RETURN ENDPROC | Rotina para anexar um registro em branco. |
| PROCEDURE rep_next REPLACE NEXT 1 contact WITH ; PROPER(contact) RETURN ENDPROC | Rotina para substituir dados no registro atual. |
| PROCEDURE rep_all REPLACE ALL contact WITH ; PROPER(contact) GO TOP RETURN ENDPROC | Rotina para substituir dados em todos os registros. |
| PROCEDURE rep_curr REPLACE contact WITH PROPER(contact) RETURN ENDPROC | Rotina para substituir dados no registro atual. |
| PROCEDURE add_recs APPEND FROM cus_copy RETURN ENDPROC | Rotina para anexar registros de outro arquivo. |

O exemplo a seguir demonstra um procedimento de erro que inicia quando o usuário pressiona ESC.
 Tratamento de erros usando a tecla ESC
| Código | Comentário |
| --- | --- |
| PROCEDURE err_fix PARAMETERS errnum, msg | Este programa é chamado quando um erro é encontrado e o usuário escapa do processo de espera. |
| DO CASE | Descubra que tipo de erro é este. É "File is in use by another"? |
| CASE errnum = 108 line1 = "File cannot be locked." line2 = "Try again later..." | |
| CASE errnum = 109 .OR. errnum = 130 line1 = "Record cannot be locked." line2 = "Try again later." | Ou "Record is in use by another"? |
| OTHERWISE line1 = msg + " " line2 = ; "See your system administrator." ENDCASE | Ou é desconhecido? |
| =MESSAGEBOX( line1 + line2, 48, "Error!" ) RETURN | Exibe a mensagem de erro em uma caixa de diálogo com um ponto de exclamação e um botão OK. |
