# Guia Geral, caixa de diálogo Propriedades da faixa de relatório (Construtor de Relatórios)

Permite especificar opções gerais para faixas de relatório no Designer de Relatórios ou no Designer de Etiquetas.

> **Observação:** Este guia substitui a funcionalidade da caixa de diálogo nativa Propriedades da faixa de relatório do Visual FoxPro quando o Construtor de Relatórios está ativo.
 - Como: alterar a altura da faixa de relatório
- Como: especificar expressões a serem avaliadas durante o processamento de faixas
- Como: configurar a saída de faixas de relatório

# Opções de faixa

As opções a seguir permitem especificar a formatação e o comportamento das faixas de relatório.
 **Group expression**
(Somente faixas Group Header e Group Footer) Especifica a expressão usada pelo mecanismo de relatório para determinar quando "interromper" a renderização da faixa de detalhes. As informações do cabeçalho e do rodapé do grupo são renderizadas sempre que o resultado da expressão muda. Expressões vazias não são válidas. Você pode digitar ou criar uma expressão clicando no botão de reticências ( … ). Para obter mais informações, consulte a caixa de diálogo Construtor de Expressões.
**Height**
Especifica a altura da faixa. A altura da faixa de relatório determina a quantidade de espaço usada por cada faixa na página, dentro das margens. As unidades desse controle spinner dependem da configuração das unidades da régua de medida do layout do relatório. Para obter mais informações, consulte Como: configurar a grade do layout de página para relatórios. Por exemplo, se a faixa de título estiver definida como meia polegada, as informações dessa faixa aparecerão na primeira meia polegada da página após a margem superior. Dica Ao adicionar itens a uma faixa de relatório, talvez seja necessário alterar sua altura para acomodar o conteúdo. Como referência para determinar a altura, use a régua à esquerda da faixa. A medida da régua é específica à altura da faixa e não inclui as margens da página. Observação Ao reduzir a altura de uma faixa, não é possível deixá-la menor que a altura dos controles no layout. Se os controles impedirem o redimensionamento, mova-os e depois reduza a altura.
**Constant band height**
Impede que a faixa seja expandida para acomodar dados longos ou ajustada por causa de linhas em branco suprimidas. Para obter mais informações, consulte Como: suprimir linhas em branco em controles de relatório.

# Executar expressão

Especifica expressões a serem avaliadas antes e depois do processamento da faixa de relatório.
 **On entry**
Especifica uma expressão a ser avaliada antes do processamento da faixa. Para criar uma expressão, clique no botão de reticências ( … ) para abrir o Construtor de Expressões. Para obter mais informações, consulte a caixa de diálogo Construtor de Expressões.
**On exit**
Especifica uma expressão a ser avaliada após o processamento da faixa. Para criar uma expressão, clique no botão de reticências ( … ) para abrir o Construtor de Expressões. Para obter mais informações, consulte a caixa de diálogo Construtor de Expressões.
