import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
FORECAST = "Tonight in Vexford: 41°F, a light drizzle of expired coupons, winds sighing at 12 mph. Bring an umbrella and low expectations."


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    line = FORECAST.strip()
    assert 1 <= len(line) <= 160, "forecast must be 1-160 chars"
    assert "\n" not in line, "forecast must be a single line"
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
