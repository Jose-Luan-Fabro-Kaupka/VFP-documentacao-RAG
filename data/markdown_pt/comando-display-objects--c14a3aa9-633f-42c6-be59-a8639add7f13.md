# Comando DISPLAY OBJECTS

Exibe informações sobre um objeto ou um grupo de objetos.

```foxpro
DISPLAY OBJECTS [LIKE cObjectSkeleton]
   [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]] [NOCONSOLE]
```

#### Parâmetros
 **LIKE cObjectSkeleton**
Exibe informações sobre um subconjunto de objetos. cObjectSkeleton é um esqueleto de especificação de objeto que suporta curingas (* e ?). Por exemplo, para exibir todos os objetos que começam com A, use o comando a seguir: DISPLAY OBJECTS LIKE A*
**TO PRINTER [PROMPT]**
Direciona a saída de DISPLAY OBJECTS para uma impressora. Você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo Print antes do início da impressão. Coloque a palavra-chave PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DISPLAY OBJECTS para o arquivo especificado com FileName. Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se deseja sobrescrever o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é sobrescrito com o valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

DISPLAY OBJECTS exibe as seguintes informações sobre todos os objetos existentes:
 - Propriedades e seus valores.
- Métodos.
- Objetos membros e a classe ou subclasse na qual são baseados.
- Classe ou subclasse na qual os objetos são baseados.
- Hierarquia de classes dos objetos.

DISPLAY OBJECTS preenche toda a janela principal do Visual FoxPro ou janela definida pelo usuário com informações e depois pausa. Pressione qualquer tecla ou clique em qualquer lugar para ver o próximo conjunto de informações. DISPLAY é semelhante a LIST, exceto que LIST exibe as mesmas informações em um fluxo contínuo sem pausar.

# Exemplo

O exemplo a seguir usa DEFINE CLASS e CREATEOBJECT( ) para criar duas classes personalizadas chamadas FormChild e FormGrandChild a partir da classe base Form do Visual FoxPro. DISPLAY OBJECTS exibe informações sobre os objetos e suas propriedades.

```foxpro
CLEAR
frmMyForm = CREATEOBJECT("FormGrandChild")
DISPLAY OBJECTS LIKE frm*
RELEASE frmMyForm
DEFINE CLASS FormChild AS FORM
ENDDEFINE
DEFINE CLASS FormGrandChild AS FormChild
ENDDEFINE
```
