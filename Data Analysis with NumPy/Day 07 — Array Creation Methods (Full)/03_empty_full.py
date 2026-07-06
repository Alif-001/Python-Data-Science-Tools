import numpy as np

# =========================
# np.empty → random garbage memory (fast but unsafe)
# =========================

arr_empty = np.empty((3, 3))

print("Empty Array:\n", arr_empty)
print("⚠️ values unpredictable (garbage memory)")

# =========================
# np.full → নির্দিষ্ট value দিয়ে fill করা
# =========================

arr_full = np.full((2, 4), 7)

print("\nFull Array:\n", arr_full)
print("All values = 7")