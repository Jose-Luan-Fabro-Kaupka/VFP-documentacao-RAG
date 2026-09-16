# Como: exportar dados para novos arquivos

Você pode copiar todos os campos e registros da sua tabela Visual FoxPro para um novo arquivo ou pode copiar somente os campos e registros que selecionar.

### Para exportar dados
- No menu File, escolha Export .
- Na caixa Type, insira o tipo de arquivo de destino.
- Na caixa To, insira o nome do arquivo de destino.
- Na caixa From, insira o nome do arquivo de origem.
- Se desejar selecionar campos ou registros para exportar, escolha Options e complete a caixa de diálogo Export Options.
- Escolha OK .

Por padrão, o Visual FoxPro exporta todos os campos da tabela de origem para o arquivo de destino. Você pode selecionar quais campos exportar usando a caixa de diálogo Export Options.

### Para selecionar campos para exportar
- No menu File, escolha Export .
- Na caixa de diálogo Export, insira o tipo e o nome do arquivo de destino.
- Na caixa From, insira o nome do arquivo de origem.
- Escolha Options .
- Escolha Fields e selecione os campos na caixa de diálogo Field Picker.
- Escolha OK .

Ao exportar dados, talvez você deseje limitar o número de registros copiados para o novo arquivo fornecendo critérios de seleção. Você pode:
 - Escolher um escopo de registros especificando uma quantidade ou intervalo.
- Criar uma expressão FOR que seleciona registros que correspondem a uma condição.
- Criar uma expressão WHILE que seleciona registros até que um registro seja encontrado que não corresponda a uma condição.

Você pode usar qualquer combinação dessas opções. A expressão WHILE substitui os outros critérios.
