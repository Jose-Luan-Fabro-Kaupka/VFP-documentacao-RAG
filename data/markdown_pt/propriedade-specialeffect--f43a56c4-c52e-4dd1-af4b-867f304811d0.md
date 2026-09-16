# Propriedade SpecialEffect

Especifica diferentes opções de formato para um controle. Disponível em tempo de design e em tempo de execução.

```foxpro
 [Form.]Control.SpecialEffect = nExpr
```

# Valor de retorno
 **nExpr**
Para um controle PageFrame, objeto Container ou objeto Control, as configurações da propriedade SpecialEffect são as seguintes: Configuração Descrição 0 Elevado. O controle parece estar elevado do formulário. 1 Rebaixado. O controle parece estar embutido no formulário. 2 Plano. Observação Para um controle PageFrame, SpecialEffect está disponível apenas se a propriedade Tabs estiver definida como false (.F.). Além disso, a propriedade BorderColor para um PageFrame se aplica apenas quando nExpr é definido como 2 (Plano). Para todos os outros controles, as configurações da propriedade SpecialEffect são as seguintes: Configuração Descrição 0 (Padrão para todos os controles e objetos, exceto o objeto Container.) 3D. A borda do controle é elevada para simular uma aparência tridimensional. 1 Simples. O controle aparece sem uma borda tridimensional. 2 Hot tracking. Fornece efeito de mouseover para controles específicos. Observação Se a propriedade Height for definida com um valor muito pequeno, a configuração 3D não tem efeito. Hot tracking é suportado nos seguintes controles: ListBox, ComboBox, Spinner, TextBox, EditBox, CommandButton, CheckBox, OptionButton. Hot tracking para controles CheckBox ou OptionButton é suportado apenas se Style = 2 (gráfico). Hot tracking é suportado para CommandButtons apenas quando Style <> 1 (invisível). A tabela a seguir descreve o suporte a hot tracking. Controle Padrão Efeito mouseover Listbox Simples 3D ComboBox Simples 3D Spinner Simples 3D TextBox Simples 3D EditBox Simples 3D CommandButton Simples na posição normal 3D CheckBox Simples Nenhum OptionButton Simples na posição normal 3D

# Observações

Aplica-se a: controle CheckBox | controle ComboBox | controle CommandButton | controle CommandGroup | objeto Container | objeto Control (Visual FoxPro) | controle EditBox | controle ListBox | controle OptionButton | controle OptionGroup | controle PageFrame | controle Shape | controle Spinner | controle TextBox (Visual FoxPro)
