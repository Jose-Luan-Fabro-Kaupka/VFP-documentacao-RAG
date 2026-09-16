# Propriedade MemberClass

Especifica o nome da classe de membro a usar ao adicionar novos membros a um contêiner. Leitura/gravação em tempo de design e em tempo de execução.

Para um contêiner pai Column e seus membros header, use a propriedade HeaderClass em vez de MemberClass.

> **Observação:** Se a classe de membro é baseada em uma classe que está armazenada em um arquivo de programa (.prg), certifique-se de que o arquivo de programa compilado (.fxp) está sincronizado com o arquivo .prg.

```foxpro
Object.MemberClass [ = cClassName ]
```

# Valor de retorno
 **cClassName**
Especifica o nome de uma classe de membro em um arquivo de programa (.prg) ou biblioteca de classes visuais (.vcx).

# Observações

Aplica-se a: PageFrame Control | CommandGroup Control | OptionGroup Control | Grid Control

O Visual FoxPro cria um objeto de membro usando MemberClass sob as seguintes condições:
 - MemberClass é especificado para uma definição de classe de contêiner em tempo de design. Quando o Visual FoxPro cria o contêiner, ele instancia membros usando MemberClass .
- A propriedade Count do objeto de membro, como as propriedades PageCount , ButtonCount ou ColumnCount , é aumentada em tempo de execução. Se a propriedade Count do objeto de membro é aumentada programaticamente ou interativamente, o Visual FoxPro adiciona novas instâncias usando MemberClass . Observação A propriedade ColumnCount é única porque você pode especificar seu valor como -1 ou 0. Todas as outras propriedades Count devem ser maiores ou iguais a zero.

Tanto MemberClass quanto MemberClassLibrary suportam os métodos Access e Assign e escopo Public, Hidden e Protected.

Um contêiner pode conter objetos de diferentes classes de membro com a mesma classe base. Por exemplo, suponha que você tenha um objeto PageFrame e duas classes de membro, myPage1 e myPage2, definidas como classes Page. Você pode especificar myPage1 para a propriedade MemberClass do PageFrame em tempo de design e alterar MemberClass do PageFrame para myPage2 em tempo de execução, seguido de um aumento na propriedade PageCount do PageFrame.

As propriedades MemberClass e MemberClassLibrary têm os seguintes comportamentos adicionais em tempo de design e em tempo de execução:
 - Comportamento em tempo de design Ao definir as propriedades MemberClass e MemberClassLibrary em tempo de design, você é solicitado a destruir classes de membro existentes, incluindo configurações de propriedade; código de método novo, adicionado ou modificado; e objetos adicionados. Quando você cria uma subclasse de um contêiner que especifica a propriedade MemberClass, a subclasse herda as propriedades MemberClass e MemberClassLibrary apropriadas, que você pode modificar. O Visual FoxPro exibe as propriedades MemberClass e MemberClassLibrary na janela Properties como somente leitura. No entanto, você pode definir essas propriedades na janela Properties clicando no botão de reticências (...) para exibir a caixa de diálogo Open, navegando e selecionando a classe de membro e biblioteca de classes que deseja usar. Observação Se você deseja especificar uma classe de membro para o contêiner, deve definir, não apenas uma, mas ambas as propriedades MemberClass e MemberClassLibrary. Se você está definindo a propriedade Count do objeto de membro em um arquivo de programa (.prg) em tempo de design, deve especificar a propriedade Count do objeto de membro depois de definir as propriedades MemberClass e MemberClassLibrary devido a certas dependências. Por exemplo: DEFINE CLASS myPageFrame AS PageFrame MemberClassLibrary = 'MyPages.prg' MemberClass = 'myPage' PageCount = 3 ENDDEFINE Ao usar a função ASELOBJ( ) para definir as propriedades MemberClass e MemberClassLibrary individualmente, o seguinte comportamento ocorre: Se você especificar apenas a propriedade MemberClass ou MemberClassLibrary usando a função ASELOBJ(), o Visual FoxPro não gera um erro, mas desconsidera a propriedade especificada e usa a classe base ao adicionar um novo objeto de membro. Se a propriedade Count do objeto de membro é 0 (ou -1 para objetos Grid), o Visual FoxPro não realiza verificação de erros ao definir MemberClass e MemberClassLibrary , que você pode definir em qualquer ordem. Se a propriedade Count do objeto de membro é maior que 0, o Visual FoxPro realiza verificação de erros quando MemberClass é definido. Portanto, nesta situação, você precisa definir MemberClassLibrary antes de definir MemberClass . Observação Se qualquer propriedade for inválida, o Visual FoxPro gera a mensagem apropriada se a classe ou biblioteca de classes for inválida e define a propriedade Count do objeto de membro de volta para 0. Se tanto MemberClass quanto MemberClassLibrary são válidos, o Visual FoxPro recria todas as classes de membro existentes baseadas na nova classe de membro, e todos os dados de objeto de membro anteriores são perdidos. Cuidado O Visual FoxPro não solicita que você destrua classes de membro existentes, incluindo configurações de propriedade; código de método novo, adicionado ou modificado; e objetos adicionados ao definir MemberClass e MemberClassLibrary no código. Como ao definir a propriedade Count do objeto de membro em um arquivo de programa (.prg) em tempo de design, você deve especificar a propriedade Count do objeto de membro depois de definir as propriedades MemberClass e MemberClassLibrary. Você pode alterar MemberClassLibrary para outra biblioteca de classes que tenha o mesmo MemberClass . Se você aumentar a propriedade Count do objeto de membro, o Visual FoxPro adiciona uma nova classe de membro usando o novo MemberClassLibrary . Embora o designer exiba classes de membro de diferentes bibliotecas de classes, somente o MemberClassLibrary mais recente persiste ao salvar a classe. Portanto, quando você instancia ou abre a classe novamente, todos os objetos de membro são criados do MemberClassLibrary mais recente.
