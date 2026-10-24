import subprocess

def test_npm_test_runs_cleanly():
    try:
        # Run the npm test command and capture the output
        result = subprocess.run(
            ["npm", "test", "--", "--runInBand"],
            capture_output=True,
            text=True,
            check=True
        )
        # Assert that the test passed (exit code 0)
        assert result.returncode == 0, f"npm test failed with output: {result.stderr}"
    except subprocess.CalledProcessError as e:
        # If the command failed, raise an assertion error with the output
        assert False, f"npm test failed with output: {e.stderr}"

# Ensure the model module imports cleanly
def test_model_module_imports_cleanly():
    import importlib

    mod = importlib.import_module("model")
    assert mod is not None, "model failed to import"
    assert hasattr(mod, "__file__"), "model has no __file__"