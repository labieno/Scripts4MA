auto file, address;
auto beginning = 0x ;
auto end = 0x ;
file = fopen("file.bin", "wb");
for ( address=beginning; address < end; address++ )
{ fputc(Byte(address), file); }