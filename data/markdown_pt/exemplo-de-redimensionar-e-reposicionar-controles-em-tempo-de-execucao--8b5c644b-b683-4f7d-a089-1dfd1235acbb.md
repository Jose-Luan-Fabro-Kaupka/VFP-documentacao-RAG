# Exemplo de redimensionar e reposicionar controles em tempo de execução

Arquivo: ...\Samples\Solution\Forms\Cresize.scx

Um usuário pode redimensionar este formulário de exemplo conforme desejado. Os controles no formulário são redimensionados ou reposicionados em relação às novas propriedades Height e Width do formulário.

Este formulário usa a classe resizable em ...\Samples\Classes\Samples.vcx para gerenciar o redimensionamento e o reposicionamento dos controles. A seguinte linha de código é adicionada ao evento Resize do formulário, chamando o método AdjustControls da classe resizable:

```foxpro
THIS.Resizable2.AdjustControls
```

No Init da classe resizable, o código percorre todos os controles no formulário, armazenando suas posições e tamanhos em relação ao formulário em um array. Quando o formulário é redimensionado, o método AdjustControls redimensiona e reposiciona os controles para seus tamanhos e posições relativos.

Você pode adicionar mais controles ao formulário e os novos controles também serão redimensionados e reposicionados.

As propriedades RepositionList e ResizeList contêm uma lista delimitada por espaços de todas as classes que você deseja reposicionar e redimensionar. Se você não deseja que uma determinada classe seja redimensionada, remova-a de ResizeList.

Você pode impedir que um usuário torne o formulário muito pequeno para os objetos contidos nele definindo as propriedades MinHeight e MinWidth do formulário.
