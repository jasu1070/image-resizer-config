const fs = require('fs');
const path = require('path');

const rootDir = __dirname;
const distDir = path.join(rootDir, 'dist');

console.log('Cleaning dist directory...');
if (fs.existsSync(distDir)) {
  fs.rmSync(distDir, { recursive: true, force: true });
}
fs.mkdirSync(distDir, { recursive: true });

const filesToCopy = [
  'index.html',
  'privacy-policy.html',
  'terms-of-use.html',
  'refund-policy.html',
  'contact-support.html',
  'subscription-terms.html',
  'version.json',
  '.nojekyll',
];

const dirsToCopy = [
  'assets',
  'salary-mate-legal-pages',
  'PocketParant _Project_Legal_Pages'
];

filesToCopy.forEach(file => {
  const src = path.join(rootDir, file);
  const dest = path.join(distDir, file);
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, dest);
    console.log(`Copied file: ${file}`);
  } else {
    console.warn(`Warning: file not found: ${file}`);
  }
});

dirsToCopy.forEach(dir => {
  const src = path.join(rootDir, dir);
  const dest = path.join(distDir, dir);
  if (fs.existsSync(src)) {
    fs.cpSync(src, dest, { recursive: true });
    console.log(`Copied directory: ${dir}`);
  } else {
    console.warn(`Warning: directory not found: ${dir}`);
  }
});

console.log('Build completed successfully!');
