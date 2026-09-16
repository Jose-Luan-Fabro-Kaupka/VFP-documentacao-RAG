# Exemplo Fornecer ajuda "O que é isto?" em um formulário

Arquivo: ...\Samples\Solution\Forms\Whatthis.scx

Quando você fornece ajuda "O que é isto?" em um formulário, um botão com um ponto de interrogação é exibido no canto superior direito do formulário.

Quando um usuário clica neste botão ou pressiona SHIFT+ F1, o formulário é definido para o modo WhatsThis. Você também pode entrar nesse estado programaticamente chamando o método WhatsThisMode do formulário. Quando o formulário está no modo WhatsThis, o ponteiro do mouse muda. Um usuário pode clicar em um controle e obter ajuda sensível ao contexto para esse controle em uma janela pop-up.

> **Observação:** Se o WhatsThisHelpID de um controle ou de um formulário estiver definido como -1 (o padrão), o texto na janela pop-up indica que não há tópico de ajuda disponível para o controle.

### Para fornecer ajuda "O que é isto?"
- Crie um arquivo de ajuda com um tópico para cada controle no formulário.
- Na seção Map do projeto de ajuda, mapeie valores HelpContextID para os tópicos.
- Defina a propriedade WhatsThisHelp do formulário como true (.T.).
- Defina a propriedade WhatsThisButton do formulário como true (.T.).
- Defina o WhatsThisHelpID dos controles para os valores helpcontextID apropriados.
- No Load ou Init do formulário, use o comando SET HELP TO para especificar o arquivo de ajuda do formulário.

Além de Whatthis.scx, este exemplo inclui os seguintes arquivos:

| Arquivo | Descrição |
| --- | --- |
| Whatthis.hlp | O arquivo de ajuda do formulário |
| Whatthis.hpj | O arquivo de projeto de ajuda |
| Whatthis.rtf | O documento de origem do arquivo de ajuda |
