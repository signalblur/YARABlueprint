import os
import sys
import argparse
import datetime
import binascii

def get_file_range(size):
    max_size = size * 2  # Example: double the size for the range
    return f"filesize < {max_size}KB"

def get_timestamp_basic(date_obj=None):
    if not date_obj:
        date_obj = datetime.datetime.now()
    return date_obj.strftime("%Y-%m-%d")

def get_uint_string(magic_bytes):
    # Convert bytes to hexadecimal string and consider endianness
    hex_string = binascii.hexlify(magic_bytes).decode('ascii')
    if len(magic_bytes) == 1:
        return f"uint8(0) == 0x{hex_string}"
    elif len(magic_bytes) == 2:
        # Adjust for endianness if necessary
        hex_string = f"{hex_string[2:]}{hex_string[:2]}"
        return f"uint16(0) == 0x{hex_string}"
    else:
        return ""

def generate_skeleton_rule(rule_name, description, author, reference, date, magic_bytes, file_size, tlp, original_name, family, scope, intel, hashes):
    magic_condition = get_uint_string(magic_bytes)
    file_size_condition = get_file_range(file_size)
    
    metadata = [
        f"description = \"{description}\"",
        f"author = \"{author}\"",
        f"reference = \"{reference}\"",
        f"date = \"{date}\"",
        f"tlp = \"{tlp}\"",
        f"hashes = \"{hashes}\""
    ]
    
    rule = f"tdo_{rule_name} {{\n"
    rule += "   meta:\n      "
    rule += ",\n      ".join(metadata) + "\n"
    rule += "   strings:\n"
    rule += "      // Add your strings here\n"
    rule += "   condition:\n"
    rule += f"      {magic_condition} and\n"
    rule += f"      {file_size_condition}\n"
    rule += "}\n"
    return rule

def generate_rule_name(file_path):
    base_name = os.path.basename(file_path)
    rule_name = "rule_" + base_name.replace('.', '_')
    return rule_name

def process_file(file_path, args):
    with open(file_path, 'rb') as file:
        # Read up to the first 2 bytes for magic bytes
        magic_bytes = file.read(2)

    file_size = os.path.getsize(file_path)
    rule_name = generate_rule_name(file_path)
    description = f"Skeleton rule for {rule_name}"
    
    # Call generate_skeleton_rule with metadata arguments
    generated_rule = generate_skeleton_rule(
        rule_name, description, args.author, args.reference, args.date,
        magic_bytes, file_size, args.TLP, args.original_name, args.Family,
        args.Scope, args.Intel, args.Hashes
    )
    print(generated_rule)

def process_directory(dir_path, args):
    for root, _, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            process_file(file_path, args)

def main():
    parser = argparse.ArgumentParser(description='YARA Skeleton Rule Generator')
    parser.add_argument('-p', help='Path to directory with files to generate rules for', required=True)
    parser.add_argument('-a', '--author', help='Author of the YARA rules', default='Author Name')
    parser.add_argument('-r', '--reference', help='Reference for the YARA rules', default='https://example.com')
    parser.add_argument('-d', '--date', help='Date for the YARA rules', default=get_timestamp_basic())
    parser.add_argument('--TLP', help='TLP value')
    parser.add_argument('--Hashes', help='Hashes (comma-separated list of strings)')

    args = parser.parse_args()
    
    # Directory of files to process and generate a Skeleton of yara rules
    process_directory(args.p, args)

if __name__ == '__main__':
    main()
