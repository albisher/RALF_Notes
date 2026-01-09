import logging
from datetime import datetime
from pathlib import Path

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
from cache.cache_manager import (
    get_cached_response,
    cache_response,
    get_cache_stats,
    clear_cache
)

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
    logger.info("="*60)
    logger.info("RALF Notes - Ollama Documentation Generator")
    logger.info("="*60)

    # Cache management
    if CLEAR_CACHE_ON_START:
        logger.info("Clearing cache...")
        clear_cache()

    if ENABLE_CACHING:
        cache_stats = get_cache_stats()
        logger.info(f"Cache: {cache_stats['entry_count']} entries, {cache_stats['total_size_mb']:.2f} MB")

    generator = build_document_generator()
    file_processor = FileProcessor()

    # Get files
    files = file_processor.get_all_files(SOURCE_PATHS)

    # Process each file
    for file_path_str in files:
        file_path = Path(file_path_str) # Convert string path to Path object
        
        output_path = Path(TARGET_DIR) / f"{file_path.stem}.md"
        output_path_parent = output_path.parent
        ensure_dir(output_path_parent) # Ensure target directory exists

        if output_path.exists() and not OVERWRITE_EXISTING: # Use OVERWRITE_EXISTING from config
            logger.info(f"⏭️  Skipping existing: {output_path.name}")
            continue

        logger.info(f"Generating for: {file_path.name}")
        
        # Original logic had no dry_run for default generation
        try:
            doc = generator.generate(file_path)
            output_path.write_text(doc.to_markdown(), encoding='utf-8')
            logger.info(f"✅ Saved: {output_path.name}")
        except Exception as e:
            logger.error(f"❌ Error generating for {file_path.name}: {e}")
    
    logger.info(f"\n✨ Complete! Processed {len(files)} files.")

if __name__ == "__main__":
    import sys

    # Handle cache CLI arguments outside of main() for simplicity in this restored state
    if len(sys.argv) > 1:
        if sys.argv[1] == '--clear-cache':
            print("Clearing cache...")
            clear_cache()
            print("Cache cleared.")
            sys.exit(0)
        elif sys.argv[1] == '--cache-stats':
            stats = get_cache_stats()
            print(f"Cache Statistics:")
            print(f"  Entries: {stats['entry_count']}")
            print(f"  Size: {stats['total_size_mb']:.2f} MB")
            print(f"  Oldest: {stats['oldest_age_days']:.1f} days")
            print(f"  Newest: {stats['newest_age_days']:.1f} days")
            sys.exit(0)

    main()