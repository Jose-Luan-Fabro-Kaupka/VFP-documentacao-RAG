# Comando CALL

Incluído para compatibilidade com versões anteriores. Use o comando SET LIBRARY em vez disso.

Executa um arquivo binário, comando externo ou função externa que foi colocado na memória com LOAD.

```foxpro
CALL file
	[WITH expC | WITH memvar1]
	[TO memvar2]
	[SAVE | NOSAVE]
```

#### Parâmetros
 file

 No FoxPro para MS-DOS e FoxPro para Windows, o arquivo binário a ser chamado é especificado com file. Não é necessário especificar uma extensão no nome do arquivo, pois a extensão é removida do arquivo quando é carregado.

 No FoxPro para Macintosh, use file para especificar o comando externo ou função externa a executar.

WITH expC | WITH memvar1

 WITH pode ser usado para passar um parâmetro de cadeia de caracteres ou variável de memória para a sub-rotina binária, comando externo ou função externa. A variável de memória pode ser de qualquer tipo de dados.

 No FoxPro para MS-DOS e FoxPro para Windows, você pode passar um único parâmetro para a rotina binária.

 No FoxPro para Macintosh, você pode passar múltiplos parâmetros em uma expressão de caractere delimitada por vírgulas.

 No FoxPro para MS-DOS e FoxPro para Windows, quando o arquivo binário chamado é executado, o segmento de código inicialmente aponta para o início do módulo. O par DS e BX aponta para o primeiro byte do parâmetro passado usando WITH. Se nenhum parâmetro é passado, BX contém 0.

TO memvar2

 Uma rotina binária, comando externo ou função externa pode retornar um valor para uma variável de memória incluindo a cláusula TO memvar2.

SAVE | NOSAVE

 No FoxPro para MS-DOS e FoxPro para Windows, CALL e LOAD suportam a palavra-chave SAVE para uso com rotinas binárias que gravam na tela.

 SAVE e NOSAVE são ignorados no FoxPro para Macintosh.

 NOSAVE é o padrão. Você pode incluir SAVE ao carregar uma rotina binária com CALL, ou SAVE e NOSAVE ao carregar uma rotina binária na memória com LOAD. Se especificado com CALL, SAVE ou NOSAVE substitui a configuração SAVE ou NOSAVE especificada com LOAD.

 Se CALL ... SAVE é especificado, o FoxPro copia o conteúdo atual da RAM de vídeo para a janela principal do FoxPro ao retornar da rotina binária (assumindo que a rotina binária está gravando diretamente na RAM de vídeo). Isso significa que qualquer coisa escrita pela rotina binária é conhecida pelo FoxPro e é tratada como se o FoxPro tivesse escrito. Em particular, se SAVE está em vigor, tais dados escritos externamente não serão apagados na primeira vez que um objeto FoxPro é arrastado sobre eles.

 A menos que seja necessário, a cláusula SAVE não é desejável, pois leva algum tempo para o FoxPro examinar e salvar o conteúdo da tela a cada retorno da rotina binária.

# Observações

CALL funciona em conjunto com LOAD.

No FoxPro para MS-DOS e FoxPro para Windows, CALL é usado para executar rotinas binárias personalizadas diretamente da memória. LOAD coloca o arquivo binário na memória. CALL executa o arquivo binário carregado.

No FoxPro para Macintosh, CALL é usado para executar um comando externo (XCMD) ou função externa (XFNC) que foi colocado na memória com SET XCMDFILE e LOAD.
