# Aprimoramentos do Ambiente de Desenvolvimento Interativo (IDE)

Para fornecer um ambiente de desenvolvimento mais integrado para seus projetos e aplicativos, o Visual FoxPro contém a seguinte funcionalidade aprimorada para a IDE.

# Comandos adicionais do menu de atalho do Project Manager

Quando acoplado, a janela Project Manager contém os seguintes comandos adicionais do menu de atalho disponíveis no menu Project:
 - Close Fecha o Project Manager.
- Add Project to Source Control Creates a new source control project based on the current project. Available only when a source code control provider is installed and specified on the Projects tab in the Options dialog box.
- Errors Displays the error (.err) file after running a build.
- Refresh Refreshes the contents of the Project Manager.
- Clean Up Project Removes deleted records from the Project Manager (.PJX) file.

# Modificando uma biblioteca de classes no Project Manager

Quando você seleciona um arquivo de biblioteca de classes (.vcx) no Project Manager, agora pode abrir e navegar em bibliotecas de classes clicando no botão Modify. A biblioteca de classes abre no Class Browser. Para obter mais informações, consulte Como: abrir bibliotecas de classes.

# Definir fonte do Project Manager

Você pode alterar as configurações de fonte do texto para a janela Project Manager. Clique com o botão direito na janela Project Manager (fora da janela de hierarquia em árvore) e escolha Font.

# Gerando logs de mensagens durante build e compilação de projeto

Quando você faz build de um projeto, aplicativo ou biblioteca de vínculo dinâmico, o Visual FoxPro gera automaticamente um arquivo de erro (.err) que inclui quaisquer mensagens de erro, se existirem, quando o processo de build é concluído. Quando você seleciona a caixa de seleção Display Errors na caixa de diálogo Build Options, o Visual FoxPro exibe o arquivo .err quando o build é concluído. Selecionar a caixa de seleção Recompile All Files inclui erros de compilação no arquivo .err. Mensagens de status de build geralmente aparecem na barra de status. No entanto, em versões anteriores, se o processo de build fosse interrompido, o Visual FoxPro não gravava o arquivo .err no disco.

Na versão atual, o Visual FoxPro grava mensagens de status de build e de erro no arquivo .err conforme ocorrem durante o processo de build. Se o processo de build for interrompido, você pode abrir o arquivo .err para revisar os erros.

> **Observação:** Se nenhum erro ocorrer durante o build, o arquivo .err é excluído.

Se a janela Debug Output estiver aberta, mensagens de status de build e de erro aparecem na janela. Você pode salvar mensagens da janela Debug Output em um arquivo.

Para obter mais informações, consulte Como: exibir e salvar mensagens de build.

# Aprimoramentos da janela Properties
 - Suporte em tempo de design para inserir valores de propriedade maiores que 255 caracteres e caracteres estendidos, como CHR(13) (carriage return) e CHR(10) (linefeed), foi adicionado a arquivos de biblioteca de classes visual (.vcx) e formulário (.scx). Agora você pode inserir até 8k caracteres de comprimento. Observação O suporte a valores de propriedade estendidos está disponível apenas pela janela Properties (caixa de diálogo Zoom) para propriedades personalizadas especificadas pelo usuário, bem como certas nativas como CursorSchema e Value. Para propriedades não suportadas, você ainda pode especificar valores com mais de 255 caracteres ou que contenham carriage returns e linefeeds atribuindo-os em código, como durante o Init Event do objeto . A caixa de diálogo Zoom e a caixa de diálogo Expression Builder foram atualizadas para suportar isso. A janela Properties inclui um botão Zoom ( Z ) que aparece ao lado da caixa de configurações de propriedade para propriedades apropriadas. Cuidado Valores de propriedade que excedem 255 caracteres ou incluem caracteres de carriage return e/ou linefeed são armazenados em um novo formato dentro do arquivo .vcx ou .scx. Se você tentar modificar essas classes em uma versão anterior, ocorre um erro. Este recurso é particularmente útil para definir a propriedade CursorSchema do CursorAdapter para qualquer expressão de esquema quando os esquemas podem exceder 255 caracteres.
- The Properties window font can now be specified by the new Font shortcut menu option. This new menu replaces the Small, Medium and Large font menu items used in prior versions. This font is also used in the description pane, and object and property value dropdowns. Note Bold and italic font styles are reserved for non-default property values and read-only properties, respectively. If a bold or italic font style is chosen, then the Properties window inverts the displayed behavior. For example, if one chooses an italic font style, read-only properties appear in normal font style and all others in italic.
- Colors can be specified for certain types of properties by right clicking on the Properties Window and selecting following menu items: Non-Default Properties Color Sets color for properties whose values have changed from default setting (same properties that are displayed when the Non-Default Properties Only menu item is selected). Custom Properties Color Sets color for custom properties. Instance Properties Color Sets color for custom properties that have been added to the current class instance (same properties that appear in bold in the Edit Property/Method Dialog Box ). Note If a conflict exists between color settings, the Instance setting takes priority followed by the Non-Default one.

