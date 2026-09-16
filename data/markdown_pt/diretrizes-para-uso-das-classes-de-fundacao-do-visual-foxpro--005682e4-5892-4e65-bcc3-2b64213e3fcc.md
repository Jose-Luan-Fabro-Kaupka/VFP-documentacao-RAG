# Diretrizes para uso das classes de fundação do Visual FoxPro

As bibliotecas de classes visuais (.vcx) localizadas no diretório ...\FFC do Visual FoxPro contêm diversas classes de fundação que aprimoram aplicativos com pouca ou nenhuma programação. Você pode distribuí-las livremente com seus aplicativos.

É possível explorar essas classes na Component Gallery, que oferece uma forma rápida de conhecer as propriedades, eventos e métodos de cada uma. Para obter mais informações, consulte Uso da Component Gallery.

Você também pode abrir uma classe no Class Designer ou Class Browser para examinar sua estrutura e seu código. Essa é uma excelente maneira de aprender como ela funciona e obter ideias sobre programação no Visual FoxPro.

As diretrizes a seguir explicam como adicionar classes de fundação do Visual FoxPro aos aplicativos.

# Tipos de classe

Antes de adicionar uma classe de fundação ao aplicativo, é necessário conhecer sua classe base do Visual FoxPro.

> **Dica:** Na Component Gallery, clique com o botão direito na classe, escolha Properties e abra a guia Class Item. O nome da classe base aparece na caixa Class name.

Algumas classes de fundação só podem ser usadas como objetos visuais em formulários; outras são não visuais e podem ser executadas por programação sem serem colocadas em um formulário. Para determinar como uma classe pode ser usada, consulte Classes de fundação do Visual FoxPro de A a Z, cujos tópicos indicam a classe base de cada uma.

A tabela lista as classes base e como podem ser adicionadas aos aplicativos.

| Categoria A – classes base que podem ser soltas em um formulário | Categoria B – classes base que podem ser soltas em um formulário ou executadas por programação | Categoria C – classes base que só podem ser executadas por programação |
| --- | --- | --- |
| Checkbox | Custom | Form |
| Combobox | Container | Formset |
| Commandbutton | Timer | Toolbar |
| Commandgroup | ProjectHook | |
| Editbox | | |
| Grid | | |
| Hyperlink | | |
| Image | | |
| Label | | |
| Line | | |
| Listbox | | |
| OLE Control | | |
| Optionbutton | | |
| Optiongroup | | |
| Shape | | |
| Spinner | | |
| Textbox | | |

# Adição de classes de fundação a formulários

Na maioria das vezes, você adicionará classes de fundação a formulários. Elas podem ser arrastadas da Component Gallery, Class Browser, Project Manager e barra de ferramentas Form Controls.

> **Observação:** Selecione uma classe adicionada ao formulário e escolha Class Browser no menu Tools para exibir mais informações.

Component Gallery: para classes com bases das categorias A e B, arraste a classe e solte-a no formulário. Você também pode clicar nela com o botão direito e escolher Add to Form.

Algumas classes têm builders associados, iniciados automaticamente para solicitar informações necessárias.

Class Browser: arraste classes das categorias A e B usando o ícone no canto superior esquerdo. Selecione a classe, clique no ícone e arraste-o até a posição desejada no formulário.

Classes arrastadas do Class Browser não iniciam o builder associado. Depois de soltá-las, selecione a classe no formulário, clique com o botão direito e escolha Builder.

Project Manager: classes das categorias A e B também podem ser arrastadas para um formulário. O builder não é iniciado automaticamente; para iniciá-lo depois, selecione a classe, clique com o botão direito e escolha Builder.

Barra Form Controls: classes das categorias A e B adicionadas a essa barra podem ser inseridas em um formulário.

Se Builder Lock estiver desativado, uma classe solta da barra Form Controls poderá iniciar o builder associado. Se estiver ativado, adicione a classe, selecione-a, clique com o botão direito e escolha Builder.

### Adição de classes de fundação a projetos

