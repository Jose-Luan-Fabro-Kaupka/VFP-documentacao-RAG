# Comando SET LIBRARY

Abre um arquivo de biblioteca API (application programming interface) externa.

```foxpro
SET LIBRARY TO [FileName [ADDITIVE]]
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo da biblioteca API ou arquivo de procedimentos a abrir. O Visual FoxPro assume a extensão .fll para bibliotecas. Se a biblioteca tem extensão .fll, você não precisa incluir a extensão com o nome do arquivo. Se uma biblioteca tem extensão diferente de .fll, você deve incluir a extensão com o nome do arquivo. Cuidado Ao usar SET LIBRARY, esteja ciente do seguinte: Você não pode usar bibliotecas API criadas para uma plataforma em outra plataforma. Por exemplo, bibliotecas criadas para FoxPro for MS-DOS não podem ser usadas no Visual FoxPro; bibliotecas criadas para Visual FoxPro não podem ser usadas no FoxPro for MS-DOS. Você não pode usar bibliotecas API criadas para uma versão em outra versão. Por exemplo, você não pode usar bibliotecas criadas para FoxPro versão 2.6 no Visual FoxPro. Você deve recompilar e vincular. O Visual FoxPro assume a extensão .prg para um arquivo de procedimentos. Quando você executa um procedimento com DO ProcedureName , o Visual FoxPro pesquisa o procedimento nos seguintes arquivos nesta ordem: O arquivo que contém DO ProcedureName . Um arquivo de procedimentos aberto com SET PROCEDURE (se houver um definido). Os programas na cadeia de execução. O Visual FoxPro pesquisa arquivos de programa começando pelo programa executado mais recentemente e continuando até o primeiro programa executado. Um arquivo de procedimentos aberto com SET LIBRARY (se houver um definido). Um arquivo de programa autônomo. Se o Visual FoxPro encontrar um arquivo de programa com o mesmo nome do nome de arquivo especificado com DO, o programa é executado. Se não encontrar um nome de arquivo de programa correspondente, o Visual FoxPro gera uma mensagem de erro.
**ADDITIVE**
Abre bibliotecas API adicionais. Inclua ADDITIVE após o nome do arquivo em comandos SET LIBRARY sucessivos. O Visual FoxPro ignora ADDITIVE quando você usa SET LIBRARY para abrir um arquivo de procedimentos.

# Observações

Use SET LIBRARY para abrir bibliotecas API externas ou um arquivo de procedimentos.

Bibliotecas de rotinas API ampliam as capacidades da linguagem e da interface do usuário do Visual FoxPro. Depois que uma biblioteca API externa é aberta, você pode usar as funções API como se fossem funções do Visual FoxPro. Use DISPLAY STATUS ou LIST STATUS para exibir as funções disponíveis da biblioteca.

Você pode usar bibliotecas API existentes ou criar suas próprias bibliotecas API.

No Visual FoxPro, a maneira preferida de registrar funções em bibliotecas compartilhadas é usar o comando DECLARE - DLL Command.

Para remover todas as bibliotecas API da memória, use SET LIBRARY TO sem incluir FileName ou ADDITIVE. Para remover uma biblioteca individual da memória, use RELEASE LIBRARY LibraryName.

Se você especificar um arquivo de procedimentos, os procedimentos dentro do arquivo de procedimentos ficam disponíveis para todos os programas e também estão disponíveis interativamente pela janela Command.

> **Observação:** A capacidade do Visual FoxPro de abrir um arquivo de procedimentos com SET LIBRARY fornece compatibilidade com dBASE IV. Usar SET LIBRARY para abrir um arquivo de procedimentos fechará todas as bibliotecas API abertas. Usar SET LIBRARY para abrir bibliotecas API fechará um arquivo de procedimentos aberto com SET LIBRARY. Use SET PROCEDURE para abrir um arquivo de procedimentos e evitar que bibliotecas API sejam fechadas.

Para informações adicionais sobre arquivos de procedimentos, consulte Comando PROCEDURE e Comando SET PROCEDURE.
