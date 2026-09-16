# Arquivos principais em aplicativos

O arquivo principal em um aplicativo pode ser um programa ou um formulário. Embora a melhor escolha para um arquivo principal seja um arquivo de programa (.prg), você pode combinar a funcionalidade de um programa principal e a interface do usuário que o usuário vê inicialmente usando um formulário. Quando os usuários executam seu aplicativo, o Visual FoxPro inicia o arquivo principal em seu aplicativo e executa todos os outros componentes conforme necessário.

Se você usar um arquivo de programa como arquivo principal em seu aplicativo, certifique-se de que ele contém comandos para tratar as tarefas principais em seu aplicativo. No entanto, o arquivo principal não precisa emitir comandos diretamente para realizar todas as tarefas. Por exemplo, o arquivo principal pode chamar procedimentos ou funções para tratar tarefas como inicializar o ambiente e limpar a memória.

A lista a seguir contém e descreve as tarefas principais e a ordem para executá-las em um arquivo de programa principal:
 - Inicialize o ambiente para o aplicativo abrindo bancos de dados, declarando variáveis e assim por diante. Para obter mais informações, consulte Como: inicializar o ambiente.
- Estabeleça e exiba a interface do usuário inicial chamando um menu ou formulário. A interface do usuário inicial pode ser um menu, formulário ou qualquer outro componente de usuário. Às vezes, um aplicativo exibe uma caixa de login para solicitar credenciais do usuário antes de exibir o menu ou formulário inicial. Você pode iniciar a interface do usuário no programa principal usando o comando DO para executar um menu ou o comando DO FORM para executar um formulário. Por exemplo, a linha de código a seguir executa um formulário chamado Startup: DO FORM BeginApp.scx Para obter mais informações, consulte Comando DO e Comando DO FORM.
- Detecte e responda a ações do usuário estabelecendo e controlando o loop de eventos usando o comando READ EVENTS. Para obter mais informações, consulte Como: controlar o loop de eventos.
- Encerre o processamento de eventos quando o usuário sair do aplicativo usando um comando de menu, como um comando Exit, ou um botão Exit. Para obter mais informações, consulte Como: controlar o loop de eventos.
- Restaure o ambiente quando o usuário sair do aplicativo. Normalmente, é recomendado salvar as configurações padrão do ambiente em variáveis públicas, uma classe personalizada ou como propriedades de um objeto de aplicativo para que você possa restaurar esses valores ao sair do aplicativo. Dica Se você inicializar o ambiente usando um programa diferente do que usa para restaurá-lo, certifique-se de que pode acessar os valores que armazenou. Por exemplo, suponha que você inicialize o ambiente chamando um procedimento, mas restaure o ambiente chamando outro. Certifique-se de armazenar os valores que deseja restaurar em variáveis públicas, classes personalizadas ou como propriedades de um objeto de aplicativo. Observação Nomes de variáveis usados com substituição de macro não devem conter o prefixo m. porque o ponto assume concatenação de variáveis e produz um erro de sintaxe.

Por exemplo, um arquivo de programa principal pode conter as linhas de código a seguir:

```foxpro
DO SETUP.PRG
DO MAINMENU.MPR
READ EVENTS
DO CLEANUP.PRG
```

Essas linhas de código executam as seguintes tarefas:
 - Executam um programa de configuração para inicializar o ambiente
- Executam um arquivo de menu para exibir um menu de aplicativo.
- Chamam READ EVENTS para estabelecer o loop de eventos.
- Executam um programa de limpeza para restaurar o ambiente.
