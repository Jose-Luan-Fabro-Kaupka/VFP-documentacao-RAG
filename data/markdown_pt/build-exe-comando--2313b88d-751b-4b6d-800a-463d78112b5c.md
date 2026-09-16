# BUILD EXE Comando

Cria um arquivo executável (.exe) a partir de um projeto Visual FoxPro.

> **Note:** The .exe file operates with the Visual FoxPro dynamic-link (.dll) libraries, VFP VersionNumber R.dll and VFP VersionNumber RENU.dll, which you need to distribute with your application to provide a complete Visual FoxPro run-time environment for your application. VersionNumber represents the version number of Visual FoxPro that you use to create the .exe file. These files are located in the ..\Program Files\Common Files\Microsoft Shared\VFP directory.

For more information, see VFP9R.DLL Run-Time Library, VFP9T.DLL Run-Time Library, Preparation for Distributing Applications, and Managing Files in an International Application.

```foxpro
BUILD EXE EXEFileName FROM ProjectName [RECOMPILE]
```

Parâmetros
**EXEFileName**
Especifica o nome do arquivo executável a criar. A extensão padrão do nome de arquivo é .exe. Nota Se um arquivo aplicativo (.app) existe com o mesmo nome de arquivo raiz que o arquivo .exe que você cria, o arquivo .app é excluído.
** FROM ProjectName**
Especifica o nome do projeto do qual o arquivo executável é construído.
**[RECOMPILE]**
Especifica que o projeto será compilado antes da compilação do arquivo executável. Todos os arquivos de programa e formato; forma, etiqueta, relatório e código fonte da biblioteca de classe visual; e procedimentos armazenados em bancos de dados no projeto são compilados.

Observações

If the .exe file contains OLEPUBLIC class definitions, BUILD EXE automatically registers the OLEPUBLIC class definitions in the system registry. OLEPUBLIC class definitions appear in the Server Classes list box on the Servers tab of the Project Information dialog box. BUILD EXE creates also registration (.vbr) and type library (.tlb) files with the same name as the .exe file. The .vbr file makes it possible for you to register class definitions in the system registry when the .exe file is moved to a different computer. The .tlb file is for use with object browsers. For more information about registering OLEPUBLIC class definitions in an executable file, see Sharing Information and Adding OLE.

Visual FoxPro inclui suporte para aplicativos que são gerados pelo processo de compilação para detectar se eles estão rodando em um Terminal Server e impede o carregamento de arquivos desnecessários de bibliotecas de links dinâmicos (.dll) que podem afetar o desempenho.

Veja também
- Como: Construir Aplicações
- BUILD DLL Command
- BUILD APP Command
- BUILD MTDLL Command
- BUILD PROJECT Command
