import pathlib
import subprocess


def test_examples_readme_is_generated_and_up_to_date():
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    script = repo_root / "scripts" / "build_examples_readme.py"
    readme = repo_root / "examples" / "README.md"

    result = subprocess.run(["python3", str(script)], capture_output=True, text=True)
    assert result.returncode in (0, 1)
    assert readme.exists(), "examples/README.md not found after generation"
    assert (
        result.returncode == 0
    ), f"examples/README.md is outdated. Run the builder and commit changes. Output: {result.stdout}\n{result.stderr}"


