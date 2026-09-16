# UseDeDataSource Propriedade

Determina se a fonte de dados do contêiner do ambiente de dados deve ser usada como fonte de dados para o objeto CursorAdapter. A fonte de dados do ambiente de dados associado é especificada pela propriedade DataEnvironment DataSource. Leitura/gravação em tempo de design e tempo de execução.

> **Nota:** UseDeDataSource se aplica somente quando o adaptador de cursor existe no ambiente de dados.

```foxpro
CursorAdapter.UseDeDataSource [ = lValue ]
```

# Valor de retorno
 **lValue**
Tipo de dados lógicos. A tabela a seguir lista as configurações para lValue . lValue Descrição Verdadeiro (.T.) Use a fonte de dados do ambiente de dados associado como a fonte de dados do adaptador do cursor. Definir UseDeDataSource como True (.T.) não é apropriado se o ambiente de dados contiver vários objetos CursorAdapter usando fontes de dados ActiveX Data Object (ADO). Vários adaptadores de cursor não podem compartilhar um único ADO RecordSet. Você deve definir as propriedades DataSource e DataSourceType de cada adaptador de cursor individualmente. Se o adaptador de cursor for um membro do ambiente de dados, as propriedades DataEnvironment DataSource e DataSourceType substituirão as propriedades CursorAdapter relevantes. Falso (.F.) Não use a origem de dados do ambiente de dados associado como origem de dados do adaptador do cursor.

# Observações
Aplica-se a: CursorAdapter Classe
