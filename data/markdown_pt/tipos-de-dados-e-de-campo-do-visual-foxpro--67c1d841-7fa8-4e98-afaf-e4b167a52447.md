# Tipos de dados e de campo do Visual FoxPro

Todos os dados no Visual FoxPro têm um tipo de dados particular, que define os valores permitidos para os dados e o intervalo e o tamanho desses valores. Depois de identificar e especificar o tipo de dados que você está usando, o Visual FoxPro pode armazenar e manipular os dados com eficiência.

Quando você cria uma tabela, pode especificar o tipo de dados a armazenar em cada campo da tabela. Você pode especificar mais tipos de dados para campos em uma tabela do que para variáveis e matrizes. Variáveis e matrizes podem armazenar apenas um subconjunto dos tipos de dados disponíveis do Visual FoxPro; no entanto, o valor que você armazena em uma variável ou elemento de matriz determina o tipo de dados na variável ou elemento de matriz. Para obter mais informações, consulte Como: escolher tipos de dados.

> **Dica:** Você pode usar a função TYPE( ) para determinar o tipo de dados armazenado em uma variável, elemento de matriz ou campo.
 Tipos de dados do Visual FoxPro
| Tipo de dados | Descrição | Tamanho | Intervalo |
| --- | --- | --- | --- |
| Blob | Dados binários de comprimento indeterminado. Valores Blob estão em um arquivo memo (.fpt). Nenhuma tradução de página de código é executada em dados Blob. | 4 bytes em uma tabela | Limitado pela memória disponível e/ou limite de tamanho de arquivo de 2 GB. |
| Character | Texto alfanumérico Por exemplo, um endereço de cliente | 1 byte por caractere até 254 | Quaisquer caracteres |
| Currency | Valores monetários Por exemplo, o preço de um item | 8 bytes | - $922337203685477.5807 a $922337203685477.5807 |
| Date | Dados cronológicos consistindo de mês, dia e ano Por exemplo, uma data de pedido | 8 bytes | Ao usar formatos de data estritos, {^0001-01-01}, 1º de janeiro de 1 d.C. a {^9999-12-31}, 31 de dezembro de 9999 d.C. |
| DateTime | Dados cronológicos consistindo de mês, dia, ano, horas, minutos e segundos Por exemplo, data e hora de chegada | 8 bytes | Ao usar formatos de data estritos, {^0001-01-01}, 1º de janeiro de 1 d.C. a {^9999-12-31}, 31 de dezembro de 9999 d.C., mais 00:00:00 a.m. a 11:59:59 p.m. |
| Logical | Valor booleano de True ou False Por exemplo, se um pedido foi atendido ou não | 1 byte | True (.T.) ou False (.F.) |
| Numeric | Inteiros ou números decimais Por exemplo, a quantidade de itens pedidos | 8 bytes na memória; 1 a 20 bytes na tabela | - .9999999999E+19 a .9999999999E+20 |
| Varbinary | Valores binários. Dados Varbinary são semelhantes a dados Varchar, pois os valores não incluem preenchimento com bytes zero (0). O comprimento do valor contido é armazenado internamente. Nenhuma tradução de página de código é executada em dados Varbinary. | 1 byte por valor hexadecimal até 255 bytes no total | Qualquer valor hexadecimal |
| Variant | Dados Variant podem ser qualquer um dos tipos de dados do Visual FoxPro e o valor null. Depois que um valor é armazenado em um variant, o variant assume o tipo de dados dos dados que contém. Variants são designados com um prefixo e na sintaxe de linguagem. | Consulte outros tipos de dados. | Consulte outros tipos de dados. |

Além disso, o Visual FoxPro fornece tipos de dados que se aplicam apenas a campos em tabelas.
 Tipos de campo do Visual FoxPro
| Tipo de campo | Descrição | Tamanho | Intervalo |
| --- | --- | --- | --- |
| Character (Binary) | Qualquer dado Character que você não deseja traduzir entre páginas de código Por exemplo, senhas de usuário armazenadas em uma tabela e usadas em diferentes países ou regiões. | 1 byte por caractere até 254 | Quaisquer caracteres |
| Double | Um número de ponto flutuante de dupla precisão Por exemplo, dados científicos que exigem alto grau de precisão. | 8 bytes | +/-4.94065645841247E-324 a +/-8.9884656743115E307 |
| Float | Igual a Numeric | 8 bytes na memória; 1 a 20 bytes na tabela | - .9999999999E+19 a .9999999999E+20 |
| General | Referência a um objeto OLE Por exemplo, uma planilha do Microsoft Excel. | 4 bytes na tabela | Limitado pela memória disponível. |
| Integer | Valor numérico sem decimais Por exemplo, um número de linha em um pedido. | 4 bytes | -2147483647 a 2147483647 |
| Integer (Autoinc) | Igual a Integer, mas também um valor de incremento automático. Somente leitura. | 4 bytes | Valor controlado pelos valores Next e Step de autoincremento. |
| Memo | Texto alfanumérico de comprimento indeterminado ou referência a um bloco de dados Por exemplo, anotações sobre uma ligação telefônica em um registro de chamadas. | 4 bytes na tabela | Limitado pela memória disponível. |
| Memo (Binary) | Igual a Memo, exceto que os dados do campo memo não mudam entre páginas de código Por exemplo, um script de login usado em diferentes países ou regiões. | 4 bytes na tabela | Limitado pela memória disponível. |
| Varchar | Texto alfanumérico. Varchar é semelhante a Character, exceto que valores em campos Varchar não incluem preenchimento com espaços adicionais. O comprimento do valor contido é armazenado internamente. | 1 byte por caractere até 254 bytes no total | Quaisquer caracteres |
| Varchar (Binary) | Dados do tipo Varchar que você não deseja traduzir entre páginas de código. | 1 byte por caractere até 254 bytes no total | Quaisquer caracteres |

Cada tipo de dados tem suas próprias características, incluindo tamanho de armazenamento:
 Diferenças de armazenamento por tipo de dados

Para ver uma lista das funções que você pode usar com cada tipo de dados, consulte Categorias de linguagem.
