# Códigos de teclas do Visual FoxPro (Construção de biblioteca de API)

A maioria das teclas possui um valor constante, mesmo quando combinada com diferentes teclas modificadoras (SHIFT, CTRL e ALT). Todas as teclas comuns do teclado (alfabéticas e caracteres especiais) têm como código de tecla seu valor ASCII.

Os valores do código de tecla e do modificador são retornados na estrutura EventRec. O código da tecla está em EventRec.message e os modificadores estão em EventRec.modifiers.

O Visual FoxPro interpreta algumas teclas com valores diferentes conforme o modificador usado. Por exemplo, ao pressionar SHIFT+F10, os campos correspondentes em EventRec são:
 - EventRec.message = 15D (Hex)
- EventRec.modifier = 1000 (Hex)

Da mesma forma, ao pressionar CTRL+F10, os valores de EventRec são:
 - EventRec.message = 167 (Hex)
- EventRec.modifiers = 2000 (Hex)

Quando mais de um modificador é usado com uma tecla, seus valores são somados. Por exemplo, ao pressionar CTRL+SHIFT+F10, são retornados:
 - EventRec.message = 167 (Hex)
- EventRec.modifiers = 3000 (Hex)

EventRec.modifiers é 0x3000 no exemplo anterior porque os modificadores CTRL e SHIFT foram incluídos. Assim, o valor de SHIFT (0x1000) foi somado ao de CTRL (0x2000), produzindo 0x3000.

> **Observação:** A forma como o Visual FoxPro interpreta teclas, especialmente com modificadores, é própria do Visual FoxPro. Outros programas podem interpretá-las de modo diferente. Se uma tecla for pressionada com uma ou mais teclas modificadoras (SHIFT, CTRL e ALT), o nibble superior representará os modificadores usados.

A tabela a seguir demonstra que F8 possui um código diferente dependendo do modificador.

| Teclas pressionadas | Modificador | Valor de F8 |
| --- | --- | --- |
| F8 | Nenhum | \x142 |
| SHIFT+F8 | SHIFT | \x15B |
| CTRL+F8 | CTRL | \x165 |
| ALT+F8 | ALT | \x16F |

Cada tecla especial que pode ser combinada com modificadores possui um valor exclusivo para cada modificador. Se uma tecla especial for combinada com vários modificadores, seu valor será o correspondente a um deles, conforme estas regras:
 - Primeiro verifique se a combinação inclui ALT, pois a tecla principal receberá seu valor ALT.
- Se não incluir ALT, verifique se CTRL foi usado, pois a tecla principal receberá seu valor CTRL.
- Se ALT e CTRL não forem usados, verifique SHIFT, pois a tecla principal receberá seu valor SHIFT.
- Por fim, sem modificadores, a tecla principal recebe seu valor sem modificadores.

# Códigos de teclas especiais

A tabela a seguir lista os valores atribuídos pelo Visual FoxPro às teclas especiais.

