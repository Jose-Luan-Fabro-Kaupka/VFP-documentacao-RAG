# Propriedade DEClass

Especifica o nome da classe DataEnvironment a ser usada ao adicionar um ambiente de dados a um formulário. Leitura/gravação em tempo de design e somente leitura em tempo de execução.

Em tempo de design, DEClass permite especificar uma classe DataEnvironment da biblioteca de classes na propriedade DEClassLibrary.

```foxpro
Form.DEClass [= cClassName]
```

# Valor de retorno
 **cClassName**
Tipo de dados Character. O parâmetro cClassName especifica um dos seguintes: Nome de uma classe programática em um arquivo de programa (.prg) Nome de uma classe não visual em um arquivo de biblioteca de classes visual (.vcx)

# Observações

Aplica-se a: Form Object

O Visual FoxPro oferece suporte a DEClass e DEClassLibrary para arquivos de formulário (.scx), biblioteca de classes visual (.vcx) e programa (.prg), mas não para objetos FormSet nem no Report Designer.

O Visual FoxPro instancia um objeto DataEnvironment a partir de DEClass e sua propriedade associada DEClassLibrary nas seguintes condições:
 - DEClass especifica uma classe DataEnvironment em tempo de design na janela Properties do formulário.
- DEClass especifica uma classe DataEnvironment ao criar o formulário programaticamente.

Quando o formulário é criado, o Visual FoxPro usa a classe DataEnvironment especificada para criar o objeto DataEnvironment. Se você especificar um valor para a propriedade DEClassLibrary, mas não para DEClass, ou se a classe DataEnvironment for do tipo incorreto ou não existir na biblioteca de classes especificada, o Visual FoxPro gera a mensagem apropriada.

Você pode definir DEClass e DEClassLibrary usando a janela Properties no Form Designer, em uma classe Form ou a partir de uma definição de classe em um arquivo .prg. O Visual FoxPro exibe DEClass e DEClassLibrary na janela Properties como somente leitura. No entanto, clicar no botão de reticências (...) na janela Properties exibe a caixa de diálogo Open para que você possa selecionar o arquivo .prg desejado ou, se suportado, o arquivo .vcx.

Você também pode usar a função ASELOBJ( ) para armazenar referências de objeto em uma matriz e definir propriedades de objeto individualmente. No entanto, se você definir apenas a propriedade DEClass ou a propriedade DEClassLibrary, o Visual FoxPro desconsidera as configurações dessas propriedades e usa a classe DataEnvironment padrão. Você deve definir ambas as propriedades.

> **Observação:** Ao definir as propriedades DEClass e DEClassLibrary usando código ou a função ASELOBJ( ), você deve definir a propriedade DEClassLibrary antes de definir a propriedade DEClass.

Quando você abre o Data Environment Designer clicando com o botão direito do mouse no formulário, ocorre o seguinte:
 - Classe DataEnvironment contendo objetos Cursor Se o cursor ou os cursores contidos referenciam uma tabela ou visualização remota existente, tabelas e visualizações colocadas na superfície do Data Environment Designer são somente leitura. Você pode arrastar e soltar campos ou tabelas na superfície do Form Designer se as seguintes propriedades estiverem definidas com os requisitos especificados: CursorSource (Obrigatório) Nome e caminho da tabela se for uma tabela livre; somente o nome da tabela se for uma tabela de contêiner de banco de dados (DBC). Database (Opcional) Nome e caminho do DBC são preenchidos automaticamente se for uma tabela ou visualização DBC. Alias (Opcional) Alias atribuído à tabela se for diferente do nome da tabela. Caso contrário, o alias assume por padrão o nome CursorSource. Se a classe DataEnvironment contém um objeto Cursor, mas o cursor não contém uma referência válida a uma tabela ou visualização, o Data Environment Designer não abre. O Visual FoxPro carrega o ambiente de dados após gerar a mensagem apropriada. Se a classe DataEnvironment contém vários objetos Cursor, somente os cursores que contêm referências válidas a tabelas e/ou visualizações são colocados na superfície do Data Environment Designer. Cursores que não contêm referências válidas a tabelas ou visualizações são desconsiderados. Se o cursor referencia um DBC, mas o cursor não referencia uma tabela ou visualização válida no DBC, o Visual FoxPro carrega o ambiente de dados após exibir a mensagem apropriada. Se a classe DataEnvironment não contém um objeto Cursor, o Data Environment Designer não abre e o Visual FoxPro gera uma mensagem apropriada. Quando você arrasta um arquivo de tabela (.dbf) de uma pasta para um formulário enquanto um ambiente de dados de classe que não seja DataEnvironment está aberto, o Visual FoxPro adiciona automaticamente a tabela ao ambiente de dados. No entanto, se o ambiente de dados aberto é baseado em uma classe DataEnvironment, o ambiente de dados é somente leitura e o Visual FoxPro não adiciona o arquivo .dbf ao ambiente de dados.
