from retriever import get_retriever
import re

def rag_answer(question):
    retriever = get_retriever()
    docs = retriever.invoke(question)

    if not docs:
        return "❌ Answer not available in SOP."

    q = question.lower()

    for doc in docs:
        lines = doc.page_content.split("\n")

        for line in lines:
            line = line.strip()

            # Skip headings / junk
            if len(line) < 25:
                continue
            if "standard operating procedure" in line.lower():
                continue
            if line.isupper():
                continue

            # Casual leave count
            if "casual" in q and "leave" in q:
                if re.search(r"\d+", line) and "casual" in line.lower():
                    return f"📄 SOP-based Answer:\n\n{line}"

            # Sick leave medical certificate
            if ("sick leave" in q or "medical certificate" in q):
                if "medical certificate" in line.lower():
                    return f"📄 SOP-based Answer:\n\n{line}"

            # Emergency leave
            if "emergency leave" in q:
                if "emergency" in line.lower():
                    return f"📄 SOP-based Answer:\n\n{line}"

            # Expense reimbursement
            if "reimbursement" in q or "expense" in q:
                if "reimburse" in line.lower():
                    return f"📄 SOP-based Answer:\n\n{line}"

            # Onboarding
            if "onboarding" in q or "first day" in q:
                if "day" in line.lower() or "orientation" in line.lower():
                    return f"📄 SOP-based Answer:\n\n{line}"

    # 🚨 IMPORTANT: No fallback SOP dumping
    return "❌ Answer not available in SOP."
