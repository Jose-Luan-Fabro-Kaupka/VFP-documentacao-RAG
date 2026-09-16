# Variável do sistema  TEXT

Directs output from the \ | \\ and TEXT ... ENDTEXT text merge commands to a low-level file.

```foxpro
_TEXT = nFileHandle
```

Parâmetros
**nFileHandle**
Especifica um valor numérico que determina o arquivo de baixo nível para o qual a saída é direcionada.

Observações

\ ~\\ e TEXT ... ENDTEXT facilitam a junção de texto com o conteúdo de tabelas, variáveis de memória e os resultados de funções e expressões. A saída gerada por estes comandos de mesclagem de texto pode ser direcionada para a tela ou uma janela ou para um arquivo de baixo nível. A variável de memória do  TEXT permite que você direcione a saída de mesclagem de texto desses comandos para um arquivo de baixo nível.

Para enviar o resultado dos comandos de mesclagem de texto \ e\\ e TEXT ... ENDTEXT para um arquivo de baixo nível, inclua o TO Cláusula do Nome do Ficheiro em SET TEXTMERGE. A pega de arquivo do Nome do Arquivo é armazenada em  TEXT. Se o manuseio de outro arquivo de baixo nível foi armazenado anteriormente em  TEXT, esse arquivo de baixo nível está fechado.

FCREATE( ) cria e abre arquivos de baixo nível e FOPEN( ) abre arquivos existentes. Estas funções devolvem um identificador de ficheiros positivo se o ficheiro for criado ou aberto com sucesso. Armazenar este arquivo para  TEXT direciona qualquer saída posterior dos comandos \,\\ e TEXT ... ENDTEXT text merge para o arquivo. Use STORE ou = para armazenar um punho de arquivo para  TEXT. Você deve abrir um arquivo de baixo nível com privilégios de escrita para que ele aceite o resultado dos comandos de mesclagem de texto.

Você pode fechar arquivos de baixo nível com FCLOSE( ) ou CLOSE ALL. Você também pode usar SET TEXTMERGE TO sem um nome de arquivo para fechar o arquivo de baixo nível cujo punho é armazenado em  TEXT.

O valor padrão de inicialização do  TEXT é –1. Se você estiver direcionando saída de mesclagem de texto para um arquivo cujo identificador de arquivo é armazenado em  TEXT, você pode desligar a saída para esse arquivo sem fechar o arquivo armazenando –1 para  TEXT. Ao armazenar diferentes manipuladores de arquivos e –1 para  TEXT, você pode direcionar saída de mesclagem de texto para arquivos alternativos.

Exemplo

O seguinte programa demonstra como direcionar a saída de mesclagem de texto para arquivos alternativos:

```foxpro
SET TALK OFF
SET TEXTMERGE ON NOSHOW      && Enable text merge, no output to screen
SET TEXTMERGE DELIMITERS TO   && Default text merge delimiters <<,>>
SET TEXTMERGE TO date.txt   && Create and send output to date.txt
STORE _TEXT TO gcDateHandle   && Save date.txt's file handle
STORE -1 TO _TEXT         && Output off to date.txt; keep it open
SET TEXTMERGE TO time.txt   && Create and send output to time.txt
STORE _TEXT TO gcTimeHandle   && Save time.txt's file handle
*** Send the following text to time.txt ***
\The time is:
STORE gcDateHandle TO _TEXT    && Now direct output to date.txt
*** Send the following text to date.txt ***
\Today's date is:
STORE gcTimeHandle TO _TEXT   && Now direct output to time.txt
*** Output the time on the same line ***
\\ <<TIME()>>
STORE gcDateHandle TO _TEXT   && Now direct output to date.txt
*** Output the date on the same line ***
\\ <<DATE()>>
CLOSE ALL  && Close all files
TYPE date.txt  && See what's in this file...
WAIT WINDOW  && Pause
TYPE time.txt  && ...and what's in this file
ERASE date.txt
ERASE time.txt
```

Veja também
- \ ~\\ Command
- FOPEN( ) Function
- FCLOSE( ) Function
- FCREATE( ) Function
- Variável do sistema  PRETEXT
