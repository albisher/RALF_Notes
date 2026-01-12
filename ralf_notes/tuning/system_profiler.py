import psutil
import time
from ollama import Client
from typing import Optional

from .models import SystemProfile

class SystemProfiler:
    """
    Box: System Profiler

    Input: None
    Output: SystemProfile
    Responsibility: Detect and measure system resources
    """

    def profile(self) -> SystemProfile:
        """
        Profile the system.

        Returns:
            SystemProfile with all detected capabilities
        """
        print("Profiling system...")
        return SystemProfile(
            cpu_cores=self._detect_cpu_cores(),
            cpu_threads=self._detect_cpu_threads(),
            total_ram_gb=self._detect_total_ram(),
            available_ram_gb=self._detect_available_ram(),
            has_gpu=self._detect_gpu(),
            gpu_memory_gb=self._detect_gpu_memory(),
            ollama_host=self._get_ollama_host(),
            ollama_responding=self._check_ollama(),
            ollama_version=self._get_ollama_version()
        )

    def _detect_cpu_cores(self) -> int:
        """Detect physical CPU cores."""
        try:
            return psutil.cpu_count(logical=False) or 0
        except Exception as e:
            print(f"Could not detect CPU cores: {e}")
            return 0

    def _detect_cpu_threads(self) -> int:
        """Detect logical CPU threads."""
        try:
            return psutil.cpu_count(logical=True) or 0
        except Exception as e:
            print(f"Could not detect CPU threads: {e}")
            return 0

    def _detect_total_ram(self) -> float:
        """Detect total system RAM in GB."""
        try:
            return psutil.virtual_memory().total / (1024**3)
        except Exception as e:
            print(f"Could not detect total RAM: {e}")
            return 0.0

    def _detect_available_ram(self) -> float:
        """Detect available RAM in GB."""
        try:
            return psutil.virtual_memory().available / (1024**3)
        except Exception as e:
            print(f"Could not detect available RAM: {e}")
            return 0.0

    def _detect_gpu(self) -> bool:
        """Check if GPU is available."""
        # This is a placeholder as GPU detection is platform-specific and complex
        return False

    def _detect_gpu_memory(self) -> float:
        """Detect GPU memory in GB."""
        # Placeholder
        return 0.0

    def _get_ollama_host(self) -> str:
        # Assuming default Ollama host for profiling purposes
        return "http://127.0.0.1:11434"

    def _check_ollama(self) -> bool:
        """Check if Ollama is responding."""
        try:
            client = Client(host=self._get_ollama_host())
            client.list()
            return True
        except Exception as e:
            print(f"Ollama check failed: {e}")
            return False

    def _get_ollama_version(self) -> str:
        """Get Ollama version."""
        # Placeholder
        return "unknown"
