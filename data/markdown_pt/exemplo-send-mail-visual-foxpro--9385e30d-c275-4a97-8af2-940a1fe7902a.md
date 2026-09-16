# Exemplo Send Mail (Visual FoxPro)

Arquivo: ...\Samples\Solution\OLE\Sendmail.scx

Este exemplo ilustra o uso da classe mailbtn em ...\Samples\Classes\Buttons.vcx para criar um formulário simples de mensagens que pode enviar dados do Visual FoxPro para um endereço de e-mail.

Mailbtn é uma classe container que contém um botão de comando e dois controles ActiveX: MAPI Session e MAPI Messages, ambos definidos em Msmapi32.ocx. O controle MAPI Session estabelece uma sessão MAPI, e o controle MAPI Messages permite que o usuário execute uma variedade de funções do sistema de mensagens.

A classe mailbtn inicia uma nova sessão Mail, coleta dados do registro atual e exibe a caixa de diálogo Send Mail com os dados inseridos como texto da mensagem.

Esta classe inclui dois métodos personalizados AddTabs e StripPath para formatar as informações coletadas da tabela e inseridas na mensagem de e-mail.

Esta classe também aproveita outro método personalizado chamado Signon, bem como uma propriedade personalizada chamada logsession, que é definida como .F. inicialmente.

Quando o usuário clica no botão cmdMail, o código a seguir no evento Click chama o método signon, definindo logsession como true (.T.):

```foxpro
this.logsession = .T.
this.OLEMSess.signon
```

Se houver uma falha no signon, o evento Error da classe é chamado e logsession é definido como .F.

Os controles MAPI são invisíveis em tempo de execução. Além disso, não há eventos para os controles. Para usá-los, você deve especificar os métodos apropriados. Para que esses controles funcionem, os serviços MAPI devem estar presentes. Os serviços MAPI são fornecidos nos sistemas de e-mail Microsoft Outlook e Exchange para Microsoft Windows 95 ou posterior.
