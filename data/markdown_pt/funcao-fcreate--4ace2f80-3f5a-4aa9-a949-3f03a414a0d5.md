# Função FCREATE( )

Cria e abre um arquivo de baixo nível.

```foxpro
FCREATE(cFileName [, nFileAttribute])
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo a criar. Você pode incluir um designador de unidade e caminho com o nome do arquivo. Se um designador de unidade ou caminho não for incluído, o arquivo é criado no diretório padrão. Observação O Visual FoxPro não reconhece um caminho corretamente se um nome de disco ou diretório contém um ponto de exclamação (!).
**nFileAttribute**
Especifica os atributos do arquivo criado. A tabela a seguir lista os atributos de arquivo que você pode especificar. nFileAttribute Atributos de arquivo 0 (Padrão) Leitura/gravação 1 Somente leitura 2 Oculto 3 Somente leitura/Oculto 4 Sistema 5 Somente leitura/Sistema 6 Sistema/Oculto 7 Somente leitura/Oculto/Sistema Observe que um arquivo criado com nFileAttribute diferente de 0 não pode ser gravado com FPUTS( ) ou FWRITE( ) até que o arquivo seja fechado e aberto novamente. Use DISPLAY STATUS ou LIST STATUS para exibir ou imprimir informações sobre arquivos criados e abertos com FCREATE( ) . DISPLAY STATUS e LIST STATUS fornecem as seguintes informações sobre cada arquivo aberto ou criado com uma função de arquivo de baixo nível: A unidade, o diretório e o nome do arquivo O número do identificador de arquivo A posição do ponteiro do arquivo Os atributos de leitura/gravação

# Valor de retorno

Numérico

# Observações

Se um arquivo com o nome especificado já existir, ele é substituído sem aviso.

FCREATE( ) atribui um número de identificador de arquivo ao arquivo, que você pode usar para identificar o arquivo em outras funções de arquivo de baixo nível do Visual FoxPro. FCREATE( ) retorna o número do identificador de arquivo quando um arquivo é criado ou retorna –1 se o arquivo não puder ser criado.

> **Dica:** Atribua o número do identificador de arquivo a uma variável de memória para que você possa acessar o arquivo pela variável em outras funções de arquivo de baixo nível.

Você não pode abrir uma porta de comunicação com FCREATE( ). Use FOPEN( ) para abrir uma porta de comunicação.

# Exemplo

```foxpro
IF FILE('errors.txt')  && Does file exist?
   gnErrFile = FOPEN('errors.txt',12)     && If so, open read/write
ELSE
   gnErrFile = FCREATE('errors.txt')  && If not create it
ENDIF
IF gnErrFile < 0     && Check for error opening file
   WAIT 'Cannot open or create output file' WINDOW NOWAIT
ELSE  && If no error, write to file
   =FWRITE(gnErrFile , 'Error information to be written here')
ENDIF
=FCLOSE(gnErrFile )     && Close file
IF gnErrFile > 0
MODIFY FILE errors.txt NOWAIT  && Open file in edit window
ENDIF
```
