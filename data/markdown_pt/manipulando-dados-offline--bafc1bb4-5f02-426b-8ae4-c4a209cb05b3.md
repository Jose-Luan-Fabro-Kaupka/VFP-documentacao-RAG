# Manipulando dados offline

Há ocasiões em que você pode querer exibir, coletar ou modificar dados independentemente do banco de dados host. Usando os recursos de view offline no Visual FoxPro, você pode usar views para conectar-se a um banco de dados host e criar um subconjunto de dados para uso offline. Em seguida, trabalhando offline, você pode usar a view diretamente ou por meio de uma aplicação que você criar. Quando terminar, pode enviar as alterações armazenadas na view de volta ao banco de dados host.

Alguns cenários em que views offline são úteis incluem:
 - Uma situação de data warehousing, em que grandes bancos de dados são mantidos centralmente em servidores MIS. Se você está interessado apenas em dados pertinentes a, por exemplo, o departamento de Marketing, pode construir uma view incluindo apenas os dados relevantes para você. Você pode então levar os dados offline, permitir que vários usuários no departamento de Marketing atualizem os dados e depois confirmar os dados alterados no banco de dados de origem.
- Uma localização geograficamente remota que exige que você leve um subconjunto de dados em um laptop, modifique os dados independentemente do banco de dados host e depois atualize o banco de dados host com os dados alterados posteriormente.
- Dados sensíveis ao tempo. Por exemplo, você pode querer atualizar dados refletindo aumentos salariais de funcionários antes que as novas taxas de pagamento entrem em vigor.
 Trabalhando com views offline

Usando a view offline, você pode exibir e atualizar dados muito como faz online com os mesmos formulários, relatórios ou aplicações.

Para criar e usar dados de view offline, você pode usar os seguintes recursos de linguagem:
 - A função CREATEOFFLINE( ).
- O comando USE SQLViewName com as cláusulas ADMIN e ONLINE. Por exemplo, o código a seguir abre a view Showproducts: USE Showproducts
- A função TABLEUPDATE.
- A função DROPOFFLINE( ).

Se você não está obtendo o subconjunto de dados esperado, verifique as configurações de otimização da view remota. Se você definiu a propriedade MaxRecords usando a função DBSETPROP( ), apenas esse número de registros aparece em suas views offline. No entanto, se você incluir um campo Memo na lista de campos de sua view, ele é automaticamente incluído no conjunto de resultados mesmo se FetchMemo estiver definido como false (.F.).

Se você planeja usar a view offline em uma máquina diferente daquela em que criou a view offline, deve preparar o destino offline criando uma cópia do arquivo de banco de dados host (.dbc); garantindo que a fonte de dados ODBC usada pela view exista na máquina de destino; e analisando seus requisitos de dados para determinar o conteúdo da view necessária.

> **Observação:** Use o programa ODBC Administrator para instalar fontes de dados em uma máquina. Você pode acessar o programa ODBC Administrator no grupo de programas do Visual FoxPro ou no Painel de Controle.

Depois de criar a view para seus dados offline, você pode usá-la como qualquer view em sua aplicação: pode adicionar, alterar e excluir registros. Vários usuários podem acessar a view offline simultaneamente usando o mesmo banco de dados em modo compartilhado. Se decidir que não deseja manter nenhuma das alterações, pode reverter as informações para refletir as informações originais.

# Administrando dados offline

Em alguns casos — especialmente em um ambiente de vários usuários onde muitas pessoas modificam dados — você pode querer examinar as alterações feitas na view offline antes de confirmar as alterações no banco de dados de origem. Com o comando USE e a cláusula ADMIN, você pode ver todas as alterações confirmadas em uma view desde que ela foi levada offline. Você pode então reverter seletivamente alterações feitas sem estar conectado à fonte de dados. Por exemplo, o código a seguir abre a view `Showproducts` em modo administrador:

```foxpro
USE Showproducts ADMIN
```
