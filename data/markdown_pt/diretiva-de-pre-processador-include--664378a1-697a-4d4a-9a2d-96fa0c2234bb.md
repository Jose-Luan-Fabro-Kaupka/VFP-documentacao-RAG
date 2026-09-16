# Diretiva de pré-processador #INCLUDE

Instrui o pré-processador do Visual FoxPro a tratar o conteúdo de um arquivo de cabeçalho especificado como se aparecesse em um programa Visual FoxPro.

> **Observação:** O número máximo de níveis de compilador para #INCLUDE é 4.

```foxpro
#INCLUDE FileName
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo de cabeçalho que é mesclado ao programa durante a compilação. Você pode incluir um caminho com o nome do arquivo de cabeçalho. Quando você inclui um caminho com o nome do arquivo de cabeçalho, o Visual FoxPro pesquisa o arquivo de cabeçalho somente no local especificado. Se você não incluir um caminho com o nome do arquivo de cabeçalho, o Visual FoxPro pesquisa o arquivo de cabeçalho no diretório padrão do Visual FoxPro e depois ao longo do caminho do Visual FoxPro. O caminho do Visual FoxPro é especificado com SET PATH.

# Observações

Você pode criar arquivos de cabeçalho contendo diretivas de pré-processador e depois usar #INCLUDE para mesclar o conteúdo do arquivo de cabeçalho em um programa quando o programa é compilado. O conteúdo do arquivo de cabeçalho é inserido no programa durante a compilação no ponto onde #INCLUDE aparece no programa.

Somente as diretivas de pré-processador #DEFINE ... #UNDEF, #IF ... #ENDIF e #INCLUDE são reconhecidas em um arquivo de cabeçalho. Comentários e comandos do Visual FoxPro incluídos em um arquivo de cabeçalho são ignorados.

Um programa pode conter qualquer número de diretivas #INCLUDE. Essas diretivas podem aparecer em qualquer lugar do programa. Colocar diretivas #INCLUDE em arquivos de cabeçalho permite que você aninhe diretivas #INCLUDE.

Arquivos de cabeçalho normalmente têm extensão .h, embora possam ter qualquer extensão. Um arquivo de cabeçalho do Visual FoxPro, Foxpro.h, está incluído. Ele contém muitas das constantes descritas em toda esta documentação.

# Exemplo

No exemplo a seguir, dois arquivos são usados: Const.h, um arquivo de cabeçalho, e Myprog.prg, um arquivo de programa. O arquivo de cabeçalho contém várias diretivas #DEFINE que criam constantes em tempo de compilação. O arquivo de programa usa #INCLUDE para mesclar o arquivo de cabeçalho Const.h na compilação, tornando as constantes em tempo de compilação no arquivo de cabeçalho disponíveis para o programa.

```foxpro
*** Header file CONST.H ***
#DEFINE ERROR_NODISK     1
#DEFINE ERROR_DISKFULL  2
#DEFINE ERROR_UNKNOWN  3
*** Program file MYPROG.PRG ***
#INCLUDE CONST.H
FUNCTION chkerror
PARAMETER errcode
  DO CASE
  CASE errcode = ERROR_NODISK
  ?"Error - No Disk"
  CASE errcode = ERROR_DISKFULL
  ?"Error - Disk Full"
  CASE errcode = ERROR_UNKNOWN
  ?"Unknown Error"
  ENDCASE
RETURN
```
