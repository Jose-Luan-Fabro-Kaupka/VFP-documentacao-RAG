# Preparando para atualizar exibições

Antes de poder atualizar dados em uma exibição, as propriedades da exibição que controlam atualizações devem ser definidas para que a exibição possa ser atualizada. Na maioria dos casos, os valores padrão das propriedades da exibição são definidos para que a exibição possa ser atualizada.

A tabela a seguir lista as propriedades da exibição que controlam atualizações e suas configurações padrão para exibições.

| Propriedade da exibição | Configuração padrão |
| --- | --- |
| Tables | Inclui todas as tabelas que têm campos atualizáveis e que possuem pelo menos um campo de chave primária. |
| KeyField | Campos-chave do banco de dados e chaves primárias remotas na tabela. |
| UpdateName | Table_name.column_name para todos os campos. |
| Updateable | Atualiza todos os campos, exceto campos de chave primária. |
| SendUpdates | O padrão é o padrão da sessão, que é originalmente definido como False (.F.). Se você alterá-lo para True (.T.), isso se torna o padrão para todas as exibições criadas na sessão. Observação Embora todas as propriedades na tabela sejam necessárias para atualizar dados, a propriedade SendUpdates da exibição controla se as atualizações serão enviadas. Você deve definir SendUpdates como True (.T.) para enviar atualizações à fonte de dados. Dica Ao desenvolver seu aplicativo, você pode querer definir SendUpdates como False (.F) para poder definir outras propriedades da exibição sem atualizar dados. Quando estiver pronto para testar seu aplicativo, defina a propriedade SendUpdates como True (.T.) para começar a atualizar dados. |
| CompareMemo | O padrão é True (.T.), o que significa que campos memo são incluídos na cláusula WHERE e são usados para detectar conflitos de atualização. |

> **Observação:** As configurações padrão das propriedades da exibição podem não habilitar atualizações para uma exibição criada programaticamente. Para habilitar atualizações para exibições criadas programaticamente, revise as configurações padrão das propriedades da exibição e ajuste-as conforme necessário. Para alterar as configurações das propriedades da exibição, use a função DBSETPROP( ) . Para obter mais informações, consulte DBSETPROP( ) Function .

> **Observação:** Por padrão, o buffer de linha otimista é usado para exibições. No entanto, você pode alterar isso para buffer de tabela. Para obter mais informações, consulte How to: Perform Updates Using Buffers .
