# A configuração da propriedade não terá efeito até que o ambiente de dados seja recarregado (Erro 1739)

Você tentou definir uma propriedade em um objeto do ambiente de dados (objeto Relation ou objeto Cursor) enquanto o ambiente de dados estava carregado. O valor da propriedade será armazenado com o objeto, mas só terá efeito depois que o ambiente de dados for descarregado e recarregado.

### Para descarregar o ambiente de dados
- Execute CloseTables no formulário: [Formset.]Form.DataEnvironment.CloseTables

### Para recarregar o ambiente de dados
- Execute OpenTables no formulário: [Formset.]Form.DataEnvironment.OpenTables
