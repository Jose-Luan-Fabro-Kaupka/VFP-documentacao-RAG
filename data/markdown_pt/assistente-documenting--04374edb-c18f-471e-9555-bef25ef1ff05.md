# Assistente Documenting

O assistente Documenting formata e produz arquivos de texto a partir do código em projetos e arquivos de programa. Você pode usar esses arquivos para compartilhar o código ou ler com mais facilidade grandes seções. Por exemplo, o assistente pode produzir arquivos com código-fonte recuado, palavras reservadas e variáveis em maiúsculas, além de um relatório das palavras-chave do programa.

> **Observação:** O assistente não modifica o código; ele apenas cria um arquivo de texto para documentá-lo.

Você pode personalizar seu funcionamento adicionando determinadas diretivas ao código. Para obter mais informações, consulte Personalizando a saída do assistente Documenting.

Para acessar o assistente no menu Tools, escolha Wizards e clique em Documenting.

# Etapa 1 – Escolher o arquivo de origem

Nesta etapa, você pode informar o nome de um arquivo de projeto ou de um arquivo de programa específico. Ao escolher um projeto, o assistente documenta todos os programas nele, incluindo código de eventos de formulários, código de bibliotecas de classes e assim por diante.

# Etapa 2 – Definir capitalização

Nesta etapa, você escolhe como o assistente deve capitalizar palavras-chave e símbolos no arquivo de texto. Palavras-chave são as palavras reservadas da linguagem Visual FoxPro, como MODIFY. Símbolos são as variáveis e os nomes definidos no código. As opções são:
 **UPPERCASE**
Palavras-chave e símbolos são exibidos totalmente em maiúsculas.
**lowercase**
Palavras-chave e símbolos são exibidos totalmente em minúsculas.
**MixedCase**
Palavras-chave são exibidas com a primeira letra de cada palavra em maiúscula, por exemplo, AddObject.
**Match first occurrence**
Símbolos são exibidos conforme a capitalização da primeira ocorrência no arquivo.
**No change**
Palavras-chave e símbolos não são modificados.

# Etapa 3 – Definir recuo

Nesta etapa, você especifica como o assistente recuará as linhas. Ele pode recuar tipos específicos de linha e permite ajustar o número de espaços. Funcionalmente, não há diferença entre espaços e tabulações no código, mas o recuo facilita a leitura.
 **Type of Indent**
Escolha tabulações ou espaços. Para desativar o recuo, escolha No Change. Se escolher Spaces, selecione o número de espaços. Se escolher Tabs, será usada a configuração atual de tabulação do Visual FoxPro.
**Text to indent**
Especifique o tipo de linha a recuar: Comments; estruturas de controle, como loops, blocos IF e DO CASE; e linhas continuadas por ponto e vírgula.

# Etapa 4 – Adicionar cabeçalhos

Nesta etapa, você especifica onde o assistente deve inserir cabeçalhos no arquivo de texto. Cabeçalhos são comentários relevantes ao código que os segue e podem ser colocados no início de arquivos, procedimentos, definições de classe e métodos.

# Etapa 5 – Selecionar relatórios

Nesta etapa, você especifica os tipos de relatório criados pelo assistente. Os relatórios são arquivos de texto.

| Tipo de relatório | Nome do arquivo | Observações |
| --- | --- | --- |
| Action Diagram | project .act | Mostra as relações hierárquicas no código. Se você não estiver trabalhando com a página de código ASCII 1250 e ANSI 1252, consulte a diretiva "*# document ACTIONCHARS". |
| Cross-Reference | Xref.lst | Lista todos os símbolos definidos pelo usuário. |
| File Listing | Files.lst | Lista todos os arquivos do projeto. |
| Source Code Listing | project .lst | Coloca todo o código formatado em um único arquivo. |
| Tree Diagram | Tree.lst | Mostra a árvore de chamadas de procedimentos. |

O assistente também cria automaticamente:
 - Files.dbf, uma tabela com um registro para cada arquivo do projeto.
- Fdxref.dbf, uma tabela com um registro para cada ocorrência de símbolos do usuário no código. Ela permite identificar o tipo de elemento do Visual FoxPro representado por cada símbolo.

> **Observação:** Fdxref.dbf contém um campo Flag para identificar palavras-chave.

| Flag | Descrição |
| --- | --- |
| B | Classe base |
| C | Nome de classe |
| D | PROCEDURE ou FUNCTION definido (não método) |
| F | Chamada de função: myproc( ) ou DO myproc |
| K | Palavra-chave |
| M | Definição de método |
| N | Nome de arquivo |
| O | Objeto |
| P | Propriedade de um objeto |
| R | Referência a símbolo do usuário |
| V | Definição de símbolo do usuário (variável) (PARA, PRIV, PUBL, DIME) |

# Etapa 6 – Concluir

Nesta etapa, você determina o local e a estrutura que conterão o documento do código e se o documento atual substituirá documentos anteriores.

Por padrão, o assistente não substitui arquivos existentes. Especifique Overwrite existing files para substituí-los pelos novos.

Para salvar todos os arquivos em um único diretório, selecione Place files in a single directory. Ao clicar em Finish, o assistente solicitará um diretório a ser criado.

Para usar um novo diretório contendo toda a árvore do projeto, selecione Place files in a new directory tree. Ao clicar em Finish, escolha o diretório no qual será criada uma cópia da árvore de origem, com os novos programas formatados nos diretórios correspondentes.

Ao selecionar Cross-reference keywords, o assistente cria ou acrescenta dados à tabela Fdxref.dbf. Depois, você pode usá-la para criar relatórios das palavras-chave do aplicativo. Um registro é adicionado para cada ocorrência de uma palavra-chave do Visual FoxPro.

O assistente também compara as palavras-chave do código com o primeiro campo, Token, de Fdkeywrd.dbf, localizado na pasta ..\Wizards do diretório raiz do Visual FoxPro. A segunda coluna, Code, contém um identificador que indica como tratar cada palavra-chave.

| Código | Descrição |
| --- | --- |
| I | Aplicar recuo |
| U | Remover recuo |
| R | Redefinir o recuo como 0 (ou 1 em DefineClass) |
| F | Procedimento ou função |
| D | While ou Case: cláusula DO |
| O | Objeto (Spinner, CommandButton) |
| P | Propriedade (Scalemode, DecimalPoints) |
| M | Método (Init, KeyPress) |
| C | ClauseUsed somente como cláusula: não pode iniciar uma instrução |

> **Observação:** Dependendo do tamanho do código, essa opção pode acrescentar muitos registros a Fdxref.dbf. Verifique se há espaço suficiente em disco antes de criar referências cruzadas de palavras-chave.

Ao selecionar Run analyzer, o assistente inicia o Visual FoxPro Code Analyzer, que rastreia dinamicamente a estrutura e os símbolos nos arquivos do aplicativo. O Code Analyzer fornece controles visuais, menu e opções de teclado para navegar pelo arquivo de texto usando a saída do assistente Documenting.
