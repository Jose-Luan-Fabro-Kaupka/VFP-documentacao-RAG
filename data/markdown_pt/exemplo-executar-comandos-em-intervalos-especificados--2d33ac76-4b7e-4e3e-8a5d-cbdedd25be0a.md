# Exemplo Executar comandos em intervalos especificados

Arquivo: ...\Samples\Solution\Controls\Timer\Timecomm.scx

Este formulário de exemplo contém uma caixa de texto e um spinner. O texto que você digita na caixa de texto é exibido em uma WAIT WINDOW. Você pode definir o spinner para o número de segundos que deseja que transcorram entre cada comando WAIT WINDOW.

No evento InteractiveChange do spinner, o intervalo do timer apropriado é definido. A propriedade Interval é 1/1000 de segundo, portanto o intervalo é definido como o valor do spinner * 1000.

```foxpro
THISFORM.Timer1.Interval = (THIS.Value * 1000)
```

No evento Timer, o comando `WAIT WINDOW` é emitido.

```foxpro
WAIT WINDOW ALLTRIM(THISFORM.Text1.Value) TIMEOUT 0.5
```

O código associado ao evento Timer pode incluir qualquer comando ou procedimento: código para atualizar dados, verificar e-mail, exibir recursos do sistema e assim por diante.
