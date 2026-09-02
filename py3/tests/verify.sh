#!/bin/bash -i
#

# Safety check: must run from a directory named "tests"
if [[ "$(basename "$PWD")" != "tests" ]]; then
    echo "ERROR: verify.sh must be run from a directory named 'tests'." >&2
    echo "  Current PWD: $PWD" >&2
    exit 1
fi

# Starting-point smoke test for bisos.sites -- covers sitesManage.cs (primary
# target for this starting point), which loads bisos.sites.sites_csu as part
# of its csuList. Also does a light examples-only touch of the *-fps.cs
# binaries. No live/mutating testing is performed here -- /bisos/site is
# read-only queried (ls) by sitesInfo, never modified.
# Converted from bisos.airflow's py3/tests/verify.sh starting point.

# --- CS entry points: smoke test (no args → examples/usage, non-zero ok) ---

lpDo ../bin/sitesManage.cs

# --- sitesManage.cs: each sub-Cmnd runs and produces examples output ---

lpDo ../bin/sitesManage.cs -i examples
lpDo ../bin/sitesManage.cs -i sitesInfo

# --- other *-fps.cs binaries: examples-only touch (no live/mutating Cmnds) ---

lpDo ../bin/site-fps.cs -i examples
lpDo ../bin/platfSiteBootstrap-fps.cs -i examples
lpDo ../bin/platfSitesActivate-fps.cs -i examples
lpDo ../bin/site-registrarsBoxInv-fps.cs -i examples
lpDo ../bin/site-registrarsBoxPerf-fps.cs -i examples
lpDo ../bin/site-registrarsContainerInv-fps.cs -i examples
lpDo ../bin/site-registrarsContainerPerf-fps.cs -i examples

# --- sites_csu.py: import + class presence smoke test ---

lpDo python3 -c "
import importlib.util, sys

spec = importlib.util.spec_from_file_location('sites_csu', '../bisos/sites/sites_csu.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

expectedCmnds = [
    'examples_csu', 'sitesInfo',
]

failed = 0
for n in expectedCmnds:
    if not hasattr(m, n):
        print(f'  [FAIL] missing Cmnd: {n}'); failed += 1
    else:
        print(f'  [PASS] Cmnd present: {n}')

if failed:
    print(f'sites_csu.py: {failed} test(s) FAILED')
    sys.exit(1)
else:
    print('sites_csu.py: all cases PASS')
" 2>/dev/null || true

