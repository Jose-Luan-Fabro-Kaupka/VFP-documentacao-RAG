# Propriedade EditorOptions

Especifica as opções do Editor do Visual FoxPro a definir. Há duas versões da sintaxe.

```foxpro
ApplicationObject.EditorOptions [= cOptionString]
```

```foxpro
_VFP.EditorOptions [= cOptionString]
```

# Valor de retorno
 **cOptionString**
Especifica uma cadeia de caracteres consistindo em uma ou mais letras que representam opções a habilitar ou desabilitar. A tabela a seguir descreve os valores válidos para cOptionString . Opção do editor cOptionString Padrão Tempo de execução List Members (Manual) l Desligado Sim 1 Quick Info (Manual) q Desligado Sim 1 List Members (Automatic) L Ligado Sim 1 Quick Info (Automatic) Q Ligado Sim 1 Habilitar hyperlinks (CTRL + Clique para seguir o link) K Ligado Sim Habilitar hyperlinks (Clique para seguir o link) k Desligado Sim DragDrop Between Words W Desligado Não Designer Value Tips T Ligado Não Suprimir formato de clipboard RTF X Desligado Sim 1 Disponível apenas em tempo de execução através do objeto oFoxCode em um script FoxCode. Observação Você não pode usar as configurações maiúsculas e minúsculas da mesma letra juntas na mesma cOptionString . Dica Você pode desabilitar toda a funcionalidade IntelliSense definindo EditorOptions como a cadeia de caracteres vazia (""). As configurações padrão são "LQKT".

# Observações

Aplica-se a: Objeto Application | Variável de sistema _VFP

Designer Value Tips ("T") são dicas de informação associadas a itens em listas e controles drop-down. Estes incluem os seguintes:
 - Campos em listas de fonte de dados (tabelas e views) nos designers Database, View e Form (Data Environment).
- Métodos e eventos em controles drop-down do editor de métodos do Form e Class Designer.

No Visual FoxPro 9.0, as opções do editor _VFP que você especifica com a propriedade EditorOptions são persistidas entre sessões do Visual FoxPro.

A opção Suppress RTF Clipboard ("X") suprime a cópia de código de sintaxe colorida como rich text (formato RTF) ao copiar de um editor do Visual FoxPro e colar em outro editor como Microsoft Word. Com esta opção definida, o texto é copiado para a área de transferência apenas como texto simples sem qualquer formatação rich.

# Exemplo

Por padrão, o IntelliSense no Visual FoxPro está definido como Automatic. Para definir o IntelliSense como Manual, tornando-o disponível através de atalhos de teclado ou menus, use as configurações minúsculas em vez de maiúsculas. Por exemplo:

```foxpro
_VFP.EditorOptions = "lq"    && Sets IntelliSense to Manual.
_VFP.EditorOptions = "LQ"    && Sets IntelliSense to Automatic.
```

Para obter mais informações, consulte Como: definir opções do IntelliSense e Janela Visual FoxPro IntelliSense Manager.
