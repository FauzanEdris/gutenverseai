const fs = require('fs');
const path = require('path');

// Get the current directory
const currentDir = __dirname;

// Define the output directory
const outputDir = path.join(currentDir, 'minified');

// Ensure the output directory exists
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
}

// Function to check if a file is a JSON file
const isJsonFile = (fileName) => path.extname(fileName).toLowerCase() === '.json';

// Function to minify JSON
const minifyJsonFile = (filePath, outputFilePath) => {
    try {
        // Read the file content
        const content = fs.readFileSync(filePath, 'utf8');

        // Parse and stringify to minify
        const minifiedContent = JSON.stringify(JSON.parse(content));

        // Write to the new file
        fs.writeFileSync(outputFilePath, minifiedContent, 'utf8');

        console.log(`Minified: ${filePath} -> ${outputFilePath}`);
    } catch (error) {
        console.error(`Error processing file ${filePath}:`, error.message);
    }
};

// Read all files in the directory
fs.readdir(currentDir, (err, files) => {
    if (err) {
        console.error('Error reading directory:', err.message);
        return;
    }

    // Filter JSON files
    const jsonFiles = files.filter(isJsonFile);

    if (jsonFiles.length === 0) {
        console.log('No JSON files found in the directory.');
        return;
    }

    // Process each JSON file
    jsonFiles.forEach((file) => {
        const filePath = path.join(currentDir, file);
        const outputFilePath = path.join(outputDir, file);
        minifyJsonFile(filePath, outputFilePath);
    });
});
