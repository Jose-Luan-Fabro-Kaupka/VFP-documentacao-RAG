# Variável de sistema _MENUDESIGNER

Especifica um aplicativo externo para criar menus.

```foxpro
_MENUDESIGNER = cProgramName
```

#### Parâmetros
 **cProgramName**
Especifica o nome do arquivo do designer de menus externo. Se o aplicativo estiver em um diretório diferente do diretório padrão atual, inclua o caminho com o nome do aplicativo. Você também pode especificar o aplicativo no arquivo de configuração Config.fpw do Visual FoxPro incluindo uma linha com esta sintaxe: _MENUDESIGNER = cProgramName. Se _MENUDESIGNER contiver a cadeia de caracteres vazia padrão, o Designer de Menus do Visual FoxPro será aberto.

# Observações

O aplicativo especificado em _MENUDESIGNER é executado durante uma sessão interativa de tempo de design do Visual FoxPro. O aplicativo é executado quando você escolhe Menu na caixa de diálogo Novo, um novo Menu no Gerenciador de Projetos, executa CREATE MENU, MODIFY MENU ou EDITSOURCE( ) na janela Comando ou em um programa, ou chama o método Modify de um objeto de arquivo acessado por meio de um objeto ProjectHook.

> **Observação:** Quando um designer de menus externo é executado, os itens de menu normalmente associados aos designers do Visual FoxPro não ficam disponíveis.

Um designer de menus externo deve incluir uma instrução PARAMETERS para aceitar três parâmetros passados pelo Visual FoxPro ao aplicativo.

| Parâmetro | Descrição |
| --- | --- |
| cFileName | Um parâmetro do tipo caractere que contém o nome do arquivo do menu a ser aberto no aplicativo de design de menus. Se CREATE MENU menuname for emitido para executar o designer de menus, cFileName conterá menuname com um caminho totalmente qualificado para o local do arquivo. Se CREATE MENU for emitido sem menuname, a caixa de diálogo Novo Menu será exibida. Depois que o usuário escolher uma opção Menu ou Menu de Atalho, o aplicativo de design de menus será executado e cFileName conterá um nome de menu gerado internamente, Menu1, Menu2 e assim por diante. O nome do menu é incrementado sempre que CREATE MENU é emitido sem menuname. Se CREATE MENU ? for emitido para executar o aplicativo de design de menus, uma caixa de diálogo será exibida para que o usuário especifique um nome de menu. Quando o usuário inserir um nome de menu e escolher Salvar, a caixa de diálogo Novo Menu será exibida. Depois que o usuário escolher uma opção Menu ou Menu de Atalho, cFileName conterá o nome de menu do usuário com um caminho totalmente qualificado para o local do arquivo. |
| nCommandType | Um parâmetro do tipo numérico que indica como o aplicativo de design de menus foi chamado. Descrição de nCommandType: 1 A opção Menu foi escolhida na caixa de diálogo Novo Menu. 2 A opção Atalho foi escolhida na caixa de diálogo Novo Menu. 3 O comando MODIFY MENU foi usado para chamar o aplicativo de design de menus. O parâmetro cFileName contém o nome do menu especificado em MODIFY MENU com um caminho totalmente qualificado para o local do arquivo. |
| aDetail | Uma matriz com informações adicionais sobre o comando que chamou o aplicativo de design de menus. Uma matriz será criada somente se o aplicativo de design de menus for chamado ao escolher um novo Menu no Gerenciador de Projetos ou ao emitir CREATE MENU ou MODIFY MENU com as cláusulas opcionais NOWAIT, SAVE, WINDOW ou IN. Quando nenhuma matriz é criada, o terceiro parâmetro é uma variável de memória que contém o valor lógico falso (.F.). Quando o aplicativo de design de menus é chamado ao escolher um novo Menu no Gerenciador de Projetos, uma matriz de dois elementos é criada. O primeiro elemento da matriz contém "PROJECT." O segundo elemento contém o nome do projeto com um caminho totalmente qualificado para o local do arquivo. Quando o aplicativo de design de menus é chamado emitindo CREATE MENU ou MODIFY MENU com as cláusulas opcionais NOWAIT, SAVE, WINDOW ou IN, a matriz contém uma linha para cada cláusula. Cada linha da matriz possui dois elementos. A tabela a seguir descreve o conteúdo de cada um dos dois elementos. 1º elemento 2º elemento NOWAIT Contém um valor lógico verdadeiro (.T.). SAVE Contém um valor lógico verdadeiro (.T.). WINDOW Contém o nome da janela especificada na cláusula WINDOW. IN Contém SCREEN ou o nome da janela especificada. |

O designer de menus externo deve retornar um valor lógico verdadeiro (.T.) se o aplicativo criar com êxito o menu do usuário. Se um valor lógico falso (.F.) for retornado, o Designer de Menus do Visual FoxPro será aberto.
