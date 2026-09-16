# Propriedade EnableHyperlinks

Especifica se hiperlinks são exibidos e habilitados dentro de um controle EditBox ou TextBox. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Object.EnableHyperlinks [ = lExpr ]
```

#### Parâmetros
 **lExpr**
Tipo de dados lógico. A tabela a seguir lista os valores para lExpr . Configuração lExpr True (.T.) Habilita a exibição e ativação de hiperlinks de URL dentro do controle. False (.F.) Exibe suporte a hiperlinks dentro do controle. (Padrão)

# Observações

Aplica-se a: EditBox Control | TextBox Control (Visual FoxPro)

Definir a opção global Enable Hyperlinks na caixa de diálogo Options afeta EnableHyperlinks, que você pode definir em tempo de execução usando `_VFP.EditorOptions`. Se você desativar hiperlinks globalmente, o Visual FoxPro ignora EnableHyperlinks e não ativa hiperlinks.

Como no editor, a ativação de um hiperlink depende da configuração _VFP.EditorOptions (se clique ou CTRL+Click vai para o link).

Se a propriedade ShowTips de um formulário estiver definida como True (.T.), o Visual FoxPro exibe uma dica de valor como "CTRL+Click to follow link" quando você move o mouse sobre o hiperlink. Se um valor for especificado para a propriedade ToolTipText, o Visual FoxPro exibe o texto ToolTip quando o mouse se move sobre qualquer parte do controle que não seja hiperlink.
