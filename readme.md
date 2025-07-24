# TrustMeBro

A lightweight Windows tray application for toggling a specific IP blocking rule on/off using Windows Firewall — inspired by tools like Cloudflare WARP. Designed for personal network testing and experimentation.

## ✨ Features

- 🟢 **Toggle Block**: Right-click the tray icon or press `Ctrl+F12` to enable/disable a specific Windows Firewall rule.
- 🎨 **Tray Icon Status**: Icon changes to indicate status (Power On = Active, Power Off = Inactive).
- 📌 **Background App**: Runs in the system tray without opening a window.
- 🚫 **No full GUI**: Interaction is via tray icon and hotkey only.

## 🧰 Installation

### Prerequisites
- **Windows OS**: This application is designed for Windows only, as it uses Windows Firewall (`netsh`) and Windows-specific APIs.
- **Python 3.8+**: Ensure Python is installed. Download from [python.org](https://www.python.org/downloads/).
- **Administrator Privileges**: The application **requires** administrator privileges to modify Windows Firewall rules. If not run as an administrator, the program will exit automatically.

### 1. Clone the Repository

```bash
git clone https://github.com/MrTomato77/TrustMeBro
cd TrustMeBro
```

### 2. Setup Python Environment

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Verify Icon Files
Ensure the `icon` folder contains `power-on.ico` and `power-off.ico` in the correct path (`icon/power-on.ico` and `icon/power-off.ico`).

## ⚙️ Usage

1. **Edit `TrustMeBro.py`**:
   - `rule_name`: Name of the Windows Firewall rule (default: `TrustMeBro`).
   - `remote_ip`: Set to a valid IPv4 address (e.g., `192.168.1.1`) to block outbound connections to that IP.
   - **Note**: Invalid IPs (e.g., `0.0.0.0` or `x.x.x.x`) will prevent the firewall rule from being created.

2. **Run the Script**:
   ```bash
   python .\main\TrustMeBro.py
   ```

3. **Interact with the App**:
   - **Hotkey**: Press `Ctrl+F12` to toggle the firewall rule.
   - **Tray Icon**: Right-click the system tray icon to toggle the rule or exit the app.

## 🏗️ Compile to EXE (Optional)

Convert the script into a standalone `.exe` using [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/):

### 1. Install auto-py-to-exe

```bash
pip install auto-py-to-exe
```

### 2. Run the Tool

```bash
auto-py-to-exe
```

### 3. Configuration in auto-py-to-exe

- **Script Location**: Select `TrustMeBro.py`.
- **Onefile**: ✅ (enabled).
- **Console Window**: ❌ (window-based / no console).
- **Additional Files**: Add the `icon` folder (containing `power-on.ico` and `power-off.ico`).

### 4. Click "Convert .py to .exe"

The output `.exe` will be generated in the `output` folder.

**Note**: If you modify `remote_ip` or other parts of the script, recompile the `.exe` to ensure changes take effect. Run the `.exe` as an administrator, or it will exit.

## ⚠️ Important Notes

- **Administrator Privileges**: The script or `.exe` **must** be run as an administrator to modify Windows Firewall rules. If not, the program will exit automatically.
- **Valid IP Address**: Ensure `remote_ip` is a valid IPv4 address. Using invalid values (e.g., `0.0.0.0` or `x.x.x.x`) may cause the firewall rule to fail.
- **Use Responsibly**: This tool is for personal network testing only.

## 📄 License

MIT License

Copyright (c) 2025 Nakrit Kreechaichana

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 💡 Credits

- Tray functionality powered by [pystray](https://github.com/moses-palmer/pystray).
- Icon handling powered by [Pillow](https://github.com/python-pillow/Pillow).
- Hotkey support powered by [keyboard](https://github.com/boppreh/keyboard).
