# Evento MouseEnter

Ocorre quando um cursor do mouse entra em um controle

```foxpro
PROCEDURE Object.MouseEnter
LPARAMETERS nButton, nShift, nXCoord, nYCoord
```

#### Parâmetros
 **nButton**
Contém um número que especifica qual botão foi pressionado para disparar o evento: 1 (esquerdo), 2 (direito) ou 4 (meio).
**nShift**
Contém um número especificando o estado das teclas modificadoras quando o mouse é pressionado. As teclas modificadoras válidas são as teclas SHIFT, CTRL e ALT. Os valores retornados em nShift para teclas modificadoras individuais estão listados na tabela a seguir. Valores de tecla modificadora para nShift Tecla Windows Valor SHIFT 1 CTRL 2 ALT 4 Se mais de uma tecla modificadora é mantida pressionada quando o mouse é pressionado, o argumento nShift contém a soma dos valores das teclas modificadoras. Por exemplo, se o usuário mantém CTRL pressionado ao pressionar o botão do mouse, o argumento nShift contém 2. Mas se o usuário mantém CTRL+ALT pressionado ao pressionar o botão do mouse, o argumento nShift contém 6.
**nXCoord , nYCoord**
Contém a posição horizontal ( nXCoord ) e vertical ( nYCoord ) atual do ponteiro do mouse dentro do formulário. Essas coordenadas são expressas em termos do sistema de coordenadas do formulário na unidade de medida especificada pela propriedade ScaleMode do formulário.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | EditBox Control | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro)

Você pode usar este e o evento MouseLeave para criar comportamentos de rollover e mouseover como em DHTML.

Um controle recebe um evento MouseEnter quando o usuário move o mouse para dentro de um controle a partir de uma posição do mouse que estava anteriormente fora do controle. No caso de controles sobrepostos ou que se intersectam, o controle mais superior na ordem z recebe o evento.

Um evento MouseEnter é passado para objetos em formulários ou barras de ferramentas. Formulários e barras de ferramentas em si não recebem este evento.
