# SYS(2335) - Modo de servidor sem intervenção

Habilita ou desabilita estados modais para servidores de automação Visual FoxPro .exe distribuíveis.

```foxpro
SYS(2335 [, 0 | 1])
```

#### Parâmetros
 **0**
Habilita o modo sem intervenção. Quando o modo sem intervenção está habilitado, um erro do Visual FoxPro é gerado sempre que ocorre um estado modal. Seu servidor de automação .exe pode capturar esses erros com uma rotina ON ERROR.
**1**
(Padrão) Desabilita o modo sem intervenção. Estados modais, que exigem intervenção do usuário, podem ocorrer. O modo sem intervenção é desabilitado na inicialização.

# Valor de retorno

Character

# Observações

Use SYS(2335) para habilitar ou desabilitar estados modais em servidores de automação Visual FoxPro .exe. Servidores de automação são criados com o Project Manager. Para informações adicionais sobre o uso do Visual FoxPro para criar servidores de automação .exe, consulte Sharing Information and Adding OLE.

Estados modais ocorrem quando caixas de diálogo ou mensagens de erro são exibidas, exigindo entrada do usuário para sair da caixa de diálogo ou mensagem de erro e continuar a execução do programa. Estados modais podem ser indesejáveis em servidores .exe implantados remotamente, possivelmente sem intervenção de um usuário. A execução do programa é interrompida e requer intervenção para continuar.

A tabela a seguir lista alguns exemplos típicos de estados modais que podem ocorrer em um servidor .exe.

| Estado modal | Exemplos |
| --- | --- |
| Comando WAIT ou função MESSAGEBOX( ) | Pode ocorrer no código do programa. |
| Erros do Visual FoxPro como "File access is denied" ou "Allowed DO nesting level exceeded" | Pode ocorrer no código do programa. |
| Caixas de diálogo Abrir | Pode ocorrer quando arquivos incluídos em uma instrução SQL não podem ser localizados. |
| Caixa de diálogo SQL Connection Login | Pode ocorrer após uma conexão não poder ser estabelecida. |

SYS(2335 ,0) deve ser executado o mais cedo possível no código do programa de um servidor de automação .exe sem intervenção, pois um estado modal pode ocorrer a qualquer momento após o início da execução do programa.

Observe que SYS(2335) se aplica apenas a servidores de automação .exe para os quais a propriedade StartMode é igual a 2 ou 4. O modo sem intervenção está sempre habilitado para servidores de automação .dll in-process (para os quais a propriedade StartMode é igual a 3).

Emitir SYS(2335) sem um argumento em um aplicativo em tempo de execução retorna sua configuração atual.

# Exemplo

O exemplo a seguir permite executar vários casos de teste para mostrar os resultados das configurações de SYS(2335) em um aplicativo que invoca elementos modais da interface do usuário.

```foxpro
CLEAR
SET SAFETY OFF
DIMENSION aTestCase[3]
aTestCase[1]="TestMessageBox"
aTestCase[2]="LocateFileDialog"
aTestCase[3]="SafetyDialog"
TEXT TO cstr  TEXTMERGE
PROCEDURE Temp(UIMode as string,cTestCase as string)
* command line parms are strings
  SYS(2335,VAL(UIMode))   && allow or disallow UI
  SET SAFETY OFF
  TRY
    _screen.Caption="UIMode = "+UIMode+" "+cTestCase+" Startmode="+TRANSFORM(_vfp.StartMode)
    DO CASE
      CASE cTestCase="<<aTestCase[1]>>"
        MESSAGEBOX("UI is allowed. UIMode = "+UIMode,0, cTestCase)
      CASE cTestCase="<<aTestCase[2]>>"
        *Try this scenario which will bring up a dialog
         SELECT * FROM NonExistFile
      CASE cTestCase="<<aTestCase[3]>>"
        *Cause "Overwrite existing file dialog to appear"
        SET SAFETY ON
        CREATE TABLE temp (name c(10),data m)
        CREATE TABLE temp (name c(10),data m) && Create table again to cause Overwrite dialog?
      OTHERWISE
        MESSAGEBOX("Unknown test case. UIMode = "+UIMode+" "+cTestCase)
    ENDCASE
  CATCH TO oEx
    SYS(2335,1) && Allow UI
    MESSAGEBOX("Err caught UIMode = "+UIMode+":"+oEx.Message + " " +oEx.details,48,"Exception "+cTestCase)
  ENDTRY
ENDTEXT
STRTOFILE(cstr,"temp.prg")
BUILD PROJECT temp FROM temp
BUILD EXE temp FROM temp
FOR nTestCase=1 TO ALEN(aTestCase)
  FOR uiMode=1 TO 0 STEP -1
   ?"UIMode=",uiMode,aTestCase[nTestCase]
   cCmd="temp "+TRANSFORM(uiMode)+" "+aTestCase[nTestCase]
   ! &cCmd
  ENDFOR
  EXIT && comment this to run the other test cases
ENDFOR
```
