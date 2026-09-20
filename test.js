const fs = require('fs');
const js = fs.readFileSync('/home/nmabbasi/.gemini/antigravity-ide/scratch/cv-repo/assets/index-DvGJtdcU.js', 'utf8');
const match = js.match(/Ajmal M.*?<\/a>/);
console.log(match[0]);
