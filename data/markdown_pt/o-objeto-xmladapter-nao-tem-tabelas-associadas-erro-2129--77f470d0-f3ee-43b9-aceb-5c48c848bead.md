# O objeto XMLAdapter não tem tabelas associadas. (Erro 2129)

O Visual FoxPro exige que um ou mais objetos XMLTable estejam associados a um objeto XMLAdapter antes de tentar chamar o método ToXML.
 - Execute o método AddTableSchema dos objetos XMLAdapter para criar as coleções XMLTable e XMLField, ou crie esses itens de outra forma.
