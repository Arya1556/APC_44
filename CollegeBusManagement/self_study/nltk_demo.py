"""A small rule-based query demo; install NLTK only for tokenization practice."""

import re

from CollegeBusManagement.modules.bus_management import list_buses
from CollegeBusManagement.modules.route_management import list_routes


def answer_query(question: str, tokenizer=None) -> str:
    words = tokenizer(question.lower()) if tokenizer else re.findall(r"[a-z0-9-]+", question.lower())
    if any(word in words for word in ("route", "routes", "stop", "stops")):
        routes = list_routes()
        return "Routes: " + (", ".join(row["route_name"] for row in routes) or "none configured")
    if any(word in words for word in ("seat", "seats", "bus", "buses")):
        buses = list_buses()
        if not buses:
            return "No buses are configured."
        return "; ".join(
            f"{row['bus_number']}: {row['available_seats']} seats available" for row in buses
        )
    return "Try asking about routes, stops, buses, or seats."


if __name__ == "__main__":
    try:
        from nltk.tokenize import TreebankWordTokenizer
    except ImportError as exc:
        raise SystemExit("Optional dependency missing. Install with: pip install nltk") from exc
    question = input("Ask about routes, stops, buses, or seats: ")
    print(answer_query(question, TreebankWordTokenizer().tokenize))
