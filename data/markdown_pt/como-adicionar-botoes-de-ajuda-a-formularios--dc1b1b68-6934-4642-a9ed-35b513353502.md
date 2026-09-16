# Como: adicionar botões de Ajuda a formulários

Você pode programar seu aplicativo para que os usuários possam clicar em um botão Help para acessar o arquivo de Ajuda. Adicionar botões Help pode facilitar o acesso à Ajuda para usuários iniciantes.

> **Dica:** Você pode salvar o botão de comando Help como uma classe para adicioná-lo a um formulário com mais facilidade.

### Para adicionar um botão Help a um formulário
- No evento Init do formulário, use o método SetAll para definir a propriedade HelpContextID de todos os objetos do formulário com o valor que você atribuiu ao tópico de Ajuda que deseja usar. Por exemplo, a linha de código a seguir define a propriedade HelpContextID de todos os objetos do formulário como 7 como número de ID de contexto de Ajuda: THIS.SetAll("HelpContextID", 7)
- Adicione um botão de comando ao formulário.
- Defina a propriedade Caption do botão de comando como o texto Help .
- No evento Click do botão de comando, adicione o seguinte comando: HELP ID THIS.HelpContextID

Para obter mais informações, consulte Init Event, SetAll Method, HelpContextID Property (Visual FoxPro), Caption Property (Visual FoxPro), Click Event e HELP Command.
