from some_enums import INPUTS, OUTPUTS
from TruthTable import TruthTable

def main():
    tt = TruthTable(INPUTS, OUTPUTS)
    input_width = TruthTable.get_width(INPUTS)
    output_width = TruthTable.get_width(OUTPUTS)
    print(f"Truth table size: {input_width}:{output_width}")
    template = tt.generate_template()
    for line in template:
        print(line)
    return


if __name__ == "__main__":
    main()
