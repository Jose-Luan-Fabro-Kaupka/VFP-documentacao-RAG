# Eventos no Visual FoxPro

Eventos ocorrem automaticamente quando o sistema ou o usuário da aplicação executa uma ação específica. Eventos associados a um objeto ocorrem quando o usuário interage com o objeto de qualquer forma, como pressionar Tab para acessá-lo, clicar nele ou mover o ponteiro do mouse sobre ele. Por exemplo, a classe CommandButton contém um evento Click que é disparado quando o usuário clica no botão de comando.

Você pode adicionar código à procedure de evento de um objeto para que, quando o evento ocorrer para o objeto, o código seja executado automaticamente. Por exemplo, você pode adicionar código ao evento Click para que, quando o usuário clicar no botão de comando, o código seja executado automaticamente para realizar uma ação, como abrir um formulário. Eventos de sistema também podem executar código em eventos, como no caso do evento Timer em um controle Timer.

A tabela a seguir contém uma lista do conjunto principal de eventos do Visual FoxPro, que se aplicam à maioria dos controles.
 Eventos principais no Visual FoxPro
| Event | Event occurs when |
| --- | --- |
| Init | An object is created. |
| Destroy | An object is released from memory. |
| Click | The user clicks the object using the primary mouse button. |
| DblClick | The user double-clicks the object using the primary mouse button. |
| RightClick | The user clicks the object using the secondary mouse button. |
| GotFocus | The object receives the focus through user action such as tabbing or clicking or by changing the focus in code using the SetFocus Method. For more information, see SetFocus Method . |
| LostFocus | The object loses the focus through user action such as tabbing to or clicking another object or by changing the focus in code using the SetFocus method . |
| KeyPress | The user presses and releases a key. |
| MouseDown | The user presses the mouse button while the mouse pointer is over the object. |
| MouseMove | The user moves the mouse pointer over the object. |
| MouseUp | The user releases the mouse button while the mouse pointer is over the object. |

# Disparando eventos programaticamente

A maioria dos eventos ocorre automaticamente quando o sistema ou o usuário executa uma ação. No entanto, você pode gerar os seguintes eventos programaticamente usando determinados comandos do Visual FoxPro:
 - Use o comando MOUSE para gerar os eventos Click , DblClick , MouseMove e DragDrop .
- Use o comando ERROR para gerar o evento Error .
- Use o comando KEYBOARD para gerar o evento KeyPress .

Para obter mais informações, consulte MOUSE Command, ERROR Command e KEYBOARD Command.

Embora você não possa disparar a maioria dos eventos programaticamente, pode chamar a procedure associada ao evento, o que executa o código no evento, mas não dispara o evento em si. Por exemplo, a linha a seguir chama a procedure do evento Activate para o formulário frmPhoneLog e executa o código no evento; no entanto, não ativa o formulário em si:

```foxpro
frmPhoneLog.Activate
```

Se você deseja ativar o formulário, use o método Show do formulário:

```foxpro
frmPhoneLog.Show
```

Chamar o método Show exibe e ativa o formulário, o que também executa o código no evento Activate.
