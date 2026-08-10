"""Null provider — used when AI is disabled or no provider configured."""

from __future__ import annotations

from apps.ai_assistance.providers.base import LLMProvider, ProviderResult
from apps.ai_assistance.safety import SAFE_FALLBACK_MESSAGE


class NullLLMProvider(LLMProvider):
    name = "null"

    def generate(
        self,
        *,
        use_case: str,
        user_text: str,
        context: dict[str, object],
        timeout_seconds: float,
    ) -> ProviderResult:
        return ProviderResult(
            text=SAFE_FALLBACK_MESSAGE,
            provider_name=self.name,
            failed=True,
            source_ids=tuple(str(x) for x in (context.get("source_ids") or [])),
        )
