
class TruthTable(object):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        return

    @staticmethod
    def get_width(table):
        table_width = 0
        for this_enum in table:
            all_values = [e.value for e in this_enum]
            biggest = max(all_values)
            num_bits = biggest.bit_length()
            table_width += num_bits
        return table_width

    def generate_fragment(self, table, start=0, prefix=""):
        all_values = [e.name for e in self.inputs[start]]
        if prefix:
            prefix += ","
        for member in all_values:
            member_prefix = prefix + member
            if (start + 1) < len(self.inputs):
                self.generate_fragment(table, start + 1, member_prefix)
            else:
                table.append(member_prefix)
        return

    def print_headings(self):
        heading = ""
        for index, item in enumerate(self.inputs):
            if index != 0:
                heading += ","
            heading += item.__name__
        for index, item in enumerate(self.outputs):
            heading += "," + item.__name__
        return heading

    def generate_template(self):
        template = [self.print_headings()]
        self.generate_fragment(template)
        return template

