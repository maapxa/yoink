#!/usr/bin/env python
import json
from pathlib import Path

base_dir = Path(__file__).parent
package_path = base_dir.joinpath("data", "packages.json")
install_path = base_dir.joinpath("out", "install.sh")

packages = json.load(package_path.open())
brew = " ".join(packages["brew"])
pipx_commands = "\n".join(f"pipx install {package}" for package in packages["pipx"])

script = f"""#!/usr/bin/env bash

echo "Installing system packages..."
brew install {brew}

echo "Installing pipx packages..."
{pipx_commands}
"""

install_path.parent.mkdir(exist_ok=True)
install_path.write_text(script)
install_path.chmod(0o755)
