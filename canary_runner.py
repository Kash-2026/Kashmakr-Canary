#!/usr/bin/env python3
import sys, subprocess, json, os
from pathlib import Path

def main():
    args = sys.argv[1:]
    target_ids = args if args else ["FP037", "FP038", "FP054", "FP057"]
    print(f"🚀 Cloud Canary Execution Starting for {len(target_ids)} target gigs: {target_ids}")
    
    results = {}
    quarantined_dirs = sorted([d for d in Path(".").glob("quarantine_gigs/*") if d.is_dir()])
    
    for qd in quarantined_dirs:
        gid = qd.name
        print(f"\n--- Verifying {gid} ---")
        req_file = qd / "requirements.txt"
        if req_file.exists():
            subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r", str(req_file)], check=False)
        res = subprocess.run(["pytest", str(qd), "-q"], capture_output=True, text=True)
        passed = (res.returncode == 0)
        status_label = "TRUE PASS" if passed else "FAILED"
        print(f"Result for {gid}: {status_label}")
        if not passed:
            print(res.stdout[:500])
        results[gid] = {
            "verdict": status_label,
            "exit_code": res.returncode,
            "output": res.stdout[-1000:]
        }
        
    Path("canary_cloud_report.json").write_text(json.dumps(results, indent=2))
    print(f"\n✅ Canary Report Generated at canary_cloud_report.json")

if __name__ == "__main__":
    main()
