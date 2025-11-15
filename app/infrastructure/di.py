from app.infrastructure.adapters.google_translator import GoogleTranslateAdapter
from app.infrastructure.adapters.cgpt_translator import CgptAdapter


def get_google_translate_adapter() -> GoogleTranslateAdapter:
    return GoogleTranslateAdapter()


def cgpt_adapter() -> CgptAdapter:
    return CgptAdapter()