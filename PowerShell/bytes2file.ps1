# $bytes containing some bytes (f.e. 4D 5A ...)
Set-Content output.bin -Value $bytes -Encoding Byte
# Add-Content appends the data to the file