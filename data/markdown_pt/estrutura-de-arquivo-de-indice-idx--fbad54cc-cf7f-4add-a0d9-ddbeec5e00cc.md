# Estrutura de arquivo de índice (.idx)

Arquivos de índice contêm um registro de cabeçalho e um ou muitos registros de nó. O registro de cabeçalho contém informações sobre o nó raiz, o tamanho atual do arquivo, o comprimento da chave, opções e assinatura do índice e representações ASCII imprimíveis das expressões key1 e FOR. O registro de cabeçalho começa na posição zero do arquivo.

Os registros de nó restantes contêm um atributo, o número de chaves presentes e ponteiros para nós à esquerda e à direita (no mesmo nível) do nó atual. Eles também contêm um grupo de caracteres que abrange o valor da chave e um ponteiro para um nó de nível inferior ou um número de registro real da tabela. O tamanho de cada registro gravado em um arquivo é de 512 bytes.
 Registro de cabeçalho do índice
| Deslocamento de byte | Descrição |
| --- | --- |
| 00 – 03 | Ponteiro para o nó raiz |
| 04 – 07 | Ponteiro para a lista de nós livres ( -1 se não presente) |
| 08 – 11 | Ponteiro para o final do arquivo (tamanho do arquivo) |
| 12 – 13 | Comprimento da chave |
| 14 | Opções de índice (qualquer um dos seguintes valores numéricos ou suas somas): 1 – um índice exclusivo 8 – índice tem cláusula FOR |
| 15 | Assinatura do índice (para uso futuro) |
| 16 – 235 | Expressão de chave (não compilada; até 220 caracteres)1,3 |
| 236 – 455 | Expressão FOR (não compilada; até 220 caracteres terminando com um byte de valor nulo) |
| 456 – 511 | Não utilizado |
 Registro de nó do índice
| Deslocamento de byte | Descrição |
| --- | --- |
| 00 – 01 | Atributos do nó (qualquer um dos seguintes valores numéricos ou suas somas): 0 – nó de índice 1 – nó raiz 2 – nó folha |
| 02 – 03 | Número de chaves presentes (0, 1 ou muitas) |
| 04 – 07 | Ponteiro para o nó diretamente à esquerda do nó atual (no mesmo nível; -1 se não presente) |
| 08 – 11 | Ponteiro para o nó diretamente à direita do nó atual (no mesmo nível; -1 se não presente) |
| 12 – 511 | Até 500 caracteres contendo o valor da chave para o comprimento da chave com um número hexadecimal de quatro bytes armazenado no formato normal da esquerda para a direita: Se o nó é uma folha (atributo = 02 ou 03), os quatro bytes contêm um número real de tabela em formato hexadecimal; caso contrário, os 4 bytes contêm um ponteiro intra-índice.2 As combinações chave/número hexadecimal de quatro bytes ocorrerão o número de vezes indicado nos bytes 02 – 03. |

1 O tipo da chave não é armazenado no índice. Ele deve ser determinado pela expressão de chave.
2 Qualquer coisa que não seja cadeias de caracteres, números usados como valores de chave e os números de quatro bytes no nó folha são representados em bytes invertidos (formato Intel 8086).
3 Números são um caso especial quando usados como chave. Eles são convertidos pelo seguinte algoritmo para que possam ser classificados usando a mesma sequência de ordenação ASCII dos caracteres:
 - Converta o número para o formato de ponto flutuante IEEE. Para detalhes, consulte Capacidades do sistema Visual FoxPro .
- Troque a ordem dos bytes da ordem Intel 8086 para a ordem da esquerda para a direita.
- Se o número era negativo, faça o complemento lógico do número (troque todos os 64 bits, 1 para 0 e 0 para 1); caso contrário, inverta apenas o bit mais à esquerda.

# Exemplo de uma estrutura de árvore ordenada

Encontrar uma chave na estrutura abaixo requer pesquisar um único caminho entre os nós raiz e folha. Os nós no nível mais baixo são nós folha. Como as chaves estão ordenadas, todas as chaves na subárvore são menores ou iguais ao nó pai.

Na ilustração acima, as letras são usadas como valores de chave. Cada chave também teria um número hexadecimal de quatro bytes. Os números associados às chaves nos nós folha seriam números reais de tabela — todas as chaves em outros nós teriam ponteiros intra-índice associados a elas.

Os bytes 12-511 no registro de nó do índice podem ser visualizados da seguinte forma:

A combinação valor da chave/número hexadecimal ocorre nos bytes 12 – 511 n vezes, onde n é o número de chaves presentes.
