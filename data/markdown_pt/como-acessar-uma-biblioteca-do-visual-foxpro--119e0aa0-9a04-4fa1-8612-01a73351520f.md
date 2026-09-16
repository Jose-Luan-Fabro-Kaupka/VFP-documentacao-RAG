# Como: acessar uma biblioteca do Visual FoxPro

Uma biblioteca do Visual FoxPro (arquivo .fll), assim como um arquivo .dll, contém funções que você pode chamar como qualquer outra função. Em geral, é mais fácil passar parâmetros para funções em arquivos .fll e receber valores delas, pois esses arquivos são criados especificamente para chamadas a partir do Visual FoxPro.

Para usar uma biblioteca do Visual FoxPro, registre o arquivo .fll especificando seu nome com o comando SET LIBRARY e, em seguida, chame a função normalmente. Diferentemente do registro de funções .dll, você não precisa registrar funções individuais no arquivo .fll nem especificar informações sobre os parâmetros ou tipos de dados usados pela função.

> **Observação:** Se você quiser usar uma biblioteca .fll de uma versão anterior do Visual FoxPro, ela deverá ser recompilada para funcionar com o Visual FoxPro versão 5.0.

### Para chamar uma função .fll
- Registre a biblioteca .fll emitindo um comando SET LIBRARY.
- Chame as funções da biblioteca como chamaria qualquer função.

Por exemplo, o código a seguir chama uma função da biblioteca Foxtools.fll no diretório de instalação do Visual FoxPro para determinar o tipo da unidade C:

```foxpro
SET LIBRARY TO "C:\Program Files\Microsoft Visual FoxPro 9.0\Foxtools.fll"
? DriveType("C:")
```

Se precisar registrar mais de um arquivo .fll, inclua a palavra-chave ADDITIVE no comando SET LIBRARY. Caso contrário, o arquivo .fll registrado anteriormente será removido e substituído pelo registrado mais recentemente.

Se o nome de uma função entrar em conflito com o de outra função já disponível no Visual FoxPro, a última função definida terá precedência. Se o nome da função em uma biblioteca vinculada for igual ao de uma função intrínseca do Visual FoxPro, a função do Visual FoxPro terá precedência.

Você só precisa registrar as funções de um arquivo .fll uma vez por sessão, pois elas permanecem disponíveis até que você encerre o Visual FoxPro. Se não pretende chamar novamente as funções de um arquivo .fll, remova-o da memória e libere recursos emitindo os comandos RELEASE LIBRARY, RELEASE ALL ou SET LIBRARY. Para obter mais informações, consulte Comando RELEASE LIBRARY e Comando RELEASE.
