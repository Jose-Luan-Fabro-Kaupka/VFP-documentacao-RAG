# Como: definir uma classe Toolbar

Se quiser criar uma barra de ferramentas que contenha botões ainda não encontrados nas barras existentes, você poderá fazer isso definindo uma classe de barra de ferramentas personalizada. O Visual FoxPro fornece uma classe base Toolbar a partir da qual você pode criar a classe necessária.

Depois de definir uma classe de barra de ferramentas, você pode adicionar objetos a ela e então definir as propriedades, os eventos e os métodos da barra personalizada. Por fim, pode adicionar a barra de ferramentas a um conjunto de formulários.

### Para definir uma classe de barra de ferramentas personalizada
- Na janela Project Manager, selecione Classes e escolha New.
- Na caixa Class Name, digite o nome da classe.
- Na caixa Based On, selecione Toolbar para usar a classe base Toolbar. -ou- Escolha o botão de diálogo para selecionar outra classe de barra de ferramentas.

Por exemplo, você pode armazenar uma classe de impressão baseada na classe base Toolbar em uma biblioteca de inventário.

Ao concluir a caixa de diálogo New Class, o Class Designer será exibido.

Você também pode definir uma classe de barra de ferramentas de uma das seguintes maneiras:
 - Escolhendo New no menu File e depois Class.
- Usando o Comando CREATE CLASS ou o Comando MODIFY CLASS.
- Definindo a classe programaticamente com o Comando DEFINE CLASS.

Durante o design de uma barra de ferramentas personalizada, você pode definir suas propriedades. Por exemplo, pode definir a propriedade Movable para permitir que o usuário mova a barra.

Além disso, pode usar métodos e eventos para controlar barras de ferramentas personalizadas. Por exemplo, use o método Dock para encaixar ou tornar flutuante uma barra de ferramentas e use os eventos BeforeDock e AfterDock para controlar o que ocorre antes e depois de a barra ser encaixada.
