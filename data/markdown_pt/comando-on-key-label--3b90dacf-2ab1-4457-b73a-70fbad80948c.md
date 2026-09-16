# Comando ON KEY LABEL

Especifica um comando que é executado quando você pressiona uma tecla ou combinação de teclas específica ou clica o botão do mouse.

```foxpro
ON KEY [LABEL KeyLabelName] [Command]
```

#### Parâmetros
 **LABEL KeyLabelName**
Especifica o nome do rótulo de tecla atribuído à tecla. O KeyLabelName é a letra ou o dígito na tecla ou um nome especial atribuído à tecla. A tabela a seguir lista os nomes especiais de rótulos de tecla. Atribuições de rótulos de tecla do Visual FoxPro Para esta tecla Especifique este valor KeyLabelName LEFTARROW RIGHTARROW UPARROW DNARROW HOME HOME END END PAGE UP PGUP PAGE DOWN PGDN DEL DEL BACKSPACE BACKSPACE SPACEBAR SPACEBAR INS INS TAB TAB SHIFT+TAB BACKTAB Left Brace LBRACE Right Brace RBRACE ENTER ENTER F1 to F12 F1, F2, F3 ... CTRL+F1 to CTRL+F12 CTRL+F1, CTRL+F2 ... SHIFT+F1 to SHIFT+F12 SHIFT+F1, SHIFT+F2 ... ALT+F1 to ALT+F12 ALT+F1, ALT+F2, ALT+F3 ... ALT+0 to ALT+9 ALT+0, ALT+1, ALT+2 ... ALT+A to ALT+Z ALT+A, ALT+B, ALT+C ... CTRL+LEFT ARROW CTRL+LEFTARROW CTRL+RIGHT ARROW CTRL+RIGHTARROW CTRL+HOME CTRL+HOME CTRL+END CTRL+END CTRL+PAGE UP CTRL+PGUP CTRL+PAGE DOWN CTRL+PGDN CTRL+A TO CTRL+Z CTRL+A, CTRL+B, CTRL+C ... CTRL+0 CTRL+0 RIGHT MOUSE BUTTON RIGHTMOUSE LEFT MOUSE BUTTON LEFTMOUSE MOUSE BUTTON MOUSE ESC ESC
**Command**
Especifica o comando que é executado quando você pressiona a tecla ou combinação de teclas especificada ou clica o botão do mouse. Você pode incluir parâmetros ou expressões de parâmetro com o comando que atribui à tecla, como no exemplo a seguir: ON KEY LABEL ALT+V WAIT WINDOW "Version: " + VERSION() Você pode incluir variáveis na atribuição, mas elas devem ser públicas. Por exemplo: PUBLIC message message = "Default drive: " + SYS(5) ON KEY LABEL ALT+D WAIT WINDOW message

# Observações

ON KEY LABEL normalmente usa DO para executar um procedimento.

ON KEY LABEL executa o comando imediatamente durante a execução de READ, BROWSE, EDIT, CHANGE e menus definidos pelo usuário. Se um programa estiver em execução quando você pressionar a tecla ou clicar o botão do mouse, o Visual FoxPro executa a linha atual do programa e depois executa o comando ON KEY LABEL. Quaisquer atribuições ON KEY LABEL criadas em um programa permanecem em vigor após a execução do programa. Você também pode criar atribuições de tecla na janela Command.

Para restaurar o comportamento normal de uma tecla específica, emita ON KEY LABEL KeyLabelName. Para restaurar todas as teclas ao comportamento padrão, emita ON KEY.

> **Dica:** Para evitar chamadas recursivas durante a execução de um procedimento ON KEY LABEL, inclua PUSH KEY CLEAR no início do procedimento para desabilitar todos os comandos ON KEY LABEL ativos. Emita POP KEY no final do procedimento para habilitar os comandos ON KEY LABEL.

As atribuições ON KEY LABEL não estão em vigor na barra de menu do sistema do Visual FoxPro, nos menus do sistema, nas caixas de diálogo, nos alertas e assim por diante. As atribuições de tecla são efetivas nas janelas do sistema do Visual FoxPro — o editor de texto do Visual FoxPro, a janela Command, a janela Trace e assim por diante.

Diferentemente de ON KEY, pode haver vários comandos ON KEY LABEL ativos. Por exemplo, você pode atribuir um comando a cada uma das teclas de seta e a um botão do mouse.

A execução de um ON KEY LABEL redefine PARAMETERS( ) para 0. Para obter mais informações, consulte a função PARAMETERS( ).

