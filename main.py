import subprocess
from pathlib import Path

import keyboard
import pystray
from PIL import Image
from pycaw.pycaw import AudioUtilities

BASE_DIR = Path(__file__).resolve().parent
ICON_PATH = BASE_DIR / "assets" / "logo.png"

if not ICON_PATH.exists():
    raise FileNotFoundError(f"Tray icon not found: {ICON_PATH}")

image = Image.open(ICON_PATH).convert("RGBA")
image.thumbnail((64, 64), Image.Resampling.LANCZOS)


def mute_system() -> None:
    """Mute the default Windows output device."""

    audio_device = AudioUtilities.GetSpeakers()
    volume = audio_device.EndpointVolume

    volume.SetMute(1, None)

    print("System muted.")


def minimize_all_windows() -> None:
    """Minimize application windows without minimizing the taskbar."""

    keyboard.press_and_release("windows+m")

    print("All windows minimized.")


def open_notepad() -> None:
    """Open Notepad after minimizing existing windows."""

    subprocess.Popen(
        ["notepad.exe"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    print("Notepad opened.")


def panic(
    icon: pystray.Icon,
    item: pystray.MenuItem,
) -> None:
    """Run all panic actions."""

    try:
        mute_system()
        minimize_all_windows()
        open_notepad()

        print("Panic actions completed.")

    except Exception as error:
        print(f"Panic action failed: {error}")


def exit_app(
    icon: pystray.Icon,
    item: pystray.MenuItem,
) -> None:
    """Exit Mole."""

    print("Exiting Mole...")
    icon.stop()


def setup_tray(icon: pystray.Icon) -> None:
    """Show the tray icon after pystray finishes initialization."""

    icon.visible = True
    print("Mole is running.")


icon = pystray.Icon(
    name="mole",
    icon=image,
    title="Mole",
    menu=pystray.Menu(
        pystray.MenuItem(
            text="Panic",
            action=panic,
            default=True,
        ),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem(
            text="Exit",
            action=exit_app,
        ),
    ),
)

icon.run(setup=setup_tray)
