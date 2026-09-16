# Amostra Control MSN Messenger

Arquivo: ...\Samples\Solution\Toledo\Messenger.scx

Esta amostra demonstra como realizar operações com o MSN Messenger usando a API do Messenger e o Windows Scripting Host. Você pode usar esses métodos para automatizar o envio de mensagens, e-mail e arquivos para qualquer usuário MSN a partir de processos automatizados. Além disso, se os usuários tiverem mensagens móveis, alertas podem ser enviados para seus pagers.

Esta amostra não pretende ser uma interface alternativa ao MSN Messenger. Para obter informações sobre as APIs do MSN Messenger, consulte o MSDN online em http://msdn.microsoft.com.

# API do MSN Messenger

Esta amostra demonstra as APIs do Messenger que você pode acessar por meio do Component Object Model (COM). Nesta amostra, o objeto Messenger é instanciado no evento Init:

```foxpro
ThisForm.oMessenger = CREATEOBJECT("Messenger.UIAutomation.1")
```

O evento Init também declara algumas APIs do Windows usadas para trazer janelas do Messenger para o primeiro plano para que você possa automatizar a composição de mensagens de e-mail e o envio de arquivos.

```foxpro
DECLARE LONG SetForegroundWindow IN WIN32API LONG
DECLARE INTEGER FindWindow IN WIN32API STRING @ cClass, STRING @ cTitle
DECLARE LONG CloseWindow IN WIN32API LONG
DECLARE Sleep IN WIN32API long
```

Depois de criar uma instância de um objeto Messenger, você pode chamar métodos como AutoSignin, InstantMessage, OpenInbox, SendFile, SendMail e SignOut. Os métodos SendFile e SendEmail também usam as APIs do Windows para trazer janelas do Messenger para o primeiro plano para que o objeto Shell do Windows Scripting Host possa ser usado para enviar pressionamentos de tecla para essas janelas.

# Windows Scripting Host

Esta amostra ilustra como usar o Windows Scripting Host para enviar pressionamentos de tecla para as janelas ativadas. Você pode então preencher formulários automaticamente para enviar e-mail e arquivos. O Windows Scripting Host é necessário porque a API do MSN Messenger não tem essa funcionalidade. O objeto Shell do Windows Scripting Host é instanciado no evento Init do formulário de amostra:

```foxpro
ThisForm.oWsh = CREATEOBJECT("wscript.Shell")
```

Para enviar pressionamentos de tecla para a janela ativa, o método SendKeys do formulário de amostra chama a função SendKeys( ) do objeto Shell do Windows Scripting Host e automatiza a composição de e-mail e o envio de arquivos.

```foxpro
ThisForm.oWsh.SendKeys(tcKeys)
```
