# Como: usar objetos Grid

O grid é um objeto contêiner. Assim como um form set pode conter formulários, um grid pode conter colunas. Além disso, as colunas contêm cabeçalhos e controles, cada um com seu próprio conjunto de propriedades, eventos e métodos, proporcionando grande controle sobre os elementos do grid.

| Contêiner | Pode conter |
| --- | --- |
| Grid | Columns |
| Column | Headers, controls |

O objeto Grid torna possível apresentar e manipular linhas e colunas de dados em um formulário ou página. Uma aplicação particularmente útil do controle Grid é criar formulários um-para-muitos, como um formulário de fatura.

### Para adicionar um controle Grid a um formulário
- Na barra de ferramentas Form Controls, escolha o botão Grid e arraste para dimensionar na janela Form.

Se você não especificar um valor para a propriedade RecordSource do grid e houver uma tabela aberta na área de trabalho atual, o grid exibirá todos os campos dessa tabela.

Por padrão, um controle grid é criado quando você arrasta uma tabela para um formulário.

### Para criar um controle grid
- Escolha qualquer tabela no Data Environment, Database Designer (Visual FoxPro) ou Project Manager Window e arraste-a para um formulário.

Você pode substituir o padrão e criar vários controles correspondentes aos mapeamentos de tipo de campo padrão especificados para cada campo na tabela. Para obter mais informações, consulte Como: criar controles arrastando e soltando campos ou tabelas.

### Definindo o número de colunas em um Grid

Uma das primeiras propriedades que você pode querer definir para o controle Grid é o número de colunas.

### Para definir o número de colunas em um grid
- Selecione a propriedade ColumnCount na lista Property and Methods.
- Na caixa Property, digite o número de colunas desejado.

Se a propriedade ColumnCount estiver definida como - 1 (o padrão), o grid conterá, em tempo de execução, tantas colunas quantos campos houver na tabela associada ao grid.

### Adicionando registros a um Grid

Você pode permitir que os usuários adicionem novos registros a uma tabela exibida em um grid definindo a propriedade AllowAddNew do grid como true (.T.). Quando a propriedade AllowAddNew está definida como true, novos registros são adicionados à tabela quando o último registro é selecionado e o usuário pressiona a tecla DOWN ARROW.

Se desejar mais controle sobre quando um usuário adiciona novos registros a uma tabela, você pode definir a propriedade AllowAddNew como false (.F.), o padrão, e usar os comandos APPEND Command ou INSERT Command para adicionar novos registros.

### Para ver exemplos de uso de grids
- Execute Solution.app no diretório Visual FoxPro ...\Samples\Solution.
- Na exibição em árvore, clique em Controls e depois em Grid.
