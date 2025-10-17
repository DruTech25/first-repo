from typing import List


def build_grep_command(query: str) -> List[str]:
    """
    Build a safe argv for running grep recursively.

    Security fix:
    - Return an argument vector instead of a shell command string.
    - Reject obviously dangerous shell metacharacters to prevent injection.
    """
    if not isinstance(query, str):
        raise TypeError("query must be a string")

    # Basic injection hardening: reject common metacharacters and constructs.
    dangerous_substrings = ["$(", "$", "`", ";", "|", "\n", "\r", ">", "<", "&&", "||"]
    if any(danger in query for danger in dangerous_substrings):
        raise ValueError("query contains potentially dangerous shell syntax")

    # Return argv form; using '--' terminates options so query cannot be parsed as flags.
    return ["grep", "-R", "--", query, "."]
