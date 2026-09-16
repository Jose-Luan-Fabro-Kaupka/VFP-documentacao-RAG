# Exemplo Member Classes

Arquivo: ...\Samples\Solution\Toledo\frmMember.scx

Você pode especificar classes de membro para as seguintes classes de contêiner:
 - PageFrame ( classe de membro Page)
- OptionGroup ( classe de membro OptionButton)
- CommandGroup ( classe de membro CommandButton)
- Grid ( classe de membro Column)
- Column ( classe de membro Header)

Você também pode criar subclasses das classes Page, OptionButton, CommandButton, Column e Header.

Neste exemplo, você pode selecionar um contêiner pai, definir a biblioteca de classes de membro, aumentar ou diminuir a contagem de membros e escolher visualizar o comportamento em tempo de design ou em tempo de execução.

> **Observação:** Observe as diferenças de comportamento que existem durante o tempo de design e o tempo de execução. Alterações em MemberClass afetam todas as classes de membro em tempo de design. Somente novos membros são afetados em tempo de execução.

Este exemplo usa classes de membro baseadas em programa (.prg) e em biblioteca de classes visual (.vcx). Para obter mais informações, consulte Member Classes (Visual FoxPro).

# Especificando uma classe de membro e biblioteca de classes de membro

Você pode especificar a classe de membro e sua biblioteca de classes de membro que deseja usar para os contêineres PageFrame, OptionGroup, CommandGroup, Grid e Column definindo as propriedades MemberClass e MemberClassLibrary para esses objetos, conforme mostrado no código a seguir:

```foxpro
MemberClassLibrary = "MyClasses.vcx"
MemberClass = "MyClassName"
```

-ou-

```foxpro
MemberClassLibrary = "MyClasses.prg"
MemberClass = "MyClassName"
```

Você deve definir MemberClassLibrary antes de definir a propriedade MemberClass.

Para obter mais informações, consulte MemberClass Property e MemberClassLibrary Property.