- Classe DataEnvironment contendo objetos CursorAdapter Se a classe DataEnvironment contém um objeto CursorAdapter, o CursorAdapter deve atender aos seguintes requisitos para aparecer na superfície do Data Environment Designer: A propriedade CursorSchema do CursorAdapter é especificada e definida com um valor válido. A propriedade Alias do CursorAdapter é especificada. Observação Se as condições anteriores forem atendidas, os adaptadores de cursor aparecem na superfície do Data Environment Designer como somente leitura. Você pode arrastar e soltar tabelas e campos no formulário. As propriedades, eventos ou métodos do ambiente de dados e de quaisquer objetos CursorAdapter contidos são somente leitura. O Data Environment Designer não abre se qualquer uma das seguintes condições for verdadeira: A classe DataEnvironment contém um objeto CursorAdapter, mas o adaptador de cursor não contém dados válidos na propriedade CursorSchema. O objeto CursorAdapter não é instanciado por qualquer motivo.

Para modificar a classe DataEnvironment, você deve fechar o Form Designer, liberar quaisquer classes em uso, modificar e recompilar a classe DataEnvironment no arquivo especificado pela propriedade DEClassLibrary e retornar ao Form Designer.

Quando as propriedades DEClass e DEClassLibrary estão definidas, executar o formulário cria e carrega o ambiente de dados a partir da classe DataEnvironment especificada. Para definir DEClass e DEClassLibrary em tempo de execução, você deve usar código.

Se você tentar converter um formulário em um conjunto de formulários em tempo de design quando o Form Designer está aberto e as propriedades DEClass e DEClassLibrary estão especificadas para o formulário, o Visual FoxPro gera a mensagem apropriada. Se um conjunto de formulários está aberto no Form Designer e você tenta adicionar um formulário que especifica as propriedades DEClass e DEClassLibrary ao conjunto de formulários em tempo de design, o Visual FoxPro gera a mensagem apropriada e torna as propriedades DEClass e DEClassLibrary indisponíveis. Se você tentar adicionar um formulário que especifica as propriedades DEClass e DEClassLibrary ao conjunto de formulários em tempo de execução, o Visual FoxPro desconsidera DEClass e DEClassLibrary e não carrega a classe de ambiente de dados especificada.

DEClass e DEClassLibrary oferecem suporte ao escopo Public, Hidden e Protected.

DEClass e DEClassLibrary não oferecem suporte aos métodos Access e Assign.

Em um formulário subclassificado, DEClass e DEClassLibrary são herdados normalmente.

# Exemplo

O exemplo a seguir cria uma classe Form e define as propriedades DEClassLibrary e DEClass para especificar uma classe DataEnvironment externa e uma biblioteca de classes.

```foxpro
DEFINE CLASS form1 as Form
   DEClassLibrary="MyProgram.prg"
   DEClass="MyDE"
ENDDEFINE
```
