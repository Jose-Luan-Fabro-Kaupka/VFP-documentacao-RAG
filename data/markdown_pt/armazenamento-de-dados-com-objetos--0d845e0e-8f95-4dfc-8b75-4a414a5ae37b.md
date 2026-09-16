# Armazenamento de dados com objetos

Em linguagens orientadas a objetos, uma classe oferece um meio útil e conveniente para armazenar dados e procedimentos relacionados a uma entidade. Por exemplo, você poderia definir uma classe de cliente para armazenar informações sobre um cliente, bem como um método para calcular a idade do cliente:

```foxpro
DEFINE CLASS customer AS CUSTOM
   LastName = ""
   FirstName = ""
   Birthday = { - - }
   PROCEDURE Age
      IF !EMPTY(THIS.Birthday)
         RETURN YEAR(DATE()) - YEAR(THIS.Birthday)
      ELSE
         RETURN 0
      ENDIF
   ENDPROC
ENDDEFINE
```

No entanto, os dados armazenados em objetos baseados na classe de cliente ficam armazenados apenas na memória. Se esses dados estivessem em uma tabela, ela seria armazenada em disco. Se você tivesse mais de um cliente para acompanhar, a tabela forneceria acesso a todos os comandos e funções de gerenciamento de banco de dados do Visual FoxPro. Como resultado, você poderia localizar informações rapidamente, classificá-las, agrupá-las, realizar cálculos com elas, criar relatórios e consultas com base nelas e assim por diante.

Armazenar e manipular dados em bancos de dados e tabelas é o que o Visual FoxPro faz melhor. Contudo, há ocasiões em que você desejará armazenar dados em objetos. Em geral, os dados serão relevantes somente enquanto o aplicativo estiver em execução e estarão relacionados a uma única entidade.

Por exemplo, em um aplicativo que inclua um sistema de segurança, normalmente haveria uma tabela de usuários com acesso ao aplicativo. A tabela incluiria a identificação do usuário, a senha e o nível de acesso. Depois que um usuário tiver feito logon, você não precisará de todas as informações da tabela. Tudo o que precisa são as informações sobre o usuário atual, que podem ser facilmente armazenadas e manipuladas em um objeto. A definição de classe a seguir, por exemplo, inicia um logon quando um objeto baseado na classe é criado:

```foxpro
DEFINE CLASS NewUser AS CUSTOM
   PROTECTED LogonTime, AccessLevel
   UserId = ""
   PassWord = ""
   LogonTime = { - - : : }
   AccessLevel = 0
   PROCEDURE Init
      DO FORM LOGON WITH ; && assuming you have created this form
         This.UserId, ;
         This.PassWord, ;
         This.AccessLevel
      This.LogonTime = DATETIME()
   ENDPROC
* Create methods to return protected property values.
   PROCEDURE GetLogonTime
      RETURN This.LogonTime
   ENDPROC
   PROCEDURE GetAccessLevel
      RETURN This.AccessLevel
   ENDPROC

ENDDEFINE
```

No programa principal do aplicativo, você poderia criar um objeto baseado na classe `NewUser`:

```foxpro
oUser = CREATEOBJECT('NewUser')
oUser.Logon
```

Em todo o aplicativo, quando precisar de informações sobre o usuário atual, você poderá obtê-las do objeto `oUser`. Por exemplo:

```foxpro
IF oUser.GetAccessLevel() >= 4
   DO ADMIN.MPR
ENDIF
```
