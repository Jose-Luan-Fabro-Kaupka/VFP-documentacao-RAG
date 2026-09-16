# Noções básicas sobre páginas de código no Visual FoxPro

O Visual FoxPro exibe dados usando uma página de código. Por padrão, é a página atual do Windows, mas você pode substituí-la especificando outra página válida no arquivo de configuração.

As tabelas são marcadas com a página de código usada quando foram criadas. Ao usar uma tabela, o Visual FoxPro compara essa página com a atual. Se forem iguais, os dados são exibidos sem alteração. Se a tabela não tiver uma página, o Visual FoxPro solicita uma e marca o arquivo.

Ao ler uma tabela cuja página não corresponde à do sistema, o Visual FoxPro tenta converter os caracteres para a página atual. Por exemplo, se um caractere tiver valor ANSI 219 na tabela e valor ANSI 252 na página atual, todas as ocorrências de 219 serão convertidas em 252 para exibição correta.

A conversão nem sempre é perfeita, pois as páginas podem conter caracteres sem correspondência direta. Caracteres de desenho de linhas do MS-DOS, por exemplo, não existem nas páginas do Windows. Também pode não haver correspondência entre alfabetos, nem um mapa de conversão no Visual FoxPro. Nesse último caso, os dados são exibidos sem conversão e nenhum erro é informado. Essas situações podem causar exibição incorreta.

Ao gravar dados de caracteres modificados em uma tabela cuja página não corresponde à do sistema, o Visual FoxPro tenta converter os caracteres da página atual para a da tabela. No exemplo anterior, o valor ANSI 252 seria convertido em ANSI 219 para ser salvo corretamente.

Para criar um aplicativo para uma localidade específica, evite problemas criando seus componentes com a página de código adequada. Para um aplicativo usado na Rússia, por exemplo, use a página 1251. Consulte Páginas de código compatíveis com o Visual FoxPro.

Para inserir caracteres sem teclas correspondentes, use ALT com o teclado numérico. A mesma combinação pode produzir resultados diferentes em ambientes distintos. ALT+0182 na página 1252 exibe o símbolo de parágrafo; na página 437 do FoxPro para MS-DOS, exibe um caractere gráfico.

Embora o Visual FoxPro aceite muitas páginas de código, somente algumas são usadas com frequência. Usuários de língua inglesa normalmente usam a página 1252.

Ao trabalhar com páginas de código, teste se a interface e os dados são exibidos corretamente na página da localidade. Se aparecerem caracteres inesperados, verifique a página subjacente.
