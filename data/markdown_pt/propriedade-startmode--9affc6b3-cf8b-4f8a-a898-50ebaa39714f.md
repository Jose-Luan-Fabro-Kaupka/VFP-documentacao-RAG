# Propriedade StartMode

Contém um valor numérico que indica como uma instância do Visual FoxPro foi iniciada. Somente leitura em tempo de execução.

```foxpro
ApplicationObject.StartMode
```

# Observações

Aplica-se a: Application Object | _VFP System Variable

A tabela a seguir lista os valores numéricos que a propriedade StartMode pode conter e como a instância do Visual FoxPro foi iniciada.

| Valor | Descrição |
| --- | --- |
| 0 | Uma versão de desenvolvimento do Visual FoxPro foi iniciada em uma sessão interativa. |
| 1 | O Visual FoxPro foi iniciado como um objeto de aplicativo. Por exemplo, o seguinte comando cria uma instância do Visual FoxPro como um objeto de aplicativo: oMyObject = CREATEOBJECT('VisualFoxPro.Application') |
| 2 | O Visual FoxPro foi iniciado como um servidor de automação .exe fora de processo. |
| 3 | O Visual FoxPro foi iniciado como um servidor de automação .dll em processo. |
| 4 | O Visual FoxPro foi iniciado como um arquivo .app ou .exe distribuível. |
| 5 | O Visual FoxPro foi iniciado como um servidor de automação .dll em processo para uso multithread. |

Para informações adicionais sobre usar o Visual FoxPro para criar servidores de automação personalizados, consulte Compartilhando informações e adicionando OLE.
