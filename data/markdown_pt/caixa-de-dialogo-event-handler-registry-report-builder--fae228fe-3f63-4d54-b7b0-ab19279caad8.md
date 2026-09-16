# Caixa de diálogo Event Handler Registry (Report Builder)

Permite navegar pela tabela de registro de manipulador de eventos atual do Report Builder. Se o Report Builder estiver usando sua tabela de registro interna, esta caixa de diálogo é somente leitura e você não poderá personalizar as configurações.

Quando o Report Builder foi configurado para usar uma tabela de registro externa, a grade se torna editável e você pode personalizar o comportamento do Report Builder para cada evento individual do Report Designer.

Certifique-se de ter lido e compreendido o tópico Report Builder Event Handler Registry Table antes de fazer alterações na tabela.
 - Como: adicionar seu próprio manipulador ao registro do Report Builder

# Grade

Exibe a tabela de registro de manipulador de eventos atual do Report Designer para edição. Isso será somente leitura, a menos que o Report Builder Como: especificar uma tabela alternativa de manipulador de eventos de relatório.
 **Type**
Especifica o Handler Type. Valores válidos são H,F,X,G,E.
**Class**
Especifica o nome da classe.
**Library**
Especifica o arquivo de biblioteca de classes. Pode ser um nome de arquivo visual (.vcx) ou não visual (.prg).
**Description**
Permite inserir notas diversas para cada registro. Não usado pelo Report Builder.
**Event**
Especifica o tipo de evento para o qual a classe manipuladora está registrada. Use um valor de -1 para representar uma correspondência "curinga".
**Objtype**
Especifica o valor de OBJTYPE para o qual a classe manipuladora está registrada. Use um valor de -1 para representar uma correspondência "curinga".
**Objcode**
Especifica o valor de OBJCODE para o qual a classe manipuladora está registrada. Use um valor de -1 para representar uma correspondência "curinga".
**Native**
Especifica que, para esta combinação de tipo de evento e tipo de objeto, o Report Builder não interceptará o evento, mas o repassará ao Designer para processamento "normal". Observação Isso não é o mesmo que excluir o registro da tabela. Você pode usar isso para forçar o tratamento de evento nativo para um evento/objeto específico, mesmo se correspondências mais genéricas/curinga estiverem registradas.
**Debug**
Especifica que, para esta combinação de tipo de evento e tipo de objeto, o Report Builder usará a classe DebugHandler em vez da especificada pelas colunas Class e Library.

# Add Record

Acrescenta um registro à tabela de registro de manipulador de eventos atual e o destaca na grade, pronto para edição. Esta opção será desabilitada se a tabela de pesquisa de eventos for somente leitura. Isso é verdadeiro quando a tabela de pesquisa interna do Report Builder está sendo usada por padrão.
