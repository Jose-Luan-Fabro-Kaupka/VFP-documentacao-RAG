# Como: exibir resultados de consulta em uma janela

Se você deseja exibir os resultados de sua instrução SELECT - SQL, pode enviar os resultados para uma janela. A janela Browse é o destino padrão para resultados de consulta e você não precisa incluir uma cláusula de destino. Você também pode enviar os resultados para a janela principal do Visual FoxPro ou outra janela ativa.

### Para exibir resultados na janela principal do Visual FoxPro
- Use a cláusula TO SCREEN de uma instrução SELECT - SQL.

### Para exibir resultados em outra janela ativa
- Defina uma janela, mostre-a para ativá-la e, em seguida, execute uma consulta SQL ou outro comando que exiba resultados em uma janela.

Este exemplo de código mostra a definição de uma janela temporária intitulada "Top Customers" que exibe os nomes de empresas com mais de US$ 5.000 em pedidos totais para o ano.
 Exibindo resultados de consulta em uma janela
| Código | Comentário |
| --- | --- |
| frmMyForm=createobj("form") frmMyForm.Left = 1 frmMyForm.Top = 1 frmMyForm.Width = 130 frmMyForm.Height = 25 frmMyForm.Caption = "Top Customers" frmMyForm.Show | Cria e inicia um objeto de janela temporário. |
| SELECT customer.company_name,; SUM(orders.freight) ; FROM tastrade!customer, tastrade!orders ; WHERE customer.customer_id = orders.customer_id ; GROUP BY customer.company_name ; HAVING SUM(orders.freight) > 5000 ; ORDER BY 2 DESC | Insere uma instrução SELECT - SQL. |
