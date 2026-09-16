# Comando SET MESSAGE

Define uma mensagem para exibição na janela principal do Visual FoxPro ou na barra de status gráfica, ou especifica a localização de mensagens para barras de menu e comandos de menu definidos pelo usuário. Existem várias versões da sintaxe.

```foxpro
SET MESSAGE TO [cMessageText]
SET MESSAGE TO [nRow [LEFT | CENTER | RIGHT]]
SET MESSAGE WINDOW [WindowName]
```

#### Parâmetros
 **TO [ cMessageText ]**
Especifica a mensagem a exibir.
**TO [ nRow [LEFT | CENTER | RIGHT]]**
Especifica o posicionamento de mensagens na janela principal do Visual FoxPro. nRow especifica a linha na qual as mensagens são exibidas. Se nRow for 0, nenhuma mensagem é exibida. LEFT, CENTER e RIGHT especificam o posicionamento horizontal na tela das mensagens. O Visual FoxPro ignora uma localização de mensagem especificada com SET MESSAGE quando a barra de status gráfica é exibida.
**WINDOW [ WindowName ]**
Especifica a janela na qual as mensagens são exibidas. Para remover uma mensagem da janela e exibi-la na tela, emita SET MESSAGE WINDOW.

# Observações

SET MESSAGE permite criar uma mensagem. Também permite especificar onde exibir mensagens criadas com DEFINE BAR, DEFINE MENU, DEFINE PAD ou DEFINE POPUP.

Por padrão, as mensagens são colocadas na última linha da janela principal do Visual FoxPro se a barra de status baseada em caracteres estiver exibida. Se a barra de status gráfica estiver exibida, as mensagens são colocadas na barra de status.

A linha SET MESSAGE é redefinida para a última linha da janela principal do Visual FoxPro sempre que SET DISPLAY é emitido.

SET MESSAGE TO sem argumentos coloca mensagens na barra de status gráfica.
