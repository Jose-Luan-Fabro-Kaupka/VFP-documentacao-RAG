# Exemplo Print an Invoice

Arquivo: ...\Samples\Solution\Reports\Invoice.frx

Este relatório mostra um relatório de fatura que usa uma view para combinar informações de várias tabelas, uma função para coletar dados do usuário e um layout de relatório um-para-muitos. Quando o relatório é executado, a view é executada primeiro e solicita ao usuário um intervalo de datas usando uma função chamada Datepick.prg. Depois que o usuário fornece as datas, a view é executada e seleciona os registros a serem exibidos no relatório.

A fonte de registros A view INVOICE usada neste relatório reside no banco de dados TESTDATA fornecido com o projeto Solution. Esta view combina dados de quatro tabelas: CUSTOMER, ORDERS, ORDITEMS e PRODUCTS. Para filtrar as tabelas para registros dentro de um intervalo de datas, a view tem dois filtros, cada um com um parâmetro, dStart_Date e dEnd_Date.

O ambiente de dados A view está incluída no ambiente de dados. Para armazenar valores coletados para a view e restaurar a configuração de caminho, o método BeforeOpenTables do ambiente de dados declara três variáveis públicas: dStart_date, dEnd_Date e cOldPath. As duas primeiras correspondem aos parâmetros especificados na view. A terceira, cOldPath, salva a configuração de caminho atual para que o caminho possa ser restaurado no método Destroy. O caminho é então alterado para que o relatório possa encontrar a função, que solicita ao usuário um intervalo de datas. O comando final executa a função.

O método Destroy do ambiente de dados tem variáveis públicas para as datas de início e fim, configuração de caminho para retornar o caminho padrão ao que era antes de o relatório ser executado e instruções RELEASE para todas as três variáveis públicas.

O Datepick.prg Esta função define e executa uma classe de formulário chamada frmDATEPICK. A classe de formulário inclui quatro caixas de combinação que exibem e coletam valores para usar nas variáveis públicas dStart_Date e dEnd_Date. As quatro variáveis coletadas são nFromMonth, nFromYear, nToMonth e nToYear. Essas variáveis armazenam a entrada do usuário e são usadas para determinar o valor de dStart_Date e dEnd_Date. A função também verifica se o usuário inseriu valores para cada elemento da data e verifica se a data final é posterior à data inicial.

O layout do relatório No layout do relatório, uma banda Group Header contém os controles para as informações do cliente, a banda Detail tem os controles para os itens do pedido e a banda Group Footer contém os controles que exibem os valores calculados para a fatura.

Para formatar o endereço adequadamente, uma expressão no controle concatena vários campos com pontuação apropriada. Para calcular valores na banda Group Footer, duas variáveis de relatório, nSubtotal e nDiscount, armazenam valores para o subtotal e o desconto percentual.
