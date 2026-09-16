# Modificação de aplicativos internacionais

Você pode evitar problemas de localização com código observando as diretrizes a seguir.

# Teste para versões internacionais

Se é importante que seu aplicativo possa determinar em qual idioma o Visual FoxPro está sendo executado, você pode chamar a função VERSION( ). Conhecer o ambiente de idioma pode ajudá-lo a determinar qual texto exibir, como formatar dados e assim por diante. Por exemplo, o código a seguir determina em qual ambiente de idioma o Visual FoxPro está sendo executado e depois executa um formulário específico do idioma:

```foxpro
IF VERSION(3) = 34 THEN
   * Running in Spanish--display Spanish form
   DO FORM CST_SPN.SCX
ELSE
   * Display English form
   DO FORM CST_ENU.SCX
ENDIF
```

> **Observação:** O suporte para cadeias de caracteres de byte duplo está disponível no Visual FoxPro somente desde a versão 3.0b. Se seu aplicativo depende da disponibilidade de funções de conjunto de caracteres de byte duplo (DBCS), você também deve chamar a função VERSION(1) para testar o número da versão do Visual FoxPro.

# Uso de cadeias de caracteres

Evite incluir cadeias de caracteres diretamente no código, pois elas dificultam a localização. Por exemplo, não inclua datas e moedas como cadeias de caracteres no código. Se possível, escreva seu código de forma que ele recupere cadeias de caracteres de arquivos ou tabelas separados do programa.

> **Observação:** O desempenho do seu programa pode sofrer se você remover todas as cadeias de caracteres dele. Por exemplo, o desempenho pode sofrer se o programa buscar cadeias de caracteres dentro de um loop.

Uma maneira de trabalhar com cadeias de caracteres em um aplicativo que será traduzido é usar constantes de cadeia de caracteres em todo o aplicativo. Você pode então definir o texto para essas constantes em um arquivo de texto separado que é referenciado de seus programas usando a diretiva de pré-processador #INCLUDE. Por exemplo, em vez de incorporar a mensagem de erro "file not found," você pode usar a constante ERR_FILE_NOT_FOUND. O texto para esta constante pode estar em um arquivo chamado ERR_TEXT.H. Um programa que usa esta técnica pode ser semelhante a este:

```foxpro
#INCLUDE ERR_TEXT.H
* processing here
IF ERR THEN
   MESSAGEBOX( ERR_FILE_NOT_FOUND )
ENDIF
```

Quando seu aplicativo é localizado, o tradutor pode criar uma versão específica do local do arquivo de texto de erro e depois recompilar o aplicativo.

### Trabalhando com cadeias de caracteres em ambientes DBCS

O Visual FoxPro inclui funções para manipular expressões de caracteres contendo qualquer combinação de caracteres de byte único ou duplo. Ao usar funções de cadeia de caracteres DBCS, você pode desenvolver aplicativos sem precisar escrever código extra que teste caracteres de byte duplo ao contar, localizar, inserir ou remover caracteres em uma cadeia de caracteres.

A maioria das funções DBCS é equivalente às suas contrapartes de byte único, exceto que são nomeadas com um sufixo C para distingui-las. Você pode usar essas funções com dados de byte único e duplo; as funções DBCS retornam exatamente o mesmo valor que suas contrapartes de byte único quando dados de byte único são passados a elas. Algumas outras funções ajudam você a trabalhar com cadeias de caracteres especificamente em ambientes de byte duplo.

| Funções de cadeia de caracteres DBCS | Descrição |
| --- | --- |
| AT_C( ) | Retorna a posição de uma cadeia de caracteres dentro de outra (diferencia maiúsculas de minúsculas), começando pela esquerda. |
| ATCC( ) | Retorna a posição de uma cadeia de caracteres dentro de outra (não diferencia maiúsculas de minúsculas). |
| CHRTRANC( ) | Substitui caracteres em uma cadeia de caracteres. |
| IMESTATUS( ) | Alterna a edição de byte duplo na janela Browse. |
| ISLEADBYTE( ) | Testa se um caractere é um caractere DBCS. |
| LEFTC( ) | Retorna os caracteres mais à esquerda de uma cadeia de caracteres. |
| LENC( ) | Retorna o número de caracteres em uma cadeia de caracteres. |
| LIKEC( ) | Determina se duas cadeias de caracteres correspondem. |
| RATC( ) | Retorna a posição de uma cadeia de caracteres dentro de outra (diferencia maiúsculas de minúsculas), começando pela direita. |
| RIGHTC( ) | Retorna os caracteres mais à direita de uma cadeia de caracteres. |
| STRCONV( ) | Converte caracteres entre representações de byte único e duplo. |
| STUFFC( ) | Substitui caracteres em uma cadeia de caracteres por outra cadeia de caracteres. |
| SUBSTRC( ) | Retorna uma substring. |

Ao trabalhar com funções de cadeia de caracteres de byte duplo, lembre-se de que o limite de comprimento máximo para variáveis, nomes e assim por diante é efetivamente reduzido pela metade. Para obter mais informações, consulte Visual FoxPro System Capacities.

> **Observação:** As funções DBCS do Visual FoxPro não são suportadas em versões anteriores do Visual FoxPro, e chamá-las pode causar resultados imprevisíveis. Se você usa qualquer função DBCS em seu aplicativo, use VERSION(1) para verificar se a versão do Visual FoxPro é posterior à versão 3.0.

# Trabalhando com formatos de data, hora e moeda

Para ajudá-lo a formatar datas, horas e moeda de acordo com o que seus usuários estão acostumados, você pode usar uma variedade de técnicas de formatação. Você pode:
 - Permitir que o Visual FoxPro use as configurações estabelecidas no Painel de Controle.
- Especificar um idioma ou um formato específico na caixa de diálogo Options do Visual FoxPro que deseja usar.

Formate datas, horas e informações de moeda no código usando os comandos SET SYSFORMATS e SET DATE. Como regra, você emitiria este comando durante a inicialização do seu aplicativo (por exemplo, no arquivo de configuração). O padrão para SET SYSFORMATS é OFF, portanto você deve definir explicitamente como ON ao iniciar seu aplicativo.

Você pode estabelecer validação de dados em caixas de texto individuais definindo a propriedade Format da caixa de texto. No entanto, como a formatação da caixa de texto tem precedência sobre a formatação em todo o sistema, isso pode dificultar a localização do seu aplicativo para um ambiente que usa um formato diferente para datas, moeda e assim por diante.

Para obter mais informações sobre como definir formatos locais, consulte How to: Set Date, Time, and Currency Formats.

# Uso de diretivas de pré-processador

Você pode criar variantes de aplicativo para diferentes locais usando diretivas de pré-processador. Essas controlam a compilação de código no aplicativo e incluem as construções #INCLUDE, #DEFINE ... #UNDEF e #IF ... #ENDIF.

O uso de diretivas de pré-processador pode produzir variantes rapidamente; no entanto, tais diretivas têm as seguintes desvantagens:
 - Para usar diretivas de pré-processador, você delimita o código, e delimitação extensiva pode aumentar a complexidade do código.
- Constantes de tempo de compilação estão disponíveis somente no programa que as cria.
