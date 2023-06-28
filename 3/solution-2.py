# Part 2
import functions as fn

def main():
    sum_priorities = 0;
    
    with open("input.txt") as file:
        length = len(file.readlines())
        file.seek(0)
        for i in range(0, length, 3):
            group = []
            for j in range(3):
                group.append(file.readline().strip())

            common_char = fn.get_common_char(group)
            sum_priorities += fn.get_priority(common_char)

    print(sum_priorities)
            

if __name__ == "__main__":
    main()