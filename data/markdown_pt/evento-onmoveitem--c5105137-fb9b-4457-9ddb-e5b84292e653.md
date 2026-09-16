# Evento OnMoveItem

Ocorre quando você seleciona e move um item para cima ou para baixo em uma caixa de listagem usando o mouse, o teclado ou programaticamente com o método MoveItem.

```foxpro
PROCEDURE OnMoveItem
LPARAMETERS nSource, nShift, nCurrentIndex, nMoveBy
```

#### Parâmetros
 **nSource**
Contém um número que especifica como o evento é disparado. nSource Descrição 0 Teclado 1 Botão esquerdo do mouse 2 Botão direito do mouse 4 Botão do meio do mouse 8 Disparado programaticamente pelo método MoveItem
**nShift**
Contém um número que especifica quais teclas modificadoras, SHIFT, CTRL e ALT, também estão pressionadas quando o botão do mouse é pressionado. A tabela a seguir lista os valores retornados por nShift para teclas modificadoras individuais. nShift Descrição 1 SHIFT 2 CTRL 4 ALT Se mais de uma tecla modificadora estiver pressionada quando o botão do mouse é pressionado, o argumento nShift contém a soma dos valores das teclas modificadoras. Por exemplo, se o usuário mantém CTRL pressionado ao clicar com o mouse, o argumento nShift contém o valor 2. No entanto, se o usuário mantém CTRL+ALT pressionado ao clicar com o mouse, o argumento nShift contém o valor 6.
**nCurrentIndex**
Contém o índice atual do item que está sendo movido.
**nMoveBy**
Indica quantas posições o item está sendo movido. Um valor positivo indica movimento para baixo. Um número negativo indica movimento para cima. O parâmetro nMoveBy sempre tem o valor 1 ou -1 se o usuário estiver movendo um item da lista usando o teclado. Geralmente tem o valor 1 ou -1 se o usuário estiver movendo um item da lista usando o mouse. No entanto, nMoveBy indica a posição para a qual o item é movido se o usuário arrastar o mouse para fora dos limites da caixa de listagem e depois de volta para uma posição distante.

# Observações

Aplica-se a: Controle ListBox

OnMoveItem ocorre após selecionar e mover um item pressionando CTRL+UP ARROW, CTRL+DOWN ARROW ou usando o mouse, ou ao chamar o método MoveItem programaticamente. OnMoveItem ocorre após cada movimento subsequente, mas antes que a caixa de listagem exiba o movimento do item. No entanto, OnMoveItem ocorre apenas uma vez ao chamar o método MoveItem programaticamente.

> **Observação:** Você pode mover itens do controle ListBox somente se a propriedade RecordSourceType da caixa de listagem estiver definida como 0 (None) ou 1 (Value).

Para impedir que o movimento ocorra, retorne False (.F.) do código no evento OnMoveItem.
