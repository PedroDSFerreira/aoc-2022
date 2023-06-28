# Part 1
import functions as fn

def main():
    sum_priorities = 0;
    
    with open("input.txt") as file:
        for line in file:
            rucksack = [line[:len(line)//2], line[len(line)//2:]]
        
            common_char = fn.get_common_char(rucksack)
            sum_priorities += fn.get_priority(common_char)

    print(sum_priorities)

if __name__ == "__main__":
    main()