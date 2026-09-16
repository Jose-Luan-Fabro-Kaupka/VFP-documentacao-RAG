# Otimização do acesso a dados remotos

A recuperação de dados de qualquer banco de dados remoto é custosa. Para obter dados de um banco de dados de servidor, as seguintes etapas devem ocorrer:
 - O cliente emite a consulta ao banco de dados remoto.
- O servidor analisa e compila a consulta.
- O servidor gera um conjunto de resultados.
- O servidor notifica o cliente que o resultado está completo.
- O cliente busca os dados pela rede a partir do servidor. Esta etapa pode ocorrer de uma só vez, ou o cliente pode solicitar que os resultados sejam enviados em partes conforme solicitado.

Você pode usar várias técnicas para acelerar a recuperação (ou atualização) de dados, como:
 - Recuperar somente os dados necessários
- Atualizar tabelas remotas com eficiência
- Enviar instruções em lote
- Definir tamanho do pacote
- Atrasar a recuperação de dados memo e binários
- Armazenar dados de pesquisa localmente
- Criar regras locais

# Recuperar somente os dados necessários

Na maioria dos aplicativos que usam dados remotos, formulários e relatórios não precisam acessar todos os dados de uma tabela de uma só vez. Portanto, você pode melhorar o desempenho criando exibições remotas que buscam ou atualizam somente os campos e registros desejados, minimizando a quantidade de dados que precisa ser transmitida pela rede.

Para criar consultas que minimizem a sobrecarga de recuperação de dados de fontes remotas, siga estas sugestões:
 - Especifique somente os campos necessários. Não use a instrução SELECT * FROM customers a menos que precise de todos os campos da tabela.
- Inclua uma cláusula WHERE para limitar o número de registros baixados. Quanto mais específica for sua cláusula WHERE, menos registros serão transmitidos ao seu computador e mais rápida a consulta terminará.
- Se você não puder prever em tempo de design quais valores usar em uma cláusula WHERE, pode usar parâmetros na cláusula. Quando a consulta é executada, o Visual FoxPro usa o valor de uma variável de parâmetro ou solicita ao usuário o valor de pesquisa. Por exemplo, esta consulta permite que o aplicativo ou o usuário preencha a região em tempo de execução: SELECT cust_id, company, contact, address ; FROM customers ; WHERE region = ?pcRegion
- Defina a propriedade NoDataOnLoad do objeto Cursor correspondente do ambiente de dados. Esta técnica é comumente usada com exibições parametrizadas em que os dados do parâmetro vêm do valor de um controle em um formulário.

# Atualizar tabelas remotas com eficiência

Quando você usa uma exibição para atualizar uma tabela em uma fonte de dados remota, o Visual FoxPro deve verificar se o registro ou os registros que você está atualizando foram alterados. Para isso, o Visual FoxPro deve examinar os dados no servidor e compará-los aos dados mantidos no seu computador. Em alguns casos, isso pode ser uma operação demorada.

Para otimizar o processo de atualização de dados em fontes de dados remotas, você pode especificar como o Visual FoxPro deve verificar registros alterados. Para fazer isso, indique a cláusula WHERE que o Visual FoxPro deve gerar para realizar a atualização.

Por exemplo, imagine que você está usando uma exibição baseada em uma tabela de clientes em uma fonte de dados remota. Você criou a exibição usando uma instrução do comando SELECT - SQL como esta:

```foxpro
SELECT cust_id, company, address, contact ;
   FROM customers ;
   WHERE region = ?vpRegion
```

Você deseja poder atualizar todos os quatro campos especificados na exibição, exceto o campo-chave (`cust_id`). A tabela a seguir ilustra a cláusula WHERE que o Visual FoxPro gerará para cada uma das opções disponíveis na cláusula SQL WHERE.

> **Observação:** A função OLDVAL( ) retorna a versão pré-atualização dos campos que você modificou, e a função CURVAL( ) retorna o valor atual armazenado na fonte de dados remota. Comparando-os, o Visual FoxPro pode determinar se o registro foi alterado na fonte de dados remota desde que você o baixou para o seu computador.

| Configuração | Cláusula WHERE resultante |
| --- | --- |
| Key fields only | WHERE OLDVAL(cust_id) = CURVAL(cust_id) |
| Key and updatable fields (default) | WHERE OLDVAL(cust_id) = CURVAL(cust_id) AND OLDVAL(<mod_fld1>) = CURVAL(<mod_fld2>) AND OLDVAL(<mod_fld2>) = CURVAL(<mod_fld2>) AND ... |
| Key and modified fields | WHERE OLDVAL(cust_id) = CURVAL(cust_id) AND OLDVAL(company) = CURVAL(company) AND OLDVAL(contact) = CURVAL(contact) AND OLDVAL(address) = CURVAL(address) |
| Key and timestamp | WHERE OLDVAL(cust_id) = CURVAL(cust_id) AND OLDVAL(timestamp) = CURVAL(timestamp) |

