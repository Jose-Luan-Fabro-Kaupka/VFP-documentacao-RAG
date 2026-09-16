# Função ASELOBJ( )

Coloca uma referência de objeto para o controle ou contêiner selecionado atualmente que existe no Form Designer, Class Designer ou janela de edição de código em uma matriz de variáveis especificada. Ao chamar ASELOBJ( ) em uma janela de edição de código, a matriz também inclui elementos para formulários (.scx), bibliotecas de classes visuais (.vcx) e nomes de arquivos #INCLUDE. Você também pode usar ASELOBJ( ) para criar construtores de controles.

```foxpro
ASELOBJ( ArrayName, [ 1 | 2 | 3 ] )
```

#### Parâmetros
 **ArrayName**
Especifica o nome da matriz que você deseja usar.
**1**
Cria uma matriz de um elemento contendo uma referência de objeto para o contêiner do controle ativo e selecionado atualmente. Por exemplo, se o controle ativo e selecionado atualmente é um spinner em um formulário, a matriz contém um elemento com o valor "FORM." Ao chamar ASELOBJ( ) na janela de comando, inclua este argumento. Observação Quando um page frame é selecionado, ASELOBJ() retorna o nome da página atual.
**2**
Cria uma matriz de um elemento contendo uma referência de objeto para o objeto DataEnvironment do formulário. O objeto DataEnvironment permite determinar as propriedades do ambiente de dados do formulário.
**3**
Cria uma matriz de três elementos contendo informações no contexto da janela de edição de código ativa atualmente: referência de objeto a um objeto contêiner, o caminho completo e o nome do arquivo .scx ou .vcx e o caminho completo e o nome do arquivo #INCLUDE, se disponível. A tabela a seguir mostra a ordem em que esses elementos aparecem. Elemento da matriz Descrição 1 Referência de objeto ao objeto contêiner 2 Caminho completo e nome do arquivo .scx ou .vcx 3 Caminho completo e nome do arquivo #INCLUDE, se disponível Observação Se nenhum arquivo #INCLUDE estiver disponível, o terceiro elemento contém uma cadeia de caracteres vazia.

# Valor de retorno

Tipo de dados numérico. ASELOBJ( ) retorna o número de objetos selecionados. A matriz contém três colunas e uma linha para cada objeto selecionado. .

# Observações

Se nenhum controle estiver selecionado e o argumento 1 for omitido, ASELOBJ( ) retorna 0 e não cria a matriz. Se não existirem controles no formulário, ASELOBJ( ) não reconhece o formulário como o controle selecionado. Se nenhum controle estiver selecionado no momento e o argumento 1 for incluído, ASELOBJ( ) retorna 1.

Se a matriz não existir, o Visual FoxPro cria a matriz automaticamente.

Se a matriz existir, mas for pequena demais para conter todas as informações, o Visual FoxPro aumenta automaticamente o tamanho da matriz para acomodar as informações. Se a matriz for maior do que o necessário, o Visual FoxPro trunca a matriz.

Se a matriz existir e ASELOBJ( ) retornar 0 porque nenhum controle está selecionado, a matriz permanece inalterada. Se a matriz não existir e ASELOBJ( ) retornar 0, a matriz não é criada.

# Exemplo

Antes de executar o exemplo a seguir, abra um novo formulário no Form Designer e adicione um ou mais controles com propriedades Caption, como Label ou CommandButton, ao formulário. Selecione vários desses controles e execute o exemplo. ASELOBJ( ) exibe os nomes dos controles selecionados e depois altera as legendas dos controles selecionados.

```foxpro
gnobjects = ASELOBJ(gaSelected)     && Create array of control names
IF gnobjects > 0  && 0 indicates no controls selected
   CLEAR
   DISPLAY MEMORY LIKE gaSelected     && Displays selected controls
   FOR nCnt = 1 TO gnobjects
      ? gaSelected(nCnt).Caption + ' => New Caption ' ;
         + LTRIM(STR(nCnt))  && Display old and new caption
      gaSelected(nCnt).Caption = 'New Caption ' ;
         + ALLTRIM(STR(nCnt))  && Assign new caption
   NEXT
ENDIF
```