| Tecla | Código (Hex) | Modificador |
| --- | --- | --- |
| LEFTMOUSE | 100 | Nenhum |
| F1 | 13B | Nenhum |
| F2 | 13C | Nenhum |
| F3 | 13D | Nenhum |
| F4 | 13E | Nenhum |
| F5 | 13F | Nenhum |
| F6 | 140 | Nenhum |
| F7 | 141 | Nenhum |
| F8 | 142 | Nenhum |
| F9 | 143 | Nenhum |
| F10 | 144 | Nenhum |
| HOME | 147 | Nenhum |
| UPARROW | 148 | Nenhum |
| PGUP | 149 | Nenhum |
| LEFTARROW | 14B | Nenhum |
| RIGHTARROW | 14D | Nenhum |
| END | 14F | Nenhum |
| DNARROW | 150 | Nenhum |
| PGDN | 151 | Nenhum |
| INS | 152 | Nenhum |
| DEL | 153 | Nenhum |
| F11 | 185 | Nenhum |
| F12 | 186 | Nenhum |
| BACKTAB | 10F | shiftKey |
| SHIFT+F1 | 154 | shiftKey |
| SHIFT+F2 | 155 | shiftKey |
| SHIFT+F3 | 156 | shiftKey |
| SHIFT+F4 | 157 | shiftKey |
| SHIFT+F5 | 158 | shiftKey |
| SHIFT+F6 | 159 | shiftKey |
| SHIFT+F7 | 15A | shiftKey |
| SHIFT+F8 | 15B | shiftKey |
| SHIFT+F9 | 15C | shiftKey |
| SHIFT+F10 | 15D | shiftKey |
| SHIFT+F11 | 187 | shiftKey |
| SHIFT+F12 | 188 | shiftKey |
| CTRL+A | 001 | ctrlKey |
| CTRL+B | 002 | ctrlKey |
| CTRL+C | 003 | ctrlKey |
| CTRL+D | 004 | ctrlKey |
| CTRL+E | 005 | ctrlKey |
| CTRL+F | 006 | ctrlKey |
| CTRL+G | 007 | ctrlKey |
| CTRL+H | 008 | ctrlKey |
| CTRL+I | 009 | ctrlKey |
| CTRL+ENTER | 00A | ctrlKey |
| CTRL+J | 00A | ctrlKey |
| CTRL+K | 00B | ctrlKey |
| CTRL+L | 00C | ctrlKey |
| CTRL+M | 00D | ctrlKey |
| CTRL+N | 00E | ctrlKey |
| CTRL+O | 00F | ctrlKey |
| CTRL+P | 010 | ctrlKey |
| CTRL+Q | 011 | ctrlKey |
| CTRL+R | 012 | ctrlKey |
| CTRL+S | 013 | ctrlKey |
| CTRL+T | 014 | ctrlKey |
| CTRL+U | 015 | ctrlKey |
| CTRL+V | 016 | ctrlKey |
| CTRL+W | 017 | ctrlKey |
| CTRL+X | 018 | ctrlKey |
| CTRL+Y | 019 | ctrlKey |
| CTRL+Z | 01A | ctrlKey |
| CTRL+LBRACKET | 01B | ctrlKey |
| CTRL+BACKSLASH | 01C | ctrlKey |
| CTRL+RBRACKET | 01D | ctrlKey |
| CTRL+CARET | 01E | ctrlKey+shiftKey |
| CTRL+HYPHEN | 01F | ctrlKey |
| CTRL+SPACEBAR | 020 | ctrlKey |
| CTRL+F1 | 15E | ctrlKey |
| CTRL+F2 | 15F | ctrlKey |
| CTRL+F3 | 160 | ctrlKey |
| CTRL+F4 | 161 | ctrlKey |
| CTRL+F5 | 162 | ctrlKey |
| CTRL+F6 | 163 | ctrlKey |
| CTRL+F7 | 164 | ctrlKey |
| CTRL+F8 | 165 | ctrlKey |
| CTRL+F9 | 166 | ctrlKey |
| CTRL+F10 | 167 | ctrlKey |
| CTRL+LEFTARROW | 173 | ctrlKey |
| CTRL+RIGHTARROW | 174 | ctrlKey |
| CTRL+END | 175 | ctrlKey |
| CTRL+PGDN | 176 | ctrlKey |
| CTRL+HOME | 177 | ctrlKey |
| CTRL+PGUP | 184 | ctrlKey |
| CTRL+F11 | 189 | ctrlKey |
| CTRL+F12 | 18A | ctrlKey |
| CTRL+UPARROW | 18D | ctrlKey |
| CTRL+DNARROW | 191 | ctrlKey |
| CTRL+INS | 192 | ctrlKey |
| CTRL+DEL | 193 | ctrlKey |
| CTRL+TAB | 194 | ctrlKey |
| ALT+Q | 110 | altKey |
| ALT+W | 111 | altKey |
| ALT+E | 112 | altKey |
| ALT+R | 113 | altKey |
| ALT+T | 114 | altKey |
| ALT+Y | 115 | altKey |
| ALT+U | 116 | altKey |
| ALT+I | 117 | altKey |
| ALT+O | 118 | altKey |
| ALT+P | 119 | altKey |
| ALT+A | 11E | altKey |
| ALT+S | 11F | altKey |
| ALT+D | 120 | altKey |
| ALT+F | 121 | altKey |
| ALT+G | 122 | altKey |
| ALT+H | 123 | altKey |
| ALT+J | 124 | altKey |
| ALT+K | 125 | altKey |
| ALT+L | 126 | altKey |
| ALT+Z | 12C | altKey |
| ALT+X | 12D | altKey |
| ALT+C | 12E | altKey |
| ALT+V | 12F | altKey |
| ALT+B | 130 | altKey |
| ALT+N | 131 | altKey |
| ALT+M | 132 | altKey |
| ALT+F1 | 168 | altKey |
| ALT+F2 | 169 | altKey |
| ALT+F3 | 16A | altKey |
| ALT+F4 | 16B | altKey |
| ALT+F5 | 16C | altKey |
| ALT+F6 | 16D | altKey |
| ALT+F7 | 16E | altKey |
| ALT+F8 | 16F | altKey |
| ALT+F9 | 170 | altKey |
| ALT+F10 | 171 | altKey |
| ALT+1 | 178 | altKey |
| ALT+2 | 179 | altKey |
| ALT+3 | 17A | altKey |
| ALT+4 | 17B | altKey |
| ALT+5 | 17C | altKey |
| ALT+6 | 17D | altKey |
| ALT+7 | 17E | altKey |
| ALT+8 | 17F | altKey |
| ALT+9 | 180 | altKey |
| ALT+0 | 181 | altKey |
| ALT+F11 | 18B | altKey |
| ALT+F12 | 18C | altKey |
| ALT+HOME | 197 | altKey |
| ALT+UPARROW | 198 | altKey |
| ALT+PGUP | 199 | altKey |
| ALT+LEFTARROW | 19B | altKey |
| ALT+RIGHTARROW | 19D | altKey |
| ALT+END | 19F | altKey |
| ALT+DNARROW | 1A0 | altKey |
| ALT+PGDN | 1A1 | altKey |
| ALT+INS | 1A2 | altKey |
| ALT+DEL | 1A3 | altKey |

# Exemplo

```foxpro
FAR EventHandler(WHandle theWindow, EventRec FAR *ev)
{
switch(ev->what)
{
case keyDownEvent:                  /* Check the keyDownEvent */
if (ev->modifiers & shiftCodeMask)      /* A modifier was pressed. */
{
if (ev->modifiers & altKey)            /* Check for the ALT Key */
_PutStr("ALT Key Code should be used.\n");
else
if (ev->modifiers & ctrlKey)         /* CTRL Key */
_PutStr("CTRL Key Code should be used.\n");
else
if (ev->modifiers & shiftKey)         /* SHIFT Key */
_PutStr("SHIFT Key Code should be used.\n");
}
else
_PutStr("Regular Key Code should be used.\n");
return NO;                        /* Let Visual FoxPro have Key also */
break;
default:
return NO;
}
}
```

> **Observação:** shiftCodeMask, altKey, ctrlKey e shiftKey são definidos em PRO_EXT.H e PRO_EXT.INC da seguinte forma:
 - #define shiftCodeMask 0xf000
- #define shiftKey 0x1000
- #define ctrlKey 0x2000
- #define altKey 0x4000
