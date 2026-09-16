# Evento KeyPress

Ocorre quando o usuário pressiona e libera uma tecla. Você pode usar o evento KeyPress para interceptar teclas digitadas em um controle. Você também pode testar teclas imediatamente para validade ou formatar caracteres conforme são digitados. Use a propriedade KeyPreview para criar rotinas globais de tratamento de teclado.

```foxpro
PROCEDURE Object.KeyPress
LPARAMETERS nKeyCode, nShiftAltCtrl
```

#### Parâmetros
 **nKeyCode**
Contém um número que identifica a tecla pressionada. Para uma lista de códigos de teclas especiais e combinações de teclas, consulte INKEY( ).
**nShiftAltCtrl**
Define um bit específico se uma tecla modificadora for mantida pressionada ao pressionar a tecla especificada por nKeyCode. As teclas modificadoras válidas são as teclas SHIFT, CTRL e ALT. A tabela a seguir lista os valores da tecla modificadora para nShiftAltCtrl. nShiftAltCtrl Tecla modificadora 1 SHIFT 2 CTRL 4 ALT Este parâmetro é a soma dos bits, com os bits menos significativos correspondendo à tecla SHIFT (bit 0), à tecla CTRL (bit 1) e à tecla ALT (bit 2). Esses bits correspondem aos valores 1, 2 e 4, respectivamente. Este parâmetro indica o estado dessas teclas. Alguns, todos ou nenhum dos bits pode estar definido, indicando que algumas, todas ou nenhuma das teclas está pressionada. Por exemplo, se CTRL e ALT estiverem pressionados, o valor de nShiftAltCtrl é 6.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | EditBox Control | Form Object | Grid Control | ListBox Control | OptionButton Control | Spinner Control | TextBox Control (Visual FoxPro)

O evento KeyPress não ocorre para nenhuma combinação de teclas com a tecla ALT.

O objeto com o foco recebe o evento KeyPress.

Um formulário pode receber o evento KeyPress em três casos especiais:
 - O formulário não contém controles, ou nenhum de seus controles está visível e habilitado.
- A propriedade KeyPreview do formulário está definida como True (.T.). O formulário recebe primeiro o evento KeyPress e, em seguida, o controle com foco recebe o evento.
- O controle no formulário não pode processar uma tecla, por exemplo, quando TAB é pressionado para mover o foco para o próximo controle.

Se a propriedade AllowCellSelection de uma grade estiver definida como True (.T.), o Visual FoxPro ignora o evento KeyPress da Grade e usa o evento no nível da célula individual.
