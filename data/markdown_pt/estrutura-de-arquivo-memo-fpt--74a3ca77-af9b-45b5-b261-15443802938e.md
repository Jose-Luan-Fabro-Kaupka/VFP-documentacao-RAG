# Estrutura de arquivo Memo (.FPT)

Arquivos memo contêm um registro de cabeçalho e qualquer número de estruturas de bloco. O registro de cabeçalho contém um ponteiro para o próximo bloco livre e o tamanho do bloco em bytes. O tamanho é determinado pelo comando SET BLOCKSIZE Command quando o arquivo é criado. O registro de cabeçalho começa na posição zero do arquivo e ocupa 512 bytes. O comando SET BLOCKSIZE TO 0 define a largura do tamanho do bloco como 1.

Após o registro de cabeçalho estão os blocos que contêm um cabeçalho de bloco e o texto do memo. O arquivo de tabela contém números de bloco que são usados para referenciar os blocos memo. A posição do bloco no arquivo memo é determinada multiplicando o número do bloco pelo tamanho do bloco (encontrado no registro de cabeçalho do arquivo memo). Todos os blocos memo começam em endereços de limite de bloco par. Um bloco memo pode ocupar mais de um bloco consecutivo.
 Registro de cabeçalho Memo
| Deslocamento de byte | Descrição |
| --- | --- |
| 00 – 03 | Localização do próximo bloco livre1 |
| 04 – 05 | Não utilizado |
| 06 – 07 | Tamanho do bloco (bytes por bloco)1 |
| 08 – 511 | Não utilizado |

1 Inteiros armazenados com o byte mais significativo primeiro.
 Cabeçalho de bloco Memo e texto Memo
| Deslocamento de byte | Descrição |
| --- | --- |
| 00 – 03 | Assinatura do bloco 1 (indica o tipo de dados no bloco) 0 – imagem (tipo de campo picture) 1 – texto (tipo de campo memo) |
| 04 – 07 | Comprimento 1 do memo (em bytes) |
| 08 – n | Texto do memo (n = comprimento) |

1 Inteiros armazenados com o byte mais significativo primeiro.
