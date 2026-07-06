import os
import subprocess
import time
from functools import wraps
from typing import Any, Callable, TypeVar

from src.common.logger import logger

F = TypeVar('F', bound=Callable[..., Any])


def retry(operation_name: str, retries: int = 3, delay_seconds: float = 2.0, exceptions: tuple[type[BaseException], ...] = (Exception,)):
    """Retry a function a fixed number of times with a short backoff."""

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error: BaseException | None = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:  # type: ignore[misc]
                    last_error = exc
                    if attempt >= retries:
                        raise
                    logger.warning(
                        "%s failed on attempt %s/%s: %s",
                        operation_name,
                        attempt,
                        retries,
                        exc,
                    )
                    time.sleep(delay_seconds)
            if last_error is not None:
                raise last_error
            raise RuntimeError(f"{operation_name} failed without a captured exception")

        return wrapper  # type: ignore[return-value]

    return decorator


def run_command_with_retry(
    command: list[str],
    cwd: str,
    env: dict[str, str] | None = None,
    retries: int = 2,
    delay_seconds: float = 2.0,
    description: str = "command",
) -> subprocess.CompletedProcess[str]:
    """Run a shell command with retries and clear logging."""

    effective_env = env or os.environ.copy()
    attempt = 0
    last_error: subprocess.CalledProcessError | None = None
    while attempt < retries:
        try:
            logger.info("Running %s: %s", description, " ".join(command))
            return subprocess.run(
                command,
                cwd=cwd,
                check=True,
                env=effective_env,
                text=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError as exc:
            last_error = exc
            attempt += 1
            if attempt >= retries:
                logger.error("%s failed after %s attempts: %s", description, retries, exc)
                raise
            logger.warning(
                "%s failed on attempt %s/%s: %s",
                description,
                attempt,
                retries,
                exc.stderr or exc.stdout or exc,
            )
            time.sleep(delay_seconds)

    if last_error is not None:
        raise last_error
    raise RuntimeError(f"{description} failed without a captured exception")
