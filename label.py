import os


def update_class_labels(folder_path, new_label=4):
    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Only process text files
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Replace the class label
            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0:
                    parts[0] = str(new_label)
                    updated_lines.append(' '.join(parts))

            # Write the updated lines back to the file
            with open(file_path, 'w') as file:
                file.write('\n'.join(updated_lines))


# Specify the folder path
folder_path = '/home/vertex/Downloads/anish_annotation/label'

# Update the class labels in all files in the specified folder
update_class_labels(folder_path)
