# Propriedade SelStart

Retorna o ponto inicial de uma seleção de texto feita pelo usuário na área de entrada de um controle ou indica a posição do ponto de inserção quando não há texto selecionado. Também especifica o ponto inicial de uma seleção. Não disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
 [Form.]Control.SelStart[= nStart]
```

# Valor de retorno
 **nStart**
Especifica o ponto inicial do texto selecionado ou indica a posição do ponto de inserção quando não há seleção. O texto selecionado aparece sombreado. O intervalo válido vai de 0 ao número total de caracteres na área de edição do controle.

# Observações

Aplica-se a: controle ComboBox | controle EditBox | controle Spinner | controle TextBox (Visual FoxPro)

Use esta propriedade com SelLength e SelText para tarefas como:
 - Definir o ponto de inserção em uma cadeia de caracteres.
- Estabelecer um intervalo que limite onde o ponto de inserção pode ir.
- Selecionar um grupo específico de caracteres (subcadeias) em um controle.
- Limpar texto.

Ao trabalhar com essas propriedades, observe:
 - Definir SelLength como menor que 0 causa erro em tempo de execução.
- Definir SelStart acima do comprimento do texto ajusta a propriedade ao comprimento existente. Alterar SelStart transforma a seleção em um ponto de inserção e define SelLength como 0.
- Definir SelText com um novo valor define SelLength como 0 e substitui o texto selecionado pela nova cadeia.
