# Evento BeforeBuild

Ocorre antes de um projeto ser reconstruído ou um arquivo de aplicativo (.app), biblioteca de vínculo dinâmico (.dll) ou arquivo executável (.exe) ser criado a partir de um projeto.

```foxpro
PROCEDURE Object.BeforeBuild
LPARAMETERS cOutputName, nBuildAction, lRebuildAll, lShowErrors, lBuildNewGuids
```

#### Parâmetros
 **cOutputName**
Especifica o nome do aplicativo, biblioteca de vínculo dinâmico ou arquivo executável que é criado. Se cOutputName incluir uma extensão de arquivo e nBuildAction for omitido, a extensão de arquivo em cOutputName determina o tipo de arquivo criado. Por exemplo, se a extensão em cOutputName for ".exe", um arquivo executável é criado.
**nBuildAction**
Especifica que o projeto é reconstruído ou gera um aplicativo, uma biblioteca de vínculo dinâmico ou um arquivo executável. A tabela a seguir lista os valores de nBuildAction com uma descrição de cada um. nBuildAction FoxPro.h constant Description 1 BUILDACTION_REBUILD Rebuilds the project 2 BUILDACTION_BUILDAPP Creates an .app 3 BUILDACTION_BUILDEXE Creates an .exe 4 BUILDACTION_BUILDDLL Creates a .dll 5 BUILDACTION_BUILDMTDLL Creates a multi-threaded .dll nBuildAction takes precedence over the file extension specified in cOutPutName. For example, an executable file is created if nBuildAction is 3 and cOutputName doesn't specify an ".exe" extension.
**lRebuildAll**
Especifica se os arquivos no projeto são recompilados antes de um .app, .dll ou .exe ser criado. Se lRebuildAll for True (.T.), os seguintes são recompilados: Program files Format files Source code in forms, labels, reports, and visual class libraries Stored procedures in databases If lRebuildAll is False (.F.) or is omitted, files in the project are not recompiled before the .app, .dll, or .exe is created.
**lShowErrors**
Especifica se erros de compilação são exibidos em uma janela de edição após a conclusão da compilação. Se lShowErrors for True (.T.), os erros são exibidos. Se lShowErrors for False (.F.) ou for omitido, erros de compilação não são exibidos.
**lBuildNewGUIDs**
Especifica se novos GUIDs de registro (globally unique identifiers) são gerados quando um arquivo executável ou biblioteca de vínculo dinâmico é criado. Se lBuildNewGUIDs for True (.T.), novos GUIDs são gerados. Se lBuildNewGUIDs for False (.F.) ou for omitido, novos GUIDs não são gerados. lBuildNewGUIDs é ignorado se nBuildAction for menor que 3.

# Observações

Aplica-se a: ProjectHook Object

Os parâmetros listados acima são passados ao evento BeforeBuild quando você executa o método Build, quando você emite os comandos BUILD APP, BUILD DLL, BUILD EXE ou BUILD PROJECT, ou quando você escolhe OK na caixa de diálogo Build Options. Os parâmetros são passados por referência com exceção do parâmetro nBuildAction, que é passado por valor. Você pode alterar os valores desses parâmetros dentro do evento BeforeBuild para alterar como um projeto, .app, .dll ou .exe é criado a partir do projeto.

Inclua NODEFAULT no evento BeforeBuild para impedir que um projeto seja reconstruído ou que um arquivo de aplicativo (.app), biblioteca de vínculo dinâmico (.dll) ou arquivo executável (.exe) seja criado.
