# Comando SET CLASSLIB

Abre uma biblioteca de classes visuais .vcx que contém definições de classe.

```foxpro
SET CLASSLIB TO ClassLibraryName [IN APPFileName | EXEFileName]
   [ADDITIVE] [ALIAS AliasName]
```

#### Parâmetros
 **TO ClassLibraryName**
Especifica o nome da biblioteca de classes visuais .vcx a ser aberta. Se ClassLibraryName não incluir um caminho totalmente qualificado, o Visual FoxPro procurará primeiro a biblioteca de classes visuais no diretório padrão do Visual FoxPro e depois nos diretórios do caminho do Visual FoxPro. O diretório padrão do Visual FoxPro é especificado com SET DEFAULT, e o caminho de pesquisa do Visual FoxPro é especificado com SET PATH. Emitir SET CLASSLIB TO sem ClassLibraryName fecha todas as bibliotecas de classes visuais abertas. Use RELEASE CLASSLIB para fechar uma biblioteca de classes visuais individual.
**IN APPFileName | EXEFileName**
Especifica um arquivo de aplicativo (.app) ou executável (.exe) do Visual FoxPro que contém a biblioteca de classes visuais.
**ADDITIVE**
Abre a biblioteca de classes visuais .vcx sem fechar nenhuma biblioteca .vcx atualmente aberta. Se essa cláusula for omitida, todas as bibliotecas de classes visuais .vcx abertas serão fechadas.
**ALIAS AliasName**
Especifica um alias para a biblioteca de classes visuais. A biblioteca pode ser referenciada por seu alias. Por exemplo, os comandos a seguir abrem uma biblioteca de classes visuais .vcx chamada MyClass, atribuem a ela o alias MyCntrls e criam um controle chamado MyButton. SET CLASSLIB TO MyClass ALIAS MyCntrls mMyButton = CREATEOBJ('MyCntrls.MyButton')

# Observações

Quando CREATEOBJECT( ), ADD OBJECT em DEFINE CLASS ou o método AddObject é emitido, o Visual FoxPro procura a definição de classe que define o objeto especificado nesses comandos nos seguintes locais e nesta ordem:
 - Classes base do Visual FoxPro.
- Definições de classe na memória, na ordem em que foram carregadas.
- Definições de classe no programa atual.
- Definições de classe nas bibliotecas de classes .vcx abertas com SET CLASSLIB.
- Definições de classe nos arquivos de procedimento abertos com SET PROCEDURE.
- Definições de classe na cadeia de execução de programas do Visual FoxPro.
- Registro OLE, se SET OLEOBJECT estiver definido como ON.

Se a definição de classe que contém o objeto não puder ser localizada, o Visual FoxPro gerará uma mensagem de erro.

# Exemplo

O exemplo a seguir usa CREATE CLASSLIB para criar uma biblioteca de classes visuais chamada `myclslib`. Uma classe chamada `myform`, baseada na classe base Form do Visual FoxPro, é criada e armazenada na biblioteca de classes visuais `myclslib`. SET CLASSLIB é usado para abrir a biblioteca de classes visuais `myclslib`, permitindo usar suas classes.

```foxpro
CREATE CLASSLIB myclslib     && Creates a new .VCX visual class library
CREATE CLASS myform OF myclslib AS "Form"  && Creates new class
SET CLASSLIB TO myclslib ADDITIVE     && Opens MyClsLib.VCX
```
