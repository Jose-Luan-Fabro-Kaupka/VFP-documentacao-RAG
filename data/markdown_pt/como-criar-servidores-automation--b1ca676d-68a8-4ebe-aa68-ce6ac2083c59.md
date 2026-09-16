# Como: criar servidores Automation

Você pode criar servidores Automation em um projeto de aplicativo criando uma classe definida pelo usuário OLE public em um arquivo de programa (.prg) ou em um arquivo de biblioteca de classes visual (.vcx).

Para exemplos de servidores Automation, consulte o diretório Visual FoxPro ..\Samples\Servers.

### Para criar um servidor Automation
- Crie a classe no Class Designer como uma classe Custom.
- No menu Class, clique em Class Info.
- Na caixa de diálogo Class Info, clique em OLE Public.

Para obter mais informações, consulte Como: criar classes e subclasses.

### Para criar um servidor Automation programaticamente
- Crie a classe usando o comando DEFINE CLASS e inclua a palavra-chave OLEPUBLIC com a cláusula AS.

Por exemplo, o código a seguir em uma definição de classe em um arquivo de programa cria uma classe OLE public customizada:

```foxpro
DEFINE CLASS person AS CUSTOM OLEPUBLIC
   FirstName = SPACE(30)
   LastName = SPACE(45)
   PROCEDURE GetName
      RETURN THIS.FirstName + " " + THIS.LastName
   ENDPROC
ENDDEFINE
```
