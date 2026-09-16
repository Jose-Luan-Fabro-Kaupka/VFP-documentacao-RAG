# Como: definir acesso a dados

Em um ambiente compartilhado, você pode acessar dados de duas maneiras: a partir de arquivos exclusivos ou de arquivos compartilhados. Se você abrir uma tabela para acesso compartilhado, outros usuários também terão acesso ao arquivo. Se você abrir uma tabela para acesso exclusivo, nenhum outro usuário poderá ler ou gravar nesse arquivo. Como o uso exclusivo anula muitos dos benefícios de compartilhar dados em uma rede, ele deve ser usado com moderação.

# Usando uma tabela com acesso exclusivo

A maneira mais restritiva de abrir um arquivo é abri-lo exclusivamente. Quando você abre uma tabela pela interface, ela abre para uso exclusivo por padrão. Você também pode abrir explicitamente uma tabela para uso exclusivo usando comandos do Visual FoxPro.

### Para abrir uma tabela para uso exclusivo
- Digite os seguintes comandos na janela Command: SET EXCLUSIVE ON USE cMyTable -ou-
- Digite o seguinte comando na janela Command: USE cMyTable EXCLUSIVE

Os seguintes comandos exigem que você abra uma tabela para uso exclusivo:
 - ALTER TABLE - SQL Command
- INDEX Command ao criar, adicionar ou excluir uma tag de índice composto.
- INSERT Command
- MODIFY STRUCTURE Command Para usar este comando para alterar a estrutura de uma tabela, você deve abrir a tabela exclusivamente. No entanto, você pode usar este comando em modo somente leitura quando abrir a tabela para uso compartilhado.
- PACK Command
- REINDEX Command
- ZAP Command

O Visual FoxPro retorna o erro "Exclusive open of file is required" se você tentar executar um desses comandos em uma tabela compartilhada.

Você pode restringir o acesso a uma tabela usando a função FLOCK( ). Se você usar FLOCK( ) para bloquear a tabela, outros usuários não podem gravar na tabela, mas podem lê-la.

# Usando uma tabela com acesso compartilhado

Quando você abre uma tabela para uso compartilhado, mais de uma estação de trabalho pode usar a mesma tabela ao mesmo tempo. Quando você abre uma tabela pela interface, pode substituir a configuração padrão ON do comando SET EXCLUSIVE. Você pode abrir explicitamente uma tabela para uso compartilhado usando comandos do Visual FoxPro.

### Para abrir uma tabela para uso compartilhado
- Digite os seguintes comandos na janela Command: SET EXCLUSIVE OFF USE cMyTable -ou-
- Digite o seguinte comando na janela Command: USE cMyTable SHARED

Quando você adiciona ou altera dados em uma tabela compartilhada, deve primeiro bloquear o registro afetado ou a tabela inteira. Você pode bloquear um registro ou uma tabela aberta para uso compartilhado das seguintes maneiras:
 - Use um comando que executa um bloqueio automático de registro ou tabela.
- Bloqueie manualmente um ou mais registros ou uma tabela inteira com as funções de bloqueio de registro e tabela.
- Inicie o buffer com a função CURSORSETPROP( ).

Arquivos memo e de índice associados sempre abrem com o mesmo status de compartilhamento de sua tabela.

Se seu aplicativo usa uma tabela apenas para consulta e todos os usuários do aplicativo a acessam, você pode melhorar o desempenho marcando a tabela como somente leitura.
