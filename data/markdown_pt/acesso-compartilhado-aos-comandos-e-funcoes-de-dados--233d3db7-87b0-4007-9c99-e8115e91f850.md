# Acesso compartilhado aos comandos e funções de dados

Esses comandos e funções permitem que vários usuários em uma rede compartilhem dados de tabelas.

Usar , para
| --- | --- |
□ CURSORSETPROP( ) Função □ Especificar as configurações de propriedade para uma tabela Visual FoxPro ou um cursor.
□ CURVAL( ) Função □ Retornar os valores do campo diretamente do disco para uma tabela ou uma fonte de dados remota.
□ FLOCK( ) Função □ Tentativa de bloquear a tabela atual ou especificada.
LOCK( ) Função ou RLOCK( ) Função □ Tentar bloquear um ou mais registros em uma tabela.
| OLDVAL( ) Function | Return original field values for fields that have been modified but not updated. |
O comando SET EXCLUSIVE Abrir arquivos de tabela para uso exclusivo ou compartilhado em uma rede. □
Comando SET LOCK Activar ou desactivar o bloqueio automático de ficheiros em determinados comandos. □
□ SET MULTILOCKS Comando □ Determinar se você pode bloquear vários registros usando LOCK( ) ou RLOCK( ). □
Comando SET REFRESH Para atualizar uma janela de navegação ou janela de edição de memorandos, ou para atualizar buffers de memória local com alterações de outros usuários na rede. □
□ SET REPROCESS Comando □ Especificar quantas vezes e por quanto tempo Visual FoxPro tenta bloquear um ficheiro ou registo após uma tentativa de bloqueio mal sucedida.
□ SYS(3051) - Definir Intervalo de Repetição de Bloqueio □ Especifique o tempo em milissegundos que Visual FoxPro espera antes de tentar bloquear um ficheiro de registo, tabela, memorando ou índice após uma tentativa de bloqueio mal sucedida.
| SYS(3052) - Override SET REPROCESS Locking | Specify whether Visual FoxPro uses the SET REPROCESS setting when attempting to lock an index or memo file. |
| TABLEREVERT( ) Function | Discard changes made to a buffered row or a buffered table or cursor and restores the OLDVAL( ) data for remote cursors and the current disk values for local tables and cursors. |
| TABLEUPDATE( ) Function | Commit changes made to a buffered row, a buffered table, cursor, or cursor adapter. |
| UNLOCK Command | Release a record lock, multiple record locks, or a file lock from a table or all open tables. |

Veja também
- Acesso compartilhado aos dados
- Categorias de idiomas
