import json
import sys
from datetime import datetime

def main():
  user_id = "Wj8icAcAAAAJ"

  try:
    from scholarly import scholarly
  except Exception:
    print("Biblioteca 'scholarly' não instalada.", file=sys.stderr)
    return 2

  try:
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["publications"])
    pubs = []
    for pub in author.get("publications", []):
      filled = scholarly.fill(pub)
      bib = filled.get("bib", {})
      year = bib.get("pub_year") or bib.get("year")
      try:
        year = int(year) if year else None
      except Exception:
        year = None

      pubs.append({
        "titulo": bib.get("title"),
        "autores": bib.get("author"),
        "veiculo": bib.get("venue") or bib.get("journal"),
        "ano": year,
        "link": filled.get("pub_url") or ""
      })

    out = {
      "atualizado_em": datetime.utcnow().strftime("%Y-%m-%d"),
      "fonte": f"https://scholar.google.com/citations?user={user_id}&hl=pt-BR",
      "publicacoes": pubs
    }

    with open("assets/data/publicacoes.json", "w", encoding="utf-8") as f:
      json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"OK: {len(pubs)} publicações.")
    return 0

  except Exception as e:
    print(f"Falha ao buscar Scholar: {e}", file=sys.stderr)
    return 1

if __name__ == "__main__":
  raise SystemExit(main())
