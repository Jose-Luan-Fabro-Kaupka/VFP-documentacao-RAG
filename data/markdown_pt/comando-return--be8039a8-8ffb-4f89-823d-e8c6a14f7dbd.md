# Comando RETURN

Retorna o controle do programa a um programa chamador.

```foxpro
RETURN [eExpression | oObjectName | TO MASTER | TO ProcedureName]
```

#### Parâmetros
 **eExpression**
Especifica uma expressão retornada ao programa chamador. Se você omitir RETURN ou a expressão de retorno, true (.T.) é automaticamente retornado ao programa chamador.
**oObjectName**
Especifica o objeto ao qual o foco é atribuído. Aplica-se apenas ao Valid Event.
**TO MASTER**
Retorna o controle ao programa chamador de nível mais alto.
**TO ProcedureName**
Especifica o procedimento ao qual o controle é retornado.

# Observações

RETURN encerra a execução de um programa, procedimento ou função e retorna o controle ao programa chamador, ao programa chamador de nível mais alto, a outro programa ou à janela Command.

O Visual FoxPro libera variáveis PRIVATE quando RETURN é executado.

RETURN geralmente é colocado no final de um programa, procedimento ou função para retornar o controle a um programa de nível superior. No entanto, um RETURN implícito é executado se você omitir RETURN.

Você pode direcionar onde o foco é atribuído usando o parâmetro opcional oObjectName no comando RETURN do Valid Event. O objeto especificado deve ser um objeto Visual FoxPro válido. Se o objeto especificado estiver desabilitado ou não puder receber foco, o foco é atribuído ao próximo objeto na ordem de tabulação. Se um objeto inválido for especificado, o Visual FoxPro mantém o foco no objeto atual. Agora você pode definir o foco em objetos em outro formulário visível ou em um controle Page ou Pageframe não visível.

# Exemplo 1

No exemplo a seguir, a função `longdate` retorna uma cadeia de caracteres adequada para impressão a partir de uma data.

```foxpro
SET CENTURY ON
? longdate({^1998-02-16})  && Displays Monday, February 16, 1998
FUNCTION longdate
PARAMETER mdate
RETURN CDOW(mdate) + ', ' + MDY(mdate)
```

# Exemplo 2

Você pode retornar matrizes diretamente de um método de classe usando o operador @. Retornar matrizes de um método de classe permite que componentes COM do Visual FoxPro se comuniquem com outros componentes COM, como os escritos em Visual Basic ou Visual C++. Isso pode afetar métodos implementados de uma interface usando a cláusula IMPLEMENTS.

Como essas matrizes devem estar no escopo após a chamada do método, matrizes LOCAL e PRIVATE são inválidas nessas declarações. Você deve usar uma matriz PUBLIC ou de membro. Este suporte a matrizes não funciona com o comando STORE TO.

No exemplo a seguir, a classe `t1` tem uma função `GetMyArray` que retorna uma matriz.

```foxpro
DEFINE CLASS t1 AS custom OLEPUBLIC
   DIMENSION Arrayelement[3]
   FUNCTION GetMyArray() AS array
      this.Arrayelement[1] = 1
      this.Arrayelement[2] = 2
      this.Arrayelement[3] = 3
      RETURN @THIS.Arrayelement
   ENDFUNC
ENDDEFINE
```
