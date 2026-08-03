# Mole

**A lightweight Windows panic-button utility that hides quietly in your system tray.**

Mole is a small open-source Windows application designed to quickly hide your current activity. When the Panic action is triggered, Mole:

* Mutes system audio
* Minimizes all open windows
* Opens Notepad as a safe application

Mole runs quietly in the Windows system tray and stays out of the way until it is needed.

## Features

* One-click Panic action
* Mutes the default Windows audio output device
* Minimizes all application windows
* Opens Notepad after minimizing existing windows
* Runs in the Windows system tray
* Double-clicking the tray icon triggers Panic
* Minimal interface with only Panic and Exit options
* Can be packaged as a standalone Windows executable
* Open source under the GNU General Public License v3.0

## Platform Support

Mole currently supports:

* Windows 10
* Windows 11

Linux and macOS are not currently supported because Mole relies on Windows-specific APIs and keyboard shortcuts.

## How It Works

Mole stays in the Windows notification area.

The tray menu contains two actions:

### Panic

Runs the following actions in order:

1. Mutes system audio
2. Minimizes all open application windows
3. Opens Notepad

Notepad is opened last so that it remains visible after the other windows have been minimized.

### Exit

Stops Mole and removes its icon from the system tray.

## Requirements

To run Mole from source, you need:

* Python 3.10 or newer
* Windows 10 or Windows 11
* `uv`, recommended for dependency management

The main Python dependencies are:

* `pystray`
* `Pillow`
* `pycaw`
* `comtypes`
* `keyboard`
* `pywin32`
* `PyInstaller`, for executable builds

## Installation

### 1. Clone the repository

```powershell
git clone <repository-url>
cd mole
```

Replace `<repository-url>` with the URL of your Mole repository.

### 2. Install dependencies

Using `uv`:

```powershell
uv sync
```

If the project does not yet have all required dependencies, install them with:

```powershell
uv add pystray pillow pycaw comtypes keyboard pywin32
uv add --dev pyinstaller
```

## Running From Source

Run Mole with:

```powershell
uv run python .\main.py
```

After starting, the Mole icon should appear in the Windows system tray.

Windows may place the icon inside the hidden icons menu. Click the upward arrow in the taskbar notification area if the icon is not immediately visible.

## Building the Windows Executable

Mole can be packaged into a standalone `.exe` using PyInstaller.

Run the following command from the project root:

```powershell
uv run python -m PyInstaller `
    --noconfirm `
    --clean `
    --name Mole `
    --onefile `
    --windowed `
    --icon "assets\logo.png" `
    --add-data "assets:assets" `
    --hidden-import pystray._win32 `
    --collect-all pycaw `
    --collect-all comtypes `
    main.py
```

The generated executable will be located at:

```text
dist\Mole.exe
```

The executable can be run without installing Python on the target computer.

### Debug build

If the executable closes unexpectedly or fails to show the tray icon, build it with a visible console:

```powershell
uv run python -m PyInstaller `
    --noconfirm `
    --clean `
    --name Mole `
    --onefile `
    --console `
    --icon "assets\logo.png" `
    --add-data "assets:assets" `
    --hidden-import pystray._win32 `
    --collect-all pycaw `
    --collect-all comtypes `
    main.py
```

The console window will display Python exceptions and diagnostic output.

Once the application works correctly, rebuild it using `--windowed`.

## Project Structure

```text
mole/
├── assets/
│   └── logo.png
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
└── LICENSE
```

After building with PyInstaller, the following files and directories may also appear:

```text
mole/
├── build/
├── dist/
│   └── Mole.exe
└── Mole.spec
```

The `build` directory contains temporary build files.

The `dist` directory contains the final executable.

## Starting Mole Automatically

To start Mole automatically when you sign in to Windows:

1. Build or download `Mole.exe`
2. Press `Windows + R`
3. Enter:

```text
shell:startup
```

4. Press Enter
5. Create a shortcut to `Mole.exe` inside the Startup folder

Mole will then start when the Windows user signs in.

## Privacy

Mole runs entirely on the local computer.

It does not:

* Collect analytics
* Send telemetry
* Upload files
* Record keystrokes
* Connect to external servers
* Store browsing activity

The application only performs the local actions required by the Panic command.

## Security Notes

Mole uses system-level functionality to:

* Control the default audio output device
* Send the Windows minimize-all shortcut
* Launch Notepad

Some antivirus products may warn about unsigned executables produced by PyInstaller. This does not automatically mean the executable is malicious.

Users should download Mole only from trusted releases or build it directly from the source code.

## Roadmap

Potential future improvements include:

* Configurable safe application
* Custom keyboard shortcut
* Configurable Panic actions
* Startup-with-Windows option
* Persistent settings
* Custom action ordering
* Improved error logging
* Installer support
* Digitally signed releases
* Multi-language support

The roadmap is not a guarantee that every listed feature will be implemented.

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new branch

```powershell
git checkout -b feature/my-feature
```

3. Make your changes
4. Test the application on Windows
5. Commit your changes

```powershell
git commit -m "Add my feature"
```

6. Push the branch

```powershell
git push origin feature/my-feature
```

7. Open a pull request

Please keep pull requests focused and include a clear explanation of the change.

Bug reports and feature requests should include:

* Windows version
* Python version
* Mole version
* Steps to reproduce
* Expected behavior
* Actual behavior
* Relevant error messages

## Disclaimer

Mole is provided without warranty of any kind.

The authors and contributors are not responsible for data loss, interrupted work, application behavior, system configuration changes, or other damages resulting from the use of this software.

Test Mole before relying on it in situations where immediate operation is important.
