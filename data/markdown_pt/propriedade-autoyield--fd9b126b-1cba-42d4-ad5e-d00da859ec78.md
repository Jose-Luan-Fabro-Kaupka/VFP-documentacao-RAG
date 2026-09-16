# Propriedade AutoYield

Especifica se uma instância do Visual FoxPro processa eventos pendentes do Windows entre a execução de cada linha de código de programa do usuário.

```foxpro
ApplicationObject.AutoYield[ = lExpr]
```

# Valor de retorno
 **lExpr**
Especifica se uma instância do Visual FoxPro processa eventos do Windows entre cada linha de código de programa do usuário. lExpr pode ser um dos seguintes valores lógicos: lExpr Descrição True (.T.) (Padrão) A instância do Visual FoxPro processa eventos pendentes do Windows entre a execução de cada linha de código de programa do usuário. Se lExpr estiver definido como true (.T.), a instância do Visual FoxPro processa eventos pendentes do Windows da mesma forma que versões anteriores do Visual FoxPro. False (.F.) A instância do Visual FoxPro não processa eventos pendentes do Windows entre cada linha de código de programa do usuário. Todos os eventos pendentes do Windows são colocados em uma fila, e os eventos na fila são processados quando DOEVENTS é emitido ou ocorre um estado de espera. Um estado de espera ocorre quando o Visual FoxPro está aguardando entrada do usuário. O comando WAIT não cria um estado de espera.

# Observações

Aplica-se a: Objeto Application | Variável de sistema _VFP

A propriedade AutoYield deve ser definida como false (.F.) quando um formulário contém um controle ActiveX. Definir AutoYield como false (.F.) impede que eventos de um controle ActiveX sejam executados entre linhas de código de programa do usuário. Por exemplo, se AutoYield estiver definido como true (.T.), clicar em um controle ActiveX enquanto o código de programa do usuário está sendo executado pode causar a execução de um evento do controle ActiveX, ignorando o código de programa do usuário para o evento, produzindo resultados indesejáveis ou imprevisíveis.

O seguinte ocorre quando a propriedade AutoYield está definida como false (.F.):
 - Controles ActiveX não podem processar eventos até que ocorra um estado de espera, então clicar em um controle ActiveX não tem efeito enquanto o código de programa do usuário está sendo executado. Este é o mesmo comportamento para controles do Visual FoxPro como o Grid.
- Comandos ON KEY LABEL e eventos de mouse são ignorados enquanto o código de programa do usuário está sendo executado. Os comandos ON KEY LABEL e eventos de mouse são colocados em uma fila e processados no próximo estado de espera.
- Pressionar Esc não interrompe a execução do programa. Isso é idêntico a definir ESCAPE como OFF. Neste caso, você não pode sair de loops infinitos sem encerrar a instância do Visual FoxPro.
- Consultas não podem ser interrompidas.
- Alternar para outras aplicações é suportado, mas você não pode alternar de volta para o Visual FoxPro enquanto o código de programa do usuário do Visual FoxPro está sendo executado.
