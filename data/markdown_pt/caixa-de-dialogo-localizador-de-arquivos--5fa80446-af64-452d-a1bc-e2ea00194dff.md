# Caixa de diálogo Localizador de arquivos

Permite pesquisas baseadas em critérios especificados.
 **Localizar agora**
Executa uma pesquisa de arquivos baseada nas opções que você especifica nas guias do Filer.
**Editar**
Abre os arquivos selecionados na lista Resultados da pesquisa para edição.
**Nova pesquisa**
Limpa as opções especificadas nas guias Pesquisa de texto, Data de modificação e Atributos de arquivo.
**Resultado da pesquisa**
Exibe os arquivos localizados pela pesquisa. Clique duas vezes em um arquivo na lista Resultado da pesquisa para abrir o arquivo para edição. Para abrir vários arquivos para edição, selecione os arquivos e clique no botão Editar.

As opções do Filer são agrupadas nas seguintes guias.

| Guia | Para acessar esses recursos |
| --- | --- |
| Nome e localização | Especifique os nomes, extensões e localizações dos arquivos que você pesquisa. |
| Pesquisa de texto | Especifique cadeias de caracteres de texto a pesquisar. |
| Data de modificação | Especifique as datas de criação, modificação ou acesso dos arquivos que você pesquisa. |
| Atributos de arquivo | Especifique o tamanho e os atributos de arquivo dos arquivos que você pesquisa. |

# Guia Nome e localização
 **Nomeado**
Especifica os arquivos que você deseja pesquisar. Especifique um nome e extensão de arquivo ou qualquer parte de um nome e extensão de arquivo que inclua caracteres curinga. Separe várias especificações de arquivo com ponto e vírgula. Por exemplo, para exibir todos os arquivos .prg e .app, use *.prg;*.app. Clique na seta para baixo para exibir uma lista de extensões de arquivo do Visual FoxPro comumente usadas.
**Procurar em**
Especifica a pasta em que a pesquisa ocorre. Clique na seta para baixo para exibir uma lista de pastas que você especificou durante a sessão atual do Filer.
**Procurar**
Exibe a caixa de diálogo Selecionar diretório, permitindo que você selecione a pasta em que a pesquisa ocorre.
**Incluir subpastas**
Se marcada, especifica que as subpastas também são pesquisadas. Observe que o Filer ignora pastas do sistema.

# Guia Pesquisa de texto
 **Expressão 1**
Uma cadeia de caracteres de texto a pesquisar nos arquivos que correspondem à especificação de arquivo na guia Nome e localização.
**Expressão 2**
Uma cadeia de caracteres de texto adicional a pesquisar. Ignorada se Expressão 1 estiver vazia.
**Expressão 3**
Uma cadeia de caracteres de texto adicional a pesquisar. Ignorada se Expressão 1 e Expressão 2 estiverem vazias.
**Contém qualquer palavra correspondente**
Se escolhida, especifica que qualquer texto nas cadeias de caracteres especificadas em Expressão 1 , Expressão 2 e Expressão 3 deve corresponder para que a pesquisa seja bem-sucedida.
**Contém todas as palavras correspondentes**
Se escolhida, especifica que todo o texto nas cadeias de caracteres especificadas em Expressão 1 , Expressão 2 e Expressão 3 deve corresponder para que a pesquisa seja bem-sucedida.
**Diferenciar maiúsculas de minúsculas**
Se marcada, especifica que a capitalização das palavras não é ignorada para o texto nas cadeias de caracteres especificadas em Expressão 1 , Expressão 2 e Expressão 3 .
**Corresponder palavras inteiras**
Se marcada, especifica que o texto nas cadeias de caracteres especificadas em Expressão 1 , Expressão 2 e Expressão 3 deve corresponder a palavras inteiras para que a pesquisa seja bem-sucedida.

# Guia Data de modificação
 **Todos os arquivos**
Se escolhida, especifica que as datas em que os arquivos são criados, modificados ou acessados são ignoradas na pesquisa.
**Localizar todos os arquivos criados ou modificados**
Se escolhida, inclui na pesquisa todos os arquivos criados ou modificados entre ou antes das datas especificadas.
**Localizar todos os arquivos acessados pela última vez**
Se escolhida, inclui na pesquisa todos os arquivos acessados entre ou antes das datas especificadas.
**Entre**
Disponível quando Localizar todos os arquivos criados ou modificados ou Localizar todos os arquivos acessados pela última vez é escolhida. Inclui na pesquisa todos os arquivos criados, modificados ou acessados entre as duas datas especificadas.
**Durante o(s) mês(es) anterior(es)**
Disponível quando Localizar todos os arquivos criados ou modificados ou Localizar todos os arquivos acessados pela última vez é escolhida. Inclui na pesquisa todos os arquivos criados, modificados ou acessados durante o número especificado de meses.
**Durante o(s) dia(s) anterior(es)**
Disponível quando Localizar todos os arquivos criados ou modificados ou Localizar todos os arquivos acessados pela última vez é escolhida. Inclui na pesquisa todos os arquivos criados, modificados ou acessados durante o número especificado de dias.

# Guia Atributos de arquivo
 **Tamanho é**
Especifica que os arquivos incluídos na pesquisa têm pelo menos ou no máximo um tamanho especificado (em kilobytes).

# Excluir arquivos com esses atributos
 **Somente leitura**
Exclui da pesquisa arquivos que têm o atributo de arquivo somente leitura definido.
**Arquivo**
Exclui da pesquisa arquivos que têm o atributo de arquivo archive definido.
**Oculto**
Exclui da pesquisa arquivos que têm o atributo de arquivo hidden definido.
**Sistema**
Exclui da pesquisa arquivos que têm o atributo de arquivo system definido.
