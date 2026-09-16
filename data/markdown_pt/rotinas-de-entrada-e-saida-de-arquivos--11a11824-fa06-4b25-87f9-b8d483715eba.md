# Rotinas de entrada e saída de arquivos

Estas rotinas da API permitem criar e manipular arquivos diretamente.
 **Rotina de biblioteca da API _FCHSize( )**
Define o tamanho do arquivo em disco como o comprimento especificado. O comprimento especificado pode estender ou truncar o arquivo.
**Rotina de biblioteca da API _FClose( )**
Encerra o acesso a um arquivo. Quaisquer buffers modificados enquanto estavam abertos são automaticamente gravados em disco.
**Rotina de biblioteca da API _FCopy( )**
Tenta copiar len bytes da posição spos no arquivo sc para a posição dpos no arquivo dc.
**Rotina de biblioteca da API _FCreate( )**
Atribui um canal do Visual FoxPro a um novo arquivo.
**Rotina de biblioteca da API _FEOF( )**
Retorna True se o arquivo estiver atualmente no fim do arquivo; caso contrário, retorna False.
**Rotina de biblioteca da API _FError( )**
Retorna o último erro de operação de arquivo registrado para qualquer canal.
**Rotina de biblioteca da API _FFlush( )**
Garante que todos os buffers modificados na memória tenham sido gravados em disco.
**Rotina de biblioteca da API _FGets( )**
Lê de um arquivo uma única linha de comprimento maxlen, delimitada por um retorno de carro.
**Rotina de biblioteca da API _FOpen( )**
Atribui um canal do Visual FoxPro a um arquivo existente.
**Rotina de biblioteca da API _FPuts( )**
Grava em um arquivo uma cadeia de caracteres terminada por nulo, seguida por um par retorno de carro/avanço de linha.
**Rotina de biblioteca da API _FRead( )**
Lê exatamente length bytes de um arquivo para buffer.
**Rotina de biblioteca da API _FSeek( )**
Move o ponteiro do arquivo para um novo local conforme especificado por position e mode.
**Rotina de biblioteca da API _FWrite( )**
Grava exatamente length bytes do seu buffer em um arquivo. Nenhum terminador é adicionado ao arquivo.
