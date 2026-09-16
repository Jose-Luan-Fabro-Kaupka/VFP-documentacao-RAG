# Visão geral dos controles ActiveX

Controles ActiveX (arquivos .ocx) são instalados por padrão quando você instala o Visual FoxPro. Você pode distribuir controles ActiveX com seus aplicativos. Controles ActiveX são adicionados a um formulário em um aplicativo usando o controle de contêiner OLE do Visual FoxPro.

A tabela a seguir lista os arquivos .ocx que são instalados com o Visual FoxPro e os controles ActiveX contidos em cada arquivo.

> **Observação:** Arquivos de ajuda para esses controles ActiveX estão disponíveis quando o MSDN está instalado.

| Arquivo | Controles |
| --- | --- |
| MSCOMCt2.ocx | Animation control DateTimePicker control FlatScrollBar control MonthView control UpDown control |
| MCI32.ocx | Multimedia MCI control |
| MSChrt20.ocx | MsChart control |
| MSCOMCtl.ocx | ImageCombo control ImageList control ListView control ProgressBar control Slider control StatusBar control TabStrip control Toolbar control TreeView control |
| MSCOMM32.ocx | MSComm control |
| MSInet.ocx | Microsoft Internet Transfer control |
| MSMapi32.ocx | MAPIMessages control MAPISession control |
| MSMask32.ocx | Masked Edit control |
| MSWinsck.ocx | Winsock control |
| Picclp32.ocx | PictureClip control |
| Richtx32.ocx | RichTextBox control |
| Sysinfo.ocx | SysInfo control |

> **Observação:** Em versões anteriores do Visual FoxPro, o arquivo contendo os controles ActiveX foi renomeado de Comctl32.ocx para MSCOMCtl.ocx. Mesmo que o Visual FoxPro tenha sido atualizado para o arquivo MSCOMCtl.ocx, formulários mais antigos com esses controles ainda referenciam o arquivo mais antigo porque o controle ActiveX é vinculado pela sua propriedade OleClass. Controles ActiveX do arquivo COMCtl32.ocx mais antigo têm versão 1. Por exemplo, a propriedade OleClass para um controle ListView em um formulário anterior diria:

```foxpro
COMCTL.ListViewCtrl.1
```

Controles ActiveX mais recentes no arquivo Mscomctl.ocx têm versão 2 (ou superior). Por exemplo:

```foxpro
COMCTL.TreeViewCtrl.2
```

O Visual FoxPro não atualiza automaticamente seu controle, portanto é importante saber qual versão de um controle ActiveX um formulário usa ao distribuir seus aplicativos.