Quando um formulário com classes de fundação é adicionado a um projeto, o Project Manager inclui automaticamente as bibliotecas de classes visuais correspondentes. Em outros casos, pode ser necessário adicioná-las manualmente. Por exemplo, uma classe da categoria C executada pelo aplicativo precisa fazer parte do projeto.

Você pode adicionar classes pela Component Gallery, arrastando a biblioteca .vcx do Windows Explorer ou usando o botão Add do Project Manager.

# Adição de classes pela Component Gallery

Arraste uma classe da Component Gallery para o projeto ou clique nela com o botão direito e escolha Add to Project. A caixa Add Class to Project oferece estas opções:
 **Add class to project**
Adiciona a classe e sua biblioteca .vcx ao projeto. Isso já ocorre automaticamente para classes soltas em formulários (categorias A e B). Escolha esta opção para classes das categorias B e C chamadas por programação.
**Create a new class from selected class**
Cria uma subclasse da classe selecionada, permitindo aprimorar a funcionalidade original, geralmente com código adicional.
**Create a new form from selected class**
Use para classes cuja base é Form, como as de _dialogs.vcx. Cria um formulário baseado na classe e permite aprimorá-lo.

### Adição de classes pelo Windows Explorer

Arraste para o Project Manager a biblioteca visual .vcx que contém a classe. Ela será incluída no item Class Libraries.

### Adição de classes pelo Project Manager

Selecione a guia Classes, clique em Add e escolha na pasta \Ffc\ a biblioteca que contém a classe desejada.

# Incorporação de classes ao aplicativo

Em muitas situações, classes de fundação não exigem programação adicional. Algumas classes não visuais das categorias B e C, porém, exigem código complementar.

### Classes de fundação não visuais

Classes não visuais costumam ser baseadas em Custom, da categoria B, e executar tarefas como consultar o Registro do Windows, controlar configurações de ambiente, gerenciar erros e usar Automation com outros aplicativos, por exemplo, para mala direta no Microsoft Word.

Você pode soltá-las em um formulário, mas talvez precise de trabalho adicional. Em alguns casos, um builder é iniciado ao arrastar a classe.

O exemplo a seguir mostra o código normalmente necessário:
 - Arraste a classe File Version da Component Gallery (pasta Foundation Classes\Utilities) para um formulário.
- Adicione um botão de comando e, no evento Click, use: WITH THISFORM._FILEVERSION1 .cFileName = HOME( )+ 'VFP8.EXE' .GetVersion( ) .DisplayVersion( ) ENDWITH
- Execute o formulário e clique no botão.

Você também pode incorporar uma classe não visual sem colocá-la em um formulário, desde que ela esteja incluída no projeto usado para criar o aplicativo:

```foxpro
LOCAL oFileVersion
oFileVersion = NewObject('_fileversion', '_utilities.vcx')
WITH oFileVersion
   .cFileName = HOME()+ 'VFP8.EXE'
   .GetVersion()
   .DisplayVersion()
ENDWITH
```

> **Observação:** O exemplo pressupõe que o código pode localizar _utilities.vcx ou um arquivo .app criado contendo _utilities.vcx.

Ao usar uma classe não visual, determine como e quando ela será usada para definir corretamente seu escopo. Se apenas um formulário a usar, arraste-a para ele. Se vários formulários ou o aplicativo inteiro a usarem, atribua-lhe escopo global para mantê-la acessível e, possivelmente, melhorar o desempenho.

# Adição de classes de fundação visuais a aplicativos

Você pode adicionar por programação classes visuais, inclusive as baseadas em Form. Por exemplo, o código a seguir exibe uma caixa About:

```foxpro
LOCAL oAbout
oAbout = NewObject('_aboutbox','_dialogs.vcx')
oAbout.Show()
```

Para personalizar a caixa About em cada aplicativo, crie uma subclasse da classe de fundação About Dialog Box:
 - Abra o projeto do aplicativo.
