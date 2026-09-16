# Criando bibliotecas de vínculo dinâmico do Visual FoxPro

Uma biblioteca de vínculo dinâmico (FLL) do Visual FoxPro é essencialmente uma DLL que contém chamadas à API do Visual FoxPro. Você pode criar a estrutura básica da DLL no seu ambiente de desenvolvimento e depois adicionar as funções do Visual FoxPro que deseja chamar. As seções a seguir descrevem modelos de exemplo para criar modelos FLL em C e C++.

# Configurando um modelo de biblioteca

Cada biblioteca FLL do Visual FoxPro tem a mesma estrutura básica. Você pode usar um modelo para a estrutura, de modo que precise apenas adicionar código para sua rotina de biblioteca específica.

Há cinco elementos em um modelo de biblioteca do Visual FoxPro:
 - Instrução #include.
- Definição de função. A definição de função tem um valor de retorno void e recebe o parâmetro ParamBlk *parm. Para obter mais informações sobre o parâmetro ParamBlk, consulte Parâmetros em bibliotecas externas.
- Código da função.
- Estrutura FoxInfo. As funções na FLL interagem com o Visual FoxPro por meio da estrutura FoxInfo. O Visual FoxPro usa FoxInfo para determinar o nome da função e o número e o tipo dos parâmetros.
- Estrutura FoxTable. A estrutura FoxTable é uma lista encadeada que mantém o controle das estruturas FoxInfo.

Para obter mais informações sobre as definições de struct FoxInfo e FoxTable, consulte o arquivo Pro_ext.h.

Você também precisa dos seguintes arquivos:
 - O arquivo de cabeçalho Pro_ext.h. Você pode imprimir este arquivo para ver as declarações de função, typedefs e structs usados na API do Visual FoxPro.
- O arquivo Winapims.lib.

Ambos os arquivos estão localizados no diretório Microsoft Visual FoxPro ..\Samples\API.

# Modelos de exemplo

Para rotinas em C, você pode usar o seguinte modelo:

```foxpro
#include <Pro_ext.h>
void Internal_Name(ParamBlk *parm)
{
// Function code goes here.
}
FoxInfo myFoxInfo[] = {
   {"FUNC_NAME", (FPFI) Internal_Name, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable *)0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```

Para rotinas em C++, você precisa declarar a estrutura FoxTable como externa no seguinte modelo:

```foxpro
#include <Pro_ext.h>
void Internal_Name(ParamBlk  *parm)
{
// Function code goes here.
}
   FoxInfo myFoxInfo[] = {
      {"FUNC_NAME", (FPFI) Internal_Name, 0, ""},
   };
extern "C" {
   FoxTable _FoxTable = {
      (FoxTable *)0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
   };
}
```
