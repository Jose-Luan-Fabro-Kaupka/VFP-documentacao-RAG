# Preparação para distribuição de aplicativos

Esta seção descreve várias questões que você deve considerar ao preparar seu aplicativo para implantação.
 - Seleção do tipo de compilação
- Questões de hardware, memória e rede
- Garantindo comportamento correto em tempo de execução
- Opções de menu padrão

# Seleção do tipo de compilação

Antes de distribuir seu aplicativo, você deve compilar um arquivo de aplicativo (.app), um arquivo executável (.exe) ou um componente COM (servidor de automação) com extensão .dll ou .exe. Ao escolher o tipo de compilação que deseja criar, considere o tamanho do arquivo final do aplicativo e se os usuários têm o Visual FoxPro instalado em seus computadores.

A tabela a seguir lista as diferenças entre os tipos de compilação.

| Tipo de compilação | Descrição |
| --- | --- |
| Arquivo de aplicativo (.app) | Este arquivo exige que o usuário tenha uma cópia do Visual FoxPro instalada. Um arquivo .app geralmente é menor que um arquivo .exe. |
| Arquivo executável (.exe) | Este arquivo inclui o carregador do Visual FoxPro, para que os usuários não precisem ter o Visual FoxPro instalado. Você deve fornecer os dois arquivos de suporte VFP VersionNumber R.dll e VFP VersionNumber RENU.dll, onde VersionNumber representa o número da versão desta versão do Visual FoxPro. As letras "EN" denotam a versão em inglês. Esses arquivos devem ser colocados no mesmo diretório do arquivo .exe ou no caminho do DOS. Consulte Comando BUILD EXE para obter detalhes sobre como criar e distribuir arquivos executáveis. |
| Arquivos de servidor COM (.dll ou .exe) | Este arquivo é usado para criar um arquivo que pode ser chamado por outros aplicativos. No Visual FoxPro, você pode criar dois tipos de arquivos de servidor COM (.dll, anteriormente OLE). Você deve fornecer arquivos de suporte de tempo de execução, incluindo os arquivos VFP VersionNumber R.dll, VFP VersionNumber T.dll e VFP VersionNumber RENU.dll, onde VersionNumber representa o número da versão desta versão do Visual FoxPro. Para obter detalhes, consulte Como: adicionar objetos OLE a aplicativos . |

# Questões de hardware, memória e rede

Você deve considerar e testar o ambiente mínimo em que seu aplicativo pode operar, incluindo a quantidade de espaço em disco e memória. Os resultados dos seus testes e a resolução de outras questões abordadas nesta seção podem ajudar a determinar o tipo de compilação que você escolhe e os arquivos que inclui com seu aplicativo.

Os aplicativos que você cria têm os mesmos requisitos de hardware, memória e rede do Visual FoxPro. Para obter mais informações sobre esses requisitos, consulte Instalando o Visual FoxPro. Para obter informações adicionais sobre como criar aplicativos para ambientes multiusuário, consulte Programação para acesso compartilhado.

# Garantindo comportamento correto em tempo de execução

Ao distribuir um aplicativo executável (.exe), você deve incluir os seguintes arquivos:
 - VFP VersionNumber R.dll, onde VersionNumber representa o número da versão desta versão do Visual FoxPro.
- VFP VersionNumber RENU.dll
- GDIPlus.dll
- MSVCR71.dll

Em alguns casos, servidores in-process do Visual FoxPro, ou arquivos .dll, podem usar a biblioteca de tempo de execução leve VFPVersionNumberT.dll. Para obter mais informações sobre bibliotecas de tempo de execução, consulte Biblioteca de tempo de execução VFP9R.DLL e Biblioteca de tempo de execução VFP9T.DLL.

> **Observação:** Se você deseja executar um aplicativo (.exe) usando a versão de desenvolvimento do Visual FoxPro, deve executar o arquivo .exe com o arquivo executável do Visual FoxPro, VFP VersionNumber .exe.

Um aplicativo consistindo apenas de formulários sem modo não funcionará corretamente em um ambiente de tempo de execução, a menos que você forneça um comando READ EVENTS. Você pode garantir que o aplicativo execute corretamente adicionando um programa de chamada ou definindo a propriedade WindowType.

Você também pode digitar `DO` seguido do nome do arquivo .exe do seu aplicativo na janela Command ou usar a opção de linha de comando -E na linha de comando que inicia o Visual FoxPro. Por exemplo, se seu aplicativo se chama MYAPP, você pode executá-lo com a seguinte linha de comando:

```foxpro
MYAPP.EXE -E
```

Esta opção de linha de comando força o aplicativo a usar o arquivo executável, VFPVersionNumber.exe, onde VersionNumber representa o número da versão desta versão do Visual FoxPro. Para que esta opção funcione corretamente, VFPVersionNumber.exe deve estar no caminho de pesquisa.

### Para executar um formulário em um ambiente de tempo de execução
- Execute o formulário de um programa contendo um comando READ EVENTS. -ou-
- Defina a propriedade WindowType do formulário como Modal .

Alguns aplicativos Visual FoxPro dependem fortemente dos menus do sistema do Visual FoxPro. Em tempo de execução, alguns menus e comandos estão indisponíveis e, sem uma provisão para um comando READ EVENTS, um aplicativo orientado a menu termina tão rapidamente quanto começa. Use a seção a seguir para revisar quaisquer menus que você inclua em seu aplicativo.

Para obter mais informações sobre como estruturar um aplicativo com o comando READ EVENTS, consulte Como: controlar o loop de eventos e exemplos de como estruturar um aplicativo em Compilando um aplicativo.

# Opções de menu padrão

Se você usar o menu do sistema do Visual FoxPro, seu arquivo de aplicativo inclui apenas os seguintes menus e comandos de menu padrão.

| Menu | Itens de menu |
| --- | --- |
| File | Close, Save, Save As, Exit |
| Edit | Undo, Redo, Cut, Copy, Paste, Paste Special, Select All, Find, Replace |
| Window | Arrange All, Hide, Hide All, Show All, Clear, Cycle, all open windows |
| Help | Contents, Search for Help on, Product Support, About Visual FoxPro |

Você pode desabilitar ou remover qualquer um dos menus e comandos de menu padrão, ou adicionar seus próprios menus e comandos de menu a aplicativos de tempo de execução.

> **Dica:** Se seu sistema de menu funciona no ambiente de desenvolvimento, mas fecha prematuramente em seu aplicativo, certifique-se de ter um comando READ EVENTS ativo enquanto seu sistema de menu está em execução. Certifique-se também de incluir um comando CLEAR EVENTS quando sair do sistema de menu.

Para obter mais informações sobre como personalizar menus, consulte Projetando menus e barras de ferramentas.
