# Caixa de diálogo Serviço Web XML - Valores de parâmetro

Permite definir valores de parâmetro ou especificar um controle e sua propriedade como origem de parâmetro para uma operação de serviço Web XML selecionada.

> **Observação:** Você pode especificar apenas tipos de dados simples nesta caixa de diálogo. Você pode definir tipos de dados complexos, como matrizes ou ADO.NET DataSets, programaticamente usando a coleção de parâmetros da operação.

Esta caixa de diálogo aparece quando você seleciona Input values now na caixa Set parameter(s) da Caixa de diálogo Serviço Web XML - Detalhe da operação.
 **Select parameter**
Especifica o parâmetro que você deseja definir.
**Parameter type**
Exibe o tipo de dados do parâmetro.
**Specify parameter source**
Especifica a origem que fornece o valor para o parâmetro selecionado. Value Especifica um valor particular para o parâmetro. O valor fornecido é automaticamente convertido para o tipo de dados correto exigido pelo parâmetro. Você também pode incluir uma expressão, que é avaliada em tempo de execução, prefixando-a com um sinal de igual (=). Por exemplo, você pode definir a data atual da seguinte forma: =DATE() Control/Property Exibe os controles disponíveis no formulário e especifica que a propriedade do controle ou objeto selecionado forneça o valor para o parâmetro. Ao selecionar um controle, uma lista de propriedades disponíveis para esse controle aparece para que você possa selecionar uma para fornecer o valor. Se você deseja que o usuário forneça o valor do parâmetro, pode selecionar a propriedade Value.
