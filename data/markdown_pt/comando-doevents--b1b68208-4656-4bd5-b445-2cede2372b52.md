# Comando DOEVENTS

Executa todos os eventos pendentes do Windows.

> **Observação:** Você não pode chamar DOEVENTS usando parênteses (()), por exemplo, "DOEVENTS( )".

Você pode usar DOEVENTS para tarefas simples, como permitir que o usuário cancele um processo depois que ele começa, por exemplo, ao pesquisar um arquivo. Processos de longa duração que cedem o controle do processador são melhor executados usando um controle Timer ou delegando a tarefa a um executável de servidor COM (.exe). Nessa situação, a tarefa pode continuar independentemente do seu aplicativo, e o sistema operacional cuida do multitarefa e da alocação de tempo.

> **Cuidado:** Sempre que você ceder temporariamente o controle do processador em um procedimento de evento, certifique-se de que o procedimento não seja executado novamente a partir de outra parte do código antes que a primeira chamada termine. Fazer isso pode causar resultados imprevisíveis. Além disso, não use DOEVENTS se outros aplicativos puderem interagir com seu procedimento de maneiras imprevistas durante o tempo em que você cedeu o controle do processador.

```foxpro
DOEVENTS [FORCE]
```

#### Parâmetros
 **FORCE**
Pausa a execução de código do Visual FoxPro até que ocorra um evento do Windows, como mover o mouse. Observação O uso da palavra-chave FORCE pode afetar o desempenho. Portanto, use cautela ao chamar DOEVENTS FORCE em um loop de código apertado, como um loop DO WHILE.

# Observações

Quando a propriedade AutoYield está definida como False (.F.) e o código do programa está em execução, os eventos de janela são colocados em uma fila. DOEVENTS executa todos os eventos pendentes do Windows e processa qualquer código do usuário associado aos eventos do Windows. Se não houver eventos na fila, o Visual FoxPro ignora DOEVENTS e continua a execução do programa.
