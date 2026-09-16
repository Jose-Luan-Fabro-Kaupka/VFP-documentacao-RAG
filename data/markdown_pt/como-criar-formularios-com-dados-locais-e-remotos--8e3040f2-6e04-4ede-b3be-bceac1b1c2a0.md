# Como: criar formulários com dados locais e remotos

Você pode criar formulários que podem ser facilmente alternados entre o uso de dados locais e dados armazenados remotamente (por exemplo, em um servidor de banco de dados). Isso permite criar um protótipo de aplicação usando dados locais ou de teste e depois alternar para dados remotos ou em produção sem alterações substanciais nos formulários.

Por exemplo, se sua aplicação Visual FoxPro é um front-end para uma grande tabela de clientes armazenada em um servidor de banco de dados, você pode criar um arquivo .dbf local que contém uma amostra pequena, mas representativa, dos dados. Você pode então criar, testar e depurar seus formulários com base nesse conjunto pequeno de dados. Quando estiver pronto para distribuir sua aplicação, você pode vincular seu formulário ao grande conjunto de dados.

A chave para poder alternar entre dados locais e remotos é garantir que você use views em vez de vincular diretamente seu formulário (e seus controles) a uma tabela. Para acessar dados remotos, você deve usar uma view de qualquer forma. Portanto, para facilitar a alternância entre dados locais e remotos, crie uma view para os dados locais também. Ao criar o formulário, você pode adicionar ambas as views ao seu ambiente de dados e alternar entre elas conforme necessário.

### Para criar um formulário que pode alternar entre dados locais e remotos
- Crie duas views dos dados, uma que aponte para os dados remotos e outra que aponte para os dados locais.
- Crie um novo formulário.
- Abra o Data Environment Designer para o formulário e adicione ambas as views.
- Clique com o botão direito no Data Environment Designer e escolha Properties.
- Na Properties Window (Visual FoxPro), defina a propriedade Alias Property para ambos os cursors com o mesmo nome.
- Defina a propriedade OpenViews Property do ambiente de dados como 1 — Local Only ou 2 — Remote Only, dependendo de qual view você deseja usar ao executar o formulário. Observação Como você está usando o mesmo alias para ambas as views, não escolha 0 — Local and Remote (o padrão).
- No formulário, adicione os controles necessários e defina suas propriedades ControlSource para os campos apropriados na view. Como ambas as views têm o mesmo alias, os controles responderão automaticamente a qualquer view estiver ativa quando o formulário for executado.

Depois que o formulário é criado, você pode alternar o alias das views alterando a propriedade OpenViews do ambiente de dados. Você pode fazer isso no Data Environment enquanto usa o Form Designer. Alternativamente, você pode escrever código e anexá-lo a um evento, o que é útil se desejar alternar views em tempo de execução. Por exemplo, você pode colocar este código no evento Activate Event (Visual FoxPro) do formulário:

```foxpro
THISFORM.DataEnvironment.OpenViews = 2 && Use remote view
```

Se você criar um formulário que pode ser alternado entre dados locais e remotos, também deve projetar seu código de navegação para acomodar ambas as views, especialmente se estiver projetando formulários com relações um-para-muitos. Por exemplo, se seu formulário acessa apenas uma tabela ou view local, você pode usar código como o seguinte em um botão de comando Next para mover para o próximo registro em um cursor:

```foxpro
SKIP 1
THISFORM.Refresh()
```

No entanto, este código é ineficiente ao navegar em uma view remota, pois assume que o cursor contém todos os dados necessários para o formulário. Como regra, você deseja minimizar a quantidade de dados baixados da fonte de dados remota.

A solução é usar uma view parametrizada. Por exemplo, a definição de uma view usada para editar informações de clientes pode ser:

```foxpro
SELECT * FROM CUSTOMERS WHERE ;
 CUSTOMERS.COMPANY_NAME = ?pCompanyName
```

Quando o formulário é executado, ele pode solicitar ao usuário um nome de cliente usando uma caixa de diálogo ou permitindo que o usuário digite um nome em uma caixa de texto. O código de um botão Display seria então semelhante ao seguinte:

```foxpro
pCompanyName = THISFORM.txtCompanyName.Value
REQUERY("customer")
THISFORM.Refresh()
```

Para obter mais informações, consulte How to: Create Parameterized Views.
