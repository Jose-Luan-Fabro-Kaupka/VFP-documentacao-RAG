# Comando DECLARE - DLL

Registra uma função em uma biblioteca compartilhada externa. Bibliotecas são arquivos de biblioteca de vínculo dinâmico (.DLL) de 32 bits.

```foxpro
DECLARE [cFunctionType] FunctionName IN LibraryName [AS AliasName]
   [cParamType1 [@] ParamName1, cParamType2 [@] ParamName2, ...]
```

#### Parâmetros
 **cFunctionType**
Indica o tipo de dados do valor de retorno da biblioteca compartilhada, se houver. Se a função não retorna um valor, omita cFunctionType . cFunctionType pode assumir os seguintes valores: cFunctionType Descrição SHORT Inteiro de 16 bits INTEGER Inteiro de 32 bits SINGLE Ponto flutuante de 32 bits DOUBLE Ponto flutuante de 64 bits LONG Inteiro longo de 32 bits STRING Cadeia de caracteres OBJECT Tipo de objeto IDispatch
**FunctionName**
Especifica o nome da função da biblioteca compartilhada a registrar no Visual FoxPro. Nomes de função passados neste parâmetro diferenciam maiúsculas de minúsculas. Observação Um nome de função DLL pode não ser o mesmo declarado no manual Win32 API. Por exemplo, a função MessageBox deve ser nomeada MessageBoxA (para caractere de byte único) e MessageBoxW (para UNICODE). Se o Visual FoxPro não conseguir localizar a função DLL que você especifica com FunctionName , a letra A é acrescentada ao final do nome da função e o Visual FoxPro pesquisa novamente a função com o novo nome. Se a função da biblioteca compartilhada que você especifica tem o mesmo nome de uma função Visual FoxPro ou não é um nome Visual FoxPro válido, use a cláusula AS para atribuir um alias à função quando a registrar, conforme descrito mais adiante neste tópico. Você também pode usar OBJECT como valor de retorno, como "DECLARE OBJECT myfunc IN some DLL ..." embora a convenção COM normalmente não tenha APIs dessa forma. Por exemplo: DECLARE INTEGER AccessibleObjectFromWindow IN oleacc.dll ; integer, integer, string , object @
**IN LibraryName**
Especifica o nome da biblioteca compartilhada externa que contém a função especificada com FunctionName . Se você especificar WIN32API para LibraryName , o Visual FoxPro pesquisa a função .dll Windows de 32 bits em Kernel32.dll, Gdi32.dll, User32.dll, Mpr.dll e Advapi32.dll.
**AS AliasName**
Especifica um nome de alias para um nome de função de biblioteca compartilhada que tem o mesmo nome de uma função Visual FoxPro ou não é um nome Visual FoxPro válido. AliasName não deve ser uma palavra reservada do Visual FoxPro nem o nome de uma função de biblioteca compartilhada já registrada com o Visual FoxPro. Se você atribuir alias à função, use o alias ao chamar a função da biblioteca compartilhada. AliasName não diferencia maiúsculas de minúsculas.
**cParameterType1 [@] ParamName1 , cParameterType2 [@] ParamName2 , ...**
Especifica os tipos de parâmetro passados à função da biblioteca compartilhada. cParameterType é obrigatório e especifica o tipo de dados de quaisquer parâmetros que a função da biblioteca compartilhada espera receber. cParameterType pode ser um dos seguintes: cParameterType Descrição INTEGER Inteiro de 32 bits SINGLE Ponto flutuante de 32 bits DOUBLE Ponto flutuante de 64 bits LONG Inteiro longo de 32 bits STRING Cadeia de caracteres O Visual FoxPro gera um erro se os parâmetros não são do tipo que a função da biblioteca compartilhada espera. Valores nulos podem ser passados como cadeias de caracteres vazias. Para passar um parâmetro por referência ao chamar a função, você deve incluir o sinal de arroba (@) depois do cParameterType neste comando e antes da variável correspondente na função de chamada. Se você não incluir @ em DECLARE, na função de chamada ou em ambos, o parâmetro é passado por valor. Para informações sobre funções de biblioteca compartilhada que requerem @ para passar parâmetros por referência, consulte o guia do programador do seu sistema operacional ou ambiente (por exemplo, consulte o Microsoft Win32 Programmer's Guide para informações sobre passagem de parâmetros para DLLs Windows). Observação Os nomes de parâmetro ParamName1 , ParamName2 e assim por diante são opcionais e não são usados pelo Visual FoxPro nem pela função da biblioteca compartilhada. Você pode incluí-los como lembrete dos nomes e tipos de parâmetros que a função recebe.

# Observações

Antes de poder chamar uma função de biblioteca compartilhada no Visual FoxPro, você deve emitir DECLARE com o nome da função, o nome da biblioteca compartilhada que contém a função e os tipos de parâmetro que a função espera receber.

Para compatibilidade com versões anteriores, o Visual FoxPro permite chamadas a bibliotecas de API externas usando o comando SET LIBRARY. (Usando SET LIBRARY, você pode acessar funções em Foxtools.fll.) No entanto, usar DECLARE é o método preferido para registrar funções de biblioteca compartilhada.

Embora o Visual FoxPro adicione o cFunctionType OBJECT a este comando principalmente para suportar algumas rotinas de API ActiveX Accessibility, você pode usá-lo genericamente com outras rotinas da API Windows.

Para mais informações sobre chamada de funções de biblioteca compartilhada, consulte o guia do programador do seu sistema operacional ou ambiente (por exemplo, consulte o Microsoft Win32 Programmer's Guide para informações sobre chamada de DLLs).

Emita DISPLAY STATUS ou LIST STATUS para exibir os nomes das funções registradas. Emita CLEAR ALL ou CLEAR DLLS para remover funções registradas da memória.

# Exemplo

Este exemplo para Windows retorna o handle da janela do Visual FoxPro ou zero se você alternar para outra aplicação Windows. Quando a janela WAIT é exibida, você tem 5 segundos para pressionar `ALT+TAB` para alternar para uma aplicação Windows diferente, ou pode deixar o Visual FoxPro como a aplicação ativa.

```foxpro
CLEAR
DECLARE INTEGER GetActiveWindow IN win32api
WAIT WINDOW "You can switch to another application now" TIMEOUT 5
? GetActiveWindow()
```
