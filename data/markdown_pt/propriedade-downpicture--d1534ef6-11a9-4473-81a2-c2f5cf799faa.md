# Propriedade DownPicture

Especifica o gráfico exibido quando o controle é selecionado. Disponível em tempo de design e em tempo de execução.

```foxpro
Control.DownPicture[ = cPicture]
```

# Valor de retorno
 **cPicture**
Especifica um caminho completo e nome de arquivo de um bitmap.

# Observações

Aplica-se a: CheckBox Control | CommandButton Control | OptionButton Control

Se você definir a propriedade DownPicture em tempo de design e o arquivo que especificar não existir, o Microsoft Visual FoxPro exibe uma mensagem de erro, mas a propriedade permanece definida para o arquivo que você especificou. O Visual FoxPro ignora a propriedade DownPicture em tempo de execução se ela estiver definida para um arquivo que não existe.

Se você não especificar uma configuração para a propriedade DownPicture, o Visual FoxPro usa o gráfico especificado pela propriedade Picture quando o controle é selecionado.

Para controles CommandButton, a propriedade Style deve ser definida como 0 (Standard) para que o bitmap seja exibido no controle; Para controles CheckBox e OptionButton, a propriedade Style deve ser definida como 1 (Graphical).
