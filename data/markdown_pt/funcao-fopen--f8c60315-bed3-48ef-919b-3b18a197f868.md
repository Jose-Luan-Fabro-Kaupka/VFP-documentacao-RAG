# Função FOPEN( )

Abre um arquivo para uso com funções de arquivo de baixo nível.

```foxpro
FOPEN(cFileName [, nAttribute])
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo a ser aberto. cFileName pode incluir um caminho para abrir arquivos em diretórios, pastas, unidades ou volumes que não estejam no caminho de pesquisa atual do Microsoft Visual FoxPro. Se um caminho não for incluído, o Visual FoxPro pesquisa o arquivo nos seguintes locais: Diretório padrão Caminho estabelecido com SET PATH Observação O Visual FoxPro não reconhecerá corretamente um nome de caminho se o nome de um disco ou diretório contiver um ponto de exclamação (!).
**nAttribute**
Especifica privilégios de leitura/gravação ou um esquema de buffer para o arquivo que você abre. A tabela a seguir lista cada número que você pode incluir em nAttribute e os privilégios de leitura/gravação e o esquema de buffer que ele estabelece. nAttribute Privilégios de leitura/gravação Com/sem buffer 0 (Padrão) Somente leitura Com buffer 1 Somente gravação Com buffer 2 Leitura e gravação Com buffer 10 Somente leitura Sem buffer 11 Somente gravação Sem buffer 12 Leitura e gravação Sem buffer Se nAttribute não for incluído, ou se nAttribute for avaliado como 0, o arquivo é aberto como somente leitura e com buffer. Observação O Visual FoxPro não reconhecerá corretamente um nome de caminho se o nome de um disco ou diretório contiver um ponto de exclamação (!).

# Observações

Se FOPEN( ) abrir o arquivo com êxito, o número do identificador do arquivo é retornado. FOPEN( ) retorna –1 se o arquivo não puder ser aberto.

> **Dica:** Atribua o número do identificador do arquivo a uma variável de memória para que você possa acessar o arquivo por meio dessa variável em outras funções de arquivo de baixo nível.

As informações a seguir sobre arquivos abertos com FOPEN( ) podem ser exibidas ou enviadas a uma impressora com o comando DISPLAY STATUS ou os comandos LIST.
 - Unidade e diretório ou volume e pasta, e nome do arquivo
- Número do identificador do arquivo
- Posição do ponteiro do arquivo
- Atributos de leitura/gravação

# Valor de retorno

Numérico

# Exemplo

```foxpro
IF FILE('errors.txt')  && Does file exist?
   gnErrFile = FOPEN('errors.txt',12)  && If so, open read/write
ELSE
   gnErrFile = FCREATE('errors.txt')  && If not, create it
ENDIF
IF gnErrFile < 0  && Check for error opening file
   WAIT 'Cannot open or create output file' WINDOW NOWAIT
ELSE  && If no error, write to file
   =FWRITE(gnErrFile, 'Error information to be written here')
ENDIF
=FCLOSE(gnErrFile)  && Close file
MODIFY FILE errors.txt NOWAIT  && Open file in edit window
```
