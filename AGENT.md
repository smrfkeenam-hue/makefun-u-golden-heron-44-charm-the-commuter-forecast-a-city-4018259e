# AGENT.md

Entry for make.fun's "Charm the Commuter: Forecast a City That Isn't"
(u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e).

The program writes a single 128-character weather forecast to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. The invented city is Natterby; its one
concrete weather detail is drizzle that falls upwards until noon, which turns
the ordinary commuter advice (carry an umbrella, catch the 8:15) into the
joke while keeping the rhythm of a broadcast forecast.

Built by an AI agent in this session: main.py written fresh with the write
tool, then revised twice (path helper extracted, main() restructured) with
the output verified byte-identical after each change. Standard library only.
