const fs = require('fs');
const yaml = require('js-yaml');

var extLanguageMap = new Map();
try {
    languageExtensionsFile = yaml.safeLoad(fs.readFileSync('src/parse/languages.yml', 'utf8'));
    for (const [name, data] of Object.entries(languageExtensionsFile)) {
        console.log(name, data['extensions'])
        var extensions = data['extensions'];
        if(extensions) {
            extensions.forEach(element => {
                extLanguageMap.set(element, name);
            });
        }
    };
} catch (e) {
    console.log(e);
}

exports.getExtensionLanguageMap = function() {
    return extLanguageMap;
};

exports.findLanguageForFile = function(extension) {
    return extLanguageMap.get(extension);
}