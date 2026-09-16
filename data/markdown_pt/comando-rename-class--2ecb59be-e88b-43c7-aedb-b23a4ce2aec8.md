# Comando RENAME CLASS

Renomeia uma definição de classe contida em uma biblioteca de classes visual .VCX.

```foxpro
RENAME CLASS ClassName1 OF ClassLibraryName TO ClassName2
```

#### Parâmetros
 **ClassName1**
Especifica o nome da definição de classe que é renomeada.
**OF ClassLibraryName**
Especifica o nome da biblioteca de classes visual .vcx que contém a definição de classe a renomear. Se você não especificar uma extensão de arquivo em ClassLibraryName , o Visual FoxPro atribui automaticamente uma extensão .vcx.
**TO ClassName2**
Especifica o novo nome da definição de classe.

# Observações

O Visual FoxPro não atualiza outras definições de classe na biblioteca de classes visual que referenciam a definição de classe renomeada — tenha cuidado ao renomear definições de classe.

# Exemplo

O exemplo a seguir usa CREATE CLASSLIB para criar uma biblioteca de classes visual chamada `myclslib`. Uma classe chamada `myform` baseada na classe base Form do Visual FoxPro é criada com CREATE CLASS e é armazenada na biblioteca de classes visual `myclslib`. RENAME CLASS é usado para alterar o nome da classe de `myform` para `yourform`.

```foxpro
CREATE CLASSLIB myclslib     && Creates a new .VCX visual class library
CREATE CLASS myform OF myclslib AS "Form"  && Creates new class
RENAME CLASS myform OF myclslib TO yourform  && Change class name
```
