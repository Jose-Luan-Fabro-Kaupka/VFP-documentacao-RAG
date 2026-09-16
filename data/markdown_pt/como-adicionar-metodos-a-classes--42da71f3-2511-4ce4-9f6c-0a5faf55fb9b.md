# Como: adicionar métodos a classes

Depois de criar uma classe, você pode criar e adicionar métodos personalizados à classe. Quando você adiciona métodos a classes, está criando um procedimento ou função na definição da classe. Para obter mais informações sobre métodos, consulte Classes in Visual FoxPro.

> **Observação:** Quando você cria métodos personalizados para classes, os métodos têm escopo da classe, não de componentes individuais na classe. Se você criar um método que tenha o mesmo nome de um evento na definição da classe, o código no método é executado quando o evento ocorre.

Você pode adicionar métodos a classes usando a IDE do Visual FoxPro ou programaticamente. Quando você adiciona um método, pode especificar o nível de visibilidade do método. Para obter mais informações sobre níveis de visibilidade para métodos, consulte Protecting and Hiding Class Members.

### Para adicionar um método a uma classe
- Abra a classe no Class Designer. Para obter mais informações sobre como abrir classes, consulte How to: Modify Classes. Quando a classe abre no Class Designer, o menu Class aparece.
- No menu Class, escolha New Method.
- Na caixa Name da caixa de diálogo New Method, digite o nome do método.
- Na caixa Visibility, escolha o nível de visibilidade do método.
- Para especificar uma descrição para o método quando o método aparecer na janela Properties, inclua uma descrição na caixa Description.
- Clique em Add.
- Continue adicionando métodos ou, se terminou, clique em Close.

Depois de adicionar o método, ele aparece na janela Properties no final da lista de propriedades. Para obter informações sobre como adicionar código a métodos, consulte How to: Add Code to Methods and Events.

### Para adicionar métodos a classes programaticamente
- Use o comando DEFINE CLASS e inclua a cláusula FUNCTION quando criar uma classe.

Para obter mais informações, consulte DEFINE CLASS Command.
