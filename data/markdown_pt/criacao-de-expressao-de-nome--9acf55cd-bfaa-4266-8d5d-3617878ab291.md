# Criação de expressão de nome

Muitos comandos e funções do Visual FoxPro exigem que você forneça um nome. Embora um nome não possa ser uma variável ou um elemento de matriz, você pode criar uma expressão de nome que substitui o valor de uma variável Character ou elemento de matriz como o nome.

Quando você armazena o nome na variável ou elemento de matriz, pode substituir o nome em um comando ou função colocando a variável entre parênteses. Para usar uma lista de nomes, separe os nomes com vírgulas. Um nome não é uma expressão, uma variável ou elemento de matriz, ou um campo. Um nome não deve ser cercado por aspas. Caso contrário, os nomes seguem as regras de nomenclatura do Visual FoxPro descritas na seção Criando nomes do Visual FoxPro.

Por exemplo, o comando REPLACE exige um nome de campo. Você pode armazenar um nome de campo em uma variável e usar uma expressão de nome em REPLACE onde o nome do campo ocorre:

```foxpro
STORE 'city' TO cVarCity
REPLACE (cVarCity) WITH 'Paris'
```

O Visual FoxPro armazena o nome do campo `city` na variável `cVarCity`, então armazena o valor "Paris" no campo, `city`, que é o valor da expressão de nome `cVarCity`.

Para obter mais informações, consulte Comando STORE e Comando REPLACE (Visual FoxPro).
