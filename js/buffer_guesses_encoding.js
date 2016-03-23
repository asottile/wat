// Demonstrates that an [Array of Buffer objects].join('') implicitly attempts
// codecs
var snowmanUTF8 = new Buffer([0xe2, 0x98, 0x83]);

var threeSnowmen = [snowmanUTF8, snowmanUTF8, snowmanUTF8];
console.log('Prints: ☃☃☃');
console.log(threeSnowmen.join(''));

var severedSnowmen = [
    snowmanUTF8,
    // Both parts of the UTF8 bytes
    snowmanUTF8.slice(0, 1),
    snowmanUTF8.slice(1, 3)
];
console.log('Prints: ☃���');
console.log(severedSnowmen.join(''));

// Correct way to do this
console.log('Prints: ☃☃');
console.log(Buffer.concat(severedSnowmen).toString('UTF-8'));
