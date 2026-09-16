# O objeto XMLField já está associado ao objeto XMLTable. (Erro 2144)

O Visual FoxPro não permite que objetos XMLField sejam adicionados à coleção XMLField de um objeto XMLTable quando já estão associados a outro objeto XMLTable.
 - Você pode verificar se um objeto XMLField já está associado a um objeto XMLTable verificando sua propriedade XMLTable. Se não estiver associado, o valor da propriedade XMLTable será NULL. Caso contrário, retornará uma referência de objeto ao objeto XMLTable proprietário.
