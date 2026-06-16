"""Generates ranking reports in text format."""

from src.ranker import RankedCandidate
from datetime import datetime

class ReportGenerator:
    def generate(self, results: list[RankedCandidate], jd_snippet: str = "") -> str:
        lines = []
        lines.append("=" * 50)
        lines.append("RESUME RANK AI — CANDIDATE REPORT")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append("=" * 50)
        if jd_snippet:
            lines.append(f"\nJD Preview: {jd_snippet[:100]}...")
        lines.append(f"\nTotal Candidates Ranked: {len(results)}\n")
        for r in results:
            lines.append(f"#{r.rank} {r.name}")
            lines.append(f"   Score     : {r.score:.0%}")
            lines.append(f"   Highlights: {', '.join(r.highlights) or 'None detected'}")
            lines.append("")
        lines.append("=" * 50)
        return "\n".join(lines)

    def save(self, report: str, path: str = "report.txt"):
        with open(path, "w") as f:
            f.write(report)
        print(f"Report saved to {path}")