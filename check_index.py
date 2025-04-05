import os

index_path = "index.php"
default_content = """<?php
// For debugging
error_reporting(E_ALL);
ini_set("display_errors", 1);

if (file_exists(__DIR__ . "/woocasino/index.php")) {
    // Option 1: Include the woocasino index file
    include_once __DIR__ . "/woocasino/index.php";
} elseif (file_exists(__DIR__ . "/casino/index.php")) {
    // Option 2: Include the casino index file
    include_once __DIR__ . "/casino/index.php";
} elseif (file_exists(__DIR__ . "/frontend/index.php")) {
    // Option 3: Include the frontend index file
    include_once __DIR__ . "/frontend/index.php";
} else {
    // Nothing found, show directory structure for debugging
    echo "<h1>Debug Information</h1>";
    echo "<pre>";
    echo "Current directory: " . __DIR__ . "\\n";
    echo "Directory contents:\\n";
    system("ls -la " . __DIR__);
    echo "\\nWoocasino directory:\\n";
    system("ls -la " . __DIR__ . "/woocasino");
    echo "\\nCasino directory:\\n";
    system("ls -la " . __DIR__ . "/casino");
    echo "</pre>";
}
"""

if os.path.exists(index_path):
    with open(index_path, "r") as file:
        content = file.read().strip()

    if not content:
        with open(index_path, "w") as file:
            file.write(default_content)
        print("[check_index.py] index.php was empty — added proper content.")
    else:
        print("[check_index.py] index.php has content — no changes made.")
else:
    with open(index_path, "w") as file:
        file.write(default_content)
    print("[check_index.py] index.php not found — created with proper content.")

