# Exemplo Read and Write Visual FoxPro Registry Values

Arquivo: ...\Samples\Solution\WINAPI\Regfox.scx

Este exemplo mostra como acessar o Registro do Windows usando o comando DECLARE-DLL nativo do Visual FoxPro. A API do Windows fornece várias funções que você pode usar para acessar, ler e gravar no registro. A biblioteca de classes Registry.prg em ...\Samples\Classes contém uma definição de classe que expõe essas funções como métodos que você pode chamar em seus aplicativos.

O conteúdo da caixa de diálogo Options do Visual FoxPro, configurações de Field Mapping e definições de Label (para citar alguns) são armazenados no Registro. Como muitas dessas configurações não estão disponíveis usando funções SET, você pode usar funções de Registro para acessar esses valores. O código a seguir preenche uma matriz de todas as configurações na caixa de diálogo Options:

```foxpro
regfile = HOME(2)+"classes\registry.prg"
SET PROCEDURE TO (m.regfile) ADDITIVE
oReg = CreateObject("FoxReg")
DIMENSION aFoxOptions[1,2]
m.nErrNum = oReg.EnumFoxOptions(@aFoxOptions)
```

O código a seguir chama o método SetFoxOption da classe FoxReg (definida em Registry.prg) para definir TALK OFF no registro:

```foxpro
regfile = HOME(2)+"classes\registry.prg"
SET PROCEDURE TO (m.regfile) ADDITIVE
oReg = CreateObject("FoxReg")
m.nErrNum = oReg.SetFoxOption("TALK","OFF")
```
