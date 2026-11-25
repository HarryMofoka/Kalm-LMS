"""Worked Example: Print-Shop Job Queue Manager.

Demonstrates pure (non-mutating) list transformations: enqueuing with optional
deduplication, order-preserving deduplication, priority bumping, cancellation,
and cyclic batch rotation.
"""

from __future__ import annotations


def enqueue_jobs(
    queue: list[str],
    new_jobs: list[str],
    allow_duplicates: bool = False,
) -> list[str]:
    """Return a new queue with new_jobs appended without mutating inputs."""
    result = list(queue)
    if allow_duplicates:
        result.extend(new_jobs)
        return result

    seen = set(result)
    for job in new_jobs:
        if job not in seen:
            result.append(job)
            seen.add(job)
    return result


def deduplicate_jobs(queue: list[str]) -> list[str]:
    """Return a new queue keeping only the first occurrence of each job ID."""
    seen: set[str] = set()
    unique: list[str] = []
    for job in queue:
        if job not in seen:
            unique.append(job)
            seen.add(job)
    return unique


def bump_job_to_front(queue: list[str], job_id: str) -> list[str]:
    """Return a new queue with the first matching job_id moved to index 0.

    Raises:
        ValueError: If job_id is not found in queue.
    """
    if job_id not in queue:
        raise ValueError(f"Job not found in queue: {job_id!r}")

    idx = queue.index(job_id)
    return [queue[idx]] + queue[:idx] + queue[idx + 1 :]


def cancel_job(queue: list[str], job_id: str) -> list[str]:
    """Return a new queue with the first occurrence of job_id removed.

    Raises:
        ValueError: If job_id is not found in queue.
    """
    if job_id not in queue:
        raise ValueError(f"Job not found in queue: {job_id!r}")

    idx = queue.index(job_id)
    return queue[:idx] + queue[idx + 1 :]


def rotate_batch(queue: list[str], shift: int) -> list[str]:
    """Return a new queue rotated left by `shift` positions (negative = right)."""
    if not queue:
        return []
    offset = shift % len(queue)
    return queue[offset:] + queue[:offset]


if __name__ == "__main__":
    initial_queue = ["JOB-101", "JOB-102", "JOB-103", "JOB-102"]
    q1 = deduplicate_jobs(initial_queue)
    q2 = enqueue_jobs(q1, ["JOB-103", "JOB-104", "JOB-105"])
    q3 = bump_job_to_front(q2, "JOB-104")
    q4 = cancel_job(q3, "JOB-102")
    q5 = rotate_batch(q4, 1)

    print("Original (untouched):", initial_queue)
    print("Deduplicated        :", q1)
    print("After enqueue       :", q2)
    print("After rush bump     :", q3)
    print("After cancel        :", q4)
    print("After rotate(1)     :", q5)
