import re

def read_decision_tree_logic(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    decision_tree_logic = []
    for line in lines:
        # Extract conditions and value
        match = re.match(r'when (.+?) then (\d+);', line.strip())
        if match:
            conditions = match.group(1).split(" and ")
            value = int(match.group(2))
            decision_tree_logic.append({"conditions": conditions, "value": value})
    
    return decision_tree_logic

def condition_to_p4_code(conditions, indent_level=3):
    indent = "    " * indent_level
    code = ""
    for condition in conditions:
        # Remove decimals
        condition = re.sub(r'\.\d+', '', condition)
        code += f"{indent}if ({condition}) {{\n"
        indent_level += 1
        indent = "    " * indent_level
    return code, indent_level

def generate_p4_code(decision_tree_logic, template_file_path="template.p4", output_file_path="output.p4"):
    with open(template_file_path, "r") as file:
        p4_template = file.read()

    decision_tree_code = ""
    for logic in decision_tree_logic:
        conditions = [c.strip() for c in logic["conditions"]]
        value = logic["value"]
        code, indent_level = condition_to_p4_code(conditions)
        code += "    " * indent_level + f'set_custom_value({value});\n'
        for i in range(0, len(conditions)):
            code += "    " * (indent_level-1-i) + '}\n'
        decision_tree_code += code

    p4_code = p4_template.replace("// Decision tree logic placeholder", decision_tree_code)

    with open(output_file_path, "w") as file:
        file.write(p4_code)

# Set path to decision tree file, template file, and output file
decision_tree_file_path = "tree.txt"
template_file_path = "template.p4"
output_file_path = "output.p4"

# Read decision tree logic from file
decision_tree_logic = read_decision_tree_logic(decision_tree_file_path)

# Generating the P4 file
generate_p4_code(decision_tree_logic, template_file_path, output_file_path)