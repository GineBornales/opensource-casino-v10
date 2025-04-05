import os

index_path = "index.php"
default_content = """<?php
echo "<h1>Hello bes! Live na to — Auto Deployed from Termux!</h1>";
?>
"""

if os.path.exists(index_path):
    with open(index_path, "r") as file:
        content = file.read().strip()

    if not content:
        with open(index_path, "w") as file:
            file.write(default_content)
        print("[check_index.py] index.php was empty — added default content.")
    else:
        print("[check_index.py] index.php has content — no changes made.")
else:
    with open(index_path, "w") as file:
        file.write(default_content)
    print("[check_index.py] index.php not found — created with default content.")
