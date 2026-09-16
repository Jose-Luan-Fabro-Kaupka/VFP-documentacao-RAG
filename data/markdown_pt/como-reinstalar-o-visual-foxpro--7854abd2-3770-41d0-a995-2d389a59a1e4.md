# Como: reinstalar o Visual FoxPro

Você pode reinstalar o Visual FoxPro desinstalando-o e instalando-o novamente. Você pode desinstalar o Visual FoxPro no menu Iniciar ou no disco de instalação original.

### Para desinstalar o Visual FoxPro
- No menu Iniciar, clique em Painel de controle .
- Na janela Painel de controle, clique duas vezes em Adicionar ou remover programas . A janela Adicionar ou remover programas é aberta.
- Na lista Programas instalados atualmente, clique na versão do Microsoft Visual FoxPro que deseja desinstalar e, em seguida, Alterar/Remover .

Se você reinstalar o Visual FoxPro ou reinstalar em outro local, pode querer limpar suas configurações de usuário e outros arquivos instalados pelo Visual FoxPro antes de reinstalar.

Você pode remover esses arquivos excluindo o conteúdo da pasta ...\Application Data\Microsoft\Visual FoxPro dentro da pasta de configurações do usuário. Para determinar o local da pasta Application Data, digite `? HOME(7)` na janela Command. Esses arquivos incluem seus arquivos de recursos FoxUser.*, que contêm configurações de usuário, e pastas para a Toolbox e o Task Pane.

No entanto, é possível que seus arquivos de recursos estejam em outro local. Você pode determinar o local deles digitando o seguinte na janela Command:

```foxpro
? SYS(2005)
```

Você deve excluir arquivos antigos do Code Reference que possam estar associados a projetos nos diretórios de projeto. Eles são identificados como arquivos projectname_ref.*. Você também pode precisar restaurar as configurações padrão do registro do Visual FoxPro.

O Visual FoxPro inclui a ferramenta VFPClean.app para que você possa garantir que todos os arquivos principais Xbase e outros arquivos estejam configurados adequadamente.

### Para executar VFPClean.app
- Digite a seguinte linha de código na janela Command: DO HOME()+"VFPCLEAN.APP"
