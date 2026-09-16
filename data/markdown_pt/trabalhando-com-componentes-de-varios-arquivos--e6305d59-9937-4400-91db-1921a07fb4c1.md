# Trabalhando com componentes de vários arquivos

Alguns componentes de projeto no Visual FoxPro consistem, na verdade, em vários arquivos: um arquivo primário e um ou mais arquivos implícitos. Por exemplo, quando você cria um formulário, o Visual FoxPro cria um arquivo .scx (o arquivo primário) e um arquivo .sct (o arquivo implícito). Os componentes a seguir têm vários arquivos:

| Componente | Tipo de arquivo primário | Tipo(s) de arquivo implícito |
| --- | --- | --- |
| Form | .scx | .sct |
| Report | .frx | .frt |
| Label | .lbx | .lbt |
| Class Library | .vcx | .vct |
| Menu | .mnx | .mnt |
| Table | .dbf | .fpt, .cdx, .idx |
| Database | .dbc | .dct, .dcx |

Quando um desenvolvedor faz check-out de um arquivo de componente, como um formulário, o Visual FoxPro também gerencia o arquivo ou arquivos implícitos correspondentes. Da mesma forma, quando um arquivo é devolvido (check-in) ou um novo arquivo é adicionado, o Visual FoxPro gerencia o arquivo ou arquivos implícitos automaticamente.

> **Observação:** Se você gerar e compilar um menu, também cria arquivos locais .mpr e .mpx. Eles não estão inicialmente sob controle de origem, mas você pode adicioná-los como arquivos ao seu projeto e colocá-los sob controle de origem como faria com outros arquivos.

# Fazendo check-in de arquivos de texto

Quando você faz check-in de um arquivo de texto como um arquivo .prg e, se várias versões do arquivo estiverem com check-out, o software de controle de origem não simplesmente sobrescreve a versão central. Em vez disso, ele verifica se houve alterações no arquivo desde o último check-out. Se houver, tenta mesclar essas alterações com seu arquivo. Para isso, adiciona, exclui e altera linhas em sua cópia do arquivo.

Quando termina a mesclagem, o software de controle de origem também pode dar a oportunidade de fazer check-in do seu arquivo. Não faça check-in do arquivo imediatamente. Em vez disso, teste seu aplicativo usando a nova versão do arquivo que incorpora tanto suas alterações quanto as de outros desenvolvedores. Somente quando estiver satisfeito de que o aplicativo funciona corretamente, faça check-in do arquivo. Se outros desenvolvedores fizeram alterações adicionais no mesmo arquivo, pode ser necessário mesclar, testar e fazer check-in novamente.

Em alguns casos, o software de controle de origem pode relatar um conflito de mesclagem, o que indica que não consegue resolver alterações entre suas alterações e as de outros desenvolvedores. Isso pode ocorrer, por exemplo, se você e outro desenvolvedor estiverem atualizando as mesmas linhas do mesmo programa. Se o software de controle de origem não conseguir mesclar com sucesso, cria uma versão do arquivo que contém o texto original mais suas alterações, marca os conflitos e grava esse arquivo em seu computador. (A forma exata como os conflitos são marcados depende do software de controle de origem que você está usando.) O arquivo então aparece no Project Manager com um ícone de conflito de mesclagem:

Para resolver o conflito de mesclagem, você deve editar o arquivo novamente, fazer suas alterações e remover os marcadores de conflito de mesclagem. Quando terminar a edição, o Visual FoxPro solicita que você confirme que resolveu todos os conflitos. O arquivo é então marcado com o ícone de mesclagem:

Teste seu aplicativo para ter certeza de que as alterações estão funcionando corretamente. Você pode então tentar fazer check-in do arquivo novamente. Se não ocorrerem mais conflitos de mesclagem, seu arquivo se torna a versão atual.
