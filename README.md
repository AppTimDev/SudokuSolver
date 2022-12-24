## Solve sudoku in different languages

---

## Environment:

---

## C#

### Compile the cs files using csc.exe 
csc.exe is located in the .NET Framework directory
```cmd
cd {project_directory}

C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /t:exe /out:main.exe main.cs
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe main.cs
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe *.cs
```

---

## C++

### download and install Dev-C++ (TDM-GCC 4.9.2 32/64bit)
https://sourceforge.net/projects/orwelldevcpp/

### Add the path to the environment variable
C:\Program Files (x86)\Dev-Cpp\MinGW64\bin
```cmd
g++ -v
> gcc version 4.9.2 (tdm64-1)
```

## Compile the cpp files
```cmd
g++ sudoku.cpp -o sudoku.exe -std=c++11
```

```cmd
g++ -g {inputFile} -o {outputFile}
```
Options starting with -g, -f, -m, -O, -W, or --param are automatically
passed on to the various sub-processes invoked by g++.  In order to pass
other options on to these processes the -W<letter> options must be used.

---

