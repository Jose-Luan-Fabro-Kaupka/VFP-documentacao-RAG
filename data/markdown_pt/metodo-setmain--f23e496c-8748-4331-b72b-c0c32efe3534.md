# Método SetMain

Define o arquivo principal em um projeto.

```foxpro
Object.SetMain([cFileName])
```

#### Parâmetros
 **cFileName**
Especifica um arquivo no projeto a ser definido como arquivo principal. O arquivo principal pode ser um programa ou um formulário. Certifique-se de incluir a extensão do arquivo em cFileName. Se cFileName for omitido ou for uma cadeia de caracteres vazia, nenhum arquivo no projeto é definido como arquivo principal.

# Observações

Aplica-se a: Project Object (Visual FoxPro)

O método SetMain retorna true (.T.) se o arquivo que você especificar for definido como arquivo principal. False (.F.) é retornado se o arquivo que você especificar não estiver no projeto ou se o arquivo que você especificar não for do tipo de arquivo apropriado.

O arquivo principal é um programa (arquivo .prg) ou formulário (arquivo .scx) que serve como ponto de partida de execução para um aplicativo compilado e a partir do qual outros componentes do seu aplicativo são chamados. Normalmente, o arquivo principal define o ambiente operacional do aplicativo, executa programas de menu ou formulários para exibir a interface do aplicativo e estabelece o loop de eventos do aplicativo com o comando READ EVENTS. Você deve designar um arquivo principal no Project Manager antes de poder criar um aplicativo (.app) ou arquivo executável (.exe) a partir do projeto.

> **Observação:** Especificar um arquivo como arquivo principal em um projeto também define a propriedade MainFile do projeto.
