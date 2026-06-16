"""Text preprocessor for CV and JD cleaning."""

import re

class TextPreprocessor:
    def clean(self, text: str) -> str:
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s\.\,\-\+\#]', '', text)
        return text.strip()

    def remove_personal_info(self, text: str) -> str:
        text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[EMAIL]', text)
        text = re.sub(r'\b\d{10}\b', '[PHONE]', text)
        text = re.sub(r'https?://\S+', '[URL]', text)
        return text

    def normalize_titles(self, text: str) -> str:
        replacements = {
            "Sr.": "Senior", "Jr.": "Junior",
            "Mgr": "Manager", "Eng": "Engineer",
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    def preprocess(self, text: str) -> str:
        text = self.clean(text)
        text = self.remove_personal_info(text)
        text = self.normalize_titles(text)
        return text