Para obter mais informações, consulte Caixa de diálogo Zoom <property>, Caixa de diálogo Expression Builder, Propriedade CursorSchema e Janela Properties (Visual FoxPro).

# Extensibilidade MemberData

A arquitetura de extensibilidade MemberData permite fornecer metadados para membros de classe (propriedades, métodos e eventos). Com MemberData, você pode especificar um editor de propriedades personalizado, exibir uma propriedade na guia Favorites ou alterar a capitalização na janela Properties (Visual FoxPro).

Para obter mais informações, consulte Extensibilidade MemberData.

# Definindo valores padrão para novas propriedades

Ao adicionar uma nova propriedade a uma classe, você pode especificar um valor inicial diferente do padrão na caixa de diálogo New Property. Subclasses herdam esses valores padrão, a menos que você redefina os valores padrão para a classe pai. Em versões anteriores, você tinha que definir o valor padrão para a nova propriedade selecionando a propriedade na janela Properties e definindo o valor padrão.

Para obter mais informações, consulte Como: adicionar propriedades a classes.

# Opções de ordenação da Document View

Agora você pode ordenar itens na janela Document View por nome para formulários e bibliotecas de classes visuais.

Consulte Janela Document View para obter mais informações sobre ordenação de itens na janela Document View.

# Compilando código em segundo plano

O Visual FoxPro executa compilação em segundo plano quando a coloração de sintaxe está ativada na janela Command e nos editores do Visual FoxPro para arquivos de programa (.prg), métodos, stored procedures e memos. A caixa Expression na caixa de diálogo Expression Builder também inclui suporte para compilação em segundo plano e coloração de sintaxe quando ativada.

Quando a linha única e atual de código que você está digitando contém sintaxe inválida, o Visual FoxPro exibe a linha de código com o estilo de formatação selecionado na guia Editor da caixa de diálogo Options.

> **Observação:** A coloração de sintaxe deve estar ativada para que a compilação em segundo plano funcione. A compilação em segundo plano não detecta sintaxe inválida em várias linhas de código, incluindo aquelas que contêm caracteres de continuação.

Para obter mais informações, consulte Como: exibir e imprimir código-fonte em cores.

# Suporte à Área de transferência em Rich Text Format (RTF)

O Visual FoxPro agora suporta copiar em RTF (Rich Text Format) para a área de transferência. O Visual FoxPro preserva os atributos de estilo (negrito, itálico e sublinhado) e cor.

RTF é suportado apenas nos editores FoxPro que permitem coloração de sintaxe, como a janela Command e janelas de edição abertas com o Comando MODIFY COMMAND. O formato de área de transferência RTF é suportado apenas quando a coloração de sintaxe está habilitada, como na Caixa de diálogo Edit Properties. Você pode desabilitar o formato de área de transferência RTF com a Propriedade _VFP EditorOptions.

A Variável de sistema _CLIPTEXT não suporta RTF.

# Melhorias na caixa de diálogo Find

As seguintes melhorias foram feitas no suporte Find:
 - Se uma palavra estiver selecionada em um editor do Visual FoxPro, a Caixa de diálogo Find (Visual FoxPro), quando aberta, agora exibe a palavra na caixa suspensa Look For. Se Find ainda não foi usado para uma instância em execução do Visual FoxPro, uma palavra posicionada sob o ponteiro de inserção aparecerá na suspensa Look For. Se várias palavras estiverem selecionadas, apenas a primeira palavra aparece na suspensa (use copiar e colar para inserir várias palavras).
- When a Browse window is open and you search for a word with the Find dialog box, you can search for the word again (Find Again) after the Find dialog box is closed by pressing the F3 key.
- You can now use Find to search for content in Name column of the Watch and Locals debug windows (see Debugger Window ). When searching object members, Find searches in these debug windows are limited to nodes that have been expanded and one level below.

# Visualizar constantes na janela Trace

