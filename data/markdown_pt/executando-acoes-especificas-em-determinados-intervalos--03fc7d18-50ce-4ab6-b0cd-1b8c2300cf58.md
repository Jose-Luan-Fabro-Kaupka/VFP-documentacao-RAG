# Executando ações específicas em determinados intervalos

O controle Timer permite executar ações ou verificar valores em intervalos específicos.

# Usando o controle Timer

Os controles Timer respondem à passagem do tempo independentemente da interação do usuário, portanto podem ser programados para agir em intervalos regulares. Um uso típico é verificar o relógio do sistema para saber se chegou o momento de executar uma tarefa. Timers também são úteis para outros tipos de processamento em segundo plano.

Para ver exemplos, execute Solution.app no diretório ...\Samples\Solution do Visual FoxPro. Na árvore, clique em Controls e depois em Timer.

Cada timer tem uma propriedade Interval, que especifica o número de milissegundos entre um evento Timer e o seguinte. A menos que seja desabilitado, ele continua recebendo eventos em intervalos aproximadamente iguais. A propriedade Interval tem algumas limitações:
 - O intervalo pode estar entre 0 e 2.147.483.647, inclusive; o mais longo é de cerca de 596,5 horas (mais de 24 dias).
- Não há garantia de que o intervalo transcorrerá no tempo exato. Para garantir precisão, o timer deve consultar o relógio do sistema quando necessário, em vez de controlar internamente o tempo acumulado.
- Embora Interval seja medida em milissegundos, o intervalo real depende do timer do sistema. No Windows XP ou posterior, um intervalo de um milissegundo pode disparar 1.000 eventos por segundo. Em sistemas anteriores, há 18 pulsos de relógio por segundo, e a precisão real não passa de um décimo oitavo de segundo. Para obter mais informações, consulte a referência online do MSDN.
- Se o aplicativo ou outro aplicativo estiver exigindo muito do sistema — com loops longos, cálculos intensivos ou acesso a disco, rede ou porta —, os eventos poderão ocorrer com frequência menor que a especificada.

# Colocando um controle Timer em um formulário

Colocar um controle Timer em um formulário é como desenhar qualquer outro controle: escolha Timer na barra de ferramentas Form Controls e clique e arraste no formulário.

O timer aparece no formulário em tempo de design para que você possa selecioná-lo, exibir suas propriedades e escrever um procedimento de evento. Em tempo de execução, ele é invisível, e sua posição e tamanho são irrelevantes.

# Inicializando um controle Timer

Um controle Timer tem duas propriedades principais.

| Propriedade | Configuração |
| --- | --- |
| Enabled | Se quiser que o timer comece a funcionar assim que o formulário for carregado, defina como verdadeiro (.T.). Caso contrário, mantenha a propriedade como falso (.F.). Um evento externo, como o clique em um botão de comando, pode iniciar o timer. |
| Interval | Número de milissegundos entre eventos Timer. |

A propriedade Enabled do timer é diferente da de outros objetos. Na maioria dos objetos, Enabled determina se o objeto pode responder a um evento causado pelo usuário. No controle Timer, definir Enabled como falso (.F.) suspende sua operação.

Lembre-se de que o evento Timer é periódico. Interval determina mais "com que frequência" do que "por quanto tempo". O intervalo deve depender da precisão desejada. Como há um potencial de erro incorporado, defina-o como metade da precisão desejada.

> **Observação:** Quanto mais frequente for a geração de eventos Timer, mais tempo de processador será consumido para respondê-los. Isso pode reduzir o desempenho geral. Não defina um intervalo especialmente pequeno, a menos que seja necessário.

# Respondendo ao evento Timer

Quando o intervalo de um controle Timer termina, o Visual FoxPro gera o evento Timer. Normalmente, você responde verificando uma condição geral, como o relógio do sistema.

Um relógio digital é um aplicativo simples, mas muito útil, que envolve um controle Timer. Depois de entender seu funcionamento, você pode aprimorá-lo como despertador, cronômetro ou outro dispositivo de temporização.

O aplicativo de relógio digital inclui um timer e um rótulo com borda. Em tempo de design, o aplicativo tem esta aparência:
 O aplicativo de relógio digital

Em tempo de execução, o timer é invisível.

| Controle | Propriedade | Configuração |
| --- | --- | --- |
| lblTime | Caption | |
| Timer1 | Interval | 500 (meio segundo) |
| Timer1 | Enabled | True |

O único procedimento do aplicativo é o procedimento do evento Timer:

```foxpro
IF THISFORM.lblTime.Caption != Time()
   THISFORM.lblTime.Caption = Time()
ENDIF
```

A propriedade Interval do timer é definida como 500, seguindo a regra de usar metade do menor período que se deseja distinguir (um segundo neste caso). Isso pode fazer o código atualizar o rótulo duas vezes no mesmo segundo, causando alguma oscilação visível. Por isso, o código verifica se a hora difere da exibida antes de alterar Caption.
