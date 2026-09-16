# Propriedade DisabledPicture

Especifica o gráfico a ser exibido quando o controle está desabilitado. Disponível em tempo de design e em tempo de execução.

```foxpro
Control.DisabledPicture[ = cPicture]
```

# Valor de retorno
 **cPicture**
Especifica o caminho completo e o nome de arquivo de um bitmap ou o nome de um campo general em uma tabela de banco de dados.

# Observações

Aplica-se a: CheckBox Control | CommandButton Control | OptionButton Control

Se você definir a propriedade DisabledPicture em tempo de design e o arquivo especificado não existir, o Visual FoxPro exibe uma mensagem de erro, mas a propriedade permanece definida para o arquivo especificado. O Visual FoxPro ignora a propriedade DisabledPicture em tempo de execução se ela estiver definida para um arquivo que não existe.

Se você não definir a propriedade DisabledPicture, o Visual FoxPro usa a configuração da propriedade Picture para determinar o gráfico exibido quando o controle está desabilitado.

Para controles CommandButton, a propriedade Style deve ser definida como 0 (Standard) para o bitmap ser exibido no controle; para controles CheckBox e OptionButton, a propriedade Style deve ser definida como 1 (Graphical).
