# Exemplo Usar o controle RichText

Arquivo: ...\Samples\Solution\OLE\Rtf.scx

Este exemplo ilustra o uso de um controle RichText para exibir e editar texto RTF armazenado no campo memo de uma tabela.

Você pode definir o ControlSource de um controle RichText diretamente para um campo de caracteres, mas não para um campo memo. Em vez disso, crie uma propriedade de formulário para mediar entre o controle RichText e o campo memo.

### Para armazenar texto RTF em um campo memo
- Defina a propriedade ControlSource do controle RichText para a propriedade do formulário. THISFORM.oleRTF.ControlSource = THISFORM.cText
- Armazene o conteúdo do campo memo na propriedade do formulário. THISFORM.cText = rtf.source
- Antes de mover o ponteiro de registro, armazene a propriedade TextRTF do controle RichText no campo memo. REPLACE rtf.Source WITH THISFORM.oleRTF.TextRTF

O texto armazenado no arquivo memo está no formato RTF padrão, por exemplo:

{\rtf1\ansi\deff0\deftab720{\fonttbl{\f0\fswiss MS Sans Serif;}{\f1\froman\fcharset2 Symbol;}{\f2\fswiss Arial;}{\f3\fswiss Arial;}} {\colortbl\red0\green0\blue0;\red255\green0\blue0;} \deflang1033\pard\qc\plain\f3\fs32\i The RichTextBox Control \par \pard\plain\f3\fs20
