# Propriedade ReadOnly

Especifica se o usuário pode editar um controle, se uma tabela ou exibição associada a um objeto Cursor permite atualizações, ou contém um valor que indica se um arquivo em um projeto pode ser editado. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
 [Form.]Control.ReadOnly[ = lExpr]
DataEnvironment.Cursor.ReadOnly[ = lExpr]
Project.Files.Item(nItem).ReadOnly
```

# Valor de retorno
 **lExpr**
As configurações da propriedade ReadOnly são: Configuração Descrição True (.T.) O usuário não pode editar o controle. A tabela ou exibição associada ao objeto Cursor não pode ser modificada. False (.F.) (Padrão) O usuário pode editar o controle. A tabela ou exibição associada ao objeto Cursor pode ser modificada.

# Observações

Aplica-se a: Controle CheckBox | Objeto Column | Controle ComboBox | Objeto Cursor | Controle EditBox | Objeto File (Visual FoxPro) | Controle Grid | Controle Spinner | Controle TextBox (Visual FoxPro)

> **Observação:** Quando o Cursor é acessado usando CURSORSETPROP(), a propriedade ReadOnly é somente leitura em tempo de execução.

A propriedade ReadOnly difere da propriedade Enabled porque, quando ReadOnly está definida como verdadeiro (.T.), o usuário ainda pode mover o foco para o controle.

Para Cursors, ReadOnly imita a cláusula NOUPDATE de USE.

Para controles de caixa de combinação, a propriedade ReadOnly não pode ser definida como verdadeiro (.T.) quando a propriedade Style está definida como 2 – Drop-down List.

Para um arquivo em um projeto, a propriedade ReadOnly contém um valor lógico que indica se o arquivo pode ser editado. Se ReadOnly for verdadeiro (.T.), o arquivo pode ser editado; caso contrário, o arquivo não pode ser editado. Somente leitura em tempo de design e em tempo de execução.
