# Exibir amostra de informações do sistema

Arquivo: ...\Samples\Solution\OLE\Sysinfo.scx

Este exemplo ilustra o uso do SysInfoControl para exibir informações do sistema e notificar quando uma configuração do sistema é alterada.

A maior parte do código neste exemplo está no método CheckStatus. O código no método this verifica as configurações de várias propriedades SysInfoControl para ver suas configurações atuais e preenche um controle treeview com essas informações. Por exemplo, a seguinte seção de código verifica a configuração BatteryLifePercent:

```foxpro
IF ThisForm.SysInfo.BatteryLifePercent = 255
   * Add a node to display the information
ENDIF
```

Quando uma configuração do sistema é alterada, ocorre o evento an do SysInfoControl. O código associado a cada um desses eventos define a legenda de um rótulo e chama o método CheckStatus para atualizar o controle treeview. Por exemplo, o código a seguir está associado ao evento SysColorsChanged:

```foxpro
ThisForm.Status.Caption = SysColorsChanged_LOC
ThisForm.CheckStatus
```
