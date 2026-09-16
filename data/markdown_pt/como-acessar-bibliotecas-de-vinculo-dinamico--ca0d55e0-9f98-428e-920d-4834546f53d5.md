# Como: acessar bibliotecas de vínculo dinâmico

Se a funcionalidade que você precisa está disponível em uma DLL, você pode vincular à biblioteca e chamar suas funções. Antes de chamar uma função DLL, você deve determinar seu protocolo de chamada, incluindo o nome da função, o número e os tipos de dados de seus parâmetros e o tipo de dados de seu valor de retorno.

No Visual FoxPro, você só pode usar DLLs que foram escritas para um ambiente de 32 bits. No entanto, se você precisar acessar uma DLL de 16 bits, pode chamá-la usando funções disponíveis em Foxtools.fll. Para detalhes, consulte a Ajuda do Foxtools (Foxtools.chm).

### Para chamar uma função DLL
- Registre a função DLL usando o Comando DECLARE - DLL . Os nomes de função diferenciam maiúsculas de minúsculas. Observação Se você especificar WIN32API para o nome da biblioteca, o Visual FoxPro procura a função DLL do Windows de 32 bits em Kernel32.dll, Gdi32.dll, User32.dll, Mpr.dll e Advapi32.dll.
- Chame a função como faria com qualquer função do Visual FoxPro.

Por exemplo, o programa a seguir registra a função GetActiveWindow( ) da DLL de sistema USER do Windows, que exibe o identificador da janela principal do Visual FoxPro. GetActiveWindow( ) não recebe parâmetros, mas retorna um único inteiro:

```foxpro
DECLARE INTEGER GetActiveWindow IN win32api
MESSAGEBOX(STR( GetActiveWindow() ) )
```

A DLL que contém a função que você está registrando deve estar disponível no diretório padrão, nos diretórios Windows ou System, ou no caminho do DOS.

Se a função que você deseja chamar tem o mesmo nome de outra função já disponível no Visual FoxPro (seja uma função nativa ou uma função DLL declarada anteriormente), você pode atribuir um alias à função com o nome duplicado e, em seguida, chamá-la usando o alias.

```foxpro
DECLARE INTEGER GetActiveWindow IN win32api AS GetWinHndl
MESSAGEBOX(STR( GetWinHndl() ) )
```

Funções DLL vinculadas permanecem disponíveis até você sair do Visual FoxPro, portanto você só precisa declará-las uma vez por sessão. Se você não pretende chamar as funções em uma DLL novamente, pode emitir o comando CLEAR Commands para removê-la da memória e liberar recursos.

> **Observação:** Emitir CLEAR DLLS limpa todas as funções DLL declaradas da memória.
