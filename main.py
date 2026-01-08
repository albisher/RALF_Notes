import os
import logging
from datetime import datetime
from pathlib import Path
from ollama import Client, ResponseError # Still needed for recursive_summarize and review_obsidian_doc


# Import from local modules
from config import *
from prompts import *
from models.document import Document, DocumentMetadata, DocumentSections
from validators.summary_validator import SummaryValidator
from validators.tags_validator import TagsValidator
from validators.structure_validator import StructureValidator
from validators.general_validator import GeneralValidator
from cleaners.summary_cleaner import SummaryCleaner
from cleaners.tags_cleaner import TagsCleaner
from cleaners.details_cleaner import DetailsCleaner
from cleaners.general_cleaner import GeneralCleaner


from utils.logger_factory import LoggerFactory, ensure_dir
from utils.token_estimator import TokenEstimator
from utils.file_processor import FileProcessor
from utils.retry_manager import RetryManager

# Import the new generator classes
from core.ollama_client import OllamaClient
from core.document_generator import DocumentGenerator
from generators.summary_generator import SummaryGenerator
from generators.details_generator import DetailsGenerator
from generators.tags_generator import TagsGenerator
from generators.key_functions_generator import KeyFunctionsGenerator
from generators.usage_generator import UsageGenerator
from generators.related_generator import RelatedGenerator
from generators.dependency_graph_generator import DependencyGraphGenerator
from generators.security_risks_generator import SecurityRisksGenerator
from generators.doc_type_generator import DocTypeGenerator


logger = LoggerFactory.get_logger()

def build_document_generator() -> DocumentGenerator:
    """
    Dependency injection: wire all boxes together.
    """
    # Core
    ollama = OllamaClient(host=OLLAMA_HOST)
    file_processor = FileProcessor()
    token_estimator = TokenEstimator()

    # Validators
    summary_validator = SummaryValidator()
    tags_validator = TagsValidator()
    general_validator = GeneralValidator()
    structure_validator = StructureValidator() # Will be used in main()

    # Cleaners
    summary_cleaner = SummaryCleaner()
    tags_cleaner = TagsCleaner()
    details_cleaner = DetailsCleaner()
    general_cleaner = GeneralCleaner()

    # Section generators
    section_generators = {
        'summary': SummaryGenerator(
            ollama_client=ollama,
            validator=summary_validator,
            cleaner=summary_cleaner,
        ),
        'details': DetailsGenerator(
            ollama_client=ollama,
            validator=general_validator, # Details uses general validation
            cleaner=details_cleaner,
        ),
        'key_functions': KeyFunctionsGenerator(
            ollama_client=ollama,
            validator=general_validator,
            cleaner=general_cleaner, # Uses clean_not_applicable
        ),
        'usage': UsageGenerator(
            ollama_client=ollama,
            validator=general_validator,
            cleaner=general_cleaner, # Uses clean_not_applicable
        ),
        'related': RelatedGenerator(
            ollama_client=ollama,
            validator=general_validator,
            cleaner=general_cleaner, # Uses clean_related
        ),
        'tags': TagsGenerator(
            ollama_client=ollama,
            validator=tags_validator,
            cleaner=tags_cleaner,
        ),
        'doc_type': DocTypeGenerator(
            ollama_client=ollama,
            validator=general_validator, # DocType uses general validation
            cleaner=general_cleaner, # Uses clean_doc_type
        ),
        'dependency_graph': DependencyGraphGenerator(
            ollama_client=ollama,
            validator=general_validator,
            cleaner=general_cleaner, # Uses clean_mermaid
        ),
        'security_risks': SecurityRisksGenerator(
            ollama_client=ollama,
            validator=general_validator,
            cleaner=general_cleaner, # Uses clean_not_applicable
        )
    }

    # Document generator
    return DocumentGenerator(
        ollama_client=ollama,
        section_generators=section_generators,
        token_estimator=token_estimator,
        file_processor=file_processor
    )


def main():
    """Main entry point."""
    generator = build_document_generator()
    file_processor = FileProcessor() # Instantiate FileProcessor for get_all_files

    # Get files
    files = file_processor.get_all_files(SOURCE_PATHS)

    # Process each file
    for file_path in files:
        doc = generator.generate(Path(file_path))
        output_path = Path(TARGET_DIR) / f"{Path(file_path).stem}.md"
        output_path.write_text(doc.to_markdown())

if __name__ == "__main__":
    main()
