# Guia General, Application Builder

Nesta guia do Application Builder, você especifica o nome da aplicação e outros recursos opcionais, como tela de abertura, formulário de inicialização e o tipo de aplicação.
 **Name**
Especifica o nome amigável da sua aplicação usado na barra de título da aplicação, na caixa de diálogo About e em toda a aplicação.
**Image**
Especifica o nome do arquivo e o local da imagem usada na tela de abertura e na caixa de diálogo About da sua aplicação. Você pode usar arquivos de ícone (.ico) fornecidos na pasta \Graphics\ICO do Visual FoxPro ou outros arquivos gráficos, como .bmp, .gif ou .jpg.

# Application Type

Os botões de opção a seguir permitem especificar a forma como sua aplicação é executada:
 **Normal**
A aplicação será executada na janela principal do Visual FoxPro, assumindo todo o ambiente do Visual FoxPro, incluindo o menu do sistema.
**Module**
A aplicação é adicionada a um projeto existente ou chamada por outra aplicação. A aplicação adiciona um único pad e menu ao menu do sistema existente e, portanto, funciona como um componente de outra aplicação. Observação Como os módulos não emitem READ EVENTS nem alteram as configurações existentes do ambiente do Visual FoxPro, funcionam bem quando chamados por outras aplicações ou em tempo de design no ambiente de desenvolvimento do Visual FoxPro. Para obter mais informações, consulte READ EVENTS Command.
**Top-Level**
A aplicação será executada na área de trabalho do Microsoft Windows. Com aplicações de nível superior, a área de trabalho baseada no Visual FoxPro não é necessariamente visível. Fornece uma interface de documentos múltiplos (MDI) do Windows com mais flexibilidade que _SCREEN porque você pode fazer subclass dela. Para obter mais informações, consulte _SCREEN System Variable.

# Common Dialogs

As caixas de seleção a seguir permitem incluir determinadas caixas de diálogo na sua aplicação:
 **Splash Screen**
Especifica se a aplicação inicia exibindo o arquivo de imagem designado no campo Image e créditos em uma tela de abertura.
**Quick Start form**
Especifica se deve ser usado um formulário Quick Start que fornece acesso a documentos da aplicação e a outros arquivos em disco. Você pode usar isso para orientar os usuários pela aplicação.
**About dialog**
Especifica se uma caixa de diálogo About aparece na aplicação.
**User Logins**
Especifica se a aplicação solicita login com senha do usuário e mantém informações de preferência para vários usuários, como configurações da caixa de diálogo Options e conteúdo do menu Favorites.
**Icon**
Especifica o gráfico que aparece na área de trabalho principal (_SCREEN) de aplicações típicas, no frame do formulário superior de aplicações de nível superior e na barra de título de formulários aos quais você não atribuiu um ícone específico.

Se você escolher OK, o builder é fechado, aplicando as configurações de propriedade de todas as guias.
