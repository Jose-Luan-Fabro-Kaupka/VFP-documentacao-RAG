# Expressões de formato para controles Field

Você pode criar vários formatos para a saída gerada por controles Field criando uma expressão de cadeia de formato. Uma cadeia de formato contém códigos e modelos de formato.

# Códigos de formato

Os códigos de formato aplicam-se a todos os caracteres da expressão do controle Field e devem ser precedidos pelo sinal de arroba (@) na cadeia de formato. Por exemplo, você pode preencher um valor numérico com zeros à esquerda em vez de espaços usando "@L 999999".

| Código de formato: | Descrição: | Aplica-se a dados do tipo: |
| --- | --- | --- |
| ! | Força o texto para maiúsculas. | Somente Character |
| B | Alinha à esquerda. | Todos os tipos |
| J | Alinha à direita. | Todos os tipos |
| I | Centraliza. | Todos os tipos |
| L | Zeros à esquerda. | Somente Numeric |
| Z | Deixa em branco se for zero. | Numeric, Date e DateTime |
| ( | Coloca números negativos entre (). | Somente Numeric |
| C | Acrescenta " CR" a números positivos diferentes de zero. | Somente Numeric |
| X | Acrescenta " DB" a números negativos diferentes de zero. | Somente Numeric |
| $ | Usa notação monetária. | Somente Numeric |
| D | Usa a configuração atual de SET DATE. | Todos os tipos |
| E | Exibe como se SET DATE BRITISH estivesse em vigor. | Todos os tipos |
| YL | Exibe usando o formato de data longa do sistema. | Date |
| YS | Exibe usando o formato de data curta do sistema. | Date |
| R | Impede que caracteres sem função de formatação na cadeia de modelo substituam o caractere correspondente do valor da expressão do campo. Quando @R é usado, a cadeia de modelo é intercalada em vez de sobreposta. (Consulte o exemplo abaixo.) | Character e Numeric |

#### Observações
 - Dados numéricos são alinhados à direita por padrão.
- Dados Character e Date são alinhados à esquerda por padrão.
- Você pode combinar códigos de formato. Por exemplo, "@CX" exibirá créditos e débitos em dados numéricos, quando apropriado.

Para obter mais informações sobre códigos de formato em controles de formulário, consulte a propriedade Format.

# Caracteres de modelo

Os caracteres do modelo de formato aplicam-se a caracteres individuais da expressão do controle Field. Você pode criar um padrão no qual cada caractere do modelo represente um caractere a exibir. Alguns caracteres alteram a exibição de tipos específicos. Por exemplo, "Y" em um modelo de expressão lógica exibe "Y" em vez de ".T." para True e "N" em vez de ".F." para False. O caractere "9" é um espaço reservado para qualquer dígito em dados Character ou Numeric. Outros caracteres, como parênteses, espaços e hifens, são exibidos literalmente.

Para obter mais informações, consulte a propriedade InputMask.

# Exemplos

Os exemplos a seguir mostram como códigos e caracteres de modelo trabalham juntos para criar a saída:

| Valor da expressão de campo | Cadeia de formato | Saída renderizada |
| --- | --- | --- |
| -43.05 | @(CX 999.999 | ( 43.050 DB) |
| 65.43 | (999) 999-9999 | ( ) - -43 |
| "4505551023" | (999) 999-9999 | (505) 102- |
| "4505551023" | @R (999) 999-9999 | (450) 555-1023 |
| ca90210 | @R !! 99999 | CA 90210 |
