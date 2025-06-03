import subprocess
import os

def run_applescript(script_path):
    result = subprocess.run(
        ['osascript', script_path],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"❌ Error running {script_path}:\n{result.stderr}")
    else:
        print(f"✅ Successfully ran {script_path}")

def export_csvs():
    base_dir = os.path.dirname(__file__)
    compound_script = os.path.join(base_dir, 'export_compound.applescript')
    component_script = os.path.join(base_dir, 'export_component.applescript')

    print("🔄 Exporting compound_input.csv from Numbers...")
    run_applescript(compound_script)

    print("🔄 Exporting component_input.csv from Numbers...")
    run_applescript(component_script)

if __name__ == "__main__":
    export_csvs()