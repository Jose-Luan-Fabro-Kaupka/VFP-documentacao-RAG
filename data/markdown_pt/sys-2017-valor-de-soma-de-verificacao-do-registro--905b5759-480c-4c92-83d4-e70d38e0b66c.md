# SYS(2017) - Valor de soma de verificação do registro

Retorna um valor de soma de verificação baseado no registro atual na área de trabalho atual. Você pode usar uma soma de verificação para testar a validade dos dados. Você também pode gerar valores de soma de verificação maiores que 16 bits para cadeias de caracteres grandes.

SYS(2017) oferece funcionalidade complementar a SYS(2007) - Valor de soma de verificação.

```foxpro
SYS(2017, cExpression [, nSeed [, nFlags]])
```

#### Parâmetros
 **cExpression**
Especifica uma lista separada por vírgulas, com ou sem espaços, contendo um ou mais campos a excluir do cálculo da soma de verificação. O comprimento máximo da cadeia de campos é limitado a 256 caracteres. Se cExpression estiver vazio, o Visual FoxPro não exclui campos, exceto campos Memo e General.
**nSeed**
Especifica um valor de semente numérico de 0 que é usado para calcular a soma de verificação e é incluído para compatibilidade com versões anteriores. Passar um valor de -1 para nSeed usa o valor padrão do sistema de 0. Para cálculos CRC32, o Visual FoxPro ignora nSeed .
**nFlags**
Especifica valores de bits aditivos para gerar a soma de verificação. Versões do Visual FoxPro anteriores à 8.0 usavam um algoritmo CRC16 de 16 bits para calcular os valores de soma de verificação de cadeias de caracteres. O Visual FoxPro agora inclui a rotina CRC32 para calcular valores maiores de 32 bits. Você pode controlar a configuração deste algoritmo definindo o primeiro valor de bit do parâmetro nFlags. A tabela a seguir lista os valores de bit que você pode adicionar para produzir um valor para nFlags . Valor Bits Descrição 1 001 Calcula o valor de soma de verificação usando o algoritmo de soma de verificação CRC32. 2 010 Inclui campos Memo no cálculo da soma de verificação. Você pode usar o segundo bit de nFlags para incluir campos Memo no cálculo CRC. O Visual FoxPro inclui todos os campos Memo, exceto os especificados por cExpression, no cálculo. A tabela a seguir lista os valores possíveis para nFlags , produzidos pela soma dos sinalizadores de bit. nFlags Descrição 0 Calcula a soma de verificação baseada no parâmetro cExpression usando o algoritmo de soma de verificação CRC16. (Padrão) 1 Calcula a soma de verificação baseada no parâmetro cExpression usando o algoritmo de soma de verificação CRC32. 2 Calcula a soma de verificação baseada no conteúdo do registro atual incluindo campos Memo usando CRC16. 3 Calcula a soma de verificação baseada no conteúdo do registro atual incluindo campos Memo usando CRC32.

# Valor de retorno

Tipo de dados Character. SYS(2017) retorna um valor de soma de verificação.

# Observações

Ao calcular o valor de soma de verificação do registro atual, o Visual FoxPro ignora campos Memo e General, a menos que nFlags esteja definido como 2 ou 3.

O Visual FoxPro gera a soma de verificação baseada no registro atual na área de trabalho atual e passa os valores de byte da cadeia de caracteres para a rotina CRC32.

O Visual FoxPro retorna um valor de "0" se nenhum cursor estiver aberto na área de trabalho atual ou se o ponteiro de registro não for válido, por exemplo, apontando para um registro fantasma.

Quando você cria uma expressão de cadeia de caracteres a partir de um registro, o Visual FoxPro remove espaços em branco à direita e retorna a expressão como uma cadeia de caracteres, semelhante à função ALLTRIM( ).

Normalmente, o Visual FoxPro usa quaisquer campos excluídos especificados por cExpression para armazenar o valor de soma de verificação e não os inclui no cálculo. O Visual FoxPro não realiza nenhuma verificação no tipo de dados desses campos. Se cExpression contiver um campo inválido, o Visual FoxPro ignora esse campo.

O Visual FoxPro calcula a soma de verificação de todos os campos incluídos, exceto Memo, General e os especificados por cExpression. Você pode determinar os campos usados e sua ordem usando a função FIELD( ). Se você especificou uma configuração para SET FIELDS, a soma de verificação é calculada baseada na lista atual especificada por SET FIELDS, que pode incluir campos calculados.

Campos calculados são campos temporários que existem no cursor atual baseados em uma expressão, mas não são definidos na estrutura real da tabela. Por exemplo, o campo LOCATION é um campo calculado:

```foxpro
Use Customer
SET FIELDS TO LOCATION = ALLTRIM(city) + ',' + state
```
