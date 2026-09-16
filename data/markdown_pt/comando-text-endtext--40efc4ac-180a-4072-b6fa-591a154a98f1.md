# Comando TEXT ... ENDTEXT

Envia linhas de texto especificadas por TextLines para o dispositivo de saída atual ou variável de memória. O Visual FoxPro envia linhas de texto para o dispositivo de saída atual até encontrar uma instrução ENDTEXT ou até o programa terminar.

O dispositivo de saída atual pode incluir a janela principal do Visual FoxPro, uma janela definida pelo usuário, uma impressora, um arquivo de texto ou um arquivo de baixo nível.

```foxpro
TEXT [TO VarName [ADDITIVE] [TEXTMERGE] [NOSHOW] [FLAGS nValue] [PRETEXT eExpression]]
      TextLines
ENDTEXT
```

#### Parâmetros
 **TextLines**
Especifica o texto a enviar para o dispositivo de saída atual. TextLines pode consistir em texto, variáveis de memória, elementos de matriz, expressões, funções ou qualquer combinação destes. Observação O Visual FoxPro avalia expressões, funções, variáveis de memória e elementos de matriz especificados com TextLines apenas se você definir SET TEXTMERGE como ON e os delimitar com os delimitadores especificados por SET TEXTMERGE DELIMITERS. Se SET TEXTMERGE estiver OFF, o Visual FoxPro envia expressões, funções, variáveis de memória e elementos de matriz como literais de cadeia de caracteres junto com seus delimitadores. Por exemplo, o Visual FoxPro avalia e envia a data atual quando você especifica a função DATE( ) como TextLines apenas se SET TEXTMERGE estiver ON e TextLines contiver a função e os delimitadores apropriados, como <<DATE( )>>. Se SET TEXTMERGE estiver OFF, o Visual FoxPro envia <<DATE( )>> como literal de cadeia de caracteres. Se você colocar comentários dentro de TEXT ... ENDTEXT ou após o caractere de barra invertida simples (\) ou caracteres de barra invertida dupla (\\), o Visual FoxPro envia os comentários.
**TO VarName**
Especifica o nome da variável de memória a ser usado para passar o conteúdo de TEXT...ENDTEXT. Esta variável pode já existir. Se a variável ainda não foi declarada, o Visual FoxPro a cria automaticamente como variável private. A cláusula TO opera independentemente de como SET TEXTMERGE está definido. Se SET TEXTMERGE estiver definido para um arquivo e a instrução TO for incluída, o Visual FoxPro envia tanto o arquivo quanto a variável.
**ADDITIVE**
Determina se o conteúdo da variável TO é substituído ou adicionado ao conteúdo existente. Observação Se o conteúdo de TO VarName não é uma cadeia de caracteres, o Visual FoxPro sempre substitui o conteúdo em VarName.
**TEXTMERGE**
Habilita a avaliação de conteúdo delimitado sem definir SET TEXTMERGE como ON.
**NOSHOW**
Desabilita a exibição da mesclagem de texto na tela.
**FLAGS nValue**
Especifica um valor numérico que determina se a saída é suprimida para um arquivo de saída ou se linhas em branco precedendo qualquer texto são incluídas na saída. Valor (aditivo) Descrição 1 Suprime a saída para o arquivo especificado com a _TEXT System Variable. 2 Quando a cláusula NOSHOW é incluída, preserva linhas em branco precedendo texto que aparece dentro de TEXT ... ENDTEXT. Definir nValue como 2 separará a saída atual de TEXT ... ENDTEXT da saída anterior de TEXT ... ENDTEXT com uma quebra de linha. Observação Combinar uma configuração nValue de 2 e PRETEXT de 4 separará a saída atual de TEXT…ENDTEXT da saída anterior de TEXT…ENDTEXT com uma quebra de linha enquanto remove linhas vazias na saída TEXT...ENDTEXT.
**PRETEXT eExpression**
Especifica uma cadeia de caracteres a inserir antes de cada linha do conteúdo de mesclagem de texto entre TEXT...ENDTEXT ou uma expressão numérica. A tabela a seguir descreve os comportamentos da cláusula PRETEXT dependendo da expressão especificada por eExpression. eExpression Comportamento PRETEXT Expressão de caractere Insere a expressão antes de cada linha do conteúdo de mesclagem de texto que aparece entre a instrução TEXT...ENDTEXT. Ao usar PRETEXT com TEXT...ENDTEXT, eExpression é limitado a um comprimento máximo de 255 caracteres. eExpression substitui o conteúdo da variável de sistema _PRETEXT. Quando eExpression contém uma expressão que precisa ser avaliada, por exemplo, uma função definida pelo usuário (UDF), o Visual FoxPro a avalia apenas uma vez quando o comando TEXT aparece pela primeira vez. Expressão numérica Especifica valores de flag aditivos para determinar o comportamento do conteúdo de mesclagem de texto que aparece entre a instrução TEXT...ENDTEXT. Por exemplo, um valor de 7 especifica que o Visual FoxPro elimine todo o espaço em branco, incluindo espaços, tabulações e retornos de carro. Um valor fora do intervalo de 0-15 produz um erro. Observação Especificar um valor zero não elimina espaço em branco. Quando eExpression é uma expressão numérica, você pode usar a variável de sistema _PRETEXT para inserir texto adicional após o Visual FoxPro eliminar espaço em branco. A tabela a seguir lista flags aditivos numéricos que você pode usar em eExpression para especificar comportamento adicional. Valor (Aditivo) Descrição 1 Elimina espaços antes de cada linha. 2 Elimina tabulações antes de cada linha. 4 Elimina retornos de carro, por exemplo, linhas em branco, antes de cada linha. 8 Elimina quebras de linha. Observação Diferentemente da variável de sistema _PRETEXT, a cláusula PRETEXT não tem escopo global e se aplica apenas à instrução TEXT...ENDTEXT em que aparece. Caracteres removidos usando a cláusula PRETEXT se aplicam apenas ao texto dentro da instrução TEXT...ENDTEXT e não ao texto mesclado avaliado de cExpression. No exemplo a seguir, os espaços na variável de memória myvar não são removidos quando mesclados com o texto em TEXT...ENDTEXT: myvar = " AAA" TEXT TO x NOSHOW ADDITIVE TEXTMERGE PRETEXT 7 Start Line <<myvar>> BBB CCC ENDTEXT

