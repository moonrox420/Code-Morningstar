import yaml
from pathlib import Path
from typing import Dict, Any

class FeatureFlagManager:
    def __init__(self, flags_path: Path):
        self.flags_path = flags_path
        self.flags = self._load_flags()

    def _load_flags(self) -> Dict[str, Any]:
        if not self.flags_path.exists():
            raise FileNotFoundError(f"Feature flags file not found: {self.flags_path}")
        with self.flags_path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def is_enabled(self, feature: str) -> bool:
        return bool(self.flags.get(feature, False))