No Visual FoxPro, certos eventos não podem ser capturados porque estão sob o controle do Windows. Em particular, ON KEY LABEL MOUSE, ON KEY LABEL LEFTMOUSE e ON KEY LABEL RIGHTMOUSE não são executados quando você clica em um controle do Windows, como um menu Control, barra de rolagem ou similar. Além disso, CTRL+0 é suportado em ON KEY LABEL no Visual FoxPro, permitindo redefinir a combinação de teclas usada para inserir um valor nulo em um campo.

Observe que ON KEY LABEL opera fora do escopo de um formulário; o evento KeyPress pode ser usado em formulários para executar código quando uma tecla é pressionada.

# Exemplo

O exemplo a seguir exibe uma mensagem quando uma tecla de seta é pressionada.

```foxpro
ON KEY [LABEL KeyLabelName] [Command]
```

#### Parameters
 **LABEL KeyLabelName**
Specifies the key label name assigned to the key. The KeyLabelName is the letter or digit on the key or a special name assigned to the key. The following table lists the special key label names. Visual FoxPro key label assignments For this key Specify this KeyLabelName value LEFTARROW RIGHTARROW UPARROW DNARROW HOME HOME END END PAGE UP PGUP PAGE DOWN PGDN DEL DEL BACKSPACE BACKSPACE SPACEBAR SPACEBAR INS INS TAB TAB SHIFT+TAB BACKTAB Left Brace LBRACE Right Brace RBRACE ENTER ENTER F1 to F12 F1, F2, F3 ... CTRL+F1 to CTRL+F12 CTRL+F1, CTRL+F2 ... SHIFT+F1 to SHIFT+F12 SHIFT+F1, SHIFT+F2 ... ALT+F1 to ALT+F12 ALT+F1, ALT+F2, ALT+F3 ... ALT+0 to ALT+9 ALT+0, ALT+1, ALT+2 ... ALT+A to ALT+Z ALT+A, ALT+B, ALT+C ... CTRL+LEFT ARROW CTRL+LEFTARROW CTRL+RIGHT ARROW CTRL+RIGHTARROW CTRL+HOME CTRL+HOME CTRL+END CTRL+END CTRL+PAGE UP CTRL+PGUP CTRL+PAGE DOWN CTRL+PGDN CTRL+A TO CTRL+Z CTRL+A, CTRL+B, CTRL+C ... CTRL+0 CTRL+0 RIGHT MOUSE BUTTON RIGHTMOUSE LEFT MOUSE BUTTON LEFTMOUSE MOUSE BUTTON MOUSE ESC ESC
**Command**
Specifies the command that executes when you press the specified key or key combination or click the mouse button. You can include parameter or parameter expressions with the command that you assign to the key, as in the following example: ON KEY LABEL ALT+V WAIT WINDOW "Version: " + VERSION() You can include variables in the assignment, but they must be public. For example: PUBLIC message message = "Default drive: " + SYS(5) ON KEY LABEL ALT+D WAIT WINDOW message

# Remarks

ON KEY LABEL typically uses DO to execute a procedure.

ON KEY LABEL executes the command immediately during the execution of READ, BROWSE, EDIT, CHANGE, and user-defined menus. If a program is executing when you press the key or click the mouse button, Visual FoxPro executes the current program line and then executes the ON KEY LABEL command. Any ON KEY LABEL key assignments created in a program remain in effect after the program is run. You can also create key assignments in the Command window.

To restore the behavior of a specific key to normal, issue ON KEY LABEL KeyLabelName. To restore all keys to their default behavior, issue ON KEY.

> **Tip:** To prevent recursive calls during the execution of an ON KEY LABEL procedure, include PUSH KEY CLEAR early in the procedure to disable all active ON KEY LABEL commands. Issue POP KEY at the end of the procedure to enable the ON KEY LABEL commands.

The ON KEY LABEL key assignments aren't in effect in the Visual FoxPro system menu bar, system menus, dialog boxes, alerts, and so on. The key assignments are effective in the Visual FoxPro system windows — the Visual FoxPro text editor, the Command window, the Trace window, and so on.

Unlike ON KEY, there can be multiple active ON KEY LABEL commands. For example, you can assign a command to each of the arrow keys and a mouse button.

Executing an ON KEY LABEL resets PARAMETERS( ) to 0. For more information, see PARAMETERS( ) Function.

In Visual FoxPro, certain events cannot be trapped because they are under the control of Windows. In particular, ON KEY LABEL MOUSE, ON KEY LABEL LEFTMOUSE, and ON KEY LABEL RIGHTMOUSE are not executed when you click a Windows control such as a Control menu, scroll bar, or the like. Also, CTRL+0 is supported in ON KEY LABEL in Visual FoxPro, allowing you to redefine the key combination used to enter a null value into a field.

Note that ON KEY LABEL operates outside of the scope of a form; the KeyPress event can be used within forms to execute code when a key is pressed.

# Example

The following example displays a message when an arrow key is pressed.
