# Exemplo Usar formatação condicional em um relatório

Arquivo: ...\Samples\Solution\Reports\Colors.frx

Este relatório de exemplo demonstra como você pode usar condições Print When para controles para alterar a formatação de campos com base nos valores no registro. O exemplo imprime um "Product Inventory Report." Se o item do produto está descontinuado, é impresso em tachado. Se a quantidade In Stock está abaixo do nível de reordenação e o produto não está descontinuado, o item é impresso em vermelho. Caso contrário, o item do produto é impresso em preto padrão.

Este relatório usa a tabela PRODUCTS, do banco de dados TESTDATA, no Data Environment. A banda Detail tem controles de campo para as informações do produto, como ID, nome, quantidade em estoque e quantidade em pedido. Outro controle de campo imprime um lembrete quando o estoque fica abaixo de uma quantidade de reordenação definida.

Para tratar os três casos, três conjuntos de controles de campo para as informações do produto são sobrepostos na banda Detail. Para o primeiro conjunto, a cor do texto é vermelha; para o segundo, a cor é preta; e para o terceiro, o efeito de fonte é Strikeout.

Cada conjunto de controles tem uma expressão Print When diferente.
 - Para os campos pretos simples: (products.in_stock > products.reorder_at) and products.discontinu = .F.
- Para os campos tachados: products.discontinu = .T.
- Para os campos com cor de texto vermelha: products.in_stock <= products.reorder_at and products.discontinu = .F.
