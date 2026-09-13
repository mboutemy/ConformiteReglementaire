"""Point d'entrée CLI du slice.

Usage :
    python -m src.cli "Nous n'avons pas de DPO désigné mais traitons les données de 800 clients."
    echo "Nous avons un plan de continuité validé en 2022" | python -m src.cli
"""

import json
import sys

from src.classify import classify


def main() -> None:
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        message = sys.stdin.read()

    result = classify(message)
    print(json.dumps(result, ensure_ascii=False))
if __name__ == "__main__":
    main()
