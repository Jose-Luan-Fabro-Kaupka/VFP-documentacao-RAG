# O objeto pai não permitirá esta configuração de propriedade para "name" (Erro 1767)

Você tentou definir um valor de propriedade em um objeto cujo pai está controlando a configuração dessa propriedade.

Por exemplo, quando você tenta definir a propriedade ControlSource de um controle contido em uma coluna de grade e a propriedade Bound da coluna da grade foi definida como true (.T.), você receberá esta mensagem de erro porque a propriedade ControlSource do controle é obtida da propriedade ControlSource da coluna da grade.
