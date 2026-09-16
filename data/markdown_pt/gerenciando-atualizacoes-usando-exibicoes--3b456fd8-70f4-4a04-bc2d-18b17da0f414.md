# Gerenciando atualizações usando exibições

Você pode usar a tecnologia de gerenciamento de conflitos de atualização integrada às exibições do Visual FoxPro para lidar com acesso multiusuário a dados. As exibições controlam o que é enviado às tabelas base subjacentes à exibição usando a propriedade WhereType. Você pode definir essa propriedade para exibições locais e remotas. A propriedade WhereType fornece quatro configurações:
 - DB_KEY
- DB_KEYANDUPDATABLE
- DB_KEYANDMODIFIED (o padrão)
- DB_KEYANDTIMESTAMP

Ao escolher uma dessas quatro configurações, você controla como o Visual FoxPro constrói a cláusula WHERE para a instrução SQL Update enviada às tabelas base da exibição. Você pode escolher a configuração desejada usando a guia Update Criteria Tab, View Designer do View Designer ou pode usar a função DBSETPROP( ) para definir WhereType para uma definição de exibição. Para alterar a configuração WhereType para um cursor de exibição ativo, use a função CURSORSETPROP( ).

| Para... | Escolha esta opção SQL WHERE... |
| --- | --- |
| Fazer a atualização falhar se um campo-chave foi alterado na tabela de origem | Key fields only |
| Fazer a atualização falhar se qualquer um dos campos marcados como atualizáveis foi alterado na tabela remota | Key and updatable fields |
| Fazer a atualização falhar se qualquer campo que você alterar localmente foi alterado na tabela de origem | Key and modified fields |
| Fazer a atualização falhar se o timestamp do registro na tabela remota mudou desde que você o recuperou pela primeira vez (disponível somente se a tabela remota tem uma coluna de timestamp) | Key and timestamp |

Por exemplo, suponha que você tenha uma exibição remota simples baseada na tabela Customer que inclui sete campos: `cust_id`, `company`, `phone`, `fax`, `contact`, `title` e `timestamp`. A chave primária da sua exibição é `cust_id`.

Você tornou apenas dois campos atualizáveis: `contact_name` e `contact_title`. Você deseja que o usuário possa alterar o contato da empresa e seu cargo a partir da exibição. No entanto, se outros fatos sobre a empresa mudarem, como o endereço da empresa, você deseja que as alterações passem por um coordenador que identificará o impacto das alterações em sua empresa, como se a região de vendas do cliente mudará. Agora que sua exibição foi configurada para enviar atualizações, você pode escolher WhereType conforme suas preferências.

Agora suponha que você altere o nome no campo `contact` de um cliente, mas não altere o valor no outro campo atualizável, `title`. Dado este exemplo, a seção a seguir discute como a configuração WhereType afetaria a cláusula WHERE que o Visual FoxPro constrói para enviar o novo nome de contato às tabelas base.

# Comparando somente o campo-chave

A atualização menos restritiva usa a configuração DB_KEY. A cláusula WHERE usada para atualizar tabelas remotas consiste apenas no campo de chave primária especificado com a propriedade KeyField ou KeyFieldList. A menos que o valor no campo de chave primária tenha sido alterado ou excluído na tabela base desde que você recuperou o registro, a atualização é concluída.

No caso do exemplo anterior, o Visual FoxPro prepararia uma instrução de atualização com uma cláusula WHERE que compara o valor no campo `cust_id` com o campo `cust_id` na linha da tabela base:

```foxpro
WHERE OLDVAL(customer.cust_id) = CURVAL(customer_remote_view.cust_id)
```

Quando a instrução de atualização é enviada à tabela base, apenas o campo-chave da tabela base é verificado.
 O campo-chave na sua exibição é comparado com seu equivalente na tabela base.

# Comparando o campo-chave e os campos modificados na exibição

A configuração DB_KEYANDMODIFIED, o padrão, é um pouco mais restritiva que DB_KEY. DB_KEYANDMODIFIED compara apenas o campo-chave e quaisquer campos atualizáveis que você modificou na exibição com seus equivalentes na tabela base. Se você modificar um campo na exibição, mas o campo não for atualizável, os campos não são comparados aos dados da tabela base.

A cláusula WHERE usada para atualizar tabelas base consiste nos campos primários especificados com a propriedade KeyFieldList e quaisquer outros campos modificados na exibição. No caso do exemplo anterior, o Visual FoxPro prepararia uma instrução de atualização que compara os valores no campo `cust_id` porque é o campo-chave, e no campo `contact` porque o nome do contato foi alterado. Embora o campo `title` seja atualizável, `title` não é incluído na instrução de atualização porque não foi modificado.
 Os campos-chave e modificados na sua exibição são comparados com seus equivalentes na tabela base.

# Comparando o campo-chave e todos os campos atualizáveis

A configuração DB_KEYANDUPDATABLE compara o campo-chave e quaisquer campos atualizáveis (modificados ou não) na sua exibição com seus equivalentes na tabela base. Se o campo for atualizável, mesmo que você não o tenha alterado na exibição, se outra pessoa alterou esse campo na tabela base, a atualização falha.

A cláusula WHERE usada para atualizar tabelas base consiste nos campos primários especificados com a propriedade Key Field ou KeyFieldList e quaisquer outros campos atualizáveis. No caso do exemplo, o Visual FoxPro prepararia uma instrução de atualização que compara os valores nos campos `cust_id`, `contact` e `title` com os mesmos campos na linha da tabela base.
 Todos os campos atualizáveis na sua exibição são comparados com seus equivalentes na tabela base.

# Comparando o timestamp de todos os campos no registro da tabela base

DB_KEYANDTIMESTAMP é o tipo de atualização mais restritivo e está disponível somente se a tabela base tem uma coluna de timestamp. O Visual FoxPro compara o timestamp atual no registro da tabela base com o timestamp no momento em que os dados foram recuperados na exibição. Se qualquer campo no registro da tabela base mudou, mesmo que não seja um campo que você está tentando alterar, ou mesmo um campo na sua exibição, a atualização falha.

No caso do exemplo, o Visual FoxPro prepara uma instrução de atualização que compara os valores no campo `cust_id` e o valor no campo `timestamp` com esses campos na linha da tabela base.
 O timestamp do registro da sua exibição é comparado com o timestamp no registro da tabela base.

Para atualizar dados com sucesso usando a configuração DB_KEYANDTIMESTAMP com uma exibição de várias tabelas, você deve incluir o campo de timestamp na sua exibição para cada tabela que é atualizável. Por exemplo, se você tem três tabelas em uma exibição e deseja atualizar apenas duas delas, e escolhe a configuração DB_KEYANDTIMESTAMP, deve trazer os campos de timestamp das duas tabelas atualizáveis para o conjunto de resultados. Você também pode usar valores lógicos na propriedade CompareMemo para determinar se campos memo são incluídos na detecção de conflitos.
