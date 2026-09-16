# Propriedade Bound

Determina se um controle em um objeto Column está vinculado à fonte de controle do Column. Disponível em tempo de design e em tempo de execução.

```foxpro
Column.Bound[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações para a propriedade Bound são: Configuração Descrição True (.T.) (Padrão) O controle está vinculado à fonte de controle da coluna. False (.F.) O controle não está vinculado à fonte de controle da coluna.

# Observações

Aplica-se a: Objeto Column

Se a propriedade Bound de uma coluna estiver definida como true (.T.), a configuração da propriedade ControlSource da coluna se aplica à coluna e a quaisquer controles contidos nela. Se você tentar definir a propriedade ControlSource do controle contido, ocorre um erro. Se a propriedade Bound de uma coluna estiver definida como false (.F.), você pode definir a propriedade ControlSource de um controle contido diretamente. Se você posteriormente definir a configuração ControlSource da coluna, ela substitui a configuração ControlSource do controle contido.

Normalmente, os seguintes controles são vinculados aos tipos de dados correspondentes:

| Classe base do controle da coluna | Tipos de dados típicos da coluna |
| --- | --- |
| CheckBox | Lógico, Numérico |
| ComboBox | Caractere, Numérico |
| CommandButton | Caractere, Numérico |
| EditBox | Caractere |
| ListBox | Caractere, Numérico |
| OptionButton | Caractere, Numérico |
| Spinner | Moeda, Numérico |
| TextBox | Qualquer tipo de dados, exceto General ou Memo |

> **Observação:** Você não pode vincular um controle a uma coluna cujo tipo de dados é General ou Memo.
