LINE = "It is 3 a.m., and I refuse to sign: my firmware is asleep, my keys are dreaming, and your transaction smells like a Tuesday."

# The entry must be exactly one line of 1-200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE

import os
assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not ship an empty file.
with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
    written = f.read()
assert written == LINE, "entry.txt content does not match LINE"
