def write_on_output_file(corpus: str, outputFile: str):
    with open(outputFile, "w", encoding="utf-8") as f:
        f.write(corpus)
