# Como: imprimir resultados de consulta em um relatório ou etiqueta

Se seu relatório ou etiqueta inclui grupos ou você precisa ordenar os dados de outra forma, você pode usar as várias cláusulas da instrução SELECT - SQL para obter exatamente os resultados necessários.

### Para enviar resultados a um relatório ou etiqueta existente
- Use a instrução SELECT - SQL com um comando REPORT ou LABEL. O exemplo a seguir usa as cláusulas GROUP BY e ORDER BY, bem como o comando REPORT FORM: SELECT * ; FROM tastrade!customer ; WHERE customer.country = "Canada" ; GROUP BY customer.region ; ORDER BY customer.postal_code, customer.company_name ; INTO CURSOR MyCursor REPORT FORM MYREPORT.FRX O exemplo a seguir usa um comando LABEL FORM: SELECT * ; FROM tastrade!customer ; WHERE customer.country = "Canada" ; GROUP BY customer.region ; ORDER BY customer.postal_code, customer.company_name ; INTO CURSOR mycursor LABEL FORM MYLABEL.LBX

Embora a instrução SELECT - SQL seja o método mais flexível para popular seu relatório ou etiqueta, não é o único método.
