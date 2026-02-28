"""Custom application exceptions."""


class DocumentNotFoundError(Exception):
    pass


class UnsupportedFileTypeError(Exception):
    pass


class EmbeddingError(Exception):
    pass


class VectorStoreError(Exception):
    pass


class OCRError(Exception):
    pass


class LLMError(Exception):
    pass
