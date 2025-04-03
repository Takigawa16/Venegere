document.getElementById('cipherForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const message = document.getElementById('message').value.toUpperCase();
    const keyword = document.getElementById('keyword').value.toUpperCase();
    const mode = document.querySelector('input[name="mode"]:checked').value;

    const result = vigenereCipher(message, keyword, mode);
    document.getElementById('result').innerText = result;
});

function vigenereCipher(message, keyword, mode) {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = '';

    // Repeat the keyword to match the length of the message
    keyword = repeatString(keyword, message.length);

    for (let i = 0; i < message.length; i++) {
        const msgPos = alphabet.indexOf(message[i]);
        const keyPos = alphabet.indexOf(keyword[i]);

        let newPos;
        if (mode === 'encrypt') {
            // Subtract keyword value from message value
            newPos = (msgPos - keyPos + 26) % 26;
        } else if (mode === 'decrypt') {
            // Add message value and keyword value (for decryption)
            newPos = (msgPos + keyPos) % 26;
        }

        result += alphabet[newPos];
    }

    return `Result: ${result}`;
}

function repeatString(str, count) {
    let result = '';
    while (result.length < count) {
        result += str;
    }
    return result.substring(0, count);
}