- No menu Tools, clique em Component Gallery.
- Expanda Visual FoxPro Catalog, Foundation Classes e clique em Dialogs.
- Arraste a classe Aboutbox para o Project Manager.
- Na caixa Add Class to Project, clique em Create new form from selected class.
- Na caixa Save As, informe um nome. Depois de salvar, o Form Designer exibirá o novo formulário.
- Na janela Properties, altere Caption para definir o título. Salve e feche o formulário.
- Adicione código como DO FORM FormName ao procedimento que executará o formulário; ou arraste a classe de botão Run Form da pasta Foundation Classes\Buttons. Um builder permitirá indicar o formulário a executar.

Se você usa o Visual FoxPro Application Framework, o Application Builder controla automaticamente a adição de formulários (.scx e classes Form .vcx). O novo Application Wizard e o item New Application da Component Gallery instalam esse framework nos projetos criados. O Application Builder interage com ele para especificar como e onde o formulário será iniciado.

Com o framework criado pelo Application Wizard, Application Builder e Component Gallery, você dispõe de um conjunto abrangente de ferramentas para criar aplicativos inteiros com pouca codificação manual.

# Convenções de nomenclatura de classes

As classes de fundação do Visual FoxPro e suas propriedades e métodos usam as convenções a seguir.

### Classes e bibliotecas de classes

A maioria das classes de fundação deriva de classes da biblioteca visual _base.vcx, localizada em \Ffc\. As convenções refletem a classe base. Por exemplo, uma subclasse de Custom chama-se _Custom em _base.vcx. Todas as classes dessa biblioteca usam sublinhado (_) como prefixo.

Algumas bibliotecas não contêm subclasses de _base.vcx porque suas classes são compartilhadas com outros componentes, como assistentes e builders. Essas bibliotecas não têm sublinhado inicial, como Registry.vcx.

### Métodos e propriedades

Métodos geralmente recebem nomes de ações, como RunForm; quando o nome tem várias palavras, a capitalização as distingue. Propriedades costumam ter uma letra inicial que indica o tipo de dados. cFileName, por exemplo, indica tipo caractere. Seus valores padrão também correspondem ao tipo: uma propriedade lógica pode iniciar com .F. e uma numérica com 0.

Propriedades de classes fornecidas em versões anteriores não seguem rigorosamente essas convenções e mantêm os nomes antigos para evitar incompatibilidade com código existente.

# Aprimoramento ou modificação das classes de fundação FoxPro

Você pode aprimorar ou modificar as classes de fundação para atender ao aplicativo. Entretanto, não é recomendável modificar diretamente essas classes, pois elas podem receber atualizações de funcionalidade.

### Criação de subclasses da classe de fundação

Como o código-fonte é fornecido, você pode criar subclasses para substituir ou ampliar propriedades e métodos. Isso é comum quando o comportamento varia entre aplicativos: um pode usar a classe diretamente e outro usar uma subclasse.

### Atualização de _base.vcx

Para aplicar alterações globais às classes de fundação, você pode modificar _base.vcx. Como elas derivam dessa biblioteca, suas alterações são propagadas automaticamente. _base.vcx fornece um conjunto comum de métodos e propriedades e pode ser alterada quando isso acrescentar o comportamento desejado, ao contrário das classes de fundação, que não devem ser modificadas diretamente.

Em vez de alterar _base.vcx, você pode redefinir suas classes para herdarem de suas próprias classes base personalizadas. Se já houver uma biblioteca personalizada derivada das classes base do Visual FoxPro, redefina as classes de _base.vcx para herdarem dela; assim, componentes que usam as classes _base também herdarão suas classes. Use o Class Browser para redefinir a classe pai.

> **Observação:** Ao redefinir classes para herdarem de suas classes base, adicione chamadas DODEFAULT() nos locais apropriados se desejar executar o código de método da classe pai.

Se substituir toda a biblioteca _base.vcx, mantenha o mesmo conjunto de nomes de classe; caso contrário, as classes de fundação terão vínculos ausentes.
