# Game

The given file is `c00l357_g4m3_3v3r.exe`.
If we run the file we get a message "Magshimim license out of date. Please buy a new one".
There is no other option but to Reverse Engineer the file.
I used IDA PRO Free.
In the generated `.idb` or `.asm` files we can find `push	offset FileName	; "Keyfile.dat"` line.
So let's create `Keyfile.dat` file in the same directory as the given `.exe` file.
Now the message that we get is `Keyfile is not valid. Sorry.`
So we know that we are on the right way.
Now let's understand the logic of the assembly code.
`esi` register is set to 0 using `xor esi, esi`.
And then we loop through the file content and check if the file contains `0x10` (16 in decimal) bytes with the value `0x47` (`G` character).
So the file content should be `GGGGGGGGGGGGGGGG`
And now we get the next message: `Done. Enjoy your new license!!!`.
So, the solution for the MMC is:

MMC{GGGGGGGGGGGGGGGG}