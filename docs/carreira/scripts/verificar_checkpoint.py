"""Confere hashes dos registros de continuidade; nao avalia competencia pessoal."""
from pathlib import Path
import hashlib
import json
import sys


def verify(manifest_path):
    manifest_path = Path(manifest_path).resolve()
    root = manifest_path.parent.parent
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    required = {
        "ROADMAP.md", "PROGRESSO.md", "COMPETENCIAS.md", "CERTIFICACOES.md",
        "PORTFOLIO.md", "DECISOES.md", "HANDOFF.md",
    }
    errors = []
    seen = set()
    for item in data["files"]:
        rel = item["path"]
        if rel in seen:
            errors.append("Caminho repetido: " + rel)
            continue
        seen.add(rel)
        path = (root / rel).resolve()
        if root not in path.parents:
            errors.append("Caminho fora da documentacao: " + rel)
            continue
        if not path.is_file():
            errors.append("Arquivo ausente: " + rel)
            continue
        content = path.read_bytes()
        if len(content) != item["size_bytes"]:
            errors.append("Tamanho divergente: " + rel)
        if hashlib.sha256(content).hexdigest() != item["sha256"]:
            errors.append("SHA-256 divergente: " + rel)
    for rel in sorted(required - seen):
        errors.append("Registro obrigatorio fora do manifesto: " + rel)
    if errors:
        print("FALHOU " + data["checkpoint_id"])
        for error in errors:
            print(error)
        return 1
    print("OK " + data["checkpoint_id"] + ": " + str(len(seen)) + " arquivos conferidos.")
    print("A identidade da versao e a publicacao devem ser conferidas no commit Git correspondente.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python verificar_checkpoint.py caminho/CP-nnnn.json")
        raise SystemExit(2)
    try:
        raise SystemExit(verify(sys.argv[1]))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("FALHOU: " + str(error))
        raise SystemExit(1)
