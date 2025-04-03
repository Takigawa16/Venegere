using System;

class Program
{
    static void Main(string[] args)
    {
        string message = "HELLO";
        string keyword = "KEY";

        string encrypted = VigenereCipher(message, keyword, "encrypt");
        string decrypted = VigenereCipher(encrypted, keyword, "decrypt");

        string encryptedHtml = ConvertToHtml(encrypted);
        string decryptedHtml = ConvertToHtml(decrypted);

        Console.WriteLine($"Encrypted HTML: {encryptedHtml}");
        Console.WriteLine($"Decrypted HTML: {decryptedHtml}");
    }

    static string VigenereCipher(string message, string keyword, string mode)
    {
        const string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string result = "";

        // Convert message and keyword to uppercase and remove spaces
        message = message.Replace(" ", "").ToUpper();
        keyword = keyword.ToUpper();

        // Repeat the keyword to match the length of the message
        keyword = RepeatString(keyword, message.Length);

        for (int i = 0; i < message.Length; i++)
        {
            // Find the position in the alphabet for the message and keyword letters
            int msgPos = alphabet.IndexOf(message[i]);
            int keyPos = alphabet.IndexOf(keyword[i]);

            int newPos;
            if (mode == "encrypt")
            {
                // Subtract keyword value from message value
                newPos = (msgPos - keyPos + 26) % 26;
            }
            else if (mode == "decrypt")
            {
                // Add message value and keyword value (for decryption)
                newPos = (msgPos + keyPos) % 26;
            }
            else
            {
                throw new ArgumentException("Invalid mode. Use 'encrypt' or 'decrypt'.");
            }

            // Append the encrypted/decrypted letter to the result
            result += alphabet[newPos];
        }

        return result;
    }

    static string RepeatString(string str, int count)
    {
        string result = "";
        while (result.Length < count)
        {
            result += str;
        }
        return result.Substring(0, count);
    }

    static string ConvertToHtml(string text)
    {
        return $"<p>{text}</p>";
    }
}
