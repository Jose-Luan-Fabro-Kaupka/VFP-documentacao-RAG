# Aceitar entrada numérica em um intervalo determinado

Embora você possa definir a propriedade InputMask e incluir código no evento Valid para garantir que os valores numéricos inseridos em caixas de texto estejam dentro de um intervalo determinado, a maneira mais fácil de verificar o intervalo de valores é usar um spinner.

# Usando spinners

Você pode usar spinners para permitir que os usuários façam escolhas "girando" pelos valores ou digitando os valores diretamente na caixa do spinner.

# Definir o intervalo de valores que os usuários podem escolher

Defina as propriedades KeyboardHighValue, KeyboardLowValue e SpinnerHighValue, SpinnerLowValue com o número mais alto que você deseja que os usuários possam inserir no spinner.

Defina as propriedades KeyboardHighValue, KeyboardLowValue e SpinnerHighValue, SpinnerLowValue com o número mais baixo que você deseja que os usuários possam inserir no spinner.

# Decrementar um spinner quando o usuário clica no botão Acima

Às vezes, se o spinner reflete um valor como "prioridade", você deseja que o usuário possa aumentar a prioridade de 2 para 1 clicando no botão Acima. Para fazer o número do spinner decrementar quando o usuário clica no botão Acima, defina a propriedade Increment como -1.

# Percorrer valores não numéricos

Embora o valor de um spinner seja numérico, você pode usar o controle Spinner e uma caixa de texto para permitir que os usuários percorram vários tipos de dados. Por exemplo, se você deseja que um usuário possa percorrer um intervalo de datas, você pode dimensionar o spinner para que apenas os botões sejam visíveis e posicionar uma caixa de texto ao lado dos botões do spinner. Defina a propriedade Value da caixa de texto para uma data e, nos eventos UpClick e DownClick do spinner, incremente ou decremente a data.

> **Dica:** Você pode usar a função da API do Windows GetSystemMetrics para definir a largura do spinner de modo que apenas os botões sejam visíveis e os botões tenham a melhor largura para exibir os bitmaps das setas para cima e para baixo.
 - Defina a propriedade BorderStyle do spinner como 0.
- Inclua o seguinte código no Init do spinner: DECLARE INTEGER GetSystemMetrics IN Win32api INTEGER THIS.Width = GetSystemMetrics(2) && SM_CXVSCROLL

# Propriedades comuns do spinner

As seguintes propriedades do spinner são comumente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| Increment | Quanto incrementar ou decrementar o valor cada vez que o usuário clica nos botões Acima ou Abaixo. |
| KeyboardHighValue | O valor mais alto que pode ser inserido na caixa de texto do spinner. |
| KeyboardLowValue | O valor mais baixo que pode ser inserido na caixa de texto do spinner. |
| SpinnerHighValue | O valor mais alto que o spinner exibirá quando o usuário clica no botão Acima. |
| SpinnerLowValue | O valor mais baixo que o spinner exibirá quando o usuário clica no botão Abaixo. |
