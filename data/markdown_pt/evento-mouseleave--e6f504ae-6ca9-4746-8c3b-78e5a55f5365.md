# Evento MouseLeave

Ocorre quando o cursor do mouse sai de um controle

```foxpro
PROCEDURE Object.MouseLeave
LPARAMETERS nButton, nShift, nXCoord, nYCoord
```

#### Parâmetros
 **nButton**
Contém um número que especifica qual botão foi pressionado para disparar o evento: 1 (esquerdo), 2 (direito) ou 4 (meio).
**nShift**
Contém um número que especifica o estado das teclas modificadoras quando o mouse é pressionado. As teclas modificadoras válidas são as teclas SHIFT, CTRL e ALT. Os valores retornados em nShift para teclas modificadoras individuais estão listados na tabela a seguir. Valores de tecla modificadora para nShift Windows key Value SHIFT 1 CTRL 2 ALT 4 Se mais de uma tecla modificadora for mantida pressionada quando o mouse é pressionado, o argumento nShift contém a soma dos valores das teclas modificadoras. Por exemplo, se o usuário mantiver CTRL pressionado ao clicar com o mouse, o argumento nShift contém 2. Mas se o usuário mantiver CTRL+ALT pressionados ao clicar com o mouse, o argumento nShift contém 6.
**nXCoord , nYCoord**
Contém a posição horizontal ( nXCoord ) e vertical ( nYCoord ) atual do ponteiro do mouse dentro do formulário. Essas coordenadas são expressas em termos do sistema de coordenadas do formulário na unidade de medida especificada pela propriedade ScaleMode do formulário.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | EditBox Control | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro)

Você pode usar este evento e o evento MouseEnter para criar comportamentos rollover e mouseover como em DHTML.

Um controle recebe um evento MouseLeave quando o usuário move o mouse para fora do controle a partir de uma posição do mouse que estava previamente dentro do controle. No caso de controles sobrepostos ou que se intersectam, o controle mais superior na ordem z recebe o evento.

Um evento MouseLeave é passado para objetos em formulários ou toolbars. Formulários e toolbars em si não recebem este evento.
