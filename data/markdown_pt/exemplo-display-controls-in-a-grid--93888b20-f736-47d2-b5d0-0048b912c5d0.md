# Exemplo Display Controls in a Grid

Arquivo: ...\Samples\Solution\Controls\Grid\Controls.scx

Este exemplo demonstra controles exibidos em colunas de grade.

Você pode adicionar controles a uma coluna no Form Designer selecionando uma coluna e adicionando um controle, ou programaticamente com o método AddObject.

Há algumas propriedades que são importantes para exibir controles em uma coluna.

# Propriedade CurrentControl

Depois de adicionar um controle a uma coluna de grade, você precisa definir a propriedade CurrentControl da coluna para o novo controle para que o novo controle seja exibido.

# Propriedade Sparse

As caixas de seleção no formulário permitem alternar a propriedade Sparse das colunas de grade que contêm controles. Quando Sparse está definido como .T., o controle é exibido apenas quando o foco está em uma célula na coluna. Quando Sparse está definido como .F., o controle é sempre exibido em cada célula na coluna.

# Controles e Eventos

Observe que o controle na coluna processa os eventos quando você define o foco em uma célula na coluna. Por exemplo, se você selecionar uma célula em uma coluna com um spinner, quando pressionar as setas para cima e para baixo, incrementa ou decrementa o valor no spinner. Este é o comportamento padrão para um spinner, não o comportamento padrão para uma caixa de texto em uma célula de grade.
