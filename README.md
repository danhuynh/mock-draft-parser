# Yahoo Salary Cap Mock Draft Parsing Tool

This tool is designed to parse mock draft results from a given string and export it to a CSV file. The data should include details like the player's number, team, name, team code, position, and price.

## How It Works

1. **Parsing the Data**: The script utilizes a regular expression to match the specific pattern in each line of the provided data. The pattern is broken down into the following groups:
    - Order Number
    - Manager
    - Player Name
    - Team
    - Position
    - Price

2. **Creating a DataFrame**: Once the data is parsed, it's structured into a pandas DataFrame. This provides an easy way to manipulate and analyze the data in Python.

3. **Exporting to CSV**: Finally, the DataFrame is exported to a CSV file, making it accessible and editable in various spreadsheet applications.

## How to Use

1. **Install Dependencies**: You'll need to have Python and pandas installed on your system. If you don't have pandas, you can install it using pip:

   \`\`\`bash
   pip install pandas
   \`\`\`

2. **Prepare Your Data**: Inside the script, you'll find a string variable named `data`. Replace the content of this variable with your data string.

3. **Run the Script**: Execute the script using Python:

   \`\`\`bash
   python your_script_name.py
   \`\`\`

4. **Access the CSV File**: The script will create a CSV file named `parsed_data.csv` in the same directory as the script. You can open this file using any spreadsheet application or text editor.

## Customization

- **Changing the Output Filename**: If you want to change the name or path of the output CSV file, modify the `csv_file_path` variable in the script.

- **Adjusting the Parsing Pattern**: If the input data format changes, you may need to update the regular expression inside the `parse_line` function to match the new pattern.

## Support

For any issues or questions regarding the tool, please contact dan@danhuynh.org.
