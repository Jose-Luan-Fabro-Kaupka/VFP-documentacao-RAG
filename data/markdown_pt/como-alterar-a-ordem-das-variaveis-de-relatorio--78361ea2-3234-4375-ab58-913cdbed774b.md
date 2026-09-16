# Como: alterar a ordem das variáveis de relatório

O Visual FoxPro avalia as variáveis de relatório na ordem em que aparecem na caixa de diálogo Variáveis de relatório, o que pode afetar o valor de expressões que fazem referência a elas. Por exemplo, suponha que uma variável de relatório `tTotal` seja especificada como contendo os resultados da soma de duas outras variáveis de relatório, `tDelivered` e `tOutstanding`. Essas duas variáveis devem aparecer na lista de variáveis de relatório antes de `tTotal`, caso contrário o valor de `tTotal` pode estar incorreto.

> **Cuidado:** Se você alterar a ordenação dos grupos de dados no relatório, as variáveis de relatório podem não ser redefinidas no campo correto. Por exemplo, se seu relatório tem dois grupos de dados e você alterar a ordem dos dois grupos, as variáveis permanecem definidas nas posições originais desses grupos.

### Para alterar a ordem das variáveis de relatório
- Abra o relatório ou etiqueta no designer apropriado.
- No menu Relatório, clique em Variáveis . A caixa de diálogo Propriedades do relatório é aberta. Observação Se a variável de sistema _REPORTBUILDER não estiver definida para o Report Builder padrão ou estiver definida para um construtor de terceiros, a caixa de diálogo Variáveis de relatório é exibida ou uma caixa de diálogo diferente pode ser exibida. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER e Caixa de diálogo Variáveis de relatório .
- Na caixa de diálogo Propriedades do relatório, clique na guia Variáveis se ela não estiver selecionada.
- Na lista Variáveis, arraste o botão de movimentação à esquerda da variável para a posição desejada.
- Quando terminar, clique em OK .

Para obter mais informações, consulte Guia Variáveis, caixa de diálogo Propriedades do relatório (Report Builder).
