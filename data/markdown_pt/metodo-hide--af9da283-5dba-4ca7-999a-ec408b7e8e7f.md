# Método Hide

Oculta um formulário, conjunto de formulários ou barra de ferramentas definindo a propriedade Visible como false (.F.).

```foxpro
Object.Hide
```

# Observações

Aplica-se a: Form Object | FormSet Object | _SCREEN System Variable | ToolBar Object

Os controles em um formulário oculto não estão acessíveis ao usuário, mas ainda estão disponíveis e podem ser acessados no código. Embora não sejam visíveis, os controles contidos em um formulário invisível mantêm sua própria configuração da propriedade Visible.

Quando a propriedade Visible do conjunto de formulários é definida como false (.F.), o usuário não pode ver os Forms que ele contém. Os Forms em um conjunto de formulários oculto não estão acessíveis ao usuário, mas ainda estão disponíveis e podem ser acessados no código. O método Hide para um conjunto de formulários não define a propriedade Visible de seus Forms filhos, portanto, quando um formulário está contido em um conjunto de formulários, você deve verificar as configurações da propriedade Visible tanto do formulário quanto do conjunto de formulários para determinar se o formulário está visível.

Depois que um conjunto de formulários é ocultado, o Visual FoxPro ativa o último objeto ativo. Se nenhum objeto estava ativo antes do conjunto de formulários, a janela principal do Visual FoxPro se torna ativa.

Chamar o método Hide para a variável de sistema _SCREEN não tem efeito.
