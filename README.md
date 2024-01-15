# YARABlueprint
YaraBlueprint: A lightweight Python tool for rapidly generating YARA rule skeletons. Effortlessly create the foundational structure for your custom YARA rules with placeholders for meta, strings, and conditions. Ideal for cybersecurity professionals and enthusiasts streamlining their rule development process.

## Example

Generate YARA rules for binary files in the directory `/path/to/files` with custom metadata:

`python main.py -p /path/to/files --author "Your Name" --reference "https://your-reference.com" --date "2023-11-30" --TLP "Amber" --Hashes "hash1,hash2,hash3"`

## CLI Args to set Metadata:

- `-a` or `--author`: Specify the author of the YARA rules (default is "Author Name").
- `-r` or `--reference`: Specify a reference for the YARA rules (default is "https://example.com").
- `-d` or `--date`: Specify the date for the YARA rules (default is the current date).
- `--TLP`: Specify the TLP (Traffic Light Protocol) value.
- `--Hashes`: Specify hashes as a comma-separated list of strings.

* The script will generate YARA rules for the binary files in the specified directory, including the specified metadata.

* The generated rules will be displayed in the terminal. You can copy and use these rules as needed. Or if you'd prefer it in file form use redirectors such as:

`python main.py -p /path/to/files --author "Your Name" --reference "https://your-reference.com" --date "2023-11-30" --TLP "Amber" --Hashes "hash1,hash2,hash3" > rule.yar`
