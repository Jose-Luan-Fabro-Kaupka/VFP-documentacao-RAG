# Personalizando a saída do Assistente de documentação

Além das opções que você escolhe ao executar o Assistente de documentação, você pode empregar opções adicionais fora do assistente alterando a tabela Fdkeywrd.dbf, que contém todas as palavras reservadas do Visual FoxPro, na pasta ...\Wizards ou adicionando diretivas do Assistente de documentação ao seu código.

# Alterando o Fdkeywrd.dbf

Você pode alterar o estilo de indentação da estrutura CASE alterando o valor do campo code em Fdkeywrd.dbf. Por padrão, o assistente procura indentação em uma estrutura CASE assim:

```foxpro
DO CASE
CASE case1=1
   case2=2
CASE case3=3
   case4=4
ENDCASE
```

Alguns desenvolvedores preferem indentar as linhas entre DO CASE e ENDCASE um nível adicional assim:

```foxpro
DO CASE
   CASE case1=1
      case2=2
   CASE case3=3
      case4=4
ENDCASE
```

Se você indenta suas estruturas CASE, como no segundo exemplo, especifique isso em Fdkeywrd.dbf.

 Para especificar indentações totalmente aninhadas em instruções DO CASE
 - Localize o arquivo Fdkeywrd.dbf na pasta ...\Wizards do diretório raiz do Visual FoxPro.
- Abra a tabela Fdkeywrd.dbf.
- Localize o registro ENDCASE.
- Altere o valor no campo Code para UU .

# Adicionando diretivas do assistente

Você pode colocar diretivas especiais em seus arquivos de código que instruem o Assistente de documentação a executar tarefas específicas ao analisar o código. As diretivas do assistente disponíveis são as seguintes:
 **ACTIONCHARS**
Especifica os caracteres usados para criar diagramas de ação ou árvore do seu código. Você pode querer alterar as configurações padrão se usar páginas de código diferentes de ASCII 1250 ou ANSI 1252 em FoxFont para obter os caracteres esperados.
**EXPANDKEYWORDS**
Especifica se a expansão de palavras-chave está ativa ou não no Assistente de documentação. O valor padrão é OFF, que mantém as palavras-chave como digitadas no código. Se você usou abreviações de quatro caracteres em todo o seu código, pode querer tornar o código mais legível definindo a expansão de palavras-chave como ON.
**XREFKEYWORDS**
Especifica se o assistente cria um arquivo que mostra todas as palavras-chave e suas localizações no documento de código. O arquivo contém os nomes das palavras-chave, o tipo de palavra-chave (de acordo com a tabela Fdxref.dbf, conforme descrito na Etapa 5 do Assistente de documentação), a linha em que está localizada e o arquivo que a contém. O padrão é ON.
**ARRAYBRACKETS**
Especifica se colchetes e parênteses são tratados de forma diferente. O padrão, ON, trata colchetes como delimitadores de matriz e parênteses como delimitadores de função ou método.
**ACTIONINDENTLENGTH**
Especifica o número de espaços de caractere que o assistente usa para indentação em diagramas de árvore ou ação. O valor mínimo é dois caracteres. Funcionalmente, no código, não há diferença entre espaços ou tabulações. A indentação facilita a leitura e compreensão do seu código.

Você pode colocar diretivas do assistente no arquivo de programa principal do seu projeto (para direcionar o assistente a analisar todos os arquivos de código no projeto) ou em arquivos de código individuais (para instruir o assistente sobre como analisar arquivos específicos).

A sintaxe das diretivas começa com um asterisco, para que o Visual FoxPro as trate como comentários e as ignore ao compilar programas. As diretivas não diferenciam maiúsculas de minúsculas. A sintaxe das diretivas é:

```foxpro
*# document directive
```

Para consistência em todo o seu código, é uma boa ideia colocar as diretivas perto do início do arquivo de programa principal, para que o Assistente de documentação encontre a instrução quando começar a analisar.

As diretivas do Assistente de documentação são descritas abaixo.
 ***# document ACTIONCHARS " abcdef "**
Por padrão, quando o assistente cria um Diagrama de ação ou um Diagrama de árvore, o assistente usa seis caracteres que aparecem como linhas e cantos quadrados quando visualizados sob a página de código ASCII 1250 ou sob a página de código ANSI 1252 em FoxFont. Nem todos os caracteres mapeiam para caracteres de linha quando visualizados sob outras páginas de código. Os seis caracteres padrão e seus caracteres FoxFont correspondentes estão listados abaixo como a , b , c , d , e e f . abcdef Padrão Valor Chr( ) Como visualizado em FoxFont a 32 (espaço) b 196 c 179 d 218 e 192 f 195

> **Dica:** Ao usar outras páginas de código, insira o seguinte código em seu arquivo de programa principal para garantir que as linhas em seus diagramas mapeiem para caracteres semelhantes a linhas (o primeiro caractere da cadeia entre aspas é um espaço):

```foxpro
*# document ACTIONCHARS " -|+++"
```

> **Observação:** Para uma lista de páginas de código suportadas, consulte Páginas de código suportadas pelo Visual FoxPro .
 ***# document XREF cMode**
Habilita referência cruzada de variáveis. O padrão é ON. cMode Descrição ON Habilita referência cruzada de variáveis OFF Desabilita referência cruzada de variáveis SUSPEND Desabilita referência cruzada de variáveis no arquivo atual até que o Assistente de documentação encontre a próxima instância de: *# document XREF ON
***# document EXPANDKEYWORDS cMode**
Habilita a expansão de palavras-chave abreviadas no seu código. Por exemplo, "DEFI WIND" seria expandido para "DEFINE WINDOW." O padrão é OFF. Cuidado Nem todas as palavras-chave no Visual FoxPro começam com uma cadeia única de quatro caracteres. Por exemplo, "REPL" pode ser abreviação de "REPLACE" ou "REPLICATE." Tenha cuidado se incluir esta diretiva e escolher substituir arquivos existentes. cMode Descrição ON Habilita expansão de palavras-chave OFF Desabilita expansão de palavras-chave SUSPEND Desabilita expansão de palavras-chave no arquivo atual até a próxima instância de: *# document EXPANDKEYWORDS ON
***# document XREFKEYWORDS cMode**
Esta diretiva corresponde à opção Referência cruzada de palavras-chave em "Etapa 6 – Concluir" no Assistente de documentação . O padrão é OFF. cMode Descrição ON Habilita referência cruzada de palavras-chave OFF Desabilita referência cruzada de palavras-chave SUSPEND Desabilita referência cruzada de palavras-chave no arquivo atual até a próxima instância de: *# document XREFKEYWORDS ON
***# document ARRAYBRACKETS cMode**
O padrão é OFF. cMode Descrição ON O Assistente de documentação assume que colchetes são usados para matrizes e que parênteses são usados para funções e métodos. OFF O Assistente de documentação trata tanto colchetes quanto parênteses como matrizes.
***# document ACTIONINDENTLENGTH nSpace**
nSpace é o número de espaços de caractere que você deseja que o Assistente de documentação use para indentação. O valor mínimo permitido é 2.
