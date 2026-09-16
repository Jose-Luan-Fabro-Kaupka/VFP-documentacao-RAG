# Exemplo de reprodução de arquivo AVI em um controle ActiveX

Arquivo: ...\Samples\Solution\OLE\Mmsample.scx

Este exemplo mostra como usar o controle Multimedia para reproduzir um AVI em um controle que possui a propriedade hWnd.

O controle com hWnd é um controle ActiveX personalizado chamado hWin, criado com o OLE Control Wizard do Microsoft Visual C++ 4.0.

No Init do formulário, a linha a seguir direciona o controle Multimedia para reproduzir o AVI no formulário:

```foxpro
ThisForm.VCR.hWndDisplay = ThisForm.Test.hWnd
```
