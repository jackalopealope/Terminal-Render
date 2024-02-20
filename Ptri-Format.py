import os

def fix_ascii_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".ptri"):  # Process only ptri files
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf8") as file:
                lines = file.readlines()
            max_length = max(len(line.rstrip()) for line in lines)  # Find the length of the longest line
            with open(filepath, "w", encoding="utf8") as file:
                for line in lines:
                    padded_line = line.rstrip().ljust(max_length)  # Pad the line with spaces
                    file.write(padded_line + "\n")  # Add newline character at the end of each line

# Example usage
directory = "C:/Users/29JHANNI/OneDrive - Davis School District/Documents/TerminalRender/"
fix_ascii_files(directory)
