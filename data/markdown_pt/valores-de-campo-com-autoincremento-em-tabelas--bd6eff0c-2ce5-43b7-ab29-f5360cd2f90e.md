# Valores de campo com autoincremento em tabelas

Você pode especificar que campos inteiros de tabelas de banco de dados e tabelas livres contenham valores que incrementam automaticamente. Uma tabela pode conter vários campos inteiros que contenham valores com incremento automático. O autoincremento não é suportado para views locais, remotas ou offline.

Quando você adiciona um campo com valores de incremento automático a uma tabela que não contenha um, os valores começam a incrementar automaticamente com a próxima linha adicionada na tabela. As linhas anteriores na tabela não são atualizadas com valores de incremento automático; portanto, certifique-se de que não ocorram conflitos como resultado.

Para obter mais informações sobre como definir valores de campo com incremento automático, consulte How to: Set Autoincrementing Field Values.

As seções a seguir contêm mais informações sobre áreas do Visual FoxPro afetadas por valores de campo com incremento automático:
 - Table Structure Changes for Autoincrementing Field Values
- Considerations for Autoincrementing Field Values
- Local Views and Autoincrementing Field Values
- Buffered Tables and Autoincrementing Field Values
- Record Locking and Autoincrementing Field Values

# Table Structure Changes for Autoincrementing Field Values

Quando você ativa valores de incremento automático para qualquer campo em uma tabela, o Visual FoxPro define o byte 0 como 0x31 para o tipo de arquivo "Visual FoxPro, Autoincrement enabled" na estrutura do registro de cabeçalho da tabela (.dbf). O Visual FoxPro define o byte 18, os bytes 19 a 22 e o byte 23 na estrutura de subregistros de campo com os seguintes valores, respectivamente:
 - 0x0C para a coluna de autoincremento.
- Próximo valor.
- Valor de incremento.

Para obter mais informações, consulte Table File Structure (.dbc, .dbf, .frx, .lbx, .mnx, .pjx, .scx, .vcx).

# Considerations for Autoincrementing Field Values

Um campo que contém valores de incremento automático torna-se somente leitura e não pode ser alterado com uma operação insert, update ou replace. Tentar atualizar esse campo gera uma mensagem de erro, a menos que você defina a propriedade AutoIncError do cursor usando a função CURSORSETPROP( ) como False (.F.) ou desative a mensagem de erro usando o comando SET AUTOINCERROR. Para obter mais informações, consulte CURSORSETPROP( ) Function e SET AUTOINCERROR Command.

Tabelas que contêm valores de campo com incremento automático acrescentam registros com buffer de tabela aproximadamente 35% mais lentamente que tabelas sem valores de campo com incremento automático, o que pode afetar o desempenho. Ao usar buffer de tabela, o cabeçalho da tabela é bloqueado quando o registro é acrescentado.

O Visual FoxPro não gerencia lacunas em sequências geradas. Lacunas podem ser causadas por reverter um registro acrescentado ou inserido ou por falhar ao atualizar a tabela base e assim por diante. Em todos os casos, o valor não utilizado é perdido e o próximo valor gerado permanece o mesmo como se a operação de append ou insert tivesse sido bem-sucedida.

Versões anteriores ao Visual FoxPro 8.0 não reconhecem tabelas que usam valores de campo com incremento automático. Se você remover o autoincremento dos campos, o estado atual contendo o último valor de incremento e os valores incrementais é limpo do subregistro de campo da tabela (.dbf) e descartado. O tipo da tabela (.dbf) é restaurado para o valor de tipo Visual FoxPro atual. Os valores de incremento automático armazenados anteriormente em cada registro permanecem.

# Local Views and Autoincrementing Field Values

Views não "herdam" o comportamento de autoincremento da tabela base, e os campos na view que representam campos de autoincremento na tabela base são leitura/gravação. Valores de campo com incremento automático ocorrem na tabela base quando a linha ou linhas são atualizadas na tabela base. Se você deseja atualizar a view com o valor de campo de autoincremento gerado anteriormente, deve usar a função REQUERY( ). Para obter mais informações, REQUERY( ) Function.

# Buffered Tables and Autoincrementing Field Values

O Visual FoxPro não executa nenhum gerenciamento de autoincremento em relação a tabelas com buffer. Todos os registros acrescentados e inseridos têm valores de campo com incremento automático gerados, independentemente de o buffer de tabela ou de linha estar ativo. No caso de buffer, quando a função TABLEUDPATE( ) é chamada, a tabela base é atualizada com o valor gerado anteriormente. Se a atualização não ocorrer, como ao chamar a função TABLEREVERT( ), quaisquer valores de campo com incremento automático gerados são descartados, resultando em lacunas na sequência.

# Record Locking and Autoincrementing Field Values

Quando você ativa valores de autoincremento para um campo, os valores inicial e incremental Next Value e Step são armazenados no cabeçalho da tabela (.dbf) na porção não utilizada ou reservada do subregistro de campo para o campo especificado. Next Value é armazenado como um inteiro de 4 bytes. O valor Step é armazenado como um inteiro de 1 byte com valor máximo de 255. O valor realmente usado para incrementar o valor do campo é a soma do valor armazenado no cabeçalho .dbf e do valor incremental. A sequência de operação ocorre da seguinte forma:
 - Execute uma operação insert ou append.
- Bloqueie o cabeçalho.
- Aumente o valor de incremento atualmente armazenado pelo valor Step e aplique ao campo.
- Armazene o novo valor, que é o valor do registro recém-adicionado, no cabeçalho do arquivo .dbf.
- Desbloqueie o cabeçalho quando a operação insert ou append for concluída. O cabeçalho contém o último valor incrementado.
