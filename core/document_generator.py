from typing import Dict
from pathlib import Path
from models.document import Document, DocumentMetadata, DocumentSections
from generators.base_section_generator import GenerationContext, BaseSectionGenerator
from utils.token_estimator import TokenEstimator
from utils.file_processor import FileProcessor
from core.ollama_client import OllamaClient
from config import MAX_CTX, MODEL_NAME, OPTIONS # From config.py
from datetime import datetime # for DocumentMetadata created field

class DocumentGenerator:
    """
    Box: Document generator orchestrator

    Input: file path
    Output: Document object
    Responsibility: Coordinate section generation
    """

    def __init__(
        self,
        ollama_client: OllamaClient,
        section_generators: Dict[str, BaseSectionGenerator],
        token_estimator: TokenEstimator,
        file_processor: FileProcessor
    ):
        self.ollama = ollama_client
        self.section_generators = section_generators
        self.token_estimator = token_estimator
        self.file_processor = file_processor

    def generate(self, file_path: Path) -> Document:
        """
        Generate documentation for file.

        Input: file path
        Output: Document object
        """
        # Read and validate file
        content = self.file_processor.read_file(file_path)

        # Build context
        context = self._build_context(content, file_path)

        # Generate each section
        sections = self._generate_sections(context)

        # Generate metadata
        metadata = self._generate_metadata(context)

        # Assemble document
        doc = Document(
            file_name=file_path.stem,
            metadata=metadata,
            sections=sections
        )

        return doc

    def _build_context(self, content: str, file_path: Path) -> GenerationContext:
        """Build generation context."""
        file_size = len(content)
        estimated_tokens = self.token_estimator.estimate(content)

        options = {
            "num_ctx": min(estimated_tokens + 2048, MAX_CTX),
            "temperature": OPTIONS["temperature"], # Use from config.py
            "keep_alive": OPTIONS.get("keep_alive", "30m") # Use from config.py, with default
        }

        return GenerationContext(
            content=content,
            file_size=file_size,
            options=options
        )

    def _generate_sections(self, context: GenerationContext) -> DocumentSections:
        """Generate all sections."""
        return DocumentSections(
            summary=self.section_generators['summary'].generate(context),
            details=self.section_generators['details'].generate(context),
            key_functions=self.section_generators['key_functions'].generate(context),
            usage=self.section_generators['usage'].generate(context),
            related=self.section_generators['related'].generate(context),
            dependency_graph=self.section_generators['dependency_graph'].generate(context),
            security_risks=self.section_generators['security_risks'].generate(context)
        )

    def _generate_metadata(self, context: GenerationContext) -> DocumentMetadata:
        """Generate metadata."""
        return DocumentMetadata(
            tags=self.section_generators['tags'].generate(context).split(),
            created=datetime.now().strftime('%Y-%m-%d'),
            doc_type=self.section_generators['doc_type'].generate(context)
        )
