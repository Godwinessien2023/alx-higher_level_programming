#!/usr/bin/node
#!/usr/bin/node
const fs = require('fs');
const path = require('path')

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath) {
    console.error('Usage: node script_name.js <file_path> <content_to_write>' );
    process.exit(1);
}

fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
    if(err) {
        console.error('An error Occured:', err);
        return;
    }
    console.log(data);
});
