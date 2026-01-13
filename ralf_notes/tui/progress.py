"""
Box: Progress Manager

Responsibility: Show progress during file processing
"""

from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
    TimeElapsedColumn,
    MofNCompleteColumn
)
from typing import Optional


class ProgressManager:
    """
    Box: Progress Manager

    Responsibility: Show progress bars during batch processing
    """

    def __init__(self, console):
        """
        Initialize progress manager.

        Args:
            console: Console instance
        """
        self.console = console
        self.progress: Optional[Progress] = None

    def __enter__(self):
        """Start progress display."""
        if not self.console.quiet:
            self.progress = Progress(
                SpinnerColumn(),
                TextColumn("[bold blue]{task.description}"),
                BarColumn(bar_width=None),
                MofNCompleteColumn(),
                TaskProgressColumn(),
                "•",
                TimeElapsedColumn(),
                "•",
                TimeRemainingColumn(),
                console=self.console.console,
                expand=True
            )
            self.progress.__enter__()
        return self

    def __exit__(self, *args):
        """Stop progress display."""
        if self.progress:
            self.progress.__exit__(*args)

    def add_task(self, description: str, total: int):
        """
        Add a progress task.

        Args:
            description: Task description
            total: Total items

        Returns:
            Task ID or None
        """
        if self.progress:
            return self.progress.add_task(description, total=total)
        return None

    def update(self, task_id, advance: int = 1, description: str = None, total: int = None):
        """
        Update progress.

        Args:
            task_id: Task ID
            advance: Amount to advance
            description: Optional new description
            total: Optional new total
        """
        if self.progress and task_id is not None:
            kwargs = {'advance': advance}
            if description:
                kwargs['description'] = description
            if total:
                kwargs['total'] = total
            self.progress.update(task_id, **kwargs)

    def complete(self, task_id):
        """
        Mark task as complete.

        Args:
            task_id: Task ID
        """
        if self.progress and task_id is not None:
            self.progress.update(task_id, completed=True)