# Observações

Por padrão, TEXT ... ENDTEXT envia saída para a janela principal do Visual FoxPro ou a janela ativa. Para suprimir a saída para a janela principal do Visual FoxPro ou a janela ativa, emita SET CONSOLE OFF. Para enviar saída para uma impressora ou um arquivo de texto, use SET PRINTER. Para enviar saída de TEXT ... ENDTEXT para um arquivo de baixo nível que você criou ou abriu usando FCREATE( ) ou FOPEN( ), armazene o handle de arquivo retornado por FCREATE( ) ou FOPEN( ) na variável de sistema _TEXT, que você pode usar para direcionar a saída para o arquivo de baixo nível correspondente.

> **Observação:** O processo de mesclagem de texto geralmente inclui qualquer espaço em branco que possa aparecer antes de cada linha em uma instrução TEXT...ENDTEXT. No entanto, a inclusão de espaço em branco pode causar falha na mesclagem de texto, por exemplo, quando XML é usado em um navegador Web. Você deve remover esse espaço em branco para evitar XML formatado incorretamente.

Aninhar instruções TEXT...ENDTEXT não é recomendado, especialmente se usar a cláusula PRETEXT, porque as instruções aninhadas podem afetar o formato das instruções externas.

# Exemplo

Exemplo 1

O exemplo a seguir demonstra a criação de um arquivo de baixo nível chamado `myNamesFile.txt` e o armazenamento de seu handle de arquivo na variável de sistema _TEXT. O programa encerra se o arquivo `myNamesFile.txt` não puder ser criado.

O Visual FoxPro abre a tabela customer e envia os nomes dos primeiros dez contatos para `myNamesFile.txt`. O Visual FoxPro envia o texto e os resultados das funções para o arquivo de texto. O exemplo usa MODIFY FILE para abrir `myNamesFile.txt`.

```foxpro
CLEAR
CLOSE DATABASES
SET TALK OFF
SET TEXTMERGE ON
STORE FCREATE('myNamesFile.txt') TO _TEXT
IF _TEXT = -1
   WAIT WINDOW 'Cannot create an output file. Press a key to exit.'
   CANCEL
ENDIF
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer
TEXT
         CONTACT NAMES
   <<DATE()>>    <<TIME()>>
ENDTEXT
WAIT WINDOW 'Press a key to generate the first ten names.'
SCAN NEXT 10
   TEXT
      <<contact>>
   ENDTEXT
ENDSCAN
CLOSE ALL
MODIFY FILE myNamesFile.txt
ERASE myNamesFile.txt
```

Exemplo 2

O exemplo a seguir mostra um procedimento personalizado que usa TEXT...ENDTEXT para armazenar um XML DataSet em uma variável. No exemplo, todos os espaços, tabulações e retornos de carro são eliminados.

```foxpro
PROCEDURE myProcedure
   DO CASE
   CASE nValue = 1
      TEXT TO myVar NOSHOW TEXT PRETEXT 7
         <?xml version="1.0" encoding="utf-8"?>
         <DataSet xmlns="http://tempuri.org">
         <<ALLTRIM(STRCONV(leRetVal.item(0).xml,9))>>
         </DataSet>
      ENDTEXT
   OTHERWISE
   ENDCASE
ENDPROC
```
