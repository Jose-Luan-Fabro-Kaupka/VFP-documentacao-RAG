# Janelas do sistema do Visual FoxPro

As janelas do sistema fazem parte da interface do Visual FoxPro. A tabela a seguir fornece detalhes para acessá-las e controlá-las.

| Janela | Acesso por código | Estado padrão de encaixe |
| --- | --- | --- |
| Command | ACTIVATE WINDOW Command | Encaixável, desencaixada |
| Data Session | SET VIEW ON, ACTIVATE WINDOW VIEW | Encaixável, desencaixada |
| Document View | ACTIVATE WINDOW Document | Encaixável, desencaixada |
| Properties | ACTIVATE WINDOW Properties | Encaixável, desencaixada |
| Debugger | DEBUG ACTIVATE WINDOW Debug[ger] | Não encaixável |
| Call Stack | (consulte a observação) | no Debugger, encaixável |
| Debug Output | (consulte a observação) | no Debugger, encaixável |
| Locals | (consulte a observação) | no Debugger, encaixável |
| Trace | (consulte a observação) | no Debugger, encaixável |
| Watch | (consulte a observação) | no Debugger, encaixável |

> **Observação:** As janelas individuais do Debugger só podem ser encaixadas quando ele está habilitado no quadro do FoxPro. Para abrir uma subjanela isoladamente por código, primeiro configure o Debugger para usar o quadro do Visual FoxPro.
