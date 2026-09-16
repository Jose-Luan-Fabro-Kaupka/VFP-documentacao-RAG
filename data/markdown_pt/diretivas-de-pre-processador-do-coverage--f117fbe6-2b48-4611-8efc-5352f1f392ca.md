# Diretivas de pré-processador do Coverage

As seguintes instruções #DEFINE dão suporte a este aprimoramento do Coverage Profiler.

# *COV_LOCS.H

Adicionadas quatro #DEFINEs na seção que trata mensagens wait window nowait/statusbar:

```foxpro
#DEFINE COV_LOADING_STACKINFO_LOC "Loading log for StackLevel analysis"
#DEFINE COV_GENERATING_STACKXML_LOC "Generating StackLevel XML..."
#DEFINE COV_WRITING_STACKXML_LOC "Writing StackLevel XML to disk"
#DEFINE COV_WRITING_TRANSFORM_LOC "Writing transformed file to disk"
```

Adicionadas quatro #DEFINEs à seção de prompts de atalho:

```foxpro
#DEFINE COV_SC_STACKLEVEL_LOC "\<Generate StackLevel XML"
#DEFINE COV_SC_VIEW_STACKLEVEL_LOC "View Stac\<klevel XML"
#DEFINE COV_SC_STACK_TRANSFORM_LOC "\<Transform StackLevel XML"
#DEFINE COV_SC_STACKLEVEL_EXTENDED_LOC "E\<xtended StackLevel XML"
```

Adicionadas sete #DEFINEs à seção que trata títulos, filtros e assim por diante das caixas de diálogo GETFILE/PUTFILE:

```foxpro
#DEFINE COV_SETSTACKXML_TITLE_LOC "Please specify location to save Coverage StackLevel XML for"
#DEFINE COV_XMLFILES_LOC "XML Files"
#DEFINE COV_XSLFILES_LOC "XSL Transforms"
#DEFINE COV_HTMFILES_LOC "HTML Files"
#DEFINE COV_SAVEDSTACKXML_AS_LOC "Your coverage stack analysis is saved as"
#DEFINE COV_SETTRANSFORMEDXML_TITLE_LOC "Please specify location to save transformed file for"
#DEFINE COV_GETXSLTFILE_TITLE_LOC "Please specify an XSL Transformation file"
```

Adicionadas três #DEFINEs à seção que trata prompts e legendas da caixa de diálogo de opções:

```foxpro
#DEFINE COV_OPT_STACK_LOC "StackLevel XML analysis"
#DEFINE COV_OPT_STACK_EXTENDED_LOC "\<Generate extended StackLevel XML tree"
#DEFINE COV_OPT_STACK_XSLT_LOC "XSL \<Transform..."
```

# COV_TUNE.H

Novas configurações ajustáveis (e comentários associados) que dão suporte ao novo recurso:

Duas configurações são usadas na criação de nomes de tag:

```foxpro
* the first two represent element node prefixes
#DEFINE COV_STACKROOT "VFPCallStackLog"
#DEFINE COV_STACK_ONEVENT_TAG event
```

* estes são semelhantes a COV_SKIPFILEDBF_SUFFIX e COV_TARGETDBF_SUFFIX

```foxpro
*the next items are used to help identify the XML and HTM files written to
* disk as being generated from this particular process.
#DEFINE COV_STACKXML_SUFFIX "_STACK"
#DEFINE COV_STACKXMLEXT_SUFFIX "_STACKX"
#DEFINE COV_TRANSFORM_SUFFIX "_XSL"
```

O seguinte é uma opção de desempenho que, como COV_TOPSPEED, raramente é necessária.

```foxpro
* the next item indicates whether lines are loaded from the Coverage
* source workfile .dbf file or are gathered directly by from the original
* text log. Coverage Profiler has a very slight speed advantage but will
* not include ON ... events, since those lines are ignored by the
* Coverage source and target workfiles (there is no code
* to mark or profile for these lines).
#DEFINE COV_LOAD_STACK_FROM_DBF .F.
```

Esta definição fornece uma expressão para as tags no XML derivadas dos itens disponíveis no log de origem.

```foxpro
* the variables in the next item have the same meaning as the columns
* of the same name in the Coverage source workfile .dbf file
* -- equivalents for these items are read in from the source text log
* when COV_LOAD_STACK_FROM_DBF is .F., and this expression stays the same.
* You can change it as long as you ensure that the result will  be empty
* only for ON ... events.
* Load a log into COVERAGE.APP,
* SET DATASESSION TO _oCoverage.DataSessionID, and refer to the
* source workfile (by default, its alias is FromLog) for some indication
* on the possible contents of these columns.
#DEFINE COV_STACKEXPR ALLTR(IIF(INLIST(FileType,".fxp",".mpx",".qpx",".spx"), ;
                      IIF(EMPTY(ObjClass), ;
                      IF(NOT EMPTY(Executing),ALLTR(Executing),""),;
                      IIF(LEFT(Executing,1)=".",ALLTR(ObjClass),"")+ALLTR(Executing)), ;
                      ALLTR(Executing)))
```
