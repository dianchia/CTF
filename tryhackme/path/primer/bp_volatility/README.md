# BP: VOLATILITY

## OBTAINING MEMORY SAMPLES
> - **What memory format is the most common?**
>> .raw

> - **The Window's system we're looking to perform memory forensics on was turned off by mistake. What file contains a compressed memory image?**
>> hiberfil.sys

> - **How about if we wanted to perform memory forensics on a VMware-based virtual machine?**
>> .vmem

## EXAMINING OUR PATIENT

`volatility -f cridex.vmem imageinfo`

> - **What profile is correct for this memory image?**
>> WinXPSP2x86

> - **Take a look through the processes within our image. What is the process ID for the smss.exe process?**
>> 368

`volatility -f cridex.vmem --profile=WinXPSP2x86 netscan`

`volatility -f cridex.vmem --profile=WinXPSP2x86 psxview`
> - **What process has only one 'False' listed?**
>> csrss.exe

`volatility -f cridex.vmem --profile=WinXPSP2x86 ldrmodules`
> - **Which process has all three columns listed as 'False'**
>> csrss.exe

`volatility -f cridex.vmem --profile=WinXPSP2x86 apihooks`

`volatility -f cridex.vmem --profile=WinXPSP2x86 malfind -D malfind`
> - **We'll use this dump later for more analysis. How many files does this generate?**
>> 12

`volatility -f cridex.vmem --profile=WinXPSP2x86 dlllist`

`volatility -f cridex.vmem --profile=WinXPSP2x86 --pid=584 dlldump -D dlldump`
> - **How many DLLs does this end up pulling?**
>> 12