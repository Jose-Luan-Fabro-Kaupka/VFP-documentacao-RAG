# Passando parâmetros para bibliotecas de vínculo dinâmico

Quando você registra uma função DLL, deve especificar o número e os tipos de dados de seus parâmetros. Por padrão, os dados são passados por valor. Você pode forçar um parâmetro a ser passado por referência incluindo um sinal de arroba (@) na frente do parâmetro.

Em geral, as funções DLL seguem as convenções de tipo de dados usadas para C, que diferem das usadas no Visual FoxPro. Por exemplo, as funções DLL não suportam um tipo de dados para data ou moeda. Se os dados que você está passando para uma função DLL estão em um tipo de dados não suportado pela função, você deve convertê-lo para um tipo apropriado antes de passá-lo. Por exemplo, você pode converter uma data para um formato numérico juliano usando comandos como os seguintes:

```foxpro
cDate = sys(11, date())
nDate = val( cDate )
```

Algumas funções DLL exigem parâmetros mais complexos, como estruturas ou matrizes. Se a função exige um ponteiro para uma estrutura, você deve determinar o layout da estrutura e então emulá-la como uma cadeia de caracteres no Visual FoxPro antes de passá-la ou recebê-la da função DLL. Por exemplo, a função de sistema do Windows GetSystemTime( ) espera um ponteiro para uma estrutura consistindo em oito palavras ou inteiros sem sinal de 16 bits indicando o ano, mês, dia e assim por diante. A estrutura é definida da seguinte forma:

```foxpro
typedef struct _SYSTEMTIME {
   WORD wYear ;
   WORD wMonth ;
   WORD wDayOfWeek ;
   WORD wDay ;
   WORD wHour ;
   WORD wMinute ;
   WORD wSecond ;
   WORD wMilliseconds ;
} SYSTEMTIME
```

Para passar dados entre o Visual FoxPro e a função GetSystemTime( ), você deve criar um buffer de cadeia de 40 bytes (consistindo inicialmente de espaços) e então passar o endereço dessa cadeia para a função para que ela a preencha. Quando a cadeia é retornada, você deve analisá-la em incrementos de 2 bytes para extrair os campos individuais da estrutura. O fragmento a seguir ilustra como você pode extrair três dos campos da estrutura:

```foxpro
DECLARE INTEGER GetSystemTime IN win32api STRING @
cBuff=SPACE(40)
=GetSystemTime(@cBuff)
tYear = ALLTRIM(STR(ASC(SUBSTR(cBuff,2)) *  ;
   256 + ASC(SUBSTR(cBuff,1))))
tMonth = ALLTRIM(STR(ASC(SUBSTR(cBuff,4)) * ;
   256 + ASC(SUBSTR(cBuff,3))))
tDOW = ALLTRIM(STR(ASC(SUBSTR(cBuff,6)) * ;
   256 + ASC(SUBSTR(cBuff,5))))
```

Para obter mais informações, você pode examinar o formulário de exemplo Systime.scx no diretório Visual FoxPro ...\Samples\Solution\Winapi. Para outros exemplos de como passar parâmetros para funções DLL, consulte o programa Registry.prg no diretório Visual FoxPro ...\Samples\Classes.

Se os dados com os quais você está trabalhando no Visual FoxPro estão em uma matriz, você deve percorrer a matriz e concatená-la em uma única cadeia de caracteres representando uma matriz no estilo C antes de passá-la para a função DLL. Se a função do Windows espera valores de 16 ou 32 bits, você deve converter os valores para seus equivalentes hexadecimais antes de concatená-los na cadeia de caracteres. Quando você passa a cadeia de caracteres contendo os dados da matriz, o Visual FoxPro passa o endereço da variável de cadeia de caracteres para a DLL, que pode então manipulá-la como uma matriz. Para um exemplo disso, consulte o formulário de exemplo Syscolor.scx no diretório Visual FoxPro ...\Samples\Solution\Winapi.
