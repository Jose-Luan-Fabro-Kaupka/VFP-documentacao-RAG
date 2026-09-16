# Controle PageFrame

Cria um page frame para conter objetos Page.

Um page frame é um objeto contêiner que contém páginas, que podem conter controles.

> **Observação:** Para que um page frame seja visível, ele deve ser adicionado a um formulário.

```foxpro
PageFrame
```

# Observações

O page frame define características globais da página: tamanho e posicionamento, estilo de borda, qual página está ativa e assim por diante. O page frame determina a localização das páginas e quanto de cada página é visível. As páginas são posicionadas no canto superior esquerdo do page frame. Se o page frame é movido, as páginas se movem com ele.

Um page frame contém páginas individuais que são nomeadas Page1, Page2, Page3 e assim por diante por padrão.

> **Observação:** Somente a página ativa é atualizada quando ocorre o método Refresh do Form para o formulário no qual a página está localizada.

A propriedade Themes do PageFrame fornece um efeito de gradiente nos objetos Page, portanto um label, option button ou controle semelhante com texto não aparece corretamente se a propriedade BackStyle do controle estiver definida como Opaque. Você pode corrigir essa situação definindo BackStyle como Transparent.

Para informações adicionais sobre como criar páginas e page frames, consulte "Adding Page Frames to a Form" em Controls for Extending Forms.
