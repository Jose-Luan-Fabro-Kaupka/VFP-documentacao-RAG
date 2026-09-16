# Comando RELEASE CLASSLIB

Fecha bibliotecas de classes visuais .vcx que contêm definições de classe.

```foxpro
RELEASE CLASSLIB ClassLibraryName1 | ALIAS AliasName1
   [, ClassLibraryName2 | ALIAS AliasName2 ...]
   [IN APPFileName | EXEFileName]
```

#### Parâmetros
 **ClassLibraryName1 | ALIAS AliasName1**
Especifica o nome ou alias de um arquivo de biblioteca de classes visual a ser fechado.
**ClassLibraryName2 | ALIAS AliasName2 ...**
Especifica os nomes ou aliases de arquivos de biblioteca de classes visual adicionais a serem fechados.
**IN APPFileName | EXEFileName**
Especifica um arquivo de aplicativo Visual FoxPro (.app) ou arquivo executável (.exe) que contém a biblioteca de classes visual.

# Observações

Bibliotecas de classes visuais .vcx são abertas com SET CLASSLIB. Depois que a biblioteca está aberta, as definições de classe dentro da biblioteca de classes visual estão disponíveis para programas e na janela Command.

Para fechar todas as bibliotecas de classes visuais abertas, emita SET CLASSLIB TO sem argumentos adicionais.

# Exemplo

O exemplo a seguir usa CREATE CLASSLIB para criar uma biblioteca de classes visual chamada `myclslib`. Uma classe chamada `myform` baseada na classe base Form do Visual FoxPro é criada e armazenada na biblioteca de classes visual `myclslib`. SET CLASSLIB é usado para abrir a biblioteca de classes visual `myclslib` para que as classes dentro dela possam ser usadas. RELEASE CLASSLIB é então usado para fechar a biblioteca de classes visual `myclslib`.

```foxpro
CREATE CLASSLIB myclslib     && Creates a new .VCX visual class library
CREATE CLASS myform OF myclslib AS "Form"  && Creates new class
SET CLASSLIB TO myclslib ADDITIVE     && Opens MyClsLib.VCX
RELEASE CLASSLIB myclslib
```
