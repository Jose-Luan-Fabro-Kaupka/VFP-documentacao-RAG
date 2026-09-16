# Propriedade HighlightStyle

Especifica se a linha selecionada em um Grid permanece destacada ao alterar o foco para outro controle no formulário. Leitura/gravação em tempo de design e em tempo de execução.

HighlightStyle funciona com as propriedades HighlightForeColor e HighlightBackColor para determinar se a linha selecionada é destacada e se permanece destacada quando você pressiona a tecla TAB para navegar na grade ou quando clica fora da grade para mover o foco para outro controle.

```foxpro
Grid.HighlightStyle [ = nValue ]
```

#### Parâmetros
 **nValue**
Tipo de dados numérico. A tabela a seguir descreve as configurações para nValue . nValue 0 Sem destaque de cor para a linha da grade (Padrão) 1 Habilita o destaque para a linha atual. 2 Habilita o destaque para a linha atual e persiste quando a grade não é o controle ativo atual.

# Observações

Aplica-se a: Grid Control

Se HighlightStyle contém um valor maior que 0, a cor padrão de HighlightBackColor aparece como um preenchimento gradiente 50% mais claro.

Se HighlightStyle é definido com o valor 2, apenas as cores de destaque persistem. Os itens selecionados são exibidos somente quando uma grade tem foco.

Quando a propriedade AllowCellSelection é definida como False (.F.), a linha atual é sempre destacada quando HighlightStyle é definido com o valor 0.

Se a propriedade Sparse de uma coluna é definida como False (.F.), a coluna não será destacada quando a propriedade HighlightStyle da grade é definida como 1 ou 2.