Constantes (valores #DEFINE) podem ser visualizadas na janela Trace quando você passa o mouse sobre elas.

> **Observação:** O Visual FoxPro avalia constantes como expressões na janela Trace e pode ter dificuldade em interpretar um #DEFINE específico quando você passa o mouse sobre ele. Consequentemente, se houver várias expressões em uma linha, todas são exibidas na dica de valor.

# Imprimindo texto selecionado em janelas do editor

Você pode imprimir texto selecionado de janelas do editor do Visual FoxPro. Quando você tem texto selecionado na janela do editor, a opção Selection na caixa de diálogo Print está disponível e selecionada.

> **Observação:** Se uma linha parcial estiver selecionada, a linha inteira é impressa.

Para obter mais informações, consulte Caixa de diálogo Print (Visual FoxPro).

# Melhorias de fonte do sistema

Para melhorar a legibilidade em monitores de alta resolução, caixas de diálogo Error e a Caixa de diálogo Zoom <property> na janela Properties agora usam a fonte de texto Windows Message Box.

No Windows XP, a fonte de texto Windows Message Box é definida abrindo Display no Painel de controle e clicando em Advanced na guia Appearance.

# IntelliSense salva configurações entre sessões de usuário

O Visual FoxPro agora salva configurações do IntelliSense, como ativar o IntelliSense, entre sessões de usuário. Essas configurações são controladas pela propriedade _VFP EditorOptions. Além disso, as configurações na propriedade _VFP EditorOptions são salvas no arquivo de recursos FoxUser.dbf. Para obter mais informações, consulte Propriedade EditorOptions.

# IntelliSense na janela do editor de campo Memo

O Visual FoxPro inclui suporte IntelliSense em janelas do editor de campo Memo quando a coloração de sintaxe está ativada.

# IntelliSense disponível para aplicativos em tempo de execução

Recursos selecionados do IntelliSense estão disponíveis em tempo de execução em aplicativos distribuídos do Visual FoxPro 9.0. Para usar IntelliSense em tempo de execução, você precisa definir as variáveis _FOXCODE e _CODESENSE e a Propriedade EditorOptions.

> **Observação:** Com aplicativos em tempo de execução, a coloração de sintaxe não precisa estar ativada para que um editor suporte IntelliSense.

Para obter mais informações, consulte Suporte IntelliSense no Visual FoxPro, Variável de sistema _FOXCODE, Variável de sistema _CODESENSE e Propriedade EditorOptions.

# Suporte IntelliSense nos comandos WITH ... ENDWITH e FOR EACH ... ENDFOR

O Visual FoxPro agora suporta IntelliSense dentro do Comando WITH ... ENDWITH e do Comando FOR EACH ... ENDFOR.

`WITH ObjectName [AS Type [OF ClassLibrary]]`

`Commands`

`ENDWITH`

`FOR EACH ObjectName [AS Type [OF ClassLibrary]] IN Group`

`Commands`

`[EXIT]`

`[LOOP]`

`ENDFOR`

O parâmetro Type pode ser qualquer tipo válido, incluindo tipos de dados, tipos de classe ou ProgID. Se o nome da classe não puder ser encontrado, o Visual FoxPro desconsidera Type e não exibe IntelliSense para ele.

> **Observação:** A referência de tipo não afeta a funcionalidade do aplicativo em tempo de execução. A referência de tipo é usada apenas para IntelliSense.

A expressão ObjectName pode referir-se a uma variável de memória ou a um array.

O parâmetro ClassLibrary deve estar em uma lista de caminhos visível ao Visual FoxPro. Você deve especificar uma biblioteca de classes válida; referências a objetos existentes não são válidas. Se o Visual FoxPro não encontrar a biblioteca de classes especificada, o IntelliSense não é exibido.

Tipos expressos como ProgIDs e bibliotecas de classes não requerem aspas ("") para os envolver, a menos que seus nomes contenham espaços.

Quando um usuário digita a palavra-chave AS, o IntelliSense exibe uma lista de tipos registrados na tabela FoxCode.dbf com Type "T". Se você especificou um tipo válido, digitar um ponto dentro de um comando WITH ... ENDWITH ou FOR EACH ... ENDFOR exibe IntelliSense para essa referência de objeto.

O Visual FoxPro suporta IntelliSense para comandos WITH ... ENDWITH e FOR EACH ... ENDFOR aninhados. O seguinte é um exemplo de comandos WITH ... ENDWITH aninhados em uma classe definida em um arquivo de programa (.prg) chamado Program1.prg. Para usar, cole este código em um novo programa chamado Program1.prg, salve-o e então digite um ponto (.) dentro do bloco WITH ... ENDWITH.

```foxpro
DEFINE CLASS f1 AS form
MyVar1 = 123
ADD OBJECT t1 AS mytext
PROCEDURE Init
  WITH THIS AS f1 OF program1.prg
    WITH .t1 AS mytext OF program1.prg
    ENDWITH
  ENDWITH
ENDPROC
ENDDEFINE
DEFINE CLASS mytext as textbox
MyVar2 = 123
ENDDEFINE
```

O IntelliSense fornece funcionalidade limitada de List Values para propriedades selecionadas que começam com "T" ou "F" dentro de um comando WITH ... ENDWITH ou FOR EACH ... ENDFOR. Isso é feito para evitar possíveis conflitos com os valores de propriedade comuns True (.T.) e False (.F.). Se você apenas digitar ".T" ou ".F" e pressionar Enter, a palavra selecionada na lista suspensa List Value não se expande. Você precisa digitar pelo menos duas letras para o IntelliSense inserir a palavra selecionada.
