# Propriedade RightToLeft

Especifica a ordem de leitura do texto em controles e a exibição de saída em fluxo em formulários. RightToLeft é ignorado a menos que você esteja executando uma versão do Microsoft Windows para o Oriente Médio. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Object.RightToLeft[ = lExpression]
```

# Valor de retorno
 **lExpression**
As configurações da propriedade RightToLeft são: Configuração Descrição True (.T.) (Padrão) O texto é inserido e exibido em controles em ordem de leitura da direita para a esquerda. A saída em fluxo (por exemplo, texto exibido com ? ou ??) é exibida em formulários em ordem de leitura da direita para a esquerda. False (.F.) O texto é inserido e exibido em controles em ordem de leitura da esquerda para a direita. A saída em fluxo é exibida em formulários em ordem de leitura da esquerda para a direita.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | EditBox Control | Form Object | Grid Control | Label Control (Visual FoxPro) | ListBox Control | OptionButton Control | PageFrame Control | _SCREEN System Variable | Spinner Control | TextBox Control (Visual FoxPro)

Use a propriedade Alignment para especificar a orientação do texto em caixas de seleção e botões de opção.
