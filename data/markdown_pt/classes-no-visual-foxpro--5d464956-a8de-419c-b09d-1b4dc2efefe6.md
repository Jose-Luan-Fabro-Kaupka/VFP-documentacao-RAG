# Classes no Visual FoxPro

Classes definem propriedades, métodos e eventos, que são características e funcionalidades que os objetos possuem e que você pode usar para manipular objetos. Classes também podem conter outros objetos ou membros de dados, como variáveis. Quando um objeto, ou instância, é criado a partir de uma classe, ele contém as propriedades, métodos, eventos e quaisquer outros objetos ou membros conforme definido pela classe.

As propriedades que uma classe define especificam características para um objeto dessa classe. Por exemplo, a classe CommandButton tem uma propriedade Name, que define o nome do botão de comando, em oposição à propriedade Caption, que define o texto que o botão de comando exibe ao usuário.

Os métodos de uma classe definem e armazenam código de procedimento que é executado quando você chama o método para um objeto dessa classe. Por exemplo, a classe CommandButton tem um método Move, que move o botão de comando para as coordenadas que você especifica.

Os eventos de uma classe definem código que é executado quando o sistema ou o usuário realiza ações que acionam os eventos para um objeto dessa classe. Por exemplo, a classe CommandButton contém um evento Click, que é um procedimento que você pode usar para definir código que é executado quando o usuário clica no botão de comando.

Classes também podem conter outros objetos, por exemplo, uma classe Form pode conter um objeto de controle, como um botão de comando. Você também pode especificar membros de dados, como variáveis, como parte de uma classe.

As seções a seguir fornecem mais informações sobre classes Visual FoxPro:
 - Benefits of Using Classes
- Types of Visual FoxPro Classes

Para obter mais informações sobre objetos no Visual FoxPro, consulte Working with Objects in Visual FoxPro.

# Benefícios de usar classes

Classes fornecem os seguintes recursos que permitem criar código reutilizável e mais fácil de manter:
 - Encapsulation O encapsulamento, que inclui empacotar código de propriedade e método em um objeto, oculta complexidade desnecessária e ajuda a contribuir para a abstração. A abstração permite que você se concentre nos aspectos do objeto que deseja ou precisa usar em vez dos detalhes de baixo nível. Por exemplo, quando uma pessoa usa um computador, geralmente não quer saber como ele opera, como processa dados ou mantém arquivos. A pessoa quer realizar tarefas, como escrever uma carta, e não precisa saber como essas tarefas são realizadas. Da mesma forma, uma classe list box encapsula propriedades que controlam como os itens são exibidos na list box e funcionalidade que determina as ações realizadas ao escolher itens na list box em um único controle.
- Subclass creation Para obter mais informações, consulte Subclasses in Visual FoxPro .
- Inheritance Para obter mais informações, consulte Subclasses in Visual FoxPro .

Esses recursos ajudam você a criar e manter código com mais facilidade e rapidez.

# Tipos de classes Visual FoxPro

Classes Visual FoxPro, e por extensão, objetos, se dividem em dois tipos principais: classes de contêiner e classes de controle. Classes também podem ser visuais ou não visuais.

### Classes de contêiner e classes de controle

Contêineres podem consistir em outros objetos, como controles, e fornecem acesso aos objetos que contêm. Classes de controle são mais encapsuladas que classes de contêiner; no entanto, por esse motivo, podem ser menos flexíveis. Classes de controle não possuem um método AddObject Method.

Por exemplo, suponha que você cria uma classe de contêiner que consiste em duas list boxes e dois botões de comando. Você então adiciona um objeto baseado na classe de contêiner a um formulário. Você pode manipular cada objeto no contêiner em tempo de design e em tempo de execução; por exemplo, pode alterar as posições das list boxes ou as legendas dos botões de comando. Você também pode adicionar outros objetos ao contêiner em tempo de design; por exemplo, pode adicionar labels para identificar as list boxes.

A tabela a seguir lista exemplos de objetos que podem existir em classes de contêiner.

| Container | Can contain |
| --- | --- |
| Column | Headers e quaisquer objetos exceto form-sets, formulários, toolbars, timers e outras colunas |
| CommandGroup | Botões de comando |
| Container | Quaisquer controles |
| Control | Quaisquer controles |
| Custom | Quaisquer controles, ambiente de dados, page frame, contêiner, custom |
| DataEnvironment | Cursors, relações e cursor adapters |
| FormSet | Formulários, toolbars |
| Form | Page frames, ambiente de dados, quaisquer controles, contêineres, custom |
| Grid | Colunas |
| OptionGroup | Botões de opção |
| PageFrame | Páginas |
| Page | Quaisquer controles, contêineres, custom |
| Project | Arquivos, servidores |
| Toolbar | Quaisquer controles, page frame, contêiner |

### Classes visuais e não visuais

No Visual FoxPro, objetos e controles criados a partir de classes visuais exibem um elemento visual em tempo de design e em tempo de execução. Objetos e controles baseados em classes não visuais, como a classe Custom e o controle Timer, exibem um elemento visual apenas em tempo de design, mas não em tempo de execução.
