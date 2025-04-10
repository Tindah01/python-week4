# Step 1: Ask the user for a filename to read
filename = input("Enter the name of the file to read (e.g., countriesC.txt): ")

try:
    # Step 2: Open and read the file content
    with open(filename, "r") as file:
        content = file.read()

    # Step 3: Modify the content – bold and capitalize country names
    content = content.replace("Kenya", "**KENYA**")
    content = content.replace("Uganda", "**UGANDA**")
    content = content.replace("Tanzania", "**TANZANIA**")

    # Step 4: Ask for output filename
    new_filename = input("Enter the filename to save the modified content (e.g., modified_africa_info.txt): ")

    # Step 5: Write the modified content to the new file
    with open(new_filename, "w") as new_file:
        new_file.write(content)

    print(f"\n✅ Modified content written to '{new_filename}' with country names bolded and capitalized.")

except FileNotFoundError:
    print(f"\n❌ Error: The file '{filename}' was not found.")
except IOError:
    print(f"\n❌ Error: There was a problem reading or writing the file.")
