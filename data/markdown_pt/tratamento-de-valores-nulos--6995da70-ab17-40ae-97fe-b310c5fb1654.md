# Tratamento de valores nulos

O Visual FoxPro fornece suporte para valores nulos. Esse suporte simplifica a tarefa de representar dados desconhecidos e facilita o trabalho com bancos de dados Microsoft Access ou SQL que podem conter valores nulos.

Valores nulos são:
 - Iguais à ausência de qualquer valor.
- Diferentes de zero, da cadeia de caracteres vazia ("") ou de espaço em branco.
- Ordenados antes de outros dados.
- Propagados em cálculos e na maioria das funções.

Valores nulos afetam o comportamento de comandos e funções, expressões lógicas e parâmetros.

O suporte do Visual FoxPro para valores nulos está em conformidade com os padrões ANSI e afeta qualquer área do produto onde valores e expressões são usados.

| Para usar valores nulos em | Consulte |
| --- | --- |
| Comandos e funções | Comportamento de valores nulos em comandos e funções |
| Expressões | Comportamento de valores nulos em expressões lógicas |
| Parâmetros | NULL como parâmetro |

# Usando NULL em valores e expressões

No Visual FoxPro, você atribui o valor nulo programaticamente com o token .NULL. ou interativamente com CTRL+0 em um campo. Observe que os pontos ao redor de .NULL. são opcionais. Para detectar se um campo ou variável contém um valor nulo, ou se uma expressão é avaliada como valor nulo, use ISNULL( ).
