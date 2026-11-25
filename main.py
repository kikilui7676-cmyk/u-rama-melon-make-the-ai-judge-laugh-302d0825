import os


def write_entry():
    joke = (
        "I asked for a raise and got a pizza party "
        "\u2014 management's way of telling me my salary is now pepperoni."
    )
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke + "\n")


write_entry()
