#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    run = True
    while run:
        memory = [0]*256
        ptr = 0
        loop = [[0, 0] for _ in range(50)]
        source = input(">")
        cnt = 0
        for i, c in enumerate(source):
            if c == "[":
                loop[cnt][0] = i
                cnt += 1
        cnt = 0
        for i, c in enumerate(source):
            if c == "]":
                loop[cnt][1] = i
                cnt += 1
        i = 0
        cnt = 0
        end = len(source)
        while True:
            if i == end:
                break
            c = source[i]
            if c == "+":
                memory[ptr] += 1
            elif c == "-":
                memory[ptr] -= 1
            elif c == ">":
                ptr += 1
            elif c == "<":
                ptr -= 1
            elif c == ".":
                print("{}".format(chr(memory[ptr])), end="")
            elif c == ",":
                memory[ptr] = ord(input())
            elif c == "[":
                if memory[ptr] == 0:
                    i = loop[cnt][1]+1
                    cnt += 1
                    continue
            elif c == "]":
                i = loop[cnt][0]
                continue
            elif c == "q":
                run = False
            else:
                pass
            i += 1
        print()
            

if __name__ == "__main__":
    main()
