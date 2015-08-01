//chmod u=rwx,go=xr,+s

#include <unistd.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
    std::string default_directory("%s");
    std::string command;
    command = default_directory + "/main.py";
    for (int i = 1; i < argc; ++i) {
        command = command + " " + std::string(argv[i]);
    }
    setuid(0);
    system(command.c_str());
    return 0;
}