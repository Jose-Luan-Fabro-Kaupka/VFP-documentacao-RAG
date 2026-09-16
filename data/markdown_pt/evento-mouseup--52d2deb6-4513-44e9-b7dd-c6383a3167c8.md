# Evento MouseUp

Ocorre quando o usuário solta um botão do mouse.

```foxpro
PROCEDURE Object.MouseUp
LPARAMETERS nButton, nShift, nXCoord, nYCoord
```

#### Parâmetros

Você deve incluir uma instrução LPARAMETERS ou PARAMETERS no procedimento do evento e especificar um nome para cada parâmetro. O Visual FoxPro passa os parâmetros do evento MouseUp na seguinte ordem.
 **nButton**
No Visual FoxPro para Windows, contém um número que especifica qual botão foi solto para disparar o evento: 1 (esquerdo), 2 (direito) ou 4 (meio).
**nShift**
Contém um número especificando o estado das teclas modificadoras quando o mouse é solto. No Visual FoxPro para Windows, as teclas modificadoras válidas são as teclas SHIFT, CTRL e ALT. Os valores retornados em nShift para teclas modificadoras individuais estão listados na tabela a seguir. Tecla modificadora Valores para nShift Tecla Windows Valor SHIFT 1 CTRL 2 ALT 4 Se mais de uma tecla modificadora é mantida pressionada quando o mouse é solto, o argumento nShift contém a soma dos valores das teclas modificadoras. Por exemplo, no Visual FoxPro para Windows, se o usuário mantém CTRL pressionado ao soltar o botão do mouse, o argumento nShift contém 2. Mas se o usuário mantém CTRL+ALT pressionado ao soltar o botão do mouse, o argumento nShift contém 6.
**nXCoord , nYCoord**
Contém a posição horizontal ( nXCoord ) e vertical ( nYCoord ) atual do ponteiro do mouse dentro do formulário. Essas coordenadas são sempre expressas em termos do sistema de coordenadas do formulário na unidade de medida especificada pela propriedade ScaleMode do formulário.

# Observações

Aplica-se a: Controle CheckBox | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Objeto Form | Controle Grid | Objeto Header | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Objeto ToolBar

Use um procedimento MouseUp para especificar ações a ocorrer quando um determinado botão do mouse é solto. Diferentemente dos eventos Click e DblClick, o evento MouseUp permite distinguir entre os botões esquerdo, direito e meio do mouse. Você também pode escrever código para combinações mouse-teclado que usam as teclas modificadoras.

Você pode usar um procedimento MouseMove para responder a um evento causado pelo movimento do mouse.

> **Observação:** O argumento nButton para MouseDown e MouseUp difere do argumento nButton usado para MouseMove. Para MouseDown ou MouseUp, o argumento nButton indica exatamente um botão por evento; para MouseMove, indica o estado atual de todos os botões.