- Comportamento em tempo de execução Alterar MemberClass e MemberClassLibrary afeta somente objetos de membro recém-criados, não objetos de membro existentes no contêiner. Você também pode usar os métodos AddObject e NewObject, que funcionam como de costume, para especificar uma classe diferente. Observação Você deve especificar ambas as propriedades MemberClass e MemberClassLibrary em tempo de execução. Se você especificar apenas MemberClass ou MemberClassLibrary em tempo de execução, o Visual FoxPro não gera um erro; no entanto, ele usa a classe base ao adicionar um novo membro e desconsidera a propriedade especificada. Para determinar de forma confiável a classe de membro usada para instanciar um objeto de membro específico, use as propriedades Class e ClassLibrary do objeto de membro em vez de MemberClass e MemberClassLibrary porque as propriedades posteriores podem mudar em tempo de execução. Observação Um contêiner pode ter objetos de membro derivados de diferentes classes de membro. O Visual FoxPro não suporta a capacidade de especificar uma classe em uma biblioteca de classes vinculada dentro de um aplicativo Visual FoxPro compilado (.app).

# Exemplo

O exemplo a seguir cria um formulário, adiciona um contêiner PageFrame ao formulário, define o contêiner PageFrame como "myPageFrame", define as propriedades MemberClassLibrary e MemberClass para "myPageFrame", define um objeto de membro Page como "myPage" e adiciona código para um botão de comando e eventos.

```foxpro
PUBLIC x
x = CREATEOBJECT("form")
x.ADDOBJECT("pf1","myPageFrame")
x.pf1.Visible = .T.
x.Show()
DEFINE CLASS myPageFrame AS PageFrame
   MemberClassLibrary = 'myPages.PRG'
   MemberClass = 'myPage'
   PageCount = 2
   TabOrientation = 1
ENDDEFINE
DEFINE CLASS myPage AS Page
   ADD OBJECT cmd1 AS commandbutton WITH ;
      Caption = "Hello", FontBold = .T.
   PROCEDURE Init
      THIS.Caption = "Funpage"+TRANSFORM(THIS.Parent.PageCount)
   ENDPROC
   PROCEDURE cmd1.Click
      MESSAGEBOX(this.Caption)
      THIS.Parent.Parent.PageCount = THIS.Parent.Parent.PageCount+1
   ENDPROC
ENDDEFINE
```
