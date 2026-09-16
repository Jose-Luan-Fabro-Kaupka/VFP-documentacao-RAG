# Classes de membros (Visual FoxPro)

Você pode definir e criar subclasses para objetos membros de certos objetos contêiner. A tabela a seguir lista esses membros e seus contêineres pai:

| Membro | Contêiner |
| --- | --- |
| Page | PageFrame |
| CommandButton | CommandGroup |
| OptionButton | OptionGroup |
| Column | Grid |
| Header | Column |

Usando classes de membros, você pode definir comportamento consistente para todos os membros de uma classe específica. Por exemplo, você pode definir um comportamento particular no evento Activate de uma classe Page para ser usada em uma classe ou objeto PageFrame específico. Todas as páginas membros desse page frame herdam o mesmo código ou comportamento.

Para definir a classe personalizada padrão para objetos membros, defina as propriedades MemberClassLibrary e MemberClass para as classes contêiner PageFrame, CommandGroup, OptionGroup e Grid. Essas propriedades especificam a classe de membro e a biblioteca de classes que você deseja usar. Quando essas propriedades estão definidas, novos objetos membros herdam da classe de membro especificada. Para objetos Column, use as propriedades HeaderClassLibrary e HeaderClass para especificar uma classe Header personalizada.

> **Cuidado:** Não altere a propriedade Name de uma classe de membro em uma definição de classe baseada em programa (.prg) em tempo de design. Fazer isso pode resultar na geração da mensagem "Class definition name is not found."

# Observações

Em geral, objetos membros devem estar contidos em um objeto contêiner pai para serem usados visualmente. Contêineres pai podem conter apenas objetos membros. Por exemplo, um objeto Page deve estar em um objeto PageFrame para ser exibido em um objeto Form e um objeto PageFrame deve ter pelo menos um objeto Page para ser visível em um objeto Form. Há duas exceções:
 - Você pode usar command buttons em outros contêineres sem exigir um CommandGroup .
- Objetos Column podem conter outros controles, mas apenas um Header .

Objetos membros existem apenas como filhos do contêiner pai, que contém apenas membros pertencentes a uma classe base específica. Por exemplo, a existência de um objeto Page requer a existência prévia de seu objeto contêiner PageFrame pai. Um objeto PageFrame pode conter apenas páginas e não command buttons.

Você pode associar um evento ao adicionar um novo objeto membro usando o método _ASSIGN da propriedade count do objeto membro. O evento Init do objeto membro ocorre quando objetos membros são adicionados. No entanto, você não pode passar parâmetros para o evento Init de um objeto membro recém-criado porque os membros são criados dinamicamente quando a propriedade count do contêiner pai é alterada. Se você precisar passar parâmetros, pode usar o método AddObject do contêiner.

> **Observação:** Em um formulário .scx, se você adicionar código de instanciação ao evento Init da classe de membro, o Visual FoxPro desconsidera esse código e apenas o código Init da definição da classe de membro é executado. No entanto, com formulários de biblioteca de classes visual (.vcx), o Visual FoxPro cria uma verdadeira subclasse. Você pode adicionar com segurança código de instanciação para outros eventos, como Click .

Quaisquer valores de propriedade acessados no evento Init da classe de membro pertencem aos da classe de membro original. Quaisquer valores que possam ter sido substituídos na subclasse são aplicados após instanciar a classe de membro.

Esses comportamentos se aplicam apenas a formulários .scx. Após o evento Init ocorrer, a classe de membro é tratada da mesma forma em formulários .scx e .vcx.
