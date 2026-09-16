# O campo para valor Unicode não deve usar conversão de página de código. (Erro 2142)

Ocorre quando o Visual FoxPro tenta converter dados Unicode de ou para XML, e a propriedade NoCpTrans é avaliada como False (.F.).
 - Verifique se os campos de caracteres e memo usados para dados Unicode têm a propriedade NoCpTrans definida como True (.T.).
