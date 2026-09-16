# Comando CREATE CLASSLIB

Cria um novo arquivo vazio de biblioteca de classes visuais (.vcx).

```foxpro
CREATE CLASSLIB ClassLibraryName
```

#### Parâmetros
**ClassLibraryName**
Especifica o nome da biblioteca de classes visuais a ser criada. Se já existir uma biblioteca de classes visuais com o nome especificado e SET SAFETY estiver ON, o Visual FoxPro perguntará se você deseja substituir a biblioteca existente. Se SET SAFETY estiver OFF, o arquivo existente será substituído automaticamente. Se você não especificar uma extensão para o nome do arquivo, o Visual FoxPro atribuirá automaticamente a extensão .vcx.

# Observações

Definições de classe podem ser adicionadas a uma biblioteca de classes visuais com ADD CLASS e CREATE CLASS.

# Exemplo

O exemplo a seguir usa CREATE CLASSLIB para criar uma biblioteca de classes visuais chamada `myclslib`. Uma classe chamada `myform`, baseada na classe base Form do Visual FoxPro, é criada e armazenada na biblioteca de classes visuais `myclslib`. SET CLASSLIB é usado para abrir a biblioteca de classes visuais `myclslib`, permitindo que as classes nela contidas sejam usadas.

```foxpro
CREATE CLASSLIB myclslib     && Creates a new .VCX visual class library
CREATE CLASS myform OF myclslib AS "Form"  && Creates new class
SET CLASSLIB TO myclslib ADDITIVE     && Opens MyClsLib.VCX
```