Em geral, você deve escolher uma opção para a cláusula SQL WHERE nesta ordem de preferência:
 - Key and timestamp , se o banco de dados remoto suportar campos com timestamp, que é a maneira mais rápida de verificar se um registro foi alterado.
- Key and modified fields , porque os campos que você atualiza no servidor quase sempre são um subconjunto do número total de campos que você poderia atualizar.
- Key and updatable fields .
- Key fields only . Usar essas configurações implica que o servidor remoto inserirá um registro totalmente novo usando a chave alterada e excluirá o registro antigo.

# Enviar instruções em lote

Alguns servidores (como o Microsoft SQL Server) permitem enviar um lote de instruções SQL em um único pacote. Isso melhora o desempenho porque você reduz o tráfego de rede e porque o servidor pode compilar várias instruções de uma só vez.

Por exemplo, se você especificar um tamanho de lote de quatro e depois atualizar 10 registros em um banco de dados, o Visual FoxPro envia quatro instruções como as seguintes ao banco de dados do servidor em um lote:

```foxpro
UPDATE customer SET contact = "John Jones" ;
   WHERE cust_id = 1;
UPDATE customer SET contact = "Sally Park" ;
   WHERE cust_id = 2;
UPDATE customer SET company = "John Jones" ;
   WHERE cust_id = 3;
UPDATE customer SET contact = "John Jones" ;
   WHERE cust_id = 4
```

### Para enviar instruções em lote
- Na caixa de diálogo Options, escolha a guia Remote Data e, em Records to batch update , especifique o número de registros a incluir em um lote. -ou-
- Chame as funções DBSETPROP( ) ou CURSORSETPROP( ) para definir estas propriedades: Defina Transaction como 2. Defina BatchUpdateCount como o número de instruções a enviar em um lote. -ou-
 - No View Designer , escolha Advanced Options no menu Query para exibir a caixa de diálogo Advanced Options.
- Na área Performance, ao lado de Number of records to batch update , especifique o número de instruções a enviar em um lote. Observação Você deve experimentar valores diferentes para esta propriedade e para a propriedade PacketSize para otimizar suas atualizações.

# Definir tamanho do pacote

Você pode otimizar o acesso a servidores remotos ajustando o tamanho do pacote de rede que é enviado e recuperado do banco de dados remoto. Por exemplo, se sua rede suportar pacotes grandes (maiores que 4.096 bytes), você pode aumentar o tamanho do pacote no Visual FoxPro para enviar mais dados cada vez que ler ou gravar na rede.

### Para definir o tamanho do pacote
- Chame as funções DBSETPROP( ) ou CURSORSETPROP( ) e defina a propriedade PacketSize como um valor inteiro positivo. O valor padrão é 4.096. Observação Diferentes provedores de rede tratarão esta propriedade de maneira diferente, portanto você deve consultar a documentação do seu serviço de rede. O Novell NetWare, por exemplo, tem um tamanho máximo de pacote de 512 bytes, portanto definir a propriedade PacketSize para um valor maior que isso não trará benefício adicional.

# Atrasar a recuperação de dados memo e binários

Se você estiver armazenando dados Memo ou binários em um servidor remoto, pode melhorar o desempenho atrasando o download desses dados até que seu aplicativo realmente precise deles.

### Para atrasar a recuperação de dados memo e binários
- Na caixa de diálogo Options, escolha a guia Remote Data e, em Remote view defaults , defina Fetch memo . -ou-
- Chame as funções DBSETPROP( ) ou CURSORSETPROP( ) para definir a propriedade FetchMemo.

# Armazenar dados de pesquisa localmente

Muitos aplicativos incluem dados de pesquisa estáticos, como abreviações de estados, códigos postais e cargos de funcionários. Se seu aplicativo contém esse tipo de dado e a tabela não é muito grande, você pode acelerar seu aplicativo mantendo cópias dessas informações no computador de cada usuário, porque pesquisas não geram tráfego de rede.

Esta técnica é principalmente útil para dados que nunca mudam ou mudam muito raramente. Se os dados mudarem ocasionalmente, você deve elaborar uma estratégia para baixar uma nova cópia da tabela de pesquisa para o computador de cada usuário.

# Criar regras locais

Você pode ganhar eficiência em seu aplicativo criando regras locais em nível de campo e de registro no Visual FoxPro, em vez de depender de regras definidas no servidor. Essas regras podem impedir que dados que não estão em conformidade com regras de dados ou de negócios entrem no banco de dados.

Ao definir regras no Visual FoxPro, você captura os dados inválidos antes que sejam enviados pela rede, o que é mais rápido e oferece melhor controle para tratar condições de erro. No entanto, usar regras locais também significa que você deve coordená-las com as regras no servidor remoto. Por exemplo, se houver alterações nas regras do servidor, você pode ter que alterar suas regras locais para corresponder.

Para obter mais informações, consulte Como: criar regras de validação para exibições.
