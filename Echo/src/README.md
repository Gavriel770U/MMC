# Echo

We got a server that uses printf.
The printf function is unsafe especially if we use % stuff,
like %x that extracts data for us.

I used requests module in order to send basic requests,
and also I sent a lot %x in order to get data,
and using pwn module 'decipher' it and get data.

Then, when we print the data we got,
we can find segments of MMC flag and if we append all parts together we get:

```
MMC{RepeatAfterMeSir!}
```