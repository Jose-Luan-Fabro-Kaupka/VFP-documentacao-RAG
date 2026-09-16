# Trabalhando com o arquivo de projeto e o arquivo de lista de projeto

No Visual FoxPro, as informações do projeto são mantidas em um conjunto de arquivos de tabela e memo com as extensões .pjx e .pjt. Por exemplo, se você criou um projeto chamado "MyProj", as informações sobre o projeto, incluindo a lista de arquivos, sua localização e se estão compilados no arquivo de aplicação (.app ou .exe), são armazenadas nos arquivos chamados Myproj.pjx e Myproj.pjt.

Ao trabalhar em um ambiente de desenvolvimento em equipe, os desenvolvedores não compartilham os mesmos arquivos de projeto (arquivos .pjx e .pjt). Em vez disso, os desenvolvedores mantêm suas próprias cópias locais dos arquivos .pjx e .pjt.

Para coordenar as alterações que desenvolvedores individuais fazem em um projeto sob controle de origem, o Visual FoxPro mantém uma lista de arquivos de projeto (ou arquivo .pjm, abreviação de "project metafile"). O arquivo que contém a lista de arquivos de projeto é um arquivo de texto que armazena as mesmas informações dos arquivos .pjx e .pjt, como quais arquivos estão incluídos no projeto no momento.

O software de controle de código-fonte mantém um arquivo de lista de arquivos de projeto central armazenado com os outros arquivos no repositório central. Além disso, cada desenvolvedor tem uma cópia local da lista de arquivos de projeto em check-out que reflete sua versão atual do projeto.

Imagine que você está trabalhando com um projeto e adicionando um novo programa (arquivo .prg). Quando você adiciona o novo arquivo (e assumindo que colocou esse arquivo sob controle de origem), o Visual FoxPro atualiza sua cópia local do projeto e mostra o arquivo quando você usa o Project Manager no seu computador. Outros desenvolvedores não ficam cientes inicialmente da sua alteração, e suas cópias locais do projeto não mostram o arquivo que você adicionou. Mesmo que você não tenha atualizado a lista de arquivos de projeto, ainda pode fazer check-in do novo arquivo para segurança e fazer check-out novamente conforme necessário.

Quando você terminar com o novo arquivo — por exemplo, quando terminar de testar seu novo programa — pode atualizar a lista de arquivos de projeto. Ao fazer isso, o Visual FoxPro mescla as informações em sua lista local de arquivos de projeto com as da lista central de arquivos de projeto.

O Visual FoxPro, por sua vez, atualiza sua lista local de arquivos de projeto com as alterações encontradas na lista central de arquivos de projeto. Se outros desenvolvedores adicionaram arquivos ao projeto, sua lista local de arquivos de projeto é atualizada, cópias locais dos novos arquivos são colocadas no seu computador, o Visual FoxPro reconstrói seu projeto (arquivos .pjx e .pjt) e o Project Manager exibe os arquivos adicionados para você trabalhar.
 Gerenciando arquivos de projeto usando a lista de projeto

> **Observação:** A lista de arquivos de projeto rastreia apenas os arquivos de projeto que estão explicitamente sob controle de origem. Se seu projeto incluir arquivos que não estão sob controle de origem, eles não aparecerão na lista de arquivos de projeto, e o Visual FoxPro não adicionará esses arquivos aos projetos de outros desenvolvedores quando eles atualizarem suas próprias listas de projeto.
