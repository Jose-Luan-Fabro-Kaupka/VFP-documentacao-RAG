# Hooks do Project Manager

No Visual FoxPro, você pode acessar um projeto programaticamente e manipular um projeto como um objeto. Você pode manipular um projeto enquanto o projeto está aberto no Project Manager em tempo de design ou enquanto o Project Manager não está visível em tempo de design e em tempo de execução.

> **Dica:** Para abrir ou modificar um projeto para que você possa manipulá-lo programaticamente sem exibir o Project Manager, use a cláusula NOSHOW nos comandos CREATE PROJECT e MODIFY PROJECT. Você pode usar a propriedade Visible do projeto para exibir o Project Manager posteriormente. Para obter mais informações, consulte Comando CREATE PROJECT e Comando MODIFY PROJECT .

A lista a seguir descreve algumas das ações que você pode realizar programaticamente com um projeto:
 - Abrir e modificar arquivos no projeto.
- Adicionar ou excluir arquivos de um projeto.
- Determinar o número de arquivos em um projeto e seus tipos.
- Alterar propriedades do projeto.
- Alterar propriedades de arquivos no projeto.
- Alterar propriedades de servidores Automation, que são arquivos de biblioteca de vínculo dinâmico (.dll) ou executáveis (.exe) criados a partir do projeto.
- Executar código quando eventos ocorrem no projeto.
- Recompilar o projeto ou criar arquivos .app, .exe ou .dll a partir do projeto.
- Adicionar arquivos no projeto a aplicativos de controle de código-fonte, como o Microsoft Visual SourceSafe, e fazer check-in e check-out de arquivos no controle de código-fonte. Observação Se você adicionar um projeto ao Visual SourceSafe, todos os arquivos contidos no projeto devem estar no diretório ou caminho do projeto para o mapeamento correto ao projeto.

Como desenvolvedor avançado, você também pode criar gerenciadores de projeto personalizados.
