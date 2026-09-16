#!/usr/bin/env python3
"""
Projeto sintético VFP 9 usado como palco dos rastros de treino agentic.

As funções em exemplos/*.pr2 são uma biblioteca plana. Um agente, porém,
trabalha dentro de uma árvore de arquivos: precisa achar onde algo mora
antes de alterar. Este módulo espalha essas funções em módulos críveis e
renderiza arquivos como as ferramentas do agente os mostrariam, para os
rastros poderem citar números de linha reais.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

# Domínio (primeira palavra depois do prefixo F_/P_) -> arquivo do módulo.
DOMAIN_MODULES: dict[str, str] = {
    "Texto": "LIB/TEXTO.PRG",
    "Nome": "LIB/TEXTO.PRG",
    "Maiusculo": "LIB/TEXTO.PRG",
    "Numero": "LIB/NUMERO.PRG",
    "Valores": "LIB/NUMERO.PRG",
    "Somar": "LIB/NUMERO.PRG",
    "Subtrair": "LIB/NUMERO.PRG",
    "Incrementar": "LIB/NUMERO.PRG",
    "Zerar": "LIB/NUMERO.PRG",
    "Tamanho": "LIB/NUMERO.PRG",
    "Data": "LIB/DATA.PRG",
    "Idade": "LIB/DATA.PRG",
    "Tempo": "LIB/DATA.PRG",
    "Matriz": "LIB/MATRIZ.PRG",
    "Arquivo": "LIB/ARQUIVO.PRG",
    "Diretorio": "LIB/ARQUIVO.PRG",
    "Caminho": "LIB/ARQUIVO.PRG",
    "Log": "LIB/ARQUIVO.PRG",
    "Sistema": "LIB/SISTEMA.PRG",
    "Configuracao": "LIB/SISTEMA.PRG",
    "Objeto": "LIB/SISTEMA.PRG",
    "Colecao": "LIB/SISTEMA.PRG",
    "Bit": "LIB/SISTEMA.PRG",
    "Cor": "LIB/SISTEMA.PRG",
    "Cliente": "APP/CLIENTE.PRG",
    "Clientes": "APP/CLIENTE.PRG",
    "Produto": "APP/PRODUTO.PRG",
    "Produtos": "APP/PRODUTO.PRG",
    "Venda": "APP/VENDA.PRG",
    "Vendas": "APP/VENDA.PRG",
    "Cursor": "APP/DADOS.PRG",
    "Tabela": "APP/DADOS.PRG",
    "Grid": "UI/FORMULARIO.PRG",
    "Formulario": "UI/FORMULARIO.PRG",
    "Controle": "UI/FORMULARIO.PRG",
    "Combo": "UI/FORMULARIO.PRG",
    "Botao": "UI/FORMULARIO.PRG",
}
FALLBACK_MODULE = "LIB/UTIL.PRG"

MODULE_HEADERS: dict[str, str] = {
    "LIB/TEXTO.PRG": "Funções de manipulação de texto",
    "LIB/NUMERO.PRG": "Funções numéricas e de cálculo",
    "LIB/DATA.PRG": "Funções de data e hora",
    "LIB/MATRIZ.PRG": "Funções de manipulação de arrays",
    "LIB/ARQUIVO.PRG": "Funções de arquivo, diretório e log",
    "LIB/SISTEMA.PRG": "Funções de sistema, objetos e configuração",
    "LIB/UTIL.PRG": "Utilitários diversos",
    "APP/CLIENTE.PRG": "Regras de negócio de clientes",
    "APP/PRODUTO.PRG": "Regras de negócio de produtos",
    "APP/VENDA.PRG": "Regras de negócio de vendas",
    "APP/DADOS.PRG": "Acesso a cursores e tabelas",
    "UI/FORMULARIO.PRG": "Formulários e controles de interface",
}


def module_for(name: str) -> str:
    match = re.match(r"^[FP]_([A-Z][a-z]+)", name)
    if match:
        return DOMAIN_MODULES.get(match.group(1), FALLBACK_MODULE)
    return FALLBACK_MODULE


def signature_of(code: str) -> str:
    """`F_TextoMaiusculo(cTexto)` from the FUNCTION header plus PARAMETERS line."""
    header = re.search(r"(?mi)^\s*(FUNCTION|PROCEDURE)\s+(\S+)", code)
    if not header:
        return ""
    name = header.group(2)
    params = re.search(r"(?mi)^\s*(?:L?PARAMETERS)\s+(.+)$", code)
    if not params:
        return f"{name}()"
    cleaned = re.sub(r"\s+", " ", params.group(1)).strip().rstrip(";")
    return f"{name}({cleaned})"


@dataclass
class Function:
    name: str
    kind: str
    code: str
    module: str
    start_line: int = 0
    end_line: int = 0


@dataclass
class Module:
    path: str
    functions: list[Function] = field(default_factory=list)
    text: str = ""

    @property
    def line_count(self) -> int:
        return len(self.text.split("\n"))


class Project:
    """A rendered file tree with stable line numbers for every function."""

    def __init__(self, functions: list[dict]) -> None:
        self.modules: dict[str, Module] = {}
        self.functions: dict[str, Function] = {}

        grouped: dict[str, list[dict]] = {}
        for item in functions:
            grouped.setdefault(module_for(item["name"]), []).append(item)

        for path in sorted(grouped):
            entries = sorted(grouped[path], key=lambda f: f["name"])
            module = Module(path=path)
            lines: list[str] = [
                "*" * 60,
                f"* {path}",
                f"* {MODULE_HEADERS.get(path, 'Módulo do projeto')}",
                "*" * 60,
                "",
            ]
            for entry in entries:
                body = entry["code"].strip().split("\n")
                start = len(lines) + 1
                lines.extend(body)
                end = len(lines)
                lines.append("")
                function = Function(
                    name=entry["name"],
                    kind=entry["kind"],
                    code=entry["code"].strip(),
                    module=path,
                    start_line=start,
                    end_line=end,
                )
                module.functions.append(function)
                self.functions[function.name] = function
            module.text = "\n".join(lines).rstrip() + "\n"
            self.modules[path] = module

    # -- renderizações voltadas às ferramentas ----------------------------- #
    def list_files(self) -> str:
        rows = []
        for path in sorted(self.modules):
            module = self.modules[path]
            rows.append(f"{path}  ({module.line_count} linhas, {len(module.functions)} rotinas)")
        return "\n".join(rows)

    def read_range(self, path: str, start: int, end: int) -> str:
        module = self.modules[path]
        lines = module.text.split("\n")
        start = max(1, start)
        end = min(len(lines), end)
        return "\n".join(f"{n:5d}| {lines[n - 1]}" for n in range(start, end + 1))

    def search(self, pattern: str, limit: int = 12) -> list[tuple[str, int, str]]:
        hits: list[tuple[str, int, str]] = []
        regex = re.compile(pattern, re.I)
        for path in sorted(self.modules):
            for number, line in enumerate(self.modules[path].text.split("\n"), 1):
                if regex.search(line):
                    hits.append((path, number, line))
                    if len(hits) >= limit:
                        return hits
        return hits


def load_functions(paths: list[Path]) -> list[dict]:
    from build_code_training_dataset import extract_functions

    seen: dict[str, dict] = {}
    for path in paths:
        for item in extract_functions(path.read_text(encoding="utf-8")):
            seen.setdefault(item["name"], item)
    return list(seen.values())
