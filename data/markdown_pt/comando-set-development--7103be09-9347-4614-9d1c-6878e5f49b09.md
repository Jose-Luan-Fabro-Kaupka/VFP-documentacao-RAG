# Comando SET DEVELOPMENT

Faz o Visual FoxPro comparar a data e hora de criação de um programa com as do seu arquivo de objeto compilado quando o programa é executado.

```foxpro
SET DEVELOPMENT ON | OFF
```

#### Parâmetros
 **ON**
(Padrão) Especifica que o Visual FoxPro recompila o programa de origem antes de executá-lo se ele for mais recente que seu programa de objeto compilado. Esta opção garante que a versão mais atual de um programa seja executada.
**OFF**
Especifica que o Visual FoxPro não compare as versões de origem e compilada do programa. Se SET DEVELOPMENT estiver definido como OFF, você pode não estar sempre executando a versão mais atual de um programa.

# Observações

SET DEVELOPMENT precisa estar definido como ON quando os programas são modificados fora do Visual FoxPro. Usar um editor externo pode exigir que você emita CLEAR PROGRAM antes de executar o programa modificado. Para obter mais informações, consulte Comandos CLEAR. Use SET DEVELOPMENT OFF para desempenho ideal.

SET DEVELOPMENT também determina se a janela Trace é aberta quando ocorre um erro em um Form em execução. Se SET DEVELOPMENT estiver ON, a janela Trace é aberta com a linha do programa que causou o erro selecionada. Se SET DEVELOPMENT estiver OFF, a janela Trace não é aberta quando ocorre um erro em um Form.
