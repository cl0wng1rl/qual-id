#!/bin/bash

import sys
from qual_id.response import Response


class Parser:
    def __init__(self, args):
        self.__args = args
        self.__shift()
        self.__config = {"format": "csv"}

    def parse(self):
        while len(self.__args):
            if self.__args[0] in {"-h", "--help"}:
                self.__print_help()
                exit()
            if self.__parameter("collection"):
                continue
            if self.__parameter("pattern"):
                continue
            if self.__parameter("number"):
                continue
            if self.__parameter("format"):
                continue
            print("invalid parameter: " + self.__args[0])
            exit()
        return self.__config

    def __shift(self):
        self.__args = self.__args[1:]

    def __parameter(self, key):
        if self.__args[0] in {"-{0}".format(key[0]), "--{0}".format(key)}:
            self.__shift()
            if len(self.__args):
                self.__config[key] = self.__args[0]
                self.__shift()
                return True
            else:
                print("no {0} specified".format(key))
                exit()
        else:
            return False

    def __print_help(self):
        print(" ")
        print("Qual ID - get qualitative IDs")
        print(" ")
        print("qual-id [options]")
        print(" ")
        print("options:")
        print("-h, --help                show brief help")
        print("-p, --pattern             specify the pattern of the qual IDs")
        print("-c, --collection          specify which collection to use")
        print("-n, --number              specify how many qual IDs to receive")
        print("-f, --format              specify the format of the qual IDs")
        print(" ")


parser = Parser(sys.argv)
config = parser.parse()
qual_id = Response(config).get_response_obj()
print(qual_id)