# Como: atualizar várias tabelas em uma view

Você pode atualizar várias tabelas base a partir de uma view. Quando sua view combina duas ou mais tabelas, defina propriedades para garantir que apenas o lado "many" da consulta da view seja atualizável.

Views são atualizadas tabela por tabela. Você deve garantir que, para cada tabela acessada em uma view, o conjunto de campos-chave seja uma chave exclusiva tanto para o conjunto de resultados da view quanto para a tabela base.

### Para tornar uma view multitable atualizável
- No Query and View Designers, escolha a guia Update Criteria e selecione as tabelas e nomes de campos que deseja atualizar. -ou-
- Use a função DBSETPROP( ).

Na maioria dos casos, os valores padrão fornecidos pelo Visual FoxPro preparam uma view multitable para ser atualizável, mesmo quando você cria a view programaticamente. O exemplo de código a seguir cria e define explicitamente propriedades para atualizar uma view de duas tabelas. Você pode usar este exemplo como guia para personalizar as configurações de propriedades de atualização em uma view.
 Atualizando várias tabelas em uma view
| Código | Comentários |
| --- | --- |
| CREATE SQL VIEW emp_cust_view AS ; SELECT employee.emp_id, ; employee.phone, customer.cust_id, ; customer.emp_id, customer.contact, ; customer.company ; FROM employee, customer ; WHERE employee.emp_id = customer.emp_id | Cria uma view que acessa campos de duas tabelas. |
| DBSETPROP('emp_cust_view', 'View', 'Tables', 'employee, customer') | Define as tabelas a serem atualizadas. |
| DBSETPROP('emp_cust_view.emp_id', 'Field', ; 'UpdateName', 'employee.emp_id') DBSETPROP('emp_cust_view.phone', 'Field', ; 'UpdateName', 'employee.phone') DBSETPROP('emp_cust_view.cust_id', 'Field', ; 'UpdateName', 'customer.cust_id') DBSETPROP('emp_cust_view.emp_id1', 'Field', ; 'UpdateName', 'customer.emp_id') DBSETPROP('emp_cust_view.contact', 'Field', ; 'UpdateName', 'customer.contact') DBSETPROP('emp_cust_view.company', 'Field', ; 'UpdateName', 'customer.company') | Define os nomes de atualização. |
| DBSETPROP('emp_cust_view.emp_id', 'Field', ; 'KeyField', .T.) | Define uma chave exclusiva de campo único para a tabela Employee. |
| DBSETPROP('emp_cust_view.cust_id', 'Field', ; 'KeyField', .T.) DBSETPROP('emp_cust_view.emp_id1', 'Field', ; 'KeyField', .T.) | Define uma chave exclusiva de dois campos para a tabela Customer. |
| DBSETPROP('emp_cust_view.phone', 'Field', ; 'Updatable', .T.) DBSETPROP('emp_cust_view.contact', 'Field', ; 'Updatable', .T.) DBSETPROP('emp_cust_view.company', 'Field', ; 'Updatable', .T.) | Define os campos atualizáveis. Normalmente, campos-chave não são atualizáveis. |
| DBSETPROP('emp_cust_view', 'View', ; 'SendUpdates', .T.) | Ativa a funcionalidade de atualização. |
| GO TOP REPLACE employee.phone WITH "(206)111-2222" REPLACE customer.contact WITH "John Doe" | Modifica dados na view. |
| TABLEUPDATE() | Confirma as alterações atualizando as tabelas base Employee e Customer. |
