"""
Media player integration using playerctl
Handles communication with media players via MPRIS
"""
import subprocess
from pathlib import Path
from typing import Optional, Tuple

PLAYER_NAME: str = 'spotify'


def _playerctl(*args) -> subprocess.CompletedProcess:
    return subprocess.run(
        ['playerctl', '--player', PLAYER_NAME, *args],
        capture_output=True, text=True, timeout=0.5
    )


def get_position() -> Optional[float]:
    try:
        result = _playerctl('position')
        return float(result.stdout.strip()) if result.returncode == 0 else None
    except Exception:
        return None


def get_track() -> Optional[Tuple[str, str]]:
    try:
        result = _playerctl('metadata', '--format', '{{artist}}|||{{title}}')
        if result.returncode == 0:
            parts = result.stdout.strip().split('|||')
            return (parts[0], parts[1]) if len(parts) == 2 else None
    except Exception:
        return None


def get_status() -> Optional[str]:
    try:
        result = _playerctl('status')
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None


def get_audio_file_info() -> Optional[Path]:
    try:
        result = _playerctl('metadata', '--format', '{{xesam:url}}')
        if result.returncode == 0:
            url = result.stdout.strip()
            if url.startswith('file://'):
                return Path(url[7:])
    except Exception:
        pass
    return None


def is_paused() -> bool:
    return get_status() == 'Paused'


def is_playing() -> bool:
    return get_status() == 'Playing'
