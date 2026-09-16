# Definindo opções de configuração na inicialização

Você pode estabelecer configurações quando inicia o programa pela primeira vez, o que permite substituir as configurações padrão.

# Usando comandos SET em aplicativos

Uma maneira de estabelecer configurações é emitir um ou mais comandos SET quando seu aplicativo inicia. Por exemplo, para configurar seu sistema para exibir um relógio na barra de status quando o aplicativo inicia, você pode emitir este comando SET:

```foxpro
SET CLOCK ON
```

O ponto exato em que você emite o comando SET depende do seu aplicativo. Em geral, você emite comandos SET a partir do arquivo de programa principal do aplicativo, que é o programa ou formulário que controla o acesso ao restante do aplicativo. Você também pode emitir comandos SET dos eventos Load ou Init do formulário. Se você estiver usando sessões de dados privadas, pode ser necessário fazer essas configurações no evento BeforeOpenTables do objeto DataEnvironment. Para detalhes sobre como especificar um arquivo principal para um aplicativo, consulte Compiling an Application.

Se seu aplicativo tem um form set como principal no project manager, e então inicia um menu, você pode adicionar comandos SETUP inserindo-os na opção Setup do menu. Para detalhes, consulte How to: Add Setup Code to a Menu System em Designing Menus and Toolbars.

> **Dica:** Uma maneira eficiente de gerenciar comandos SET na inicialização é criar um procedimento que contenha todos os comandos que você deseja emitir. Você pode então chamar o procedimento do ponto apropriado em seu aplicativo. Manter todos os comandos SETUP em um único procedimento facilita a depuração e a manutenção de suas configurações. Você também pode colocar o código na classe na qual seu objeto de aplicativo é baseado, ou na classe na qual seus formulários são baseados.

# Usando um arquivo de configuração

Além de configurar o ambiente do Visual FoxPro usando a caixa de diálogo Options ou comandos SET, você pode estabelecer configurações preferidas e salvá-las em um ou mais arquivos de configuração. Um arquivo de configuração do Visual FoxPro é um arquivo de texto no qual você pode especificar valores para comandos SET, definir variáveis de sistema e executar comandos ou chamar funções. O Visual FoxPro lê o arquivo de configuração na inicialização, estabelecendo as configurações e executando os comandos no arquivo. As configurações feitas no arquivo de configuração substituem as configurações padrão feitas na caixa de diálogo Options (e armazenadas no registro do Windows).

Usar um arquivo de configuração oferece várias vantagens. Você pode:
 - Substituir as configurações padrão estabelecidas na caixa de diálogo Options.
- Manter vários arquivos de configuração diferentes, cada um com configurações diferentes, para que o Visual FoxPro possa carregar uma configuração adequada a um usuário ou projeto específico.
- Fazer alterações mais facilmente do que se você estabelecer configurações com os comandos SET na sequência de inicialização do programa.
- Iniciar um programa ou chamar uma função automaticamente quando o Visual FoxPro inicia.

Para instruções sobre como trabalhar com arquivos de configuração, consulte How to: Create a Configuration File e How to: Specify the Configuration File.
