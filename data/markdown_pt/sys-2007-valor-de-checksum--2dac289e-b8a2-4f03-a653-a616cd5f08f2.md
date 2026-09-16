# SYS(2007) - Valor de checksum

Retorna o valor de checksum de uma expressão de caractere. Você pode usar um checksum para testar a validade dos dados ou comparar duas expressões de caractere. Você também pode gerar valores de checksum maiores que 16 bits para cadeias de caracteres grandes.

SYS(2017) oferece funcionalidade complementar gerando valores de checksum baseados no registro atual na área de trabalho atual. Para obter mais informações, consulte SYS(2017) - Valor de checksum de registro.

```foxpro
SYS(2007, cExpression, [, nSeed, [, nFlags]])
```

#### Parâmetros
 **cExpression**
Especifica uma expressão de caractere (cadeia de caracteres) para a qual SYS(2007) retorna um valor de checksum.
**nSeed**
Especifica um valor numérico de semente de 0 que é usado para calcular o checksum e é incluído para compatibilidade com versões anteriores. Passar um valor de -1 para nSeed usa o valor padrão do sistema de 0. Para cálculos CRC32, o Visual FoxPro desconsidera nSeed .
**nFlags**
Define um valor de bit adicional para gerar o checksum. Versões do Visual FoxPro anteriores à 8.0 usavam um algoritmo CRC16 de 16 bits para calcular os valores de checksum de cadeias de caracteres. O Visual FoxPro agora inclui a rotina CRC32 para calcular valores maiores de 32 bits. Você pode controlar a configuração deste algoritmo definindo o primeiro valor de bit do parâmetro nFlags . A tabela a seguir lista o valor de bit que você pode definir para produzir um dos valores para nFlags . Valor Bit Descrição 1 001 Calcula o valor de checksum usando o algoritmo de checksum CRC32. A tabela a seguir lista os valores possíveis para nFlags , produzidos pela definição do sinalizador de bit. nFlags Descrição 0 Calcula o checksum baseado no parâmetro cExpression usando o algoritmo de checksum CRC16. (Padrão) 1 Calcula o checksum baseado no parâmetro cExpression usando o algoritmo de checksum CRC32. Por exemplo, se você quiser usar checksum com o algoritmo de checksum CRC32 para calcular o checksum baseado em cExpression , você deve especificar um valor nFlags de 1. Para usar o algoritmo de checksum CRC16, defina o valor nFlags como 0.

# Valor de retorno

Tipo de dados Caractere
