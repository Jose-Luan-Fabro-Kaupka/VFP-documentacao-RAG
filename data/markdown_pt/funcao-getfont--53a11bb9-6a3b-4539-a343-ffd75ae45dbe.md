# Função GETFONT( )

Exibe a caixa de diálogo Fonte e retorna informações sobre a fonte que você escolhe.

```foxpro
GETFONT([cFontName [, nFontSize [, cFontStyle [, nFontCharSet]]]])
```

#### Parâmetros
 **cFontName**
Especifica o nome da fonte selecionada inicialmente na caixa de diálogo Fonte. Se a fonte que você especifica não está instalada, a fonte padrão é selecionada inicialmente.
**nFontSize**
Especifica o tamanho da fonte selecionado inicialmente na caixa de diálogo Fonte. Se o tamanho da fonte que você especifica não é suportado, o tamanho de fonte padrão é selecionado inicialmente. Se você omitir nFontSize ou se nFontSize é menor ou igual a zero, o tamanho de fonte selecionado tem como padrão 10 pontos. Observação A caixa de diálogo permite selecionar tamanhos entre 4 e 127 , inclusive. Você pode especificar outros valores para nFontSize ao chamar a função GETFONT; nenhum erro ocorre. Se você fizer isso, no entanto, o usuário deve selecionar um tamanho dentro do intervalo designado de valores antes de clicar em OK na caixa de diálogo. Caso contrário, a caixa de diálogo exibe um alerta e não aceita o valor.
**cFontStyle**
Especifica o estilo de fonte selecionado inicialmente na caixa de diálogo Fonte ou para exibir apenas as fontes disponíveis na impressora selecionada. Se o estilo de fonte que você especifica não é suportado, o estilo de fonte padrão é selecionado inicialmente. A tabela a seguir lista os valores disponíveis para cFontStyle . cFontStyle Descrição B Seleciona o estilo de fonte Bold inicialmente. I Seleciona o estilo de fonte Italic inicialmente. BI Seleciona o estilo de fonte Bold Italic inicialmente. P Exibe apenas as fontes disponíveis na impressora padrão atual.
**nFontCharSet**
Especifica um valor para o script de idioma. Os valores que você pode especificar diferem dependendo da sua versão do Windows. Observação Omitir este valor desabilita a lista suspensa de script na caixa de diálogo. A tabela a seguir descreve alguns valores de exemplo para nFontCharSet. nFontCharSet Script de idioma 0 Western 1 Default 2 Symbol 128 Japanese 161 Greek 162 Turkish 163 Vietnamese 177 Hebrew 178 Arabic 186 Baltic 204 Cyrillic 238 Central European Observação Se você especificar 1 para nFontCharSet , a caixa de diálogo que GETFONT( ) abriu exibe o script de idioma padrão no sistema operacional. GETFONT( ) nunca retorna 1 porque retorna o valor do script de idioma selecionado na caixa de diálogo GETFONT( ). Para obter mais informações, consulte Propriedade FontCharSet .

# Valor de retorno

Character. GETFONT( ) retorna um dos seguintes, dependendo de certas condições:
 - Uma cadeia de caracteres contendo três tipos de informações de fonte com vírgulas separando os itens retornados: nome da fonte, tamanho e estilo. Esse comportamento ocorre quando você escolhe um na caixa de diálogo Fonte e não incluiu o quarto argumento opcional ao chamar a função GETFONT( ).
- Uma cadeia de caracteres contendo quatro tipos de informações de fonte com vírgulas separando os itens retornados: nome da fonte, tamanho, estilo e script de idioma. Esse comportamento ocorre se você incluir um valor para o parâmetro nFontCharSet.

> **Observação:** Em versões do Visual FoxPro anteriores ao Visual FoxPro 9.0, se você incluía um valor de 0 como quarto argumento para GETFONT() , recebia as mesmas informações de retorno como se não incluísse o quarto argumento. A lista suspensa de script não era habilitada, e o valor de retorno continha apenas três tipos de informações de fonte. No Visual FoxPro 9.0, um valor de 0 indica explicitamente o valor numérico correspondente ao script Western. A lista suspensa de script também pode exibir inicialmente Western se você especificar 1 para este valor, mas somente se Western é o script padrão para suas configurações regionais.
 - Uma cadeia de caracteres vazia se você sair da caixa de diálogo Fonte clicando em Cancelar , Fechar no menu Controle ou pressionando a tecla ESC.

# Observações

> **Dica:** Você pode abreviar alguns comandos e funções do Visual FoxPro para quatro caracteres quando conflitos com outros comandos e funções não existem. No caso de GETFONT( ) e GETFILE( ) , que ambos começam com as mesmas quatro letras, a precedência é dada a GETFILE( ) ; portanto, emitir GETF( ) exibe a caixa de diálogo Abrir.

# Exemplo

O exemplo a seguir ilustra diferentes tipos de valores de retorno que você pode obter da função GETFONT( ).

```foxpro
* Invoke the dialog with script drop-down list disabled:
? GETFONT("Arial",12,"B") && press OK in the dialog box
* return value is the string:
* "Arial,12,B"
* Enable the script drop-down list, Western script selected:
? GETFONT("Arial",12,"B",0) && press OK after selections
* sample return value is the string:
* "Verdana,16,N,161"
* Return from the dialog box without making a selection:
? GETFONT("Arial",12,"B") && press Cancel in the dialog box
* return value is an empty string
? GETFONT("Arial",12,"B",0) && press Cancel in the dialog box
* return value is still an empty string
```
