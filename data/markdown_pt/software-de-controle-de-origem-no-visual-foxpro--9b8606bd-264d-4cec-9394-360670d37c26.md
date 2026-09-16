# Software de controle de origem no Visual FoxPro

Um dos aspectos mais críticos do desenvolvimento em equipes é a capacidade de controlar quem tem permissão para alterar arquivos. Por exemplo, se não há controles sobre arquivos, e se mais de um desenvolvedor está alterando um programa ao mesmo tempo, há uma forte probabilidade de que um conjunto de alterações acabe sendo substituído ou descartado, desperdiçando tempo e esforço.

O Visual FoxPro ajuda sua equipe a gerenciar arquivos em seus projetos permitindo que você integre um sistema de controle de código-fonte no Project Manager do Visual FoxPro. Ao fazer isso, você pode gerenciar arquivos de projeto em um ambiente de desenvolvimento em equipe e garantir que os esforços de desenvolvimento prossigam sem problemas.

# Integrando controle de origem com projetos do Visual FoxPro

O Visual FoxPro suporta ferramentas de controle de código-fonte permitindo que você integre software de controle de origem comercialmente disponível diretamente em seus projetos. Você pode usar muitos dos sistemas de controle de versão atualmente disponíveis. (Entre em contato com o fornecedor do software para descobrir se o software pode ser integrado com ferramentas de desenvolvimento da Microsoft.) Por exemplo, se sua equipe de desenvolvimento já usa o Microsoft Visual SourceSafe, você pode especificar isso como o software de controle de origem a usar com o Visual FoxPro.

> **Observação:** Se você adicionar um projeto ao Visual SourceSafe, para mapeamento adequado ao projeto, todos os arquivos contidos no projeto devem estar no diretório ou caminho do projeto.

Todo o controle de origem no Visual FoxPro é gerenciado através do Project Manager. Quando você configura um projeto no Visual FoxPro, você tem a opção de criar um projeto de controle de código-fonte correspondente, que é referido como "colocar o projeto sob controle de origem." Depois que você colocou um projeto sob controle de origem, o Visual FoxPro ajuda você a gerenciar os arquivos no projeto controlado por origem. Quando você deseja modificar um arquivo — por exemplo, se você edita um programa ou modifica um formulário — o Visual FoxPro solicita que você faça check-out desse arquivo.

No Visual FoxPro, o controle de origem é usado para gerenciar arquivos de todos os tipos, não apenas arquivos .prg, mas também arquivos .scx, .frx, .lbx, .mnx e .vcx, e outros. Embora arquivos individuais possam ser compartilhados entre diferentes projetos do Visual FoxPro, todas as operações de controle de origem são conduzidas em arquivos no contexto de um projeto específico.

> **Observação:** O Visual FoxPro não solicita que você coloque tabelas de dados como arquivos .dbf e .dbc sob controle de origem quando você os cria, mas você pode adicioná-los manualmente ao seu projeto controlado por origem.

Quando você trabalha no Project Manager com um projeto que está sob controle de origem, o Visual FoxPro exibe ícones ao lado de arquivos que estão sob controle de origem para indicar seu status.

A tabela a seguir resume os ícones usados no Project Manager para indicar o status de controle de origem.

| Ícone | Significado |
| --- | --- |
| O arquivo está com check-out para você. | |
| O arquivo está com check-out para você e para um ou mais outros desenvolvedores. | |
| O arquivo está com check-out para outro desenvolvedor. | |
| O arquivo não está com check-out; você não pode alterar o arquivo até fazer check-out. | |
| O arquivo foi mesclado. Depois de examinar as alterações, você pode fazer check-in do arquivo. | |
| O arquivo foi mesclado e há conflitos que precisam ser resolvidos. | |
| O Visual FoxPro não pode determinar o status de controle de origem do arquivo. | |

Se um arquivo não está sob controle de origem, nenhum ícone aparece ao lado dele.
