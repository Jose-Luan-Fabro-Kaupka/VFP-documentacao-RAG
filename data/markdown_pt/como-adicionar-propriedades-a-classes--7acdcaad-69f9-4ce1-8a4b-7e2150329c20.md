# Como: adicionar propriedades a classes

Quando você cria uma classe, pode adicionar propriedades personalizadas à classe. Para obter mais informações sobre propriedades, consulte Classes in Visual FoxPro.

> **Observação:** Quando você cria propriedades personalizadas para classes, as propriedades se aplicam à classe, não a componentes individuais na classe.

Você pode adicionar propriedades a classes usando o IDE do Visual FoxPro ou programaticamente.

### Para adicionar uma propriedade a uma classe
- Abra a classe no Class Designer . Quando a classe abre no Class Designer , o menu Class aparece.
- No menu Class, escolha New Property .
- Na caixa Name da caixa de diálogo New Property, digite o nome da propriedade.
- Na caixa Visibility, escolha o nível de visibilidade para a propriedade.
- Para criar um método Access, selecione Access Method . Para criar um método Assign, selecione Assign method . Para criar ambos os métodos Access e Assign, selecione ambas as caixas.
- Para especificar um valor padrão diferente de False (.F.) para a propriedade, inclua um valor padrão diferente na caixa Default Value. Dica Para definir o valor padrão de uma propriedade como uma cadeia de caracteres vazia (""), clique na caixa Default Value e pressione a tecla SPACE.
- Para especificar uma descrição a ser exibida para a propriedade na janela Properties, inclua uma descrição na caixa Description. Dica Você pode documentar valores válidos de propriedade na caixa Description.
- Clique em Add .
- Continue adicionando propriedades ou, se terminou, clique em Close .

> **Observação:** Propriedades em subclasses herdam os valores padrão de propriedade que você especifica, a menos que você redefina os valores padrão para os da classe pai. Quando você adiciona uma propriedade que pode ser definida pelo usuário, o usuário pode inserir um valor de propriedade inválido que pode causar erros em tempo de execução. É recomendado incluir código em seu aplicativo que valide valores inseridos para a propriedade ou documentar os valores válidos de propriedade.

Após adicionar a propriedade, ela aparece na janela Properties no final da lista de propriedades junto com qualquer valor padrão que você especificou. Você pode alterar valores da propriedade na Properties Window (Visual FoxPro).

Para obter mais informações sobre abertura de classes, consulte How to: Modify Classes. Para obter mais informações sobre níveis de visibilidade para propriedades, consulte Protecting and Hiding Class Members. Para obter mais informações, consulte Access and Assign Methods e How to: Create Access and Assign Methods.

### Para adicionar propriedades a classes programaticamente
- Use o comando DEFINE CLASS. Em tempo de execução, você pode adicionar propriedades a objetos usando a função ADDPROPERTY( ) ou o método AddProperty do objeto.

Para obter mais informações, consulte DEFINE CLASS Command, ADDPROPERTY( ) Function e AddProperty Method.

# Propriedades de array

Você pode criar e adicionar propriedades de array a uma classe. Propriedades de array são arrays que você pode adicionar à classe como propriedades. Uma propriedade de array é somente leitura em tempo de design e aparece em itálico na janela Properties; no entanto, você pode manipular e redimensionar uma propriedade de array em tempo de execução. Por exemplo, você pode criar uma propriedade de array para um formulário para armazenar variáveis de objeto associadas a cada instância de um formulário. Para um exemplo de uso de propriedade de array, consulte How to: Manage Multiple Instances of a Form. Para informações sobre limites no número de elementos em arrays, consulte Visual FoxPro System Capacities.

### Para criar uma propriedade de array
- Siga as etapas para adicionar uma propriedade a uma classe.
- Na caixa Name da caixa de diálogo New Property, digite o nome, tamanho e dimensão do array.

Por exemplo, especificar `myArrayProperty[10,2]` cria uma propriedade de array chamada myArrayProperty com dez linhas e duas colunas.
