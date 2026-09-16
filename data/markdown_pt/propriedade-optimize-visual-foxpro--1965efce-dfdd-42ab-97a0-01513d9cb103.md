# Propriedade Optimize (Visual FoxPro)

Especifica se o controle Grid usa a otimização Rushmore. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Grid.Optimize [ = lExpr]
```

# Valor de retorno
 **lExpr**
Expressão lógica que especifica se o controle Grid usa a otimização Rushmore. Descrição da configuração: True (.T.) O controle Grid usa a otimização Rushmore. False (.F.) (Padrão) O controle Grid não usa a otimização Rushmore.

# Observações

Aplica-se a: controle Grid

Quando a otimização Rushmore é habilitada definindo a propriedade Optimize como True (.T.), o conjunto de registros correspondentes é atualizado durante as seguintes operações:
 - Quando o Grid é preenchido inicialmente
- Quando o Grid é ativado
- Quando o método Refresh do Grid é chamado

> **Observação:** Como ocorre com qualquer comando de manipulação de dados que possa afetar a otimização Rushmore, lembre-se de que as ações realizadas na origem de dados do Grid podem resultar em um comportamento diferente daquele observado quando a propriedade Optimize é definida como False (.F.). Por exemplo, a otimização Rushmore pode acionar implicitamente um TABLEUPDATE para um cursor com buffer de linha. Além disso, um erro pode ou não ocorrer dependendo de o registro estar em branco ou de o cursor ser uma exibição.
