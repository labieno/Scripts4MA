# Scripts4MA
**Scripts for malware analysis**

Code snippets, implementing and detection malware techniques, automating unpacking routines, extracting configs, IOCs...

_Content:_

- **Decrypting**
    - RC4
    - XOR
- **Encoding/Decoding**
    - ROT13
- **Hashing**
    - CRC32
- **IDA**
    - IDAPython
    - IDC
- **MalwareTechniques**
    - Enumeration
        - enumerateProcesses
            - *CreateToolhelp32Snapshot, Process32First, Process32Next*
        - enumerateProcessesTree
        - ...
        - enumerateThreads
    - Injection
        - selfInjection
            - *VirtualAlloc, RtlMoveMemory, VirtualProtect, CreateThread, WaitForSingleObject*
        - classicCodeInjection
            - *OpenProcess, VirtualAllocEx, WriteProcessMemory, CreateRemoteThread*
        - classicDllInjection
            - *GetModuleHanlde, GetProcAddress (LoadLibraryA) + classicCodeInjection*
        - Dll1
            - *Code in main*
        - Dll2
            - *Code in export function*
        - APC Injection
            - *OpenThread, QueueUserAPC, Sleep + classicCodeInjection*
        - EarlyBird
            - *CreateProcessA (suspended), VirtualAllocEx, WriteProcessMemory, QueueUserAPC, ResumeThread*
        - APC Injection NlTestAlert
            - *VirtualAlloc, WriteProcessMemory, QueueUserAPC, NtTestAlert*
        - ...
        - Dll hijacking & sideloading
        - Process Hollowing
        - Reflective Dll
        - Process Doppelganging
        - PROPgate Injection
        - API hooking
        - ...
    - Communications
    - Stealing
        - Keylog
        - Store credentials
        - ...
    - Miscellaneous
        - Self destruction
    - Loaders
- **Powershell**
- **Python**
    - Process Memoria Scanner with Yara
