# Como: definir o número máximo de registros baixados

Você pode controlar a quantidade de dados baixados ao abrir uma view definindo a propriedade MaxRecords. Quando o Visual FoxPro envia uma instrução SQL à origem de dados para criar uma view, a origem de dados constrói e armazena um conjunto de resultados. A propriedade MaxRecords especifica o número máximo de linhas buscadas do conjunto de resultados remoto para sua view. A configuração padrão é –1, que baixa todas as linhas do conjunto de resultados.

### Para controlar o número de linhas baixadas em uma view
- No menu Tools, escolha Options e selecione a guia Remote Data; em seguida, na área Remote view defaults, ao lado da caixa Maximum records to fetch, desmarque All, insira um valor na caixa de texto e escolha OK. -ou-
- Use a propriedade MaxRecords da função DBSETPROP( ) ou CURSORSETPROP( ).

Por exemplo, o código a seguir altera a definição da view para limitar o número de linhas baixadas na view a 50, independentemente do tamanho do conjunto de resultados construído na origem de dados remota:

```foxpro
OPEN DATABASE testdata
USE VIEW remote_customer_view
?DBSETPROP ('Remote_customer_view', ;    'View','MaxRecords', 50)
```

Você pode usar a função CURSORSETPROP( ) para definir o limite MaxRecords para uma view ativa.

> **Dica:** Você não pode usar a propriedade MaxRecords para interromper uma consulta descontrolada, porque a propriedade MaxRecords não controla a construção do conjunto de resultados. Use a propriedade QueryTimeOut para controlar o tempo de execução na origem de dados remota.
