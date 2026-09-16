# Exemplo Return a Value from a Form

Arquivo: ...\Samples\Solution\Forms\Logform.scx

Este exemplo ilustra como retornar um valor de um formulário de logon. O formulário de lançamento (Logform.scx) usa o comando DO FORM para executar o formulário de logon e armazenar o valor de retorno em uma variável (cUser).

```foxpro
DO FORM Login TO cUser
```

> **Observação:** Para retornar um valor de um formulário, a propriedade WindowType do formulário deve estar definida como 1 - Modal.

O formulário de logon (Login.scx) permite que um usuário insira um nome de usuário e uma senha. O código associado ao evento Click de cmdOK verifica se a senha correta foi inserida.

```foxpro
LOCATE FOR UPPER(login.userid) = UPPER(ALLTRIM(THISFORM.txtUserName.Value))
IF FOUND() AND ALLTRIM(password) == ALLTRIM(THISFORM.txtPassword.Value)
   THISFORM.cUser = ALLTRIM(login.userid)
   THISFORM.Release
ELSE
   #DEFINE MISMATCH_LOC "The user name or password is incorrect. Please try again."
   WAIT WINDOW MISMATCH_LOC TIMEOUT 1.5
   THISFORM.txtUserName.Value = ""
   THISFORM.txtPassword.Value = ""
   THISFORM.txtUserName.SetFocus
ENDIF
```

O código associado ao evento Unload do formulário de logon retorna o nome do usuário, se o usuário inseriu a senha correta, ou uma cadeia vazia.

```foxpro
RETURN THIS.cUser
```
