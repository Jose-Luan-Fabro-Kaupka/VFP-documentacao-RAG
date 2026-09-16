# Propriedade CLSID

Contém o CLSID (Class Identifier) registrado para um servidor em um projeto. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Object.CLSID
```

# Observações

Aplica-se a: Server Object

Um CLSID é criado no registro do Windows para um servidor quando você compila um arquivo executável (.exe) ou biblioteca de vínculo dinâmico (.dll) a partir de um projeto.

# Exemplo

O exemplo a seguir demonstra um uso da propriedade CLSID após a criação de um servidor COM (.dll).

```foxpro
* In a program("Testclass.prg"), create a class
DEFINE CLASS myclass AS SESSION OLEPUBLIC
ENDDEFINE
...
```

Em um projeto, inclua o arquivo .prg em um Build .dll ou MTDLL. As propriedades do objeto servidor ficam então disponíveis por acesso de código. Por exemplo, na janela Command, digite o seguinte:

```foxpro
MyServer = _VFP.ActiveProject.Servers("myclass")
? "Class ID is ", MyServer.CLSID      && Class ID is {620E56FE-F7F8-4E99-B767-CB08009261F0}
                                    && a GUID
? "Description is ", MyServer.Description    && testclass.myclass
